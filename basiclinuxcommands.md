Linux Command Line Basics
This guide provides a step-by-step walkthrough of essential Linux commands, from file management to setting environment variables. Each section includes the necessary commands and an explanation of how they work.

1. Creating and Renaming Files/Directories
Task: Create a directory named test_dir, create an empty file called example.txt inside it, and then rename that file to renamed_example.txt.

Commands:

# 1. Create the directory
mkdir test_dir

# 2. Navigate into the new directory
cd test_dir

# 3. Create the empty file
touch example.txt

# 4. Rename the file
mv example.txt renamed_example.txt

Explanation:

mkdir test_dir: The mkdir command stands for "make directory." It creates a new directory with the specified name, in this case, test_dir.

cd test_dir: The cd command stands for "change directory." It moves you from your current location into the test_dir directory.

touch example.txt: The touch command is used to create a new, empty file. If the file already exists, touch updates its timestamp without changing its contents.

mv example.txt renamed_example.txt: The mv command stands for "move." It is used to either move a file to a different directory or, as in this case, rename it. The syntax is mv [source] [destination].

2. Viewing File Contents
Task: Display the full contents of /etc/passwd, then show only the first 5 lines, and finally, show only the last 5 lines.

Commands:

# 1. Display the entire file
cat /etc/passwd

# 2. Display the first 5 lines
head -n 5 /etc/passwd

# 3. Display the last 5 lines
tail -n 5 /etc/passwd

Explanation:

cat /etc/passwd: The cat (concatenate) command reads data from files and prints their contents to the standard output.

head -n 5 /etc/passwd: The head command displays the beginning of a file. The -n 5 option tells it to show the first 5 lines.

tail -n 5 /etc/passwd: The tail command displays the end of a file. The -n 5 option tells it to show the last 5 lines.

3. Searching for Patterns
Task: Find all lines containing the word "root" in the /etc/passwd file.

Command:

grep "root" /etc/passwd

Explanation:

grep: This is a powerful command-line utility for searching plain-text data for lines that match a regular expression or a simple string.

"root": This is the pattern you are searching for.

/etc/passwd: This is the file you are searching within. The command will output every line in the file that contains the word "root".

4. Zipping and Unzipping
Task: Compress the test_dir directory into test_dir.zip and then extract its contents into a new directory called unzipped_dir.

Commands:

# (Assuming you are outside the test_dir)
# 1. Compress the directory
zip -r test_dir.zip test_dir

# 2. Unzip the archive into a new directory
unzip test_dir.zip -d unzipped_dir

Explanation:

zip -r test_dir.zip test_dir: The zip command creates a zip archive.

The -r option stands for "recursive," which is crucial for directories. It tells zip to include all files and subdirectories within test_dir.

test_dir.zip is the name of the archive file to be created.

test_dir is the source directory to be compressed.

unzip test_dir.zip -d unzipped_dir: The unzip command extracts files from a zip archive.

The -d option specifies the destination directory. unzip will create unzipped_dir if it doesn't exist and place the extracted contents inside it.

5. Downloading Files
Task: Download a file from a URL.

Command:

# Example using Google's robots.txt file
wget https://www.google.com/robots.txt

Explanation:

wget: This is a command-line utility for downloading files from the web. It supports HTTP, HTTPS, and FTP protocols.

https://www.google.com/robots.txt: This is the full URL of the file to be downloaded. wget will download the file and save it in your current directory with its original name (robots.txt).

6. Changing Permissions
Task: Create a file named secure.txt and change its permissions to be read-only for everyone.

Commands:

# 1. Create the empty file
touch secure.txt

# 2. Change its permissions
chmod 444 secure.txt

Explanation:

touch secure.txt: Creates a new, empty file named secure.txt.

chmod 444 secure.txt: The chmod command changes the permissions (or mode) of a file.

The numeric mode 444 sets read-only permissions. Each digit corresponds to a user class: Owner, Group, and Others.

4 represents "read" permission. So, 444 grants read-only access to the owner, the group, and everyone else.

7. Working with Environment Variables
Task: Set a new environment variable called MY_VAR with the value "Hello, Linux!".

Commands:

# 1. Set the environment variable
export MY_VAR="Hello, Linux!"

# 2. Verify it was set
echo $MY_VAR

Explanation:

export MY_VAR="Hello, Linux!": The export command makes a variable available to the current shell session and any child processes it starts. It assigns the string "Hello, Linux!" to the variable MY_VAR.

echo $MY_VAR: The echo command displays text. When you prefix a variable name with a $ sign, the shell replaces it with the variable's value. This command will print "Hello, Linux!" to the screen, confirming the variable was set correctly. Note that this variable is temporary and will only exist for the current terminal session.
