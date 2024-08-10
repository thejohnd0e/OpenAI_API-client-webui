# OpenAI API Client WebUI

## Overview

The Universal OpenAI Chat Client is a versatile and user-friendly application that allows interaction with various AI models through OpenAI-compatible APIs. Built with Python using the Gradio library for the interface and the OpenAI library for API interactions, this client supports a wide range of language models and API endpoints.

## Features

- **Customizable API Settings**: Easily switch between different API endpoints and models.
- **Adjustable Model Parameters**: Fine-tune your interactions by modifying parameters like temperature, top_p, and token limits.
- **Custom System Prompts**: Create specialized AI assistants by defining custom system prompts.
- **Profile Management**: Save and load different configuration profiles for quick switching between setups.
- **Real-time Streaming**: Experience responsive conversations with real-time streaming of AI responses.
- **User-friendly Interface**: Intuitive chat interface with easy-to-use settings panel.


A web interface for interacting with the OpenAI API.

## Requirements

- Python 3.7 or higher
- pip (Python package installer)

## Installation and Running


1. Clone the repository:
   ```
   git clone https://github.com/yourusername/universal-openai-chat-client.git
   cd universal-openai-chat-client
   ```

2. Install the required dependencies:
   ```
   pip install openai gradio
    ```




1. Run the application:
   ```
   python main.py
   ```

 Open your web browser and navigate to the local URL provided in the console (typically `http://127.0.0.1:7860`).

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



### Windows

1. Double-click on `install.bat` to set up the environment and install dependencies.
2. After installation, double-click on `run.bat` to start the application.

### macOS/Linux

1. Open a terminal in the project directory.
2. Run the following commands:
   ```
   chmod +x nstall.sh run.sh
   ./install.sh
   ./run.sh
   ```

The application should now be running. Open your web browser and navigate to `http://localhost:5000` to access the web interface.

## Manual Installation and Running

If you prefer to run commands manually:

1. Create a virtual environment:
   - Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   - Windows: `python main.py`
   - macOS/Linux: `python3 main.py`


