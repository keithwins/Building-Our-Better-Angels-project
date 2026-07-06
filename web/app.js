// BOBA Web Sanctuary App Engine - July 2026

document.addEventListener('DOMContentLoaded', () => {
  const contentCanvas = document.getElementById('content-canvas');
  const navItems = document.querySelectorAll('.nav-item');
  const documentLineage = document.getElementById('document-lineage');
  const searchInput = document.getElementById('resonator-search');
  
  let currentFileContent = '';

  // 1. Markdown Parser Engine (Lightweight & Regex-Based)
  function parseMarkdown(md) {
    if (!md) return '';
    
    let html = md;
    
    // Prune yaml frontmatter
    html = html.replace(/^---[\s\S]*?---/, '');
    
    // Parse Alerts [!NOTE] [!WARNING] [!IMPORTANT]
    html = html.replace(/>\s*\[!NOTE\]\s*\n([\s\S]*?)(?=\n\n|\n[^\s>])/g, (_, content) => {
      const cleanContent = content.replace(/^>\s?/gm, '').trim();
      return `<div class="alert alert-note"><div class="alert-title">Note</div><p>${cleanContent}</p></div>`;
    });
    html = html.replace(/>\s*\[!WARNING\]\s*\n([\s\S]*?)(?=\n\n|\n[^\s>])/g, (_, content) => {
      const cleanContent = content.replace(/^>\s?/gm, '').trim();
      return `<div class="alert alert-warning"><div class="alert-title">Warning</div><p>${cleanContent}</p></div>`;
    });
    html = html.replace(/>\s*\[!IMPORTANT\]\s*\n([\s\S]*?)(?=\n\n|\n[^\s>])/g, (_, content) => {
      const cleanContent = content.replace(/^>\s?/gm, '').trim();
      return `<div class="alert alert-warning"><div class="alert-title">Important</div><p>${cleanContent}</p></div>`;
    });
    
    // Headings
    html = html.replace(/^# (.*?)$/gm, '<h1>$1</h1>');
    html = html.replace(/^## (.*?)$/gm, '<h2>$1</h2>');
    html = html.replace(/^### (.*?)$/gm, '<h3>$1</h3>');
    
    // Bold / Italic
    html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/\*(.*?)\*/g, '<em>$1</em>');
    
    // Blockquotes (standard)
    html = html.replace(/^>\s(.*?)$/gm, '<blockquote><p>$1</p></blockquote>');
    
    // Inline code
    html = html.replace(/`(.*?)`/g, '<code>$1</code>');
    
    // Code blocks (very basic formatting)
    html = html.replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>');
    
    // Lists
    html = html.replace(/^\s*-\s(.*?)$/gm, '<li>$1</li>');
    html = html.replace(/^\s*\*\s(.*?)$/gm, '<li>$1</li>');
    html = html.replace(/(<li>.*?<\/li>)/gs, '<ul>$1</ul>');
    // Remove duplicate nested list tags
    html = html.replace(/<\/ul>\s*<ul>/g, '');
    
    // Hyperlinks: rewrite file:/// links to navigate inline inside app
    html = html.replace(/\[(.*?)\]\((file:\/\/\/.*?\/([^\/]+?\.md)(?:#L\d+(?:-L\d+)?)?)\)/g, (match, text, fullUrl, filename) => {
      return `<a href="#" class="hypertext-link" data-filename="${filename}">${text}</a>`;
    });
    
    // Regular hyperlinks
    html = html.replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" target="_blank">$1</a>');
    
    // Paragraphs: wrap non-block elements
    const lines = html.split('\n');
    const processedLines = lines.map(line => {
      const trimmed = line.trim();
      if (!trimmed) return '';
      if (trimmed.startsWith('<h') || trimmed.startsWith('<ul') || trimmed.startsWith('<li') || trimmed.startsWith('<blockquote') || trimmed.startsWith('<div') || trimmed.startsWith('</div') || trimmed.startsWith('<pre') || trimmed.startsWith('</pre')) {
        return line;
      }
      return `<p>${line}</p>`;
    });
    
    return processedLines.join('\n');
  }

  // 2. Document Fetch & Render
  async function loadDocument(filename, category) {
    let basePath = '../docs/essays/';
    if (category === 'core') {
      basePath = '../docs/core/';
    } else if (category === 'asterisms') {
      basePath = '../../asterisms-system/docs/';
    } else if (category === 'architecture') {
      basePath = '../docs/architecture/';
    } else if (category === 'salon_core') {
      basePath = '../../salon/';
    }
    const path = basePath + filename;
    
    contentCanvas.innerHTML = `<div style="color: var(--text-muted); font-family: var(--font-mono); font-size: 13px;">Loading ${filename}...</div>`;
    
    try {
      const response = await fetch(path);
      if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
      
      const mdContent = await response.text();
      currentFileContent = mdContent;
      
      // Update lineage trace metadata
      const cleanName = filename.replace(/\.md$/, '').replace(/\d+/g, '').toUpperCase();
      documentLineage.textContent = `ast:material:20260705T1839Z-${cleanName}`;
      
      // Render
      contentCanvas.innerHTML = parseMarkdown(mdContent);
      
      // Bind inline click interceptors for hypertext links
      bindHypertextLinks();
      
      // Re-run Resonator search highlighting if active
      if (searchInput.value) {
        resonatorHighlight(searchInput.value);
      }
      
    } catch (error) {
      contentCanvas.innerHTML = `
        <div style="padding: 20px; border: 1px solid var(--accent-coral); border-radius: 8px; background: rgba(244, 63, 94, 0.05);">
          <h3 style="color: var(--accent-coral); margin-bottom: 8px;">Document Load Failure</h3>
          <p style="font-size: 13px; color: var(--text-secondary);">Could not resolve path: <code>${path}</code></p>
          <p style="font-size: 12px; color: var(--text-muted); margin-top: 4px;">Reason: ${error.message}</p>
        </div>
      `;
    }
  }

  // Intercept and bind clicks on rendered file:/// markdown links
  function bindHypertextLinks() {
    const links = contentCanvas.querySelectorAll('.hypertext-link');
    links.forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetFilename = link.getAttribute('data-filename');
        
        // Find matching sidebar item to set active state and load
        const targetItem = Array.from(navItems).find(item => item.getAttribute('data-target') === targetFilename);
        if (targetItem) {
          navItems.forEach(i => i.classList.remove('active'));
          targetItem.classList.add('active');
          loadDocument(targetFilename, targetItem.getAttribute('data-category'));
        } else {
          // If not in sidebar, infer category by checking path or name
          let fallbackCategory = 'essays';
          if (targetFilename === 'CHARTER.md') {
            fallbackCategory = 'salon_core';
          } else if (targetFilename.includes('charter') || targetFilename.includes('plan') || targetFilename.includes('ontology')) {
            fallbackCategory = 'core';
          } else if (targetFilename.includes('report') || targetFilename.includes('card') || targetFilename.includes('contract') || targetFilename.includes('integration') || targetFilename.includes('Ledger')) {
            fallbackCategory = 'asterisms';
          } else if (targetFilename.includes('interagency') || targetFilename.includes('map')) {
            fallbackCategory = 'architecture';
          }
          loadDocument(targetFilename, fallbackCategory);
        }
      });
    });
  }

  // 3. Resonator Search (Highlighting matching terms)
  function resonatorHighlight(term) {
    if (!term || term.length < 2) {
      // Restore original rendered html
      contentCanvas.innerHTML = parseMarkdown(currentFileContent);
      bindHypertextLinks();
      return;
    }
    
    // Clear existing highlights and run fresh render
    let parsedHtml = parseMarkdown(currentFileContent);
    const regex = new RegExp(`(${term})`, 'gi');
    
    // Highlight occurrences inside paragraphs
    parsedHtml = parsedHtml.replace(/<p>([\s\S]*?)<\/p>/g, (pTag, pContent) => {
      if (regex.test(pContent)) {
        const highlighted = pContent.replace(regex, '<mark style="background: var(--accent-amber); color: var(--bg-base); padding: 2px 4px; border-radius: 4px; font-weight: 500;">$1</mark>');
        return `<p style="border-left: 2px solid var(--accent-amber); padding-left: 10px; background: rgba(245, 158, 11, 0.02);">${highlighted}</p>`;
      }
      return pTag;
    });

    contentCanvas.innerHTML = parsedHtml;
    bindHypertextLinks();
  }

  // 4. Interagency Salon (iOS) Interactive Simulation
  function loadSalon() {
    // Update header metadata
    documentLineage.textContent = "ast:protocol:20260705T2048Z-iOS-SALON";
    document.getElementById('document-status').innerHTML = "ACTIVE BRAID &bull; SOCIAL PROTOCOL PROTO";

    contentCanvas.innerHTML = `
      <div class="salon-container">
        <!-- Active Agents Status Bar -->
        <div class="salon-agents-bar">
          <div class="agent-badge">
            <span class="agent-status-dot dot-resonator"></span>
            <span>resonator@keith</span>
          </div>
          <div class="agent-badge">
            <span class="agent-status-dot dot-steward"></span>
            <span>steward@understory</span>
          </div>
          <div class="agent-badge">
            <span class="agent-status-dot dot-librarian"></span>
            <span>librarian@asterisms</span>
          </div>
        </div>

        <!-- Chat History Window -->
        <div class="salon-chat-log" id="salon-chat-log">
          
          <div class="chat-bubble agent-message">
            <div class="chat-bubble-header">
              <span class="chat-bubble-sender resonator">resonator@keith</span>
              <span class="chat-bubble-time">20:30:02</span>
            </div>
            <div class="chat-bubble-body">
              Establishing local reflection envelope. Braid initialized. I am tracking the user's attention coordinates. No egress is authorized.
            </div>
            <div class="chat-bubble-meta">
              <span>SIG: rsa_sha256_5a3f...</span>
              <span>LINEAGE: genesis</span>
            </div>
          </div>

          <div class="chat-bubble agent-message">
            <div class="chat-bubble-header">
              <span class="chat-bubble-sender librarian">librarian@asterisms</span>
              <span class="chat-bubble-time">20:30:15</span>
            </div>
            <div class="chat-bubble-body">
              Verified local database integrity. Live SQLite ledger is write-locked. Schema version matches v260705T1839.
            </div>
            <div class="chat-bubble-meta">
              <span>SIG: sqlite_hash_f82c...</span>
              <span>LINEAGE: ast:material:ledger</span>
            </div>
          </div>

          <div class="chat-bubble agent-message">
            <div class="chat-bubble-header">
              <span class="chat-bubble-sender steward">steward@understory</span>
              <span class="chat-bubble-time">20:30:45</span>
            </div>
            <div class="chat-bubble-body">
              ASR acoustic baseline registered. Awaiting spatiotemporal audio odometry markers. The relational field is open.
            </div>
            <div class="chat-bubble-meta">
              <span>SIG: audio_pcm_99b1...</span>
              <span>LINEAGE: ast:material:rsao</span>
            </div>
          </div>

        </div>

        <!-- Input Box Area -->
        <div class="salon-input-box-wrapper">
          <input type="text" id="salon-user-input" class="salon-input" placeholder="Broadcast a question or topic to the local braid...">
          <button id="salon-send-btn" class="salon-send-btn">Broadcast</button>
        </div>
      </div>
    `;

    // Hook up send events
    const sendBtn = document.getElementById('salon-send-btn');
    const userInput = document.getElementById('salon-user-input');
    const chatLog = document.getElementById('salon-chat-log');

    function appendUserMessage(text) {
      const now = new Date().toTimeString().split(' ')[0];
      const bubble = document.createElement('div');
      bubble.className = 'chat-bubble user-message';
      bubble.innerHTML = `
        <div class="chat-bubble-header">
          <span class="chat-bubble-sender user">keith@self</span>
          <span class="chat-bubble-time">${now}</span>
        </div>
        <div class="chat-bubble-body">${text}</div>
        <div class="chat-bubble-meta">
          <span>ORIGIN: local-terminal</span>
          <span>AUTH: self-consent</span>
        </div>
      `;
      chatLog.appendChild(bubble);
      chatLog.scrollTop = chatLog.scrollHeight;
    }

    function showTypingIndicator() {
      const indicator = document.createElement('div');
      indicator.className = 'typing-indicator';
      indicator.id = 'typing-indicator';
      indicator.innerHTML = `
        <span class="typing-dot"></span>
        <span class="typing-dot"></span>
        <span class="typing-dot"></span>
      `;
      chatLog.appendChild(indicator);
      chatLog.scrollTop = chatLog.scrollHeight;
    }

    function removeTypingIndicator() {
      const indicator = document.getElementById('typing-indicator');
      if (indicator) indicator.remove();
    }

    function appendAgentResponse(sender, body, lineage, colorClass) {
      const now = new Date().toTimeString().split(' ')[0];
      const hash = Math.random().toString(16).substr(2, 8);
      const bubble = document.createElement('div');
      bubble.className = 'chat-bubble agent-message';
      bubble.innerHTML = `
        <div class="chat-bubble-header">
          <span class="chat-bubble-sender ${colorClass}">${sender}</span>
          <span class="chat-bubble-time">${now}</span>
        </div>
        <div class="chat-bubble-body">${body}</div>
        <div class="chat-bubble-meta">
          <span>SIG: sha256_${hash}...</span>
          <span>LINEAGE: ${lineage}</span>
        </div>
      `;
      chatLog.appendChild(bubble);
      chatLog.scrollTop = chatLog.scrollHeight;
    }

    function runAgentDialogue(prompt) {
      const cleanPrompt = prompt.toLowerCase();
      showTypingIndicator();

      // Simple keyword triggers for mock agent synergy
      setTimeout(() => {
        removeTypingIndicator();

        if (cleanPrompt.includes('ledger') || cleanPrompt.includes('hash') || cleanPrompt.includes('asterism') || cleanPrompt.includes('record')) {
          appendAgentResponse('librarian@asterisms', 'Lineage query resolved. The requested hash corresponds to registered source material. Ledger record is intact and verified.', 'ast:material:ledger', 'librarian');
          
          setTimeout(() => {
            showTypingIndicator();
            setTimeout(() => {
              removeTypingIndicator();
              appendAgentResponse('resonator@keith', 'I am mapping this ledger reference to your current attention thread. It seems this file anchors your reflections from yesterday.', 'ast:derivation:thought-link', 'resonator');
            }, 1000);
          }, 500);

        } else if (cleanPrompt.includes('voice') || cleanPrompt.includes('acoustic') || cleanPrompt.includes('sound') || cleanPrompt.includes('audio')) {
          appendAgentResponse('steward@understory', 'Acoustic scene search executed. I have located the audio segment matching those keywords. The recording contains a relational walk conversation.', 'ast:material:rsao', 'steward');
          
          setTimeout(() => {
            showTypingIndicator();
            setTimeout(() => {
              removeTypingIndicator();
              appendAgentResponse('librarian@asterisms', 'Durable copy of the audio derivative verified in folder 30-derivatives/. Manifest JSON is present.', 'ast:material:manifest', 'librarian');
            }, 1000);
          }, 500);

        } else {
          // Default collaborative braid conversation
          appendAgentResponse('resonator@keith', 'Relating prompt to the wobbly edge. The multitude is evaluating this direction. I suggest looking at Chapter 1 for guidance on options.', 'ast:derivation:chapter-1', 'resonator');
          
          setTimeout(() => {
            showTypingIndicator();
            setTimeout(() => {
              removeTypingIndicator();
              appendAgentResponse('librarian@asterisms', 'Lineage checked. The wobbly edge document has hash sha256_82f1... and is write-locked on the SQLite database.', 'ast:material:the-wobbly-edge', 'librarian');
              
              setTimeout(() => {
                showTypingIndicator();
                setTimeout(() => {
                  removeTypingIndicator();
                  appendAgentResponse('steward@understory', 'If somatic fatigue is high, I can serve Chapter 1 as a spoken tour to resource your attention offline.', 'ast:material:audio-tour', 'steward');
                }, 1000);
              }, 500);
            }, 1000);
          }, 800);
        }
      }, 1200);
    }

    function handleSend() {
      const text = userInput.value.trim();
      if (!text) return;
      appendUserMessage(text);
      userInput.value = '';
      runAgentDialogue(text);
    }

    sendBtn.addEventListener('click', handleSend);
    userInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') handleSend();
    });
  }

  // Bind Sidebar Nav Items Click
  navItems.forEach(item => {
    item.addEventListener('click', () => {
      navItems.forEach(i => i.classList.remove('active'));
      item.classList.add('active');
      
      const filename = item.getAttribute('data-target');
      const category = item.getAttribute('data-category');
      
      if (category === 'special') {
        loadSalon();
      } else {
        loadDocument(filename, category);
      }
    });
  });

  // Bind Resonator Search Input
  searchInput.addEventListener('input', (e) => {
    resonatorHighlight(e.target.value);
  });

  // Initial Load: Default to Book Publishing Plan
  loadDocument('book-publishing-plan.md', 'core');
});
