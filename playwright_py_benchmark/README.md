## Introduction
- Execute tests from CI/CD (headless mode): `pytest`
- Execute tests while developing (to see what happens): `pytest --headless`
- Example:
    `pytest --headed layer3_test_cases/regression_suite/web/test_login.py`
    `pytest --headed --video=on layer3_test_cases/regression_suite/web/test_login.py`