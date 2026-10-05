#empty list
shopping_list = []

# loop to show list again and again
while True:
    choice = input("add / remove / show / done:").strip().lower()
    if choice == "add":
        item = input("What item do you want to add?").strip()
        shopping_list.append(item)
        print(item, "added.")

    elif choice == "remove":
        item = input("What item do you want to remove?").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "removed.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if len(shopping_list) == 0:
            print("Your shopping list is empty.")
        else:
            for item in shopping_list:
                print(item)

    elif choice == "done":
        print("Goodbye! Happy shopping.")
        break

    else:
        print("Please type add, remove, show or done")