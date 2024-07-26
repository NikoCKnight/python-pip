import os
import random
import sys
import time

opciones = ('piedra', 'papel', 'tijera')
derrotas = 0
victorias = 0

while derrotas < 3 and victorias < 3:
  print('MARCADOR:\n usuario =>', victorias, 'sistema =>', derrotas)
  print('¿Crees poder vencer a la consola?')
  usuario = input('¿Piedra, papel o tijera? =>')
  consola = random.choice(opciones)
  
  opcion = usuario.lower()
  
  if not opcion in opciones:
    sys.exit('\nno estas eligiendo opciones validas')
  
  print('\nUsuario: ',opcion)
  print('Consola: ', consola)

  if opcion == consola:
    print('\nEmpate!')
    time.sleep(2)
    os.system('clear')
  elif opcion == 'piedra':
    if consola == 'tijera':
      print('\npiedra gana a tijera')
      print('Ganaste!')
      victorias += 1
      time.sleep(2)
      os.system('clear')
    else:
      print('\nPapel gana a piedra')
      print('Perdiste!')
      derrotas += 1
      time.sleep(2)
      os.system('clear')
  elif opcion == 'papel':
    if consola == 'piedra':
      print('\npapel gana a piedra')
      print('Ganaste!')
      victorias += 1
      time.sleep(2)
      os.system('clear')
    else:
      print('\ntijera gana a papel')
      print('Perdiste!')
      derrotas += 1
      time.sleep(2)
      os.system('clear')
  elif opcion == 'tijera':
    if consola == 'papel':
      print('\ntijera gana a papel')
      print('Ganaste!')
      victorias += 1
      time.sleep(2)
      os.system('clear')
    else:
      print('\npiedra gana a tijera')
      print('Perdiste!')
      derrotas += 1
      time.sleep(2)
      os.system('clear')