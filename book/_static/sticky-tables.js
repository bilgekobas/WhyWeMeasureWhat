/* Preserve native table semantics, column widths and horizontal scrolling. */
(() => {
  const init = () => {
    const tables = [...document.querySelectorAll(".bd-article table")]
      .filter(table => table.tHead && !table.classList.contains("glossary-spec"));
    tables.forEach(table => table.classList.add("wwmw-sticky-table"));
    let pending = false;
    const update = () => {
      pending = false;
      let top = 0;
      document.querySelectorAll(".bd-header, .bd-header-article").forEach(el => {
        const style = getComputedStyle(el), rect = el.getBoundingClientRect();
        if (style.display !== "none" && ["fixed", "sticky"].includes(style.position)
            && rect.top <= top && rect.bottom > top) top = rect.bottom;
      });
      tables.forEach(table => {
        const head = table.tHead;
        const previous = Number(head.dataset.stickyOffset || 0);
        const rect = head.getBoundingClientRect();
        const naturalTop = rect.top - previous;
        const bottom = table.getBoundingClientRect().bottom;
        const offset = Math.max(0, Math.min(top - naturalTop, bottom - rect.height - naturalTop));
        head.style.transform = offset ? "translateY(" + offset + "px)" : "";
        head.dataset.stickyOffset = String(offset);
      });
    };
    const schedule = () => {
      if (!pending) { pending = true; requestAnimationFrame(update); }
    };
    window.addEventListener("scroll", schedule, { passive: true, capture: true });
    window.addEventListener("resize", schedule, { passive: true });
    window.addEventListener("beforeprint", () => tables.forEach(t => {
      t.tHead.style.transform = ""; t.tHead.dataset.stickyOffset = "0";
    }));
    window.addEventListener("afterprint", schedule);
    const observer = new ResizeObserver(schedule);
    tables.forEach(table => observer.observe(table));
    if (document.fonts) document.fonts.ready.then(schedule);
    schedule();
  };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
