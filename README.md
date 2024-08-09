# OpenAI API Client WebUI

A web interface for interacting with the OpenAI API.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation and Running

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

## Note

Make sure to keep your API key secure and never share it publicly. The application will look for an `OPENAI_API_KEY` environment variable. You can set this variable in your system or create a `.env` file in the project root with the following content:

```
OPENAI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual OpenAI API key.
