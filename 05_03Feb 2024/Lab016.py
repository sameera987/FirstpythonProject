name = 'superhero'
# lens starts from 1
print(len(name))
print(len(name)-1)
print(name[len(name)-1])  #len(name)-1] =8

#index starts from 0
print(name[0])
print(name[5])
#print(name[9]) #IndexError: string index out of range
print("Test")

#Strings are immutable
#that cant be changed, modify
string = "Test"
#string[0] = "P" #TypeError: 'str' object does not support item assignment