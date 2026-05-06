
// docs/assets/js/citations.js
// Citation popover for MkDocs Material.
// Supports:
//   #ref-13
//   #ref-13-15
//   #ref-13–15
//   #ref-13,15,18
// References must be rendered as:
//   1. ... {#ref-1}
// which becomes: <li id="ref-1">...</li>

(async function () {

  const REFERENCES_URL = "/09_references/09_01_references/";

  // ---------- Popup UI ----------
  const pop = document.createElement("div");
  pop.id = "cite-pop";
  pop.style.position = "fixed";
  pop.style.maxWidth = "560px";
  pop.style.zIndex = "9999";
  pop.style.display = "none";
  pop.style.padding = "12px 14px";
  pop.style.border = "1px solid rgba(0,0,0,0.15)";
  pop.style.borderRadius = "12px";
  pop.style.boxShadow = "0 10px 30px rgba(0,0,0,0.16)";
  pop.style.background = "white";
  pop.style.fontSize = "0.95rem";
  pop.style.lineHeight = "1.4";
  pop.style.color = "#111";
  document.body.appendChild(pop);

  const closePop = () => (pop.style.display = "none");

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closePop();
  });

  document.addEventListener("click", (e) => {
    if (pop.style.display === "none") return;
    if (!pop.contains(e.target) && !e.target.closest("a")) closePop();
  });

  function escapeHtml(s) {
    return (s || "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  // ---------- Load references ----------
  let refMap = null;

  async function loadReferences() {
    if (refMap) return refMap;
    refMap = {};

    let res;
    try {
      res = await fetch(REFERENCES_URL, { credentials: "same-origin" });
    } catch (err) {
      console.warn("[citations] Could not fetch references page:", err);
      return refMap;
    }

    if (!res.ok) {
      console.warn("[citations] References page fetch failed:", res.status);
      return refMap;
    }

    const html = await res.text();
    const doc = new DOMParser().parseFromString(html, "text/html");

    const items = doc.querySelectorAll('[id^="ref-"]');
    items.forEach((el) => {
      const id = el.id;
      const n = parseInt(id.replace("ref-", ""), 10);
      if (!Number.isFinite(n)) return;
      refMap[n] = el.textContent.trim();
    });

    return refMap;
  }

  // ---------- Parse reference IDs (ranges + lists) ----------
  function parseRefIdsFromHref(href) {
    const h = href.split("#")[1] || "";
    if (!h.startsWith("ref-")) return [];

    const raw = h.slice(4);
    const parts = raw.split(",").map(s => s.trim()).filter(Boolean);

    const ids = [];
    for (const part of parts) {
      const p = part.replace("–", "-");
      const range = p.match(/^(\d+)-(\d+)$/);
      if (range) {
        let a = parseInt(range[1], 10);
        let b = parseInt(range[2], 10);
        if (!Number.isFinite(a) || !Number.isFinite(b)) continue;
        if (b < a) [a, b] = [b, a];
        for (let i = a; i <= b; i++) ids.push(i);
        continue;
      }
      if (/^\d+$/.test(p)) ids.push(parseInt(p, 10));
    }

    return Array.from(new Set(ids)).sort((x, y) => x - y);
  }

  // ---------- Show popup ----------
  function showPopMulti(targetEl, ids, map) {
    const rect = targetEl.getBoundingClientRect();
    const margin = 10;

    const itemsHtml = ids.map((n) => {
      const txt = map[n] || "Reference text not found.";
      return `
        <div style="margin-top:10px;">
          <div style="font-weight:600;">[${n}]</div>
          <div style="margin-top:4px;">${escapeHtml(txt)}</div>
          <div style="margin-top:6px;">
            <a href="${REFERENCES_URL}#ref-${n}" style="font-size:0.9rem;">
              Open in References
            </a>
          </div>
        </div>
      `;
    }).join("");

    pop.innerHTML = `
      <div style="display:flex;justify-content:space-between;gap:12px;">
        <div style="font-weight:600;">
          References ${ids[0]}${ids.length > 1 ? "–" + ids[ids.length - 1] : ""}
        </div>
        <button id="cite-close"
          style="border:0;background:transparent;font-size:18px;cursor:pointer;">×</button>
      </div>
      ${itemsHtml}
    `;

    pop.querySelector("#cite-close").onclick = closePop;
    pop.style.display = "block";

    const popRect = pop.getBoundingClientRect();
    let top = rect.bottom + margin;
    let left = rect.left;

    if (left + popRect.width > window.innerWidth - margin)
      left = window.innerWidth - popRect.width - margin;
    if (top + popRect.height > window.innerHeight - margin)
      top = rect.top - popRect.height - margin;

    if (top < margin) top = margin;
    if (left < margin) left = margin;

    pop.style.top = `${top}px`;
    pop.style.left = `${left}px`;
  }

  // ---------- Intercept citation clicks ----------
  document.addEventListener("click", async (e) => {
    const a = e.target.closest("a");
    if (!a) return;

    const href = (a.getAttribute("href") || "").trim();
    if (!href.includes("#ref-")) return;

    if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || a.target === "_blank")
      return;

    const ids = parseRefIdsFromHref(href);
    if (!ids.length) return;

    e.preventDefault();

    const map = await loadReferences();
    showPopMulti(a, ids, map);
  });

})();
