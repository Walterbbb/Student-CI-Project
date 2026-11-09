# Student-CI-Project

## Structure
- `app.py` - application with `add_numbers(a, b)`
- `tests/test_app.py` - unit tests
- `Jenkins-build.bat` - build commands used by the Jenkins job

## Run the application
    python app.py

## Run the tests
    python -m unittest discover -s tests

## CI
A Jenkins job (`Student-CI-Project`) pulls this repo, runs the tests, and
reports pass/fail. It is triggered by a GitHub webhook on push.
A small change here :)
