import fileUtLib

targetDirName = "../generatedFiles"
fileExtension = "txt"

def main():
    nm = "someName.txt"
    fileUtLib.assureFileExistence(nm)

if __name__ == "__main__":
    main()


