import copy

def ShallowCopy():
    print("*"*60,"\nShallow Copy Example\n")

    a=[10,[20,30],40]
    b=copy.copy(a)

    print(f"Values of A:{a} and B:{b}")

    new_val=int(input("Enter new value to insert into A:"))
    a[1][0]=new_val

    print(f"New Values of A:{a} and B:{b}")

def DeepCopy():
    print("*"*60,"\nDeep Copy Example\n")

    a=[10,[20,30],40]
    b=copy.deepcopy(a)

    print(f"Values of A:{a} and B:{b}")

    new_val=int(input("Enter new value to insert into A:"))
    a[1][0]=new_val

    print(f"New Values of A:{a} and B:{b}")


ShallowCopy()
DeepCopy()