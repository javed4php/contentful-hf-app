async function generate() {
  const prompt = document.getElementById("prompt").value;
  const outputDiv = document.getElementById("output");

  outputDiv.innerHTML = "⏳ Generating...";
  const response = await fetch("http://localhost:5000/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt })
  });

  const data = await response.json();
  outputDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
}
