@echo off
if exist venv (
    echo Opening autocraft.py...
    start autocraft.py
) else (
    echo Creating a virtual environment...
    python -m venv venv
    call venv\Scripts\activate

    echo Installing dependencies...
    pip install -r requirements.txt

    echo Installation complete.
    echo Opening autocraft.py...
    start autocraft.py
)
