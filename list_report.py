# starting list
items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

#loop through the list and print each item numbered
for index, item in enumerate(items, start=1):
    print(f"{index}. {item}")

# count how many item names have more than 4 letters
count = 0
for item in items:
    if len(item) > 4:
        count = count + 1
        print(item, "has more than 4 letters:")

# longest item name using loop comparison
longest_item_name = items[0]
for item in items:
    if len(item) > len(longest_item_name):
        longest_item_name = item
print("Longest item name: ", longest_item_name)