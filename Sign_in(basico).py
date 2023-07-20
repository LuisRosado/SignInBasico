import os

i = 0
Usuario = 'Luis'
Contraseña = '123'

user = ''
password = ''


while ((Usuario != user or Contraseña != password) and i<3):
    os.system("cls")
    print('\nBienvenido Ingrese su Nombre de usuario y su contraseña(Solo tiene 3 intentos)\n')
    user = input('Usuario: ')
    password = input('Contraseña: ')

    if Usuario != user or Contraseña != password:
      os.system("cls")
      print('Nombre de Usuario o Contraseña incorrecta')
      print('Porfavor Intenta de nuevo')
      input('Presiona ENTER para continuar...')
      i = i+1
    else:
      os.system("cls")
      print('Bienvenido XD')
if(i>=3):      
  os.system("cls")
  print('\nSu Cuenta ha sido bloqueada')     