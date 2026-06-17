# Pixel Liquid phone-node proof of life — 2026-06-17

## Milestone

Manual local Liquid audio loop succeeded on Pixel / Termux.

Proven:

- Termux is installed and usable.
- Debian PRoot is installed and usable.
- Liquid LFM2.5 Audio GGUF bundle is present.
- Official Liquid Android ARM64 runner is installed in native Termux.
- `llama-liquid-audio-cli` executes in native Termux.
- Text-to-speech works locally using the exact supported system prompt:
  - `Perform TTS. Use the US male voice.`
- Audio input works locally using:
  - `--audio <wav>`
  - `-sys "Respond with interleaved text and audio."`
- Human recording test passed after converting MP3 to WAV:
  - Liquid understood the human recording and found the test word.

## Important findings

Generic `llama-server` could start with the Liquid model stack, but did not expose a useful OpenAI-style TTS endpoint.

Generic `llama-tts` was the wrong runner for this Liquid bundle.

The correct runner path is the Liquid-specific Android ARM64 runner:

- `llama-liquid-audio-cli`

The runner requires `LD_LIBRARY_PATH` to include the runner directory so it can find `libliquid-audio.so`.

## F-Droid / ADB status

F-Droid/ADB remains useful later for clean Termux + Termux:API infrastructure, microphone integration, Android intents, notifications, and a polished phone-node conductor.

But F-Droid/ADB is not blocking manual Liquid audio experiments anymore.

## Current manual loop

Current working rough path:

1. Record human speech with Android recorder.
2. Export/copy recording to `/sdcard/Download/`.
3. Convert MP3 to WAV with ffmpeg.
4. Run Liquid Android runner with `--audio`.
5. Inspect text/audio response.

## Next useful work

- Wrap record / convert / run / play into one script.
- Test longer natural speech.
- Compare Liquid direct audio understanding against modular STT → router → TTS.
- Decide whether Liquid is a module inside the BOBA conductor, not the whole architecture.
