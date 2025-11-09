n = int(input("Number of items: "))


fruits = []
for i in range(n):
    item = input("Enter item: ")
    fruits.append(item)

print("Your list:", fruits)


search_item = input("What do you want to search: ")


found = False
for index, item in enumerate(fruits):
    if item.lower() == search_item.lower():  # case-insensitive search
        print(f"{search_item} is in {index} position")
        found = True
        break

if not found:
    print(f"{search_item} not found in the list.")
