class Piyush():
    """
        THIS IS EXAMPLE FOR CLASS WHICH WILL ACCEPT 2 PARAMETR ID AND NAME
        THIS WILL ALSO HAVE INSTANCE METHOD, CLASS METHOD, STATIC METHOD 
    """
    def __init__(self, id, name):   #id and name is the example of Instance vatiable
        self.myid=id
        self.myname=name

    def __str__(self):
        return f"{self.__dict__}"
    
    def __repr__(self):
        return str(self)

    ClassVaraible="This is class veriable"  #This is example of class variable

    
    @classmethod #This is class method, this takes one default parameter CLS
    def Class_method(cls):
        return "This is class method"

    
    @staticmethod #This is static method, this method can not access class data and it is self sufficient
    def Static_method():
        return "This is static method"
    

p1 = Piyush(id=101, name="PiyushPatil")
p2 = Piyush(102, "Vaibhav")

print(p1)
print(p2)
print(p1.Static_method())
print(p2.Class_method())
print(p1.ClassVaraible)