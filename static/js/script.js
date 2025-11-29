async function sendText() {
    const userInput = document.getElementById("userInput").value;

    try {
        const response = await axios.post("/generate", {
            text: userInput
        });

        document.getElementById("outputBox").value = response.data.output;
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("outputBox").value = "Error generating content.";
    }
}
