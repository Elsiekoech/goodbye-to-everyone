list_of_names = []
while True:
    try:
        name = input("enter name or control_d to exit")
        list_of_names.append(name)
    except EOFError:
        break

if len(list_of_names) == 1:
    print("Adieu,adieu,to ",list_of_names[0])
elif len(list_of_names) == 2:
    print("Adieu,adieu,to ",list_of_names[0],"and",list_of_names[1])

else:
    print("Adieu,adieu, to ",end ="")
    for item in list_of_names:
        if item == list_of_names[0] :
            print(item,end ="")
        elif item == list_of_names[-1]:
            print(" and",item)
        else:
            print(",",item,end = "")

