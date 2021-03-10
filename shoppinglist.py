listFile = "TEXT FILE"
shoppingList = []
def cycleList():
    f = open(listFile, "r")
    listItems = f.readlines()
    [shoppingList.append(line.rstrip("\n"))for line in listItems]
while True:
    print("Commands: (a)dd, (d)elete, (v)iew, (c)lear")
    command = input("Enter Command: ").lower()
    if len(command) == 0:
        break
    else:
        if command == "a" or command == "add":
            print("Press Enter where there's no text to stop adding items.")
            while True:
                addItem = input("Enter item: ").capitalize().rstrip()
                if len(addItem) == 0:
                    break
                else:
                    f = open(listFile, "a")
                    f.write(addItem + "\n")
                    print(addItem + " added.")
                    f.close()
        elif command == "d" or command == "delete":
            cycleList()
            print("# SHOPPING LIST #")
            for x in shoppingList:
                print(x)
            print("Press Enter where there's no text to stop deleting items.")
            while True:
                delItem = input("Enter item: ").capitalize().rstrip()
                if len(delItem) == 0:
                    break
                else:
                    try:
                        shoppingList.remove(delItem)
                        f = open(listFile, "w")
                        for y in shoppingList:
                            f.write(y + "\n")
                        f.close()
                        print(delItem + " deleted.")
                    except:
                        print(delItem + " doesn't exist in your shopping list.")
        elif command == "v" or command == "view":
            cycleList()
            print("# SHOPPING LIST #")
            for x in shoppingList:
                print(x)
        elif command == "c" or command == "clear":
            clearPrompt = input("Are you sure you want to clear the shopping list? (Y/N): ").lower()
            try:
                if clearPrompt == "y" or clearPrompt == "yes":
                    f = open(listFile, "w")
                    f.write("")
                    f.close()
                    print("Shopping list cleared.")
                elif clearPrompt == "n" or clearPrompt == "no":
                    print("Shopping list not cleared.")
            except:
                print("Your response could not be recognised.")
        else:
            print("Invalid command entered.")
