#!/usr/bin/env python3
"""
AgentLang interpreter - Run .al files
Usage: python -m agentlang.cli script.al
"""

import sys
import os
from pathlib import Path

# Import transpiler and runtime
from .transpiler import transpile
from .runtime import __extract, load_file

def run_agentlang(filepath):
    """Run an AgentLang script file"""

    # Read the .al file
    with open(filepath, 'r') as f:
        agentlang_code = f.read()

    # Transpile to Python
    python_code = transpile(agentlang_code)

    # Execute with AgentLang runtime available
    exec(python_code, {'__extract': __extract, 'load_file': load_file, 'print': print})

def main():
    if len(sys.argv) < 2:
        print("Usage: python agentlang.py <script.al>")
        print("       python agentlang.py --transpile <script.al>  # Show transpiled code only")
        sys.exit(1)

    # Handle flags
    if sys.argv[1] == '--transpile':
        if len(sys.argv) < 3:
            print("Usage: python agentlang.py --transpile <script.al>")
            sys.exit(1)
        filepath = sys.argv[2]
        with open(filepath, 'r') as f:
            code = f.read()
        print(transpile(code))
        sys.exit(0)

    filepath = sys.argv[1]

    # Check file exists and has .al extension
    if not Path(filepath).exists():
        print(f"Error: File '{filepath}' not found")
        sys.exit(1)

    if not filepath.endswith('.al'):
        print(f"Warning: File '{filepath}' doesn't have .al extension")

    # Run the AgentLang script
    try:
        run_agentlang(filepath)
    except Exception as e:
        print(f"Error running AgentLang script: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()