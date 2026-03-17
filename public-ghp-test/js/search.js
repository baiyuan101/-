async function bootSearch() {
  const input = document.querySelector("[data-search-input]");
  const status = document.querySelector("[data-search-status]");
  const results = document.querySelector("[data-search-results]");

  if (!input || !status || !results) {
    return;
  }

  let records = [];

  const loadIndex = async () => {
    const candidates = [
      new URL("index.json", window.location.href).toString(),
      new URL("./index.json", window.location.href).toString(),
      new URL("../index.json", window.location.href).toString(),
      "/index.json"
    ];

    for (const url of candidates) {
      try {
        const response = await fetch(url);
        if (!response.ok) {
          continue;
        }
        return await response.json();
      } catch (error) {
        // Try the next candidate path.
      }
    }

    throw new Error("Search index could not be loaded.");
  };

  try {
    records = await loadIndex();
    status.textContent = `Loaded ${records.length} searchable pages.`;
  } catch (error) {
    status.textContent = "Search index could not be loaded.";
    return;
  }

  const render = (items, query) => {
    results.innerHTML = "";

    if (!query) {
      status.textContent = `Loaded ${records.length} searchable pages. Start typing to filter them.`;
      return;
    }

    if (!items.length) {
      status.textContent = `No results for "${query}".`;
      return;
    }

    status.textContent = `${items.length} result${items.length === 1 ? "" : "s"} for "${query}".`;

    for (const item of items) {
      const li = document.createElement("li");
      li.className = "search-result";

      const date = item.date ? `<div class="quiet">${item.date}</div>` : "";
      const tags = item.tags && item.tags.length
        ? `<div class="quiet">${item.tags.join(", ")}</div>`
        : "";
      const summary = item.summary ? `<p>${item.summary}</p>` : "";

      li.innerHTML = `
        <a href="${item.permalink}">${item.title}</a>
        ${date}
        ${summary}
        ${tags}
      `;

      results.appendChild(li);
    }
  };

  input.addEventListener("input", (event) => {
    const query = event.target.value.trim().toLowerCase();

    if (!query) {
      render([], "");
      return;
    }

    const filtered = records.filter((item) => {
      const haystack = [
        item.title,
        item.summary,
        item.section,
        ...(item.tags || [])
      ]
        .join(" ")
        .toLowerCase();

      return haystack.includes(query);
    });

    render(filtered, event.target.value.trim());
  });
}

document.addEventListener("DOMContentLoaded", bootSearch);
