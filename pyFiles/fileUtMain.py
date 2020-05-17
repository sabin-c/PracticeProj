import fileUtilityStuff
import os

targetDirName = "../generatedFiles"
fileExtension = "txt"

def checkFileExistence(fileName):
    fileExists = False
    try:
        fileToOpen = openFile(fileName)
        fileExists = True
    except FileNotFoundError:
        fileExists = False
        print("The file {} does not exist, creating it now".format(fileName))
        makeFile(fileName)
        fileToOpen = openFile(fileName)
    finally:
        fileToOpen.close()
    return fileExists

def openFile(fileName):
    fileToOpen = open(targetDirName + '/' + fileName)
    return fileToOpen

def makeFile(fileName):
    os.system('touch '+ targetDirName + '/' + fileName)

def deleteFile(fileName):
    os.system('rm ' + targetDirName + '/' + fileName)

def doStuff():
    nm = "someName.txt"
    deleteFile(nm)

if __name__ == "__main__":
    doStuff()


