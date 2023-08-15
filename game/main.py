import random

#opciones de la pc almacenadas como tuplas
option = ("piedra", "papel", "tijera")
puntos_user = 0
puntos_pc = 0

print("El primero en llegar a 3 puntos gana!")

while (puntos_user < 3 and puntos_pc < 3):
  user_option = input("Piedra, papel o tijera => ")
  user_option = user_option.lower()
  #pasa la respuesta del user a minus

  if not user_option in option:
    print("Así no se puede jugar :(")
    continue

  #elección aleatoria de la pc
  pc = random.choice(option)

  #imprimir un espacio y las opciones de cada uno
  print(" ")
  print("Jugador elije => ", user_option)
  print("PC elije => ", pc)
  
  if user_option == pc:
    print("Empate!")
  elif user_option == "piedra":
    if pc == "tijera":
      print("El jugador gana la ronda!")
      puntos_user += 1
    else:
      print("La PC gana la ronda!")
      puntos_pc += 1
  elif user_option == "tijera":
    if pc == "papel":
      print("El jugador gana la ronda!")
      puntos_user += 1
    else:
      print("La PC gana la ronda!")
      puntos_pc += 1
  elif user_option == "papel":
    if pc == "piedra":
      print("El jugador gana la ronda!")
      puntos_user += 1
    else:
      print("La PC gana la ronda!")
      puntos_pc += 1
  else:
    print(":(")

  #contador total
  print(" ")
  print("Jugador = ", puntos_user, "PC = ", puntos_pc)
  if puntos_user > puntos_pc:
    print("El Jugador va ganando!")
  elif puntos_user < puntos_pc:
    print("La PC va ganando!")
  else:
    print("El Jugador y la PC están empatados!")

print(" ")
if puntos_user > puntos_pc :
  print ("¡¡¡El Jugador ganó!!!")
else:
  print ("¡¡¡La PC ganó!!!")
print ("__________________________")  