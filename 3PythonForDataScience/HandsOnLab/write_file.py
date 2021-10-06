exmp2 = 'Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")

with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

lines = ["This is line A\n", "This is line B\n", "This is line C\n"]

with open('Example2.txt', 'w') as writefile:
    for line in lines:
        writefile.write(line)

with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")

with open(exmp2, 'r') as test_write_file:
    print(test_write_file.read())

"""
Additional Modes
r+ : Reading and writing. Cannot truncate the file.
w+ : Writing and reading. Truncates the file.
a+ : Appending and Reading. Creates a new file, if none exists.
"""