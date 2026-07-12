// BOBA orientation surface — thin cut 2026-07-10
// Loads only public-allowlist.json. Real Salon is salon.js (not a mock).

document.addEventListener("DOMContentLoaded", () => {
  const contentCanvas = document.getElementById("content-canvas");
  const documentLineage = document.getElementById("document-lineage");
  const documentStatus = document.getElementById("document-status");
  const searchInput = document.getElementById("resonator-search");
  const navRoot = document.getElementById("nav-root");

  let allowlist = null;
  let byFile = new Map();
  let currentFileContent = "";
  let currentDoc = null;

  const DIR_TO_PATH = {
    core: "../docs/core/",
    essays: "../docs/essays/",
    architecture: "../docs/architecture/",
    method: "../docs/method/",
    manuscript: "../docs/manuscript/",
    "reader-v0-root": "../docs/manuscript/reader-v0/",
    "reader-v0": "../docs/manuscript/reader-v0/sections/",
  };

  function escapeRegExp(s) {
    return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  }

  function parseMarkdown(md) {
    if (!md) return "";
    let html = md;
    html = html.replace(/^---[\s\S]*?---/, "");
    html = html.replace(/^# (.*?)$/gm, "<h1>$1</h1>");
    html = html.replace(/^## (.*?)$/gm, "<h2>$1</h2>");
    html = html.replace(/^### (.*?)$/gm, "<h3>$1</h3>");
    html = html.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
    html = html.replace(/\*(.*?)\*/g, "<em>$1</em>");
    html = html.replace(/^>\s(.*?)$/gm, "<blockquote><p>$1</p></blockquote>");
    html = html.replace(/`(.*?)`/g, "<code>$1</code>");
    html = html.replace(/```([\s\S]*?)```/g, "<pre><code>$1</code></pre>");
    html = html.replace(/^\s*-\s(.*?)$/gm, "<li>$1</li>");
    html = html.replace(/(<li>.*?<\/li>)/gs, "<ul>$1</ul>");
    html = html.replace(/<\/ul>\s*<ul>/g, "");
    html = html.replace(
      /\[(.*?)\]\((file:\/\/\/.*?\/([^\/]+?\.md)(?:#L\d+(?:-L\d+)?)?)\)/g,
      (_, text, _u, filename) =>
        `<a href="#" class="hypertext-link" data-filename="${filename}">${text}</a>`
    );
    html = html.replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
    const lines = html.split("\n");
    return lines
      .map((line) => {
        const trimmed = line.trim();
        if (!trimmed) return "";
        if (
          trimmed.startsWith("<h") ||
          trimmed.startsWith("<ul") ||
          trimmed.startsWith("<li") ||
          trimmed.startsWith("<blockquote") ||
          trimmed.startsWith("<div") ||
          trimmed.startsWith("<pre") ||
          trimmed.startsWith("</")
        ) {
          return line;
        }
        return `<p>${line}</p>`;
      })
      .join("\n");
  }

  function buildNav(docs) {
    const sections = new Map();
    for (const doc of docs) {
      if (!sections.has(doc.nav)) sections.set(doc.nav, []);
      sections.get(doc.nav).push(doc);
    }
    navRoot.innerHTML = "";
    for (const [title, items] of sections) {
      const section = document.createElement("div");
      section.className = "nav-section";
      section.innerHTML = `<div class="nav-section-title">${title}</div>`;
      const ul = document.createElement("ul");
      ul.className = "nav-list";
      items.forEach((doc, i) => {
        const li = document.createElement("li");
        li.className = "nav-item" + (title === "Invitation" && i === 0 ? " active" : "");
        li.textContent = doc.label;
        li.dataset.target = doc.file;
        li.dataset.dir = doc.dir;
        li.dataset.id = doc.id;
        li.addEventListener("click", () => selectDoc(doc, li));
        ul.appendChild(li);
      });
      section.appendChild(ul);
      navRoot.appendChild(section);
    }
  }

  function selectDoc(doc, liEl) {
    document.querySelectorAll(".nav-item").forEach((i) => i.classList.remove("active"));
    if (liEl) liEl.classList.add("active");
    else {
      const match = document.querySelector(`.nav-item[data-target="${CSS.escape(doc.file)}"]`);
      if (match) match.classList.add("active");
    }
    loadDocument(doc);
  }

  async function loadDocument(doc) {
    currentDoc = doc;
    const basePath = DIR_TO_PATH[doc.dir];
    if (!basePath) {
      contentCanvas.innerHTML = `<p>Unknown dir: ${doc.dir}</p>`;
      return;
    }
    const path = basePath + doc.file;
    contentCanvas.innerHTML = `<div style="color: var(--text-muted); font-family: var(--font-mono); font-size: 13px;">Loading ${doc.file}...</div>`;
    try {
      const response = await fetch(path);
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const mdContent = await response.text();
      currentFileContent = mdContent;
      documentLineage.textContent = `docs/${doc.dir}/${doc.file}`;
      documentStatus.textContent = "allowlisted · invitation spine";
      contentCanvas.innerHTML = parseMarkdown(mdContent);
      bindHypertextLinks();
      if (searchInput.value) resonatorHighlight(searchInput.value);
    } catch (error) {
      contentCanvas.innerHTML = `
        <div style="padding: 20px; border: 1px solid var(--accent-coral); border-radius: 8px;">
          <h3 style="color: var(--accent-coral);">Document Load Failure</h3>
          <p><code>${path}</code></p>
          <p>${error.message}</p>
        </div>`;
    }
  }

  function bindHypertextLinks() {
    contentCanvas.querySelectorAll(".hypertext-link").forEach((link) => {
      link.addEventListener("click", (e) => {
        e.preventDefault();
        const filename = link.getAttribute("data-filename");
        const doc = byFile.get(filename);
        if (doc) selectDoc(doc);
        else {
          documentStatus.textContent = "link not on public allowlist";
        }
      });
    });
  }

  function resonatorHighlight(term) {
    if (!term || term.length < 2) {
      contentCanvas.innerHTML = parseMarkdown(currentFileContent);
      bindHypertextLinks();
      return;
    }
    let parsedHtml = parseMarkdown(currentFileContent);
    const regex = new RegExp(`(${escapeRegExp(term)})`, "gi");
    parsedHtml = parsedHtml.replace(/<p>([\s\S]*?)<\/p>/g, (pTag, pContent) => {
      regex.lastIndex = 0;
      if (regex.test(pContent)) {
        regex.lastIndex = 0;
        const highlighted = pContent.replace(
          regex,
          '<mark style="background: var(--accent-amber); color: var(--bg-base); padding: 2px 4px; border-radius: 4px;">$1</mark>'
        );
        return `<p style="border-left: 2px solid var(--accent-amber); padding-left: 10px;">${highlighted}</p>`;
      }
      return pTag;
    });
    contentCanvas.innerHTML = parsedHtml;
    bindHypertextLinks();
  }

  searchInput.addEventListener("input", (e) => resonatorHighlight(e.target.value));

  fetch("./public-allowlist.json")
    .then((r) => r.json())
    .then((data) => {
      allowlist = data;
      byFile = new Map(data.documents.map((d) => [d.file, d]));
      buildNav(data.documents);
      const first = data.documents[0];
      if (first) {
        const li = document.querySelector(".nav-item.active") || document.querySelector(".nav-item");
        selectDoc(first, li);
      }
    })
    .catch((err) => {
      contentCanvas.innerHTML = `<p>Could not load public-allowlist.json: ${err.message}</p>`;
    });
});
