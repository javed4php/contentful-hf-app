const API_BASE = "https://contentful-hf-app.onrender.com/"; // replace after deploy

async function generate() {
  const prompt = document.getElementById("prompt").value;
  const outputDiv = document.getElementById("output");
  outputDiv.innerHTML = "⏳ Generating...";

  const response = await fetch(`${API_BASE}/generate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt })
  });

  const data = await response.json();
  outputDiv.innerHTML = `<pre>${data.output}</pre>`;
}
