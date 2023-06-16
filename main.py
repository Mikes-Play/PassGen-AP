import string
import secrets

#TODO Crear menu de seleccion de:
#* Alfabetos a utilizar
#* Longitud de Contraseña

#TODO Reordenar y estilizar alphabet y strings
alphabet = string.ascii_letters + string.digits

#TODO Reemplazar por "inputs"
password = ''.join(secrets.choice(alphabet) for i in range(8))

