#!/bin/bash

# Activate the virtual environment
source venv/Scripts/activate

# Run the test suite
pytest

# Return the pytest exit code
exit $?