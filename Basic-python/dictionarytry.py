'''
Creating and Altering Dictionary
'''
#Creating a dictionary
details = {'name':'Robin','age':23,'city':'chennai'}

#Adding values into a dictionary
details.update({'Company':'Hitach','role':'Tech Support'}) 

#Removing last added values from a dictionary in this case role.
details.popitem()

#To remove a specific key
del details['Company']

#To update a pre-existing key
details.update({'name':'Anand'})
details['name'] = 'Gowtham'

#Renaming a Key
details['employee-name'] = details.pop('name')

print(details)