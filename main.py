#!/usr/bin/env python3
"""
VarLang Interpreter - Main Entry Point

Now expects source files with the .six extension.
"""

import sys
from interpreter import run_varlang

def main():
    """Main entry point for the VarLang interpreter"""
    
    if len(sys.argv) > 1:
        # Run from .six file
        filename = sys.argv[1]
        if not filename.endswith('.six'):
            print("ERROR: Please provide a .six file")
            sys.exit(1)
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                code = file.read()
            run_varlang(code)
        except FileNotFoundError:
            print(f"ERROR: File '{filename}' not found")
            sys.exit(1)
        except Exception as e:
            print(f"ERROR: {e}")
            sys.exit(1)
    else:
        # Interactive mode
        print("VarLang Interpreter")
        print("Type 'exit' to quit")
        print("-" * 30)
        
        while True:
            try:
                line = input("varlang> ")
                if line.strip().lower() == 'exit':
                    break
                if line.strip():
                    run_varlang(line)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break

if __name__ == "__main__":
    main()