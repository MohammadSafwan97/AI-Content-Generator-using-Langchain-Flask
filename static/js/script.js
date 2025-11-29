async function sendText() {
    const userInput = document.getElementById("userInput").value;
    const mode = document.getElementById("modeSelect").value;

    const btn = document.getElementById("submitBtn");
    const btnText = document.getElementById("btnText");
    const loader = document.getElementById("loader");

    // Show loading state
    btn.disabled = true;
    btnText.textContent = "Generating...";
    loader.classList.remove("hidden");

    try {
        const response = await axios.post("/generate", {
            text: userInput,
            mode: mode
        });

        document.getElementById("outputBox").value = response.data.output;
    } catch (err) {
        console.error(err);
        document.getElementById("outputBox").value = "Error generating content.";
    }

    // Reset button
    btn.disabled = false;
    btnText.textContent = "Generate";
    loader.classList.add("hidden");
}
