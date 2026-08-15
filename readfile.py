from pathlib import Path

def readfiles(filename: str):
    path = Path(filename)
    if path.is_file():
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    else:
        print(f"File not found: {filename}")

if __name__ == "__main__":
    filename=input("Enter the filename to read: ")
    if(filename):
        readfiles(filename)
    else:
        print("No filename provided.")
