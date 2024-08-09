#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "Installation completed. You can now run the application using ./run.sh"