items = ["apple", "banana", "cherry", "date", "elderberry" , "apple"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("duplicate: ", item)
        break
unique_item.add(item)
