## How to run tests
- Execute tests from CI/CD (headless mode): `pytest`
- Execute tests while developing (to see what happens): `pytest --headless`
- Example:
    `pytest --headed layer3_test_cases/regression_suite/web/test_login.py`
    `pytest --headed --video=on layer3_test_cases/regression_suite/web/test_login.py`

## Layer 5 - Test Execution
- Config Tutorial: https://www.way2automation.com/taking-screenshots-and-record-videos-using-playwright-python/
- If you have cloned the repo and want to execute the scripts locally from `layer5_test_execution` module,
on Ubuntu system you have to make the bash scripts executable like so: `chmod +x ./run_<script_name>.sh`.
Then just execute the scripts from the project root directory `playwright_py_benchmark` with `./layer5_test_execution/run_regression_web.sh`

## Layer 6 - Generate Documentation
- Code documentation:
    - `sphinx-apidoc -o layer6_documentation/docs ./`

## Other Topics
# Screenshot Testing
- Integrated 