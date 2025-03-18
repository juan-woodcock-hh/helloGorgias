# Echo Chatbot

A simple Streamlit application that creates a chat interface which echoes back whatever the user types.

## Description

Echo Chatbot is a minimalist demo application built with Streamlit that showcases the basics of creating a chat interface. The app maintains a chat history and responds by repeating the user's input - demonstrating the fundamental structure of a conversational UI.

## Features

- Clean, intuitive chat interface
- Persistent chat history within the session
- Simple user input handling
- Visual distinction between user and chatbot messages

## Installation

1. Clone this repository or download the source code
2. Install the required dependencies:

```bash
pip install streamlit
```

## Usage
1. Run the application
```
streamlit run app.py
```
2. Open your web browser and navigate to the provided URL (typically http://localhost:8501)
3. Type messages in the input field and click "Send" to see the Echo Chatbot respond

## Code Structure
The application consists of a single Python file with the following components:

- Title and introduction
- Chat history initialization and display
- User input field and send button
- Logic to process user input and generate responses

##Customization
This basic structure can be extended to create more complex chatbots by:

- Integrating with LLMs or other AI services
- Adding memory or context tracking
- Implementing more sophisticated response generation
- Enhancing the UI with custom styling

## Requirements

- Python 3.6+
- Streamlit

## License
- MIT License

## Acknowledgments

- Built with Streamlit
