document.addEventListener("DOMContentLoaded", function () {
  const search = document.getElementById("glossary-search");
  const suggestions = document.getElementById("glossary-suggestions");

  const entries = Array.from(
    document.querySelectorAll(".sd-dropdown, .dropdown, details, div[class*='dropdown']")
  );

  function getTitle(entry) {
    const titleEl =
      entry.querySelector(".sd-summary-title") ||
      entry.querySelector(".dropdown-title") ||
      entry.querySelector(".admonition-title") ||
      entry.querySelector("summary") ||
      entry.querySelector("button");

    return titleEl ? titleEl.innerText.trim() : "";
  }

  function findLabelForEntry(entry) {
    let node = entry.previousElementSibling;

    while (node) {
      if (node.id && node.id.startsWith("label-")) {
        return node.id;
      }

      const labelled = node.querySelector && node.querySelector("[id^='label-']");
      if (labelled) {
        return labelled.id;
      }

      node = node.previousElementSibling;
    }

    return "";
  }

  const entryData = entries
    .map(entry => {
      return {
        entry: entry,
        title: getTitle(entry),
        id: findLabelForEntry(entry)
      };
    })
    .filter(item => item.title && item.id);

  function openDropdown(entry) {
    if (!entry) return;

    if (entry.tagName.toLowerCase() === "details") {
      entry.open = true;
      return;
    }

    const button =
      entry.querySelector("button.sd-summary-title") ||
      entry.querySelector("button.dropdown-toggle") ||
      entry.querySelector("button");

    if (button && button.getAttribute("aria-expanded") !== "true") {
      button.click();
    }
  }

  function updateSuggestions(query) {
    if (!suggestions) return;

    suggestions.innerHTML = "";
    if (query.length < 3) return;

    entryData
      .filter(item => item.title.toLowerCase().includes(query.toLowerCase()))
      .forEach(item => {
        const option = document.createElement("option");
        option.value = item.title;
        suggestions.appendChild(option);
      });
  }

  function openAndJumpToTitle(title) {
    const match = entryData.find(
      item => item.title.toLowerCase() === title.toLowerCase()
    );

    if (!match) return;

    openDropdown(match.entry);

    history.replaceState(null, "", "#" + match.id);

    setTimeout(() => {
      match.entry.scrollIntoView({
        behavior: "smooth",
        block: "start"
      });
    }, 150);
  }

  function openAndJumpToHash() {
  const id = window.location.hash.replace("#", "");
  if (!id) return;

  const target = document.getElementById(id);
  if (!target) return;

  let dropdown = null;

  // Case 1: label is inside the dropdown
  dropdown = target.closest(".sd-dropdown, .dropdown, details, div[class*='dropdown']");

  // Case 2: label is immediately before the dropdown
  if (!dropdown) {
    let node = target.nextElementSibling;

    while (node) {
      if (
        node.matches &&
        node.matches(".sd-dropdown, .dropdown, details, div[class*='dropdown']")
      ) {
        dropdown = node;
        break;
      }

      const nested = node.querySelector &&
        node.querySelector(".sd-dropdown, .dropdown, details, div[class*='dropdown']");

      if (nested) {
        dropdown = nested;
        break;
      }

      node = node.nextElementSibling;
    }
  }

  if (!dropdown) return;

  openDropdown(dropdown);

  setTimeout(() => {
    dropdown.scrollIntoView({
      behavior: "smooth",
      block: "start"
    });
  }, 150);
}

  if (search && suggestions) {
    search.addEventListener("input", function () {
      const query = search.value.trim();
      updateSuggestions(query);

      const exact = entryData.find(
        item => item.title.toLowerCase() === query.toLowerCase()
      );

      if (exact) {
        openAndJumpToTitle(query);
      }
    });

    search.addEventListener("keydown", function (event) {
      if (event.key === "Enter") {
        event.preventDefault();
        openAndJumpToTitle(search.value.trim());
      }
    });

    search.addEventListener("change", function () {
      openAndJumpToTitle(search.value.trim());
    });
  }

  // ===== BACK TO TOP BUTTON =====
  const topButton = document.getElementById("back-to-top");

  function updateTopButtonVisibility() {
    if (!topButton) return;

    if (window.scrollY > 350) {
      topButton.classList.add("visible");
    } else {
      topButton.classList.remove("visible");
    }
  }

  if (topButton) {
    topButton.addEventListener("click", function () {
      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    });

    updateTopButtonVisibility();

    window.addEventListener("scroll", updateTopButtonVisibility);
  }

  setTimeout(openAndJumpToHash, 300);

  window.addEventListener("hashchange", function () {
    setTimeout(openAndJumpToHash, 100);
  });
});