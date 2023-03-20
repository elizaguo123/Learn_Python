from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRC-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file, Goodbye!")
target.truncate()
# truncating here is not useful because when open with 'w'
# file is already truncated
#truncated means to resize file to given bytes
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
# how to reduce repetitions for these lines?
"""
For loop method:
thislist = [line 1: , line 2: , line 3: ,]
for x in range (0, 3)
thislist.input()

Function method:

"""


print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
