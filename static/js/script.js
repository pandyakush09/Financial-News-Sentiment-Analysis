document.getElementById("sentimentForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const newsUrl = document.getElementById("newsUrl").value;
    const resultDiv = document.getElementById("result");

    resultDiv.classList.add('hidden'); // Hide result initially
    resultDiv.innerText = ""; // Clear previous result

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ news_url: newsUrl })
        });

        const data = await response.json();

        if (response.ok) {
            resultDiv.innerText = `Sentiment: ${data.sentiment}`;
            resultDiv.className = data.sentiment.toLowerCase() === "positive" ? "positive" : "negative";
        } else {
            resultDiv.innerText = data.error || "An error occurred.";
            resultDiv.className = "negative";
        }

        resultDiv.classList.remove("hidden");

    } catch (error) {
        resultDiv.innerText = "An error occurred while processing your request.";
        resultDiv.className = "negative";
        resultDiv.classList.remove("hidden");
    }
});
