@echo off
echo === CI Build Started ===
echo Checking source files...
dir
echo === Running Application Tests ===
python -m unittest discover -s tests
if errorlevel 1 (
    echo TESTS FAILED
    exit /b 1
)
echo === Running Application ===
python app.py
echo === CI Build Completed Successfully ===
exit /b 0
