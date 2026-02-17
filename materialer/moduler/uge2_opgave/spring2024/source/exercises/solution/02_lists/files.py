# Create a file and call it lyrics.txt (it does not need to have any content)

open('lyrics.txt', 'w')

# Create a new file and call it songs.docx and in this file write 3 lines of text to it.

f = open('songs.docx' 'w')
f.writeline('Hello')
f.writeline('World')
f.writeline('And you')

#open and read the content and write it to your terminal window. 
* you should use both the read(), readline(), and readlines() methods for this. (so 3 times the same output).

f = open('songs.docx', 'r')
print(f.read())

f = open('songs.docx', 'r')
line = f.readline()
while line:
    print(line)
    line = f.readline()


f = open('songs.docx', 'r')
for i in f.readlines():
    print(i)
