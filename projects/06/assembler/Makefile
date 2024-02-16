# Makefile for running main.py with Python 3

# This Makefile checks if Python 3 is installed and then runs the main.py script with the provided arguments.

# Rule to check if Python 3 is installed
check_python:
	@python3 -c "import sys" || (echo "Python 3 is not installed. Please install Python 3."; exit 1)

# Rule to run the main.py script
run_main: check_python
	@python3 Main.py $(ARGS)

# Default rule to run when executing 'make'
# This rule depends on 'run_main', which ensures Python 3 is installed before running the script
all: run_main
