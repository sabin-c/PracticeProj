import heapsOfFun




if __name__ == '__main__':
    hp = heapsOfFun.myHeapThingy()
    optionDict = {'a':'add new value', 'c' : 'check contents', 't' : 'terminate', 's' : 'show array', 'h' : 'heap sort'}
    programIsRunning = True
    while programIsRunning:
        print("=========================================================================")
        for entry in optionDict:
            print("({}): {}".format(entry, optionDict[entry]))
        print("=========================================================================")
        choice = input("Choose an option\n")
        if choice not in optionDict:
            print("\nPlease choose a valid option")
        elif choice == 'a':
            intVal = input("\nenter a number\n")
            heapsOfFun.addItem(hp.h, intVal)
        elif choice == 'c':
            heapsOfFun.checkValues(hp.h)
        elif choice == 's':
            heapsOfFun.printHeap(hp.h)
        elif choice == 'h':
            heapsOfFun.makeHeap(hp.h)
        elif choice == 't':
            programIsRunning = False



