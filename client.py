import requests
from flask import jsonify

url= "http://127.0.0.1:5000/students"

# GET request
print("\n------------ GET ALL STUDENTS ------------")
getAllResponse = requests.get(url)
print(getAllResponse.json())

# GET request for a single student data
print("\n------------ GET ONE STUDENT DATA ------------")
code = 'T00045059'
getResponse= requests.get(url+'/'+code)
print("\n",getResponse.json())

# POST request
print("\n------------ CREATING A NEW STUDENT ------------")
newStudent = {
 'id':'T00055568',
 'name':'Daniela Barboza',
 'course':'Backend development'
 }
postResponse = requests.post(url, json = newStudent)
print("\n",postResponse.json())

print("\nALL STUDENTS - UPDATED")
print(requests.get(url).json())

# PUT request
print("\n------------ UPDATING STUDENT DATA (NAME) ------------")
changedData = {
 'id':'T00045059',
 'name':'Marcela Barboza',
 'course':'QA'
 }
putResponse = requests.put(url+"/"+changedData["id"], json = changedData)

print("\n",putResponse.json())

# DELETE request
print("\n------------ DELETING STUDENT DATA ------------")
codeToDelete = 'T00045678'
deleteResponse = requests.delete(url+"/"+codeToDelete)

print("\n",deleteResponse.json())

print("\nALL STUDENTS - UPDATED")
print(requests.get(url).json())

print (" ")