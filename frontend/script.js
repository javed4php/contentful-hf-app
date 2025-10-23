const API_BASE = "https://contentful-hf-app.onrender.com/"; // replace after deploy

async function generate() {
  const prompt = document.getElementById("prompt").value;
  const outputDiv = document.getElementById("output");
  outputDiv.innerHTML = "⏳ Generating...";

  try {
    const response = await fetch(`${API_BASE}/generate`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt }),
    });

    if (!response.ok) {
      throw new Error(`Server error: ${response.status}`);
    }

    const data = await response.json();

    // Assuming your backend returns { output: "some text" }
    outputDiv.innerHTML = `<pre>${data.output}</pre>`;
  } catch (error) {
    outputDiv.innerHTML = `❌ Error: ${error.message}`;
    console.error("Error generating:", error);
  }
}

