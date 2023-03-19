from sys import argv

script, filename = argv
# from system, imports a filename
txt = open(filename)
"""
    passes filename as a parameter
    to function called open. Open function 
    opens a file and returns as a file object
    the file object is then assigned to a variable
    named txt
"""

print(f"Here's your file {filename}:")
# types out the string with the name
print(txt.read())
# prints out the text from the file
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt.close()
txt_again.close()