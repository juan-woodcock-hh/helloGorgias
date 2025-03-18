import streamlit as st

st.title("Echo Chatbot")

# Intro message
st.write("This is a demo app. I am programmed just to repeat what you say.\nHappy chat!")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Display chat history
# We'll show each message as if it came from a "user" or "assistant"
for message in st.session_state["chat_history"]:
    if message["role"] == "user":
        st.write(f"**You:** {message['content']}")
    else:
        st.write(f"**Echo:** {message['content']}")

# Input field for the user
user_input = st.text_input("Type your message here and click 'Send'")

# Button to send
if st.button("Send"):
    if user_input.strip():
        # User's message
        st.session_state["chat_history"].append({"role": "user", "content": user_input})
        # Echo repeats the same text
        st.session_state["chat_history"].append({"role": "assistant", "content": user_input})

        # Optionally clear the input (re-run to refresh the UI)
        st.rerun()
