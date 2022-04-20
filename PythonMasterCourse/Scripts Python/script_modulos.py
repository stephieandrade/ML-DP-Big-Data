def suma(a, b):
    try: 
        r = a+b
    except TypeError:
        print("Tipo de dato no valido")
    else:
        return r

def resta(a, b):
    try: 
        r = a-b
    except TypeError:
        print("Tipo de dato no valido")
    else:
        return r

def multiplicacion(a, b):
    try: 
        r = a*b
    except TypeError:
        print("Tipo de dato no valido")
    else:
        return r

def division(a, b):
    try: 
        r = a/b
    except TypeError:
        print("Tipo de dato no valido")
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    else:
        return r