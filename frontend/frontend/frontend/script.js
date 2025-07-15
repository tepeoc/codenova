async function askCodeNova() {
  const task = document.getElementById("task").value;
  const content = document.getElementById("content").value;
  const resBox = document.getElementById("response");
  resBox.textContent = "⏳ En cours...";

  const res = await fetch("https://codenova-backend.onrender.com/ask", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ task, content })
  });

  const data = await res.json();
  resBox.textContent = data.response || "Erreur : " + data.error;
}
