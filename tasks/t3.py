'''
Write a function that will except a string
and return it without special characters
like !@#$%^&*()_-–+[]''"\\|;:,./?~`

Example:
"\\Hel@lo, Wo$rld!/" => 'Hello World'
'''


def remove_special_char(str):
    str_l= list(str)
    spec_char='!@#$%^&*()_-–+[]''"\\|;:,./?~`'
    abc=''
    for i in str_l :
        if i in spec_char:
            pass
        else: abc+=i

    return abc
print(remove_special_char('!@#$%^&*()_-–g+[]''"\\|;:,./?~'))





























    
=======
    # your code goes here
    pass  # delete this line it does nothing
>>>>>>> 3e019487c0191bf5e4cada8962afcca6683761bb
