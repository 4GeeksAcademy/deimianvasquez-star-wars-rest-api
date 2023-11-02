class Human():
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    
    def __repr__(self):
        return '<class Human>' 
    

    def __str__(self):
        return f"Hola soy una clase que genera humanos"


human = Human("Deimian", "Vásquez")

print(human)