@ECHO  OFF
REM We have to create a virtual environment to prevent cluttering the user's global Python installation
REM This script creates a virtual environment in the .venv folder and installs the required packages from requirements.txt

REM Check if .venv folder already exists
IF EXIST .venv (
    ECHO Virtual environment already exists. Skipping creation.
    EXIT /B 0
)

REM Inform the user that the virtual environment is being created
ECHO Creating virtual environment...
python -m venv .venv

REM Inform the user that packages are being installed
ECHO Installing required packages...
.\.venv\Scripts\pip.exe install -r python\requirements.txt

ECHO Done! Virtual environment is set up.