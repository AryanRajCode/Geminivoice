@echo off

REM Function to check if Python is installed
:check_python
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Installing Python...
    REM Download and install Python from the official website
    REM Modify the download link according to your system architecture
    curl -o python_installer.exe https://www.python.org/ftp/python/3.10.3/python-3.10.3-amd64.exe
    python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python_installer.exe
    echo Python installed successfully.
) else (
    echo Python is already installed.
)

REM Function to install dependencies
:install_dependencies
echo Installing dependencies...
REM Install dependencies using pip
pip install -r requirements.txt
echo Dependencies installed successfully.

REM Run the Python main script
echo Running main.py...
python main.py
