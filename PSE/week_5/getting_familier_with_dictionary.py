dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {'d':4, 'e':5, 'f':6}

merged_dict = {
    **{k:v for k,v in dict1.items() if k in 'aeiou'},
    **{k:v for k,v in dict2.items() if k in 'aeiou'},
}

print(merged_dict)


x, _, y = (1,"ignored",3)

print(x,y)


names = ['John', 'Jane', 'Jim', 'Jill']

for i in range(len(names)):
    print(i,names[i])

print("--------------------------------\n")
for i, name in enumerate(names):
    print(i,name)
    
print("--------------------------------\n")
for i, name in enumerate(names, start=1):
    print(i,name)



ages = [10,20,30,40]

paired = zip(names, ages)
print(paired)
# print(list(paired))
print(dict(paired))



ids = [1,2,3]
names = ['John', 'Jane', 'Jim', 'Jill', 'Jack']
grades = ['A','B','C','D','E']

students = dict(zip(ids,zip(names, grades)))

print(students)





