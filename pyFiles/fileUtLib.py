import os

targetDirName = "../generatedFiles"
fileExtension = "txt"

def assureFileExistence(fileName):
    #fileExists = False
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

def deleteFile(fileName, *,fromDir=targetDirName):
    os.system('rm ' + fromDir + '/' + fileName)

def makeDirectory(dirName):
    try:
        os.system('mkdir ' + dirName)
        alreadyExists = False
    except FileExistsError:
        alreadyExists = True
        print("Directory already exists")
    finally:
        return alreadyExists


#check directory exists

#if so, check file exists

#check target directory exists

#if so, make sure file is not already there
def changeFileDirectory(fromDir, toDir, fileName):
    pass
