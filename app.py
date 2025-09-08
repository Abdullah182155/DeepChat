import streamlit as st
from utils.llm import chat_with_openrouter

st.set_page_config(page_title="ChatGPT Clone (OpenRouter + DeepSeek)", page_icon="🤖", layout="wide")

st.title("🤖 ChatGPT Clone (DeepSeek via OpenRouter)")

# Sidebar settings
st.sidebar.header("⚙️ Settings")
temperature = st.sidebar.slider("Temperature", 0.0, 1.5, 0.7, 0.1)
top_p = st.sidebar.slider("Top-p", 0.0, 1.0, 1.0, 0.05)
max_tokens = st.sidebar.slider("Max tokens", 50, 2000, 500, 50)
model = st.sidebar.selectbox(
    "Model",
    [
        "deepseek/deepseek-chat-v3.1:free",
        "openai/gpt-oss-120b:free",
        "qwen/qwen3-coder:free",
        "google/gemma-3n-e2b-it:free"
    ],
    index=0
)
stream_mode = st.sidebar.checkbox("Enable streaming (typing effect)", value=True)

# --- Summary function ---
def summarize_history(messages):
    summary = []
    for msg in messages:
        if msg["role"] in ["user", "assistant"]:
            summary.append(f'{msg["role"].capitalize()}: {msg["content"]}')
    return "\n".join(summary)

# --- Compact history for low tokens ---
MAX_HISTORY_MESSAGES = 10  # Number of recent messages to keep

def compact_history():
    messages = st.session_state["messages"]
    if len(messages) > MAX_HISTORY_MESSAGES + 2:  # +2 for system and possible summary
        system_msg = messages[0]
        to_summarize = messages[1:-MAX_HISTORY_MESSAGES]
        recent = messages[-MAX_HISTORY_MESSAGES:]
        summary_content = summarize_history(to_summarize)
        summary_msg = {"role": "system", "content": f"Summary of previous conversation:\n{summary_content}"}
        st.session_state["messages"] = [system_msg, summary_msg] + recent

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Session state for summary
if "summary" not in st.session_state:
    st.session_state["summary"] = ""

# Display chat history
for msg in st.session_state["messages"]:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# Button to save summary
if st.sidebar.button("Save Summary"):
    st.session_state["summary"] = summarize_history(st.session_state["messages"])
    st.sidebar.success("Summary saved!")

# Optionally display summary in sidebar
if st.session_state["summary"]:
    st.sidebar.subheader("Chat Summary")
    st.sidebar.text_area("Summary", st.session_state["summary"], height=200)

# User input
if prompt := st.chat_input("Type your message..."):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    compact_history()
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            if stream_mode:
                response_container = st.empty()
                partial_text = ""
                for chunk in chat_with_openrouter(
                    st.session_state["messages"],
                    model=model,
                    temperature=temperature,
                    top_p=top_p,
                    max_tokens=max_tokens,
                    stream=True
                ):
                    partial_text += chunk
                    response_container.markdown(partial_text)
                reply = partial_text
            else:
                reply = chat_with_openrouter(
                    st.session_state["messages"],
                    model=model,
                    temperature=temperature,
                    top_p=top_p,
                    max_tokens=max_tokens,
                    stream=False
                )
                st.markdown(reply)

    st.session_state["messages"].append({"role": "assistant", "content": reply})