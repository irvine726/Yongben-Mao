filename = 'tracker.txt'

with open(filename) as file_object:
    nx = list(set(file_object.readlines()))


with open('tracker2.txt','w') as file_object:
    file_object.writelines(nx)

with open('tracker2.txt','w') as file_object:
    lines = file_object.readlines()
    i = ''
    for i in lines:
        i = i + "\r"
        print(i)


'''

with open('tracker2.txt','w') as file_object:
    file_object.writelines(nx)





with open('tracker2.txt') as file_object:
    for i in file_object:
        print(i)
'''

