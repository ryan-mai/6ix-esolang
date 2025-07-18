import sys
from interpreter import run_varlang

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if not filename.endswith('.six'):
            print("Vro wyd: we need in the 6ix slide the .six file")
            sys.exit(1)
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                code = file.read()
            run_varlang(code)
        except FileNotFoundError:
            print(f"ERROR: File '{filename}' not found")
            sys.exit(1)
        except Exception as e:
            print(f"Broski fam: {e}")
            sys.exit(1)
    else:
        print("6ix Esolang Interpreter")
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