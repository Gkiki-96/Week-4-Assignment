filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()

    new_filename = "modified_" + filename
    with open(new_filename, "w") as file:
        file.write(content.upper())

    print(f"Modified file saved as {new_filename}")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
