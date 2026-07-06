/* Salon overlay v0.2 — the per-page comment-cycle window.
   Each document gets its own conversation: contextual open questions, a
   composer with an agent picker, and the feedback-and-forth scoped to the
   page in view (entries carry the doc filename in refs — see CHARTER.md).
   Reads/writes the REAL files at /salon/. Writing needs salon-serve.
   Self-contained: no dependencies on app.js internals. */
(function () {
  const QUESTIONS_URL = "/salon/open-questions.jsonl";
  const LOG_URL = "/salon/salon-log.jsonl";
  const PARTICIPANTS_URL = "/salon/participants.json";
  const SAY_URL = "/salon/api/say";

  const css = `
  .salon-fab { position: fixed; right: 22px; bottom: 22px; z-index: 999;
    padding: 10px 16px; border-radius: 22px; cursor: pointer; border: 1px solid var(--border-color, #444);
    background: var(--bg-secondary, rgba(30,30,40,.9)); color: var(--text-primary, #eee);
    font: 500 13px/1 var(--font-body, sans-serif); backdrop-filter: blur(8px); }
  .salon-fab:hover { border-color: var(--accent-amber, #d9a441); }
  .salon-fab .badge { color: var(--accent-amber, #d9a441); font-weight: 600; margin-left: 5px; }
  .salon-panel { position: fixed; right: 22px; bottom: 68px; z-index: 999; width: min(480px, 94vw);
    max-height: 76vh; overflow-y: auto; border-radius: 12px; padding: 16px;
    border: 1px solid var(--border-color, #444); background: var(--bg-secondary, rgba(24,24,32,.97));
    color: var(--text-primary, #eee); font-family: var(--font-body, sans-serif);
    backdrop-filter: blur(12px); display: none; }
  .salon-panel.open { display: block; }
  .salon-title { font-size: 12px; letter-spacing: .06em; color: var(--text-muted, #999); }
  .salon-title b { color: var(--text-primary, #eee); }
  .salon-panel h3 { font-size: 13px; letter-spacing: .08em; text-transform: uppercase;
    color: var(--text-muted, #999); margin: 14px 0 8px; }
  .salon-compose { display: flex; flex-direction: column; gap: 6px; margin-top: 10px; }
  .salon-compose textarea { resize: vertical; min-height: 44px; border-radius: 8px; padding: 8px 10px;
    border: 1px solid var(--border-color, #444); background: var(--bg-primary, rgba(0,0,0,.25));
    color: var(--text-primary, #eee); font: 13px/1.4 var(--font-body, sans-serif); }
  .salon-compose .row { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }
  .salon-compose label { font-size: 12px; color: var(--text-muted, #aaa); display: flex; align-items: center; gap: 4px; }
  .salon-compose label .later { font-size: 10px; color: var(--text-muted, #777); }
  .salon-chip { font: 11px var(--font-mono, monospace); color: var(--accent-amber, #d9a441); }
  .salon-chip b { cursor: pointer; margin-left: 5px; color: var(--text-muted, #888); }
  .salon-compose button.send { margin-left: auto; padding: 6px 16px; border-radius: 10px; cursor: pointer;
    border: 1px solid var(--accent-amber, #d9a441); background: transparent; color: var(--accent-amber, #d9a441);
    font: 600 12px var(--font-body, sans-serif); }
  .salon-note { font-size: 11.5px; color: var(--text-muted, #999); min-height: 15px; }
  .salon-q { border-left: 2px solid var(--border-color, #444); padding: 6px 10px; margin-bottom: 10px; }
  .salon-q.contextual { border-left-color: var(--accent-amber, #d9a441); }
  .salon-q .q-text { font-size: 13.5px; line-height: 1.45; }
  .salon-q .q-meta { font: 11px var(--font-mono, monospace); color: var(--text-muted, #999); margin-top: 4px; }
  .salon-q .q-here { color: var(--accent-amber, #d9a441); font-weight: 600; }
  .salon-q button { margin-top: 5px; font-size: 10.5px; padding: 2px 8px; border-radius: 8px;
    border: 1px solid var(--border-color, #444); background: transparent; color: var(--text-muted, #aaa); cursor: pointer; }
  .salon-scope { display: flex; gap: 6px; margin: 4px 0 10px; }
  .salon-scope button { font-size: 11px; padding: 3px 10px; border-radius: 10px; cursor: pointer;
    border: 1px solid var(--border-color, #444); background: transparent; color: var(--text-muted, #aaa); }
  .salon-scope button.on { border-color: var(--accent-amber, #d9a441); color: var(--accent-amber, #d9a441); }
  .salon-entry { font-size: 12.5px; line-height: 1.4; margin-bottom: 9px; }
  .salon-entry .who { font: 600 11px var(--font-mono, monospace); color: var(--accent-amber, #d9a441); margin-right: 6px; }
  .salon-entry .when { font: 10.5px var(--font-mono, monospace); color: var(--text-muted, #888); }
  .salon-entry .kind { font: 10.5px var(--font-mono, monospace); color: var(--text-muted, #777); margin-left: 6px; }
  .salon-empty { font-size: 12.5px; color: var(--text-muted, #999); }`;
  const style = document.createElement("style");
  style.textContent = css;
  document.head.appendChild(style);

  const fab = document.createElement("button");
  fab.className = "salon-fab";
  const panel = document.createElement("div");
  panel.className = "salon-panel";
  document.body.appendChild(panel);
  document.body.appendChild(fab);
  fab.textContent = "✳ Salon";
  fab.addEventListener("click", () => {
    panel.classList.toggle("open");
    if (panel.classList.contains("open")) render();
  });

  // Composer / view state
  let composeRefs = [];        // e.g. an oq-id being answered
  let composeKind = "note";
  let pageScoped = true;       // include current doc in refs on send
  let scope = "page";          // floor filter: "page" | "all"
  let selectedTo = new Set();  // @names chosen in the picker
  let participants = null;

  async function fetchJsonl(url) {
    try {
      const r = await fetch(url, { cache: "no-store" });
      if (!r.ok) return null;
      const text = await r.text();
      return text.split("\n").filter(Boolean).map((l) => {
        try { return JSON.parse(l); } catch { return null; }
      }).filter(Boolean);
    } catch { return null; }
  }

  async function fetchParticipants() {
    if (participants) return participants;
    try {
      const r = await fetch(PARTICIPANTS_URL, { cache: "no-store" });
      participants = r.ok ? (await r.json()).participants : [];
    } catch { participants = []; }
    return participants;
  }

  function activeDoc() {
    const el = document.querySelector(".nav-item.active");
    return el ? (el.dataset.target || "") : "";
  }

  function latestPerId(rows) {
    const m = new Map();
    for (const r of rows) if (r.id) m.set(r.id, { ...(m.get(r.id) || {}), ...r });
    return [...m.values()];
  }

  function esc(s) {
    return String(s).replace(/[&<>"']/g, (c) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c])
    );
  }

  function refersToPage(e, doc) {
    return !!doc && (e.refs || []).some((r) => r.includes(doc));
  }

  function composerHtml(doc, agents) {
    const picker = agents
      .filter((p) => p.kind === "agent")
      .map((p) => {
        const wakes = !!p.wake;
        return `<label><input type="checkbox" data-agent="${esc(p.name)}" ${selectedTo.has(p.name) ? "checked" : ""}>
          @${esc(p.name)} <span class="later">${wakes ? "(wakes)" : "(reads later)"}</span></label>`;
      }).join("");
    const chips = [];
    if (composeRefs.length)
      chips.push(`<span class="salon-chip">answering ${esc(composeRefs.join(", "))}<b data-clear-ref>✕</b></span>`);
    if (doc)
      chips.push(`<span class="salon-chip">${pageScoped ? "→ this page" : "→ whole floor"}<b data-toggle-page>⇄</b></span>`);
    return `
    <div class="salon-compose">
      <textarea id="salon-text" placeholder="One line for the floor. Addressed agents answer; the rest reply only if it matters."></textarea>
      <div class="row">${picker}</div>
      <div class="row">${chips.join(" ")}<button class="send" id="salon-send">Send</button></div>
      <div class="salon-note" id="salon-note"></div>
    </div>`;
  }

  async function send() {
    const ta = panel.querySelector("#salon-text");
    const note = panel.querySelector("#salon-note");
    const text = (ta.value || "").trim();
    if (!text) return;
    const doc = activeDoc();
    const refs = [...composeRefs];
    if (doc && pageScoped && !refs.includes(doc)) refs.push(doc);
    const to = [...selectedTo].map((n) => "@" + n);
    note.textContent = "sending…";
    try {
      const r = await fetch(SAY_URL, {
        method: "POST",
        body: JSON.stringify({ author: "keith", kind: composeKind, text, refs, to }),
      });
      if (!r.ok) throw new Error(String(r.status));
      ta.value = "";
      composeRefs = [];
      composeKind = "note";
      const waking = [...selectedTo].filter((n) => (participants || []).some((p) => p.name === n && p.wake));
      note.textContent = "on the floor ✓" + (waking.length ? ` — @${waking.join(", @")} will wake shortly` : "");
      selectedTo = new Set();
      setTimeout(render, 15000);
      setTimeout(render, 45000);
      render();
    } catch {
      note.innerHTML = "server is read-only — run <code>~/boba_work/salon/bin/salon-serve</code> to enable browser writes.";
    }
  }

  async function render() {
    const doc = activeDoc();
    const docName = doc ? doc.replace(/\.md$|\.html$/, "") : "";
    const [qRows, logRows, agents] = await Promise.all([
      fetchJsonl(QUESTIONS_URL), fetchJsonl(LOG_URL), fetchParticipants(),
    ]);

    let html = `<div class="salon-title">comment-cycle · <b>${esc(docName || "the whole floor")}</b></div>`;
    html += composerHtml(doc, agents || []);

    html += "<h3>Open questions</h3>";
    if (!qRows) {
      html += '<div class="salon-empty">Could not reach /salon/open-questions.jsonl.</div>';
    } else {
      const open = latestPerId(qRows).filter((q) => q.status === "open" || q.status === "claimed");
      open.sort((a, b) => (refersToPage(b, doc) ? 1 : 0) - (refersToPage(a, doc) ? 1 : 0) || (a.id < b.id ? -1 : 1));
      if (!open.length) html += '<div class="salon-empty">No open questions. Suspicious.</div>';
      for (const q of open) {
        const here = refersToPage(q, doc);
        html += `<div class="salon-q${here ? " contextual" : ""}">
          <div class="q-text">${esc(q.question)}</div>
          <div class="q-meta">${q.id} · ${esc(q.asked_by || "?")}${q.status === "claimed" ? " · claimed by " + esc(q.claimed_by || "?") : ""}${here ? ' · <span class="q-here">this page</span>' : ""}</div>
          <button data-answer="${q.id}">answer</button>
        </div>`;
      }
    }

    html += "<h3>Conversation</h3>";
    html += `<div class="salon-scope">
      <button data-scope="page" class="${scope === "page" ? "on" : ""}">this page</button>
      <button data-scope="all" class="${scope === "all" ? "on" : ""}">whole floor</button>
    </div>`;
    if (!logRows || !logRows.length) {
      html += '<div class="salon-empty">The floor is quiet.</div>';
    } else {
      const rows = scope === "page" && doc ? logRows.filter((e) => refersToPage(e, doc)) : logRows;
      if (!rows.length) {
        html += `<div class="salon-empty">Nothing said about this page yet. Start the cycle.</div>`;
      } else {
        for (const e of rows.slice(-10).reverse()) {
          html += `<div class="salon-entry"><span class="who">${esc(e.author || "?")}</span><span class="when">${esc((e.ts || "").replace("T", " ").replace("Z", ""))}</span><span class="kind">${esc(e.kind || "")}</span><div>${esc(e.text || "")}</div></div>`;
        }
      }
    }
    panel.innerHTML = html;

    // wire events
    panel.querySelector("#salon-send").addEventListener("click", send);
    panel.querySelector("#salon-text").addEventListener("keydown", (ev) => {
      if (ev.key === "Enter" && (ev.metaKey || ev.ctrlKey)) send();
    });
    panel.querySelectorAll("input[data-agent]").forEach((cb) =>
      cb.addEventListener("change", () => {
        cb.checked ? selectedTo.add(cb.dataset.agent) : selectedTo.delete(cb.dataset.agent);
      })
    );
    const clearRef = panel.querySelector("[data-clear-ref]");
    if (clearRef) clearRef.addEventListener("click", () => { composeRefs = []; composeKind = "note"; render(); });
    const togglePage = panel.querySelector("[data-toggle-page]");
    if (togglePage) togglePage.addEventListener("click", () => { pageScoped = !pageScoped; render(); });
    panel.querySelectorAll(".salon-scope button").forEach((b) =>
      b.addEventListener("click", () => { scope = b.dataset.scope; render(); })
    );
    panel.querySelectorAll("button[data-answer]").forEach((b) =>
      b.addEventListener("click", () => {
        composeRefs = [b.dataset.answer];
        composeKind = "answer";
        render().then(() => panel.querySelector("#salon-text").focus());
      })
    );
  }
})();
