# Universal OpenAI API Client

## Overview

The Universal OpenAI API Client is a versatile and user-friendly application that allows interaction with various AI models through OpenAI-compatible APIs. Built with Python using the Gradio library for the interface and the OpenAI library for API interactions, this client supports a wide range of language models and API endpoints.

## Features

- **Customizable API Settings**: Easily switch between different API endpoints and models.
- **Adjustable Model Parameters**: Fine-tune your interactions by modifying parameters like temperature, top_p, and token limits.
- **Custom System Prompts**: Create specialized AI assistants by defining custom system prompts.
- **Profile Management**: Save and load different configuration profiles for quick switching between setups.
- **Real-time Streaming**: Experience responsive conversations with real-time streaming of AI responses.
- **User-friendly Interface**: Intuitive chat interface with easy-to-use settings panel.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/thejohnd0e/OpenAI_API-client-webui.git
   cd universal-openai-chat-client
   ```

2. Install the required dependencies:
   ```
   pip install openai gradio
   ```

## Usage

1. Run the application:
   ```
   python openai_chat_client.py
   ```

2. Open your web browser and navigate to the local URL provided in the console (typically `http://127.0.0.1:7860`).

3. In the settings panel:
   - Enter your API key
   - Adjust the base URL if using a different API endpoint
   - Select or enter the model name
   - Customize the system prompt and other parameters as needed

4. Start chatting with the AI in the main chat interface!

## Configuration Profiles

- To save your current configuration, enter a profile name and click "Save current settings".
- To load a saved profile, select it from the dropdown and click "Load selected profile".

## Customizing the AI Assistant

You can create specialized AI assistants by modifying the system prompt. For example:
- For a coding assistant: "You are a helpful assistant specialized in programming and software development."
- For a creative writing aide: "You are a creative writing assistant, helping with story ideas and character development."
- For a financial advisor: "You are a financial advisor, providing information on investments and market trends."

## Contributing

Contributions to improve the Universal OpenAI Chat Client are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project uses the [OpenAI API](https://openai.com/blog/openai-api) and is compatible with other OpenAI-like APIs.
- The user interface is built with [Gradio](https://www.gradio.app/), an excellent library for creating web-based ML interfaces.

## Disclaimer

This tool is for educational and research purposes. Ensure you comply with the terms of service of the API you're using.
