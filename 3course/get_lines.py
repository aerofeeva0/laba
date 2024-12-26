import argparse

try:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)  # Add required=True to enforce file argument
    args = parser.parse_args()

    def count_lines(filename):  # count_lines now accepts filename
        with open(filename, 'r') as f: # Use with statement for proper file handling
            print(sum(1 for _ in f))
    def main():
        count_lines(args.file)
    if __name__ == "__main__":
        main()
except FileNotFoundError:  # Catch only FileNotFoundError
    print(0)
except Exception as e: #Catch other exceptions, and print a message showing the error
    print(f"An error occurred: {e}")