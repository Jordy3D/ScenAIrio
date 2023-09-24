@ECHO OFF

@TITLE Prepare and Install
ECHO Installing requirements...
pip install -r requirements.txt

ECHO Creating secret.py...
IF NOT EXIST secret.py (
    ECHO openaikey = 'YOUR OPENAI TOKEN HERE >> secret.py
)