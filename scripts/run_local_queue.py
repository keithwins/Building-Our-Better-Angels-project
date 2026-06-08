#!/usr/bin/env python3
"""
File-backed local job queue runner.

Job files are JSON in jobs/queue/, sorted by filename (use a prefix to order):
  { "title": "...", "command": "...", "max_seconds": 300 }

Runner picks the lexicographically first queued job, moves it to jobs/running/,
runs it, writes stdout+stderr to logs/jobs/, then moves it to jobs/done/ or
jobs/failed/.

One job runs at a time. Ctrl-C once: finish current job, then stop.
Ctrl-C twice: kill current job immediately, return it to jobs/queue/.
"""

import json
import os
import shutil
import signal
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
QUEUE   = REPO / "jobs" / "queue"
RUNNING = REPO / "jobs" / "running"
DONE    = REPO / "jobs" / "done"
FAILED  = REPO / "jobs" / "failed"
LOGS    = REPO / "logs" / "jobs"


def setup():
    for d in [QUEUE, RUNNING, DONE, FAILED, LOGS]:
        d.mkdir(parents=True, exist_ok=True)


def next_job():
    jobs = sorted(f for f in QUEUE.iterdir() if f.suffix == ".json")
    return jobs[0] if jobs else None


def run_job(job_path: Path, stop_after: list) -> bool:
    """Run one job. Returns True if completed (done/failed), False if interrupted."""
    job = json.loads(job_path.read_text())
    title      = job["title"]
    command    = job["command"]
    max_secs   = int(job.get("max_seconds", 300))

    ts          = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path    = LOGS / f"{ts}_{job_path.stem}.log"
    running_path = RUNNING / job_path.name

    shutil.move(str(job_path), str(running_path))

    print(f"\n[{ts}] START  {title}")
    print(f"  cmd:     {command}")
    print(f"  timeout: {max_secs}s")
    print(f"  log:     {log_path.relative_to(REPO)}")

    start = time.time()
    proc  = None
    interrupted = False

    def _second_ctrl_c(sig, frame):
        nonlocal interrupted
        interrupted = True
        if proc:
            print("\n  Second Ctrl-C — killing job and returning to queue.")
            proc.kill()

    with open(log_path, "w") as log:
        log.write(f"# title:   {title}\n")
        log.write(f"# command: {command}\n")
        log.write(f"# started: {ts}\n\n")
        log.flush()

        proc = subprocess.Popen(
            command,
            shell=True,
            stdout=log,
            stderr=subprocess.STDOUT,
            cwd=str(REPO),
        )

        signal.signal(signal.SIGINT, _second_ctrl_c)
        try:
            proc.wait(timeout=max_secs)
        except subprocess.TimeoutExpired:
            proc.terminate()
            time.sleep(2)
            proc.kill()
            elapsed = time.time() - start
            log.write(f"\n# TIMEOUT after {elapsed:.1f}s\n")
            proc.wait()
        finally:
            signal.signal(signal.SIGINT, signal.SIG_DFL)

    elapsed = time.time() - start

    if interrupted:
        shutil.move(str(running_path), str(job_path))
        print(f"  RETURNED to queue (interrupted after {elapsed:.1f}s)")
        return False

    rc = proc.returncode
    if rc == 0:
        shutil.move(str(running_path), str(DONE / job_path.name))
        print(f"  DONE    rc=0  {elapsed:.1f}s")
    else:
        shutil.move(str(running_path), str(FAILED / job_path.name))
        print(f"  FAILED  rc={rc}  {elapsed:.1f}s")
    return True


def main():
    setup()

    stop_after_current = [False]

    def _first_ctrl_c(sig, frame):
        stop_after_current[0] = True
        print("\nCtrl-C: will stop after current job finishes. Ctrl-C again to kill now.")
        # re-register default so a second Ctrl-C during sleep raises KeyboardInterrupt
        signal.signal(signal.SIGINT, signal.SIG_DFL)

    signal.signal(signal.SIGINT, _first_ctrl_c)

    print(f"Queue runner started.")
    print(f"  queue:  {QUEUE.relative_to(REPO)}")
    print(f"  logs:   {LOGS.relative_to(REPO)}")
    print(f"  Ctrl-C once to stop gracefully after current job.\n")

    try:
        while not stop_after_current[0]:
            job = next_job()
            if job:
                signal.signal(signal.SIGINT, _first_ctrl_c)
                completed = run_job(job, stop_after_current)
                if not completed:
                    break
            else:
                time.sleep(5)
    except KeyboardInterrupt:
        pass

    print("\nQueue runner stopped.")
    remaining = len(list(QUEUE.glob("*.json")))
    if remaining:
        print(f"  {remaining} job(s) still in queue.")


if __name__ == "__main__":
    main()
