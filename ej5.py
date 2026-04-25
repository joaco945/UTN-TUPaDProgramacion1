#ejercicio 5
print("--- BIENVENIDO A LA ARENA ---")

nombre=input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre=input("Nombre del Gladiador: ")
vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado_base = 15
ataque_enemigo = 12
juego_activo=True  

print("=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print(""""Elige acción:
    1. Ataque Pesado
    2. Ráfaga Veloz
    3. Curar""")
    
    opcion=input("Opción: ")
    
    while not (opcion.isdigit() and (opcion == "1" or opcion == "2" or opcion == "3")):
        print("Error: Ingrese un número válido (1, 2 o 3).")
        opcion=input("Opción: ")
    if opcion == "1":
        if vida_enemigo < 20:
            danio_final=ataque_pesado_base * 1.5 
            print(f"¡GOLPE CRÍTICO!")
        else:
            danio_final=float(ataque_pesado_base)
        
        vida_enemigo -= danio_final
        print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")

    elif opcion == "2":
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print(" > Golpe conectado por 5 de daño")

    elif opcion == "3":
        if pociones > 0:
            vida_jugador += 30
            if vida_jugador > 100: vida_jugador = 100
            pociones -= 1
            print(f"¡Te has curado! Vida actual: {vida_jugador}")
        else:
            print("¡No quedan pociones! Pierdes el turno intentando buscar una.")
    if vida_enemigo > 0:
        vida_jugador -= ataque_enemigo
        print(f">> ¡El enemigo te atacó por {ataque_enemigo} puntos de daño!")

print("=== FIN DEL COMBATE ===")
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")