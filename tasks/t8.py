'''
<<<<<<< HEAD
create a text file using python, write "hello world" in it,
try to read the text from it and print it into the console
=======
create a text file using python, write "hello world" in it, try to read the text from it and print it into the console
>>>>>>> 3e019487c0191bf5e4cada8962afcca6683761bb
'''


def create_file(filename):
<<<<<<< HEAD
    file = open (filename,'w+')
    file.write('Hello world')
    file = open (filename,'r')
    if file.mode=="r":
        contents = file.read()
        print(contents)

create_file('dupa.txt')

=======
    pass
>>>>>>> 3e019487c0191bf5e4cada8962afcca6683761bb
