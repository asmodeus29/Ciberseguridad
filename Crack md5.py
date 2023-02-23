import hashlib

encontrada = 0
input_hash = input ("Contraseña hasheada: ")
file = ("documento")

try:
    pass_file = open("dic.txt", 'r')
except:
    print("Error el " + file + "no ha sido econtrado")

for palabra in pass_file:
    palabra_cifrada = palabra.encode('utf-8')
    palabra_hasheada = hashlib.md5(palabra_cifrada.strip())
    digest = palabra_hasheada.hexdigest()

    if digest == input_hash:
       print("Contraseña encontrada!!! \n La contaseña es: " + palabra)
       encontrada = 1
       break

if not encontrada:
    print("Contraseña no encontrada en el archivo " + file)
