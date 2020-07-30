'''
create a text file using python, write "hello world" in it,
try to read the text from it and print it into the console
'''


def create_file(filename):
    file = open (filename,'w+')
    file.write('Hello world')
    file = open (filename,'r')
    if file.mode=="r":
        contents = file.read()
        print(contents)

create_file('dupa.txt')

