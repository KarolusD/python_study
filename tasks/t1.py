'''
Write a function that will take string 
and return it in reverse.

Example:
"Dawid" => "diwaD"
'''

def reverse_str(str):
    abc=''
    str_l = list(str)
    for i in range (len(str_l)-1,-1,-1):
        abc += str_l[i]
    return  abc 

print(reverse_str("Dawid"))