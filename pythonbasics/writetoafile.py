content = "Hello, this is a sample text file.\n"
content += "This is the second line of the file.\n"
content += "File handling in Python is straightforward."

try:
    file = open("sample.txt", "w")
    file.write(content)
    file.close()
    
    print("Successfully wrote to the file 'sample.txt'.")

except IOError:
    print("An error occurred while writing to the file.")
