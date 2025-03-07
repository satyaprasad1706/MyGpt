🤖 MyGpt

🌟 Overview
MyGpt is a simple chatbot application built using Streamlit and powered by the Gemini API. This project replicates the functionalities of ChatGPT, allowing users to interact with an AI-powered assistant in a conversational format.

🚀 Features
- 🖥️ User-friendly chat interface using Streamlit.
- 🗂️ Stores conversation history within the session.
- 🔗 Integrates with Google's Gemini API for AI-powered responses.
- 💬 Real-time message exchange between user and assistant.

📥 Installation
1. Clone the repository:
   ```
   git clone <repository_url>
   cd MyGpt
   ```
2. Install dependencies:
   ```
   pip install streamlit requests
   ```
3. Run the application:
   ```
   streamlit run MyGpt.py
   ```

🔑 API Key Setup
Replace the existing API key in `MyGpt.py` with your own valid API key from Google’s Gemini API:
```
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=YOUR_API_KEY"
```

🎯 Usage
1. ▶️ Run the script using Streamlit.
2. ✍️ Enter a prompt in the chat input box.
3. 🤖 The chatbot responds based on the Gemini API's output.

📅 Development & History
- 📆 Project Creation Date: November 29, 2024
- 🛠️ Technology Stack: Python, Streamlit, Gemini API
- 🎯 Purpose: To create a simple AI-powered chatbot similar to ChatGPT.

🔮 Future Improvements
- 🎨 Improve UI design with enhanced styling.
- 🖼️ Add support for multimodal inputs (images, voice, etc.).
- 🔐 Implement authentication for API security.

📜 License
This project is for educational and personal use. Ensure compliance with the Google Gemini API terms when deploying the application.



👨‍💻 Author: Vakkalagadda Hima Venkata Satya Prasad  
📆 Date: November 29, 2024

