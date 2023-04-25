import random

opciones = ["papel","piedra","tijera"]
opcion_maquina = random.choice(opciones)

print("JUEGO PIEDRA, PAPEL y TIJERA")
opcion_humano = input("Elegi una opción para el juego: ")
print("La opción de la maquina es: " + opcion_maquina)

if (opcion_maquina == opcion_humano):
  print("Es un empate!!!")
elif(opcion_maquina == 'papel') and (opcion_humano == 'piedra'):
  print("Perdiste, La opción ganadora es " + opcion_maquina)
elif(opcion_maquina == 'piedra') and (opcion_humano == 'tijera'):
  print("Perdiste, La opción ganadora es " + opcion_maquina)
elif(opcion_maquina == 'tijera') and (opcion_humano == 'papel'):
  print("Perdiste, La opción ganadora es " + opcion_maquina)
else:
  print("Ganaste con la opción " + opcion_humano)