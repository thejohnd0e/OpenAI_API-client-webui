@echo off
python -m venv venv
call venv\Scripts\activate.bat
pip install -r requirements.txt
echo Installation completed. You can now run the application using run.bat
pause
