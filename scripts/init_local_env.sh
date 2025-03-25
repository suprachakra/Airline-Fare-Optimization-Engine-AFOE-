#!/bin/bash
# init_local_env.sh
# Script to initialize the local development environment.
# - Sets up Python virtual environments.
# - Installs necessary dependencies.
# - Configures Git hooks for pre-commit checks.

set -e

echo "Initializing local development environment..."

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip and install dependencies for backend services (example)
pip install --upgrade pip
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

# Install Node.js dependencies for the front-end (if applicable)
if [ -f ../frontend/web-portal/package.json ]; then
    cd ../frontend/web-portal
    npm install
    cd -
fi

# Set up Git pre-commit hook (example)
HOOKS_DIR=".git/hooks"
PRE_COMMIT_HOOK="$HOOKS_DIR/pre-commit"
echo "#!/bin/bash" > $PRE_COMMIT_HOOK
echo "echo 'Running lint and tests...'" >> $PRE_COMMIT_HOOK
echo "./scripts/lint_and_format.sh" >> $PRE_COMMIT_HOOK
echo "./scripts/run_tests.sh" >> $PRE_COMMIT_HOOK
chmod +x $PRE_COMMIT_HOOK

echo "Local development environment initialized successfully."
