function sendText() {
    const userInput = document.getElementById("userInput").value;

    axios.post("/generate", {
        text: userInput
    })
    .then(response => {
        document.getElementById("outputBox").value = response.data.output;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}
