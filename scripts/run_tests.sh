#!/bin/bash
# run_tests.sh
# Script to run the entire test suite across all services.
# It searches for test directories in the 'services/' folder and executes pytest in each.
#
# Usage:
#   ./run_tests.sh
#
# This script aggregates results for a quick pre-commit check.
# It exits with a non-zero status if any tests fail.

set -e

echo "Running tests across all services..."

# Find and run tests in every 'tests' directory under the 'services' folder
# This command finds all directories named "tests" and runs pytest inside each.
for dir in $(find services -type d -name tests); do
    echo "Running tests in $dir"
    (cd "$dir" && pytest --maxfail=1 --disable-warnings -q)
done

echo "All tests passed successfully."
