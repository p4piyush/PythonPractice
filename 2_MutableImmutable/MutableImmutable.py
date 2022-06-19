def Immutable():
    print("*"*60,"\nExaple of Immutable\n")
    a=10
    id1=id(a)
    """
        This is example of Immutable
        where INTEGER is used
    """
    #print(type(a),"\nThis is example of Immutable:")
    print(f"Value of A: {a} and ID of A :{id(a)}")

    a=20
    id2=id(a)
    print(f"New Value of A: {a} and New ID of A :{id(a)}")

    if id1!=id2:
        print(f"So memory location is changed for same variable A\n So this is example of Immutable\n")
        print("*"*60)
    else:
        print("ID is same...")


def Mutable():
    print("*"*60,"\nExaple of Mutable\n")
    a=[1,2,3,4]  
    id1=id(a)  
    '''
        Now this is example of Mutable 
        where LIST is used
    '''
    print(f"Original list:{a} and ID is {id(a)}")

    a[3]=44
    id2=id(a)
    print(f"Modified list:{a} and ID is {id(a)}")

    if id1==id2:
        print("So after modification of value ID not changed \nSo this is example of Mutable")
        print("*"*60)
    else:
        print("ID changed...")



Mutable()
Immutable()

