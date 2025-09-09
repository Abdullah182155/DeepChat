# 🤖 ChatGPT Clone (Streamlit + OpenAI)

A simple **ChatGPT-style app** built with
[Streamlit](https://streamlit.io/) and the official [OpenAI Python
SDK](https://pypi.org/project/openai/).\
Supports both **streaming** (typing effect) and **non-streaming**
responses, with settings for temperature, top-p, max tokens, and model
selection.

------------------------------------------------------------------------

## 📦 Features

-   💬 Chat interface with memory (keeps conversation in session).\
-   ⚡ Streaming (typing effect) or non-streaming responses.\
-   ⚙️ Adjustable parameters:
    -   `temperature`
    -   `top_p`
    -   `max_tokens`
    -   `model` (choose between deepseek/deepseek-chat-v3.1, openai/gpt-oss-120b, wen/qwen3-coder,
        etc.)\
-   🎨 Clean UI with Streamlit's new `st.chat_message` and
    `st.chat_input`.

------------------------------------------------------------------------

## 🚀 Installation & Setup

### 1. Clone the repository

``` bash
git clone https://github.com/Abdullah182155/chatgpt-clone.git
cd chatgpt-clone
```

### 2. Create a virtual environment (recommended)

``` bash
python -m venv .venv
source .venv/bin/activate   # on macOS/Linux
.venv\Scripts\activate      # on Windows
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Copy `.env.example` to `.env`:

``` bash
cp .env.example .env
```

Open `.env` and paste your OpenAI API key:

``` bash
OPENAI_API_KEY=your_api_key_here
```

*(Get your API key from
[OpenAI](https://platform.openai.com/account/api-keys)).*

------------------------------------------------------------------------

## ▶️ Run the app

``` bash
streamlit run app.py
```

Then open your browser at <http://localhost:8501>.

------------------------------------------------------------------------

## 🖥️ Usage

1.  Type your message in the chat input box.\
2.  The assistant replies with either:
    -   **Streaming mode** → response appears word-by-word (typing
        effect).\
    -   **Non-streaming mode** → response appears instantly.\
3.  Adjust **temperature**, **top_p**, **max_tokens**, or switch models
    in the sidebar.

------------------------------------------------------------------------

## 📂 Project Structure

    chatgpt-clone/
    │── app.py              # Main Streamlit app
    │── requirements.txt    # Dependencies
    │── README.md           # This file
    │── .env.example        # Example env file for API key
    │── utils/
    │    └── llm.py         # OpenAI client wrapper

------------------------------------------------------------------------

## 🔧 Example Commands

Run app with streaming enabled (typing effect):

``` bash
streamlit run app.py
```

Change settings from the sidebar: - Increase creativity → raise
`temperature`.\
- More deterministic responses → lower `temperature` or `top_p`.\
- Change model → pick from dropdown (`gpt-4o`, `gpt-4o-mini`, etc.).

------------------------------------------------------------------------

## ⚠️ Notes

-   Requires **Python 3.8+**.\
-   You must have a valid **OpenAI API key** with quota.\
-   Session state is **per browser tab** --- closing the tab resets the
    chat.

------------------------------------------------------------------------

## 🚀 Live Demo
👉 [Try it on Streamlit Cloud](https://deepchat-abdullahemara.streamlit.app/)
