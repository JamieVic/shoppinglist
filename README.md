# Shopping List
## About the Project
The shopping list program allows user to create a list of items they need at the grocery store. The program provides users the ability to add and delete items, view their shopping list and clear it when they're done.
## How to Use
This program works using any Python interpreter. The user is prompted to make a selection out of four commands. The program's four functionalities include the following:
- Adding items: items are added one by one.
- Deleting items: items are deleted one by one.
- Viewing list: the entire shopping list can be viewed.
- Clearing list: the entire shopping list can be cleared.
The shopping list data is stored in a text file. The data is accessed by a Python list to allow the program to view and alter the data in the text file.
## How it Works
Two variables have been created to access the text file and the Python list. The cycleList() function is created to make it easy for the items in the text file to be read by the program. The function is called to prevent repetitive code being typed everytime the list needs to be accessed.

The command input variable takes either add, delete, view or clear as valid entries which is checked by an if/else statement.

If items need to be added, a while loop runs to allow users to enter the item they wish to add. The addItem input variable takes the value and adds it inside the text file and adds a new line afterwards in case a new item needs to be added again. The capitalize() and rstrip() string methods keep the item inputs clean if the user decides to view the entire list later. Once the user is done adding items, they can leave the input prompt blank and hit Enter to go back to selecting a command.

Deleting items works similarly to how adding items works program-wise. The difference is the items in the text file are collected inside the Python list that was created at the beginning of the program. This allows the .remove() list method to find the item to remove, and to loop through the list and re-add the remaining items to the text file.

Viewing the shopping list is simple, the cycleList() function is called and a for loop runs to print each item in the console.

Clearing the list is also quite simple, an input prompt appears asking the user if they're certain on clearing the whole shopping list. If they confirm that it is the choice they want to make, the text file is overwritten so that the text file is empty.

A while loop keeps the whole program running until the user hits Enter with a blank response in the command input.
