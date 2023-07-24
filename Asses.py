list1=["John Problem", "James Scott", "Joseph Elenor"]
First_name=[]
last_name=[]

def no_of_names(list1):
    no_of_names=len(list1)
    return no_of_names

num= no_of_names(list1)

print(num)

def process_names(names):
    for name in names:
        First_name.append(name.split(' ')[0])
        last_name.append(name.split(' ')[1])

process_names(list1)
print(last_name)


    


