import fileUtLib
import os

targetDirName = "../generatedFiles"
fileExtension = "txt"

def doStuff():
    nm = "someName.txt"
    fileUtLib.assureFileExistence(nm)

if __name__ == "__main__":
    doStuff()


