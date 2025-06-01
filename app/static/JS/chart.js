export function renderChartFromData(dataId, chartId) {
  const dataEl = document.getElementById(dataId);
  const oldChartEl = document.getElementById(chartId);

  if (!dataEl || !oldChartEl) {
    console.warn("❌ Chart elements not found.");
    return;
  }

  try {
    const history = JSON.parse(dataEl.textContent);
    const x = history.map(d => d.Date);
    const y = history.map(d => d.Close);

    // ✅ Remove old chart container completely
    const newChartEl = document.createElement("div");
    newChartEl.id = chartId;
    newChartEl.style.width = "100%";
    newChartEl.style.height = "400px";
    oldChartEl.replaceWith(newChartEl);

    // ✅ Now render into fresh element
    Plotly.newPlot(chartId, [{
      x: x,
      y: y,
      type: "scatter",
      mode: "lines+markers",
      line: { color: "#FFD700" }
    }], {
      title: {
        text: "Stock Price History",
        font: { color: "#FFD700", size: 24 }
      },
      paper_bgcolor: "#1e1e1e",
      plot_bgcolor: "#1e1e1e",
      xaxis: {
        title: { text: "Date", font: { color: "#FFD700" } },
        tickfont: { color: "#FFD700" },
        gridcolor: "#333"
      },
      yaxis: {
        title: { text: "Price (USD)", font: { color: "#FFD700" } },
        tickfont: { color: "#FFD700" },
        gridcolor: "#333"
      },
      margin: { t: 50, l: 60, r: 30, b: 60 }
    });

  } catch (e) {
    console.error("❌ Failed to render chart:", e);
  }
}
