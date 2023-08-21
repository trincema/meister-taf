#!/bin/bash
# Bash script to run all regression tests for web app
echo Running Web app regression tests
echo Cleanup test-results directory...
rm -r test-results
pytest --video=on layer3_test_cases/regression_suite/ios/