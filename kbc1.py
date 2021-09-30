
print("Ankit's challlenging Questions")
# 1 Employe list change into dictionary
len_employee=int (input('enter how many employee do you need'))
dict1={}
for i in range(0,len_employee):
    dict2={}
    name =input("Enter employee's name" )
    age=int(input("Enter employee's age"))
    sex=input("Enter employee's sex")
    job=input("In which company employee do work")
    dict2={'name':name,'age':age,'sex':sex,'job':job}
    dict1[i+1,'employee']=dict2
print(dict1)

