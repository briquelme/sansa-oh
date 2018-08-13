class simple:
    def __init__(self):
        self.msg = "hola"

    def saludar(self):
        print(self.msg)

def cambio(clase):
    clase.msg = "chao"
test = simple()
test.saludar()

cambio(test)
test.saludar()
