#!/bin/bash
# lint_and_format.sh
# Script to run linters and code formatters for all languages used in the project.
# This ensures code quality and style consistency across all services.
#
# Usage:
#   ./lint_and_format.sh
#
# For Python, this example uses flake8 (linter) and black (formatter check).
# For JavaScript, it uses eslint. Adjust commands as needed for your project.

set -e

echo "Running lint and format checks..."

# Check Python files using flake8 and black (format check)
echo "Linting Python code..."
if command -v flake8 &> /dev/null; then
    flake8 .
else
    echo "flake8 not found. Please install it."
fi

echo "Checking Python code format with black..."
if command -v black &> /dev/null; then
    black --check .
else
    echo "black not found. Please install it."
fi

# Check JavaScript/JSX files using eslint
echo "Linting JavaScript/JSX code..."
if command -v eslint &> /dev/null; then
    eslint .
else
    echo "eslint not found. Skipping JS linting. Please install it if needed."
fi

echo "Lint and format checks completed successfully."
