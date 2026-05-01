document.addEventListener("DOMContentLoaded", function () {
  const search = document.getElementById("glossary-search");
  const suggestions = document.getElementById("glossary-suggestions");

  // ===== SEARCH FUNCTIONALITY =====
  if (search && suggestions) {
    const entries = Array.from(
      document.querySelectorAll(
        ".sd-dropdown, .dropdown, details, div[class*='dropdown']"
      )
    );

    const entryData = entries
      .map(entry => {
        const titleEl =
          entry.querySelector(".sd-summary-title") ||
          entry.querySelector(".dropdown-title") ||
          entry.querySelector(".admonition-title") ||
          entry.querySelector("summary") ||
          entry.querySelector("button");

        const title = titleEl ? titleEl.innerText.trim() : "";
        const section = entry.closest("section");
        const id = section ? section.id : "";

        return { entry, title, id };
      })
      .filter(item => item.title && item.id);

    function updateSuggestions(query) {
      suggestions.innerHTML = "";

      if (query.length < 3) return;

      entryData
        .filter(item =>
          item.title.toLowerCase().includes(query.toLowerCase())
        )
        .forEach(item => {
          const option = document.createElement("option");
          option.value = item.title;
          suggestions.appendChild(option);
        });
    }

    function openAndJumpTo(title) {
      const match = entryData.find(
        item => item.title.toLowerCase() === title.toLowerCase()
      );

      if (!match) return;

      // Open dropdown if needed
      if (match.entry.tagName.toLowerCase() === "details") {
        match.entry.open = true;
      }

      const button = match.entry.querySelector("button");
      if (button && button.getAttribute("aria-expanded") !== "true") {
        button.click();
      }

      // Scroll to entry
      window.location.hash = match.id;
      match.entry.scrollIntoView({
        behavior: "smooth",
        block: "start"
      });
    }

    search.addEventListener("input", function () {
      const query = search.value.trim();
      updateSuggestions(query);

      const exact = entryData.find(
        item => item.title.toLowerCase() === query.toLowerCase()
      );

      if (exact) {
        openAndJumpTo(query);
      }
    });

    search.addEventListener("keydown", function (event) {
      if (event.key === "Enter") {
        event.preventDefault();
        openAndJumpTo(search.value.trim());
      }
    });

    search.addEventListener("change", function () {
      openAndJumpTo(search.value.trim());
    });
  }

  // ===== BACK TO TOP BUTTON =====
  const topButton = document.getElementById("back-to-top");

  if (topButton) {
    topButton.addEventListener("click", function () {
      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    });
  }
});