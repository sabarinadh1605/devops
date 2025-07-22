file = open("sample.txt", "r")
file_content = file.read()
file.close()
    
print("--- Content of 'sample.txt' ---")
print(file_content)
