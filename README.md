# AI Assistant with Groq

A conversational AI chatbot powered by **Groq** and **Langchain**. This project leverages the power of large language models (LLMs) to provide interactive conversation capabilities. The chatbot remembers context over multiple exchanges, allowing users to interact with a personalized assistant.

## Features
- **Multiple Language Models**: Choose from different available models such as `mixtral-8x7b-32768` and `llama2-70b-4096`.
- **Conversation Memory**: The assistant can retain context over a set number of interactions, providing more relevant responses.
- **Interactive UI**: User-friendly interface using **Streamlit** for easy and intuitive interaction.

## Tech Stack
- **Groq**: Provides access to powerful language models for natural language understanding.
- **Langchain**: Used for managing conversational chains and memory.
- **Streamlit**: A lightweight framework for building interactive web applications.
- **dotenv**: For managing environment variables such as API keys securely.

## Setup

### 1. Clone the Repository
Clone the repository to your local machine using:

```bash
git clone https://github.com/yadivyanshu/ai-assistant-groq.git
cd ai-assistant-groq
```

### 2. Create a Virtual Environment
It is recommended to set up a virtual environment for managing dependencies.

```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install Dependencies
Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root of the project directory to store sensitive information like API keys.

Example `.env` file:

```plaintext
GROQ_API_KEY=your-groq-api-key-here
```

Ensure you replace `your-groq-api-key-here` with your actual API key from Groq. [Create API Key](https://console.groq.com/keys)

### 5. Run the App
Start the Streamlit application:

```bash
streamlit run app.py
```

This will open the chatbot interface in your default browser.

## Usage

Once the app is running, you can interact with the AI assistant through the following features:

- **Select Language Model**: Use the sidebar to choose between available models.
- **Memory Length**: Adjust the conversational memory length to decide how many previous interactions the assistant should remember.
- **Ask Questions**: Type in your questions in the provided text area to receive a response from the assistant.
- **Chat History**: View the history of the conversation displayed below the chat interface.

## Configuration Options

- **Language Model**: Choose between different language models like `mixtral-8x7b-32768` and `llama2-70b-4096`.
- **Memory Length**: Use the slider to adjust how many past interactions the chatbot should remember for context (1 to 10 messages).


## Contributing
Feel free to fork this repository and submit pull requests. For any issues or feature requests, please open an issue on GitHub.

## Acknowledgments
- **Groq** for providing the API and powerful language models.
- **Langchain** for the conversational memory and chain management.
- **Streamlit** for the simple yet powerful UI framework.
