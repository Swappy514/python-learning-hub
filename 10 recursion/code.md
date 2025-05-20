# Industry Example: Recursive Directory Traversal (Simulated)

Recursion is often used in real applications such as:

- Traversing folders and files in nested directory structures.
- Solving problems naturally defined by recursive patterns.

### Example Code:

def print_folders(folder_name, level=0):
print(" " \* level + folder_name)
if folder_name == "root":
print_folders("folder1", level + 1)
print_folders("folder2", level + 1)
elif folder_name == "folder1":
print_folders("subfolder1", level + 1)

# Base case: stops when no further subfolders

print_folders("root")

### Output:

root
folder1
subfolder1
folder2
This pattern helps manage hierarchical data structures like file systems.
