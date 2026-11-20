list_m = [100, 50, 400, 500]

# a) Change Element
list_m[1] = 200
print(f"Updated (Change): {list_m}")

# b) Append Element
list_m.append(600)
print(f"Updated (Append): {list_m}")

# c) Insert Element
list_m.insert(2, 300)
print(f"Updated (Insert): {list_m}")

# d) Remove Element by value
list_m.remove(600)
print(f"Updated (Remove 600): {list_m}")

# e) Remove Element by index
list_m.pop(0)
print(f"Updated (Remove Index 0): {list_m}")


