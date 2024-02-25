class person:
    def __init__(self,name) -> None:
        self.name = name      
    
    def __repr__(self) -> str:
        return self.name

    def __mul__(self,p):
        if type(p) is not int:
            raise Exception("Invalid argument")
        self.name = self.name*p
    
p =person("Sumit")
print(p)
p*4
print(p)


        