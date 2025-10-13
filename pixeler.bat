@ECHO OFF

REM Check if .venv folder exists, if it doesn't, run install-requirements.bat and activate the virtual environment
IF NOT EXIST .venv (
    REM Inform the user that the virtual environment is being set up
    ECHO Setting up virtual environment and installing requirements...
    CALL install-requirements.bat
)

REM Check if .venv exists, if it does, activate the virtual environment
IF EXIST .venv (
    REM Inform the user that the virtual environment is being activated
    ECHO Activating virtual environment...
    CALL .venv\Scripts\activate
)

ECHO Running pixeler.py...
ECHO #################################
REM Run script using virtual environment's python file.
.\.venv\Scripts\python.exe .\python\pixeler.py