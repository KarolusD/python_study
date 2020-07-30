'''
Make a request to that link: 
https://randomuser.me/api?results=10' 
it will return data of 10 users, 
loop through users names and print 
fist name of each user.
'''
import requests,json
response = requests.get('https://randomuser.me/api?results=10')

data = response.json()
def create_file(filename):
    file = open (filename,'w+')
    file.write(json.dumps(data))
    file.close()

create_file('users.json')
def first_name(res):
    for user in res :
        print(user["name"]["first"])

first_name(data["results"])
