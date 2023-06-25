import string
import secrets



Mayusculas = string.ascii_uppercase
Minusculas = string.ascii_lowercase
Numeros = string.digits
Caracteres_Especiales = string.punctuation


def sel_char_type():
    char_type = {"1":"Mayusculas", "2":"Minusculas", "3":"Numeros", "4":"Caracteres_Especiales"}
    for x, y in char_type.items():
        print(x, y)

    global selected_char_type

    selected_char_type=[(input("Bienvenid@ a PassGen, que familia de caracteres queres utilizar en tu contraseña?: "))]
    print(selected_char_type)

    another_char_type = input("Quieres agregar otra familia?: ")
    print(another_char_type)
    selected_char_type.append(another_char_type)
    print(selected_char_type)


def pswd_length():
    global length
    length = int(input("Cual es el largo deseado de su contraseña?: "))
    return length
    print(f"Su longitud dde contraseña deseada es: {length}")


def conv():
    if (selected_char_type[0]=="1"):
        selected_char_type[0]=Mayusculas

    elif(selected_char_type[0]=="2"):
        selected_char_type[0]=Minusculas

    elif(selected_char_type[0]=="3"):
        selected_char_type[0]=Numeros

    elif(selected_char_type[0]=="4"):
        selected_char_type[0]=Caracteres_Especiales
    

    if (selected_char_type[1]=="1"):
        selected_char_type[1]=Mayusculas

    elif(selected_char_type[1]=="2"):
        selected_char_type[1]=Minusculas

    elif(selected_char_type[1]=="3"):
        selected_char_type[1]=Numeros

    elif(selected_char_type[1]=="4"):
        selected_char_type[1]=Caracteres_Especiales


def gen_pswd():
    pswd = ''
    conv()

    for i in range(length):
        pswd += ''.join(secrets.choice(selected_char_type[0]+selected_char_type[1]))

    print(pswd)


sel_char_type(), pswd_length(), gen_pswd()