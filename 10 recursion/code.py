# Industry Example: Recursive Directory Traversal (Simulated)

# Simulating recursion by printing nested folder structure

def print_folders(folder_name, level=0):
    print("  " * level + folder_name)
    if folder_name == "root":
        print_folders("folder1", level + 1)
        print_folders("folder2", level + 1)
    elif folder_name == "folder1":
        print_folders("subfolder1", level + 1)
    # Base case: No more subfolders

print_folders("root")
