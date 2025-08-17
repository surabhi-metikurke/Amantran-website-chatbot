document.addEventListener("DOMContentLoaded", () => {
    const chatBox = document.getElementById("chat-box");
    const inputField = document.getElementById("user-input");

 
    function appendMessage(sender, message, isAI = false) {
        const chatBox = document.getElementById("chat-box");
        const messageElement = document.createElement("div");
        messageElement.classList.add(isAI ? "ai-message" : "user-message");
        messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
        chatBox.appendChild(messageElement);
        chatBox.scrollTop = chatBox.scrollHeight;
    }
    

    async function fetchAIResponse(userMessage) {
        appendMessage("AI", "🤖 Thinking...", true);
    
        try {
            const response = await fetch("http://127.0.0.1:5000/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: userMessage })
            });
    
            const data = await response.json();
            console.log("Backend Response:", data);  // ✅ Logs response in console
    
            const aiReply = data.response || "Sorry, I couldn't process your request.";
    
            chatBox.removeChild(chatBox.lastChild);
            appendMessage("AI", aiReply, true);
        } catch (error) {
            console.error("Error fetching AI response:", error);
            chatBox.removeChild(chatBox.lastChild);
            appendMessage("AI", "⚠️ Oops! Something went wrong. Please try again.", true);
        }
    }
    

    window.sendMessage = function () {
        const userMessage = inputField.value.trim();
        if (userMessage === "") return;

        appendMessage("You", userMessage);
        inputField.value = "";

        fetchAIResponse(userMessage);
    };
});
