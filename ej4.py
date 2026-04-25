#ejercicio 4
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidos = 0  

nombre=input("Nombre del agente: ")
while not nombre.isalpha():
    print("Error: El nombre debe contener solo letras.")
    nombre=input("Nombre del agente: ")
print(f"Bienvenido, Agente {nombre}. La bóveda te espera.")
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    if alarma and tiempo <= 3:
        print("¡BLOQUEO DEL SISTEMA! La alarma y el tiempo agotado te atraparon.")
        break

    print(f"--- ESTADO ---")
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3")
    print(f"Alarma: {'ACTIVADA' if alarma else 'Apagada'} | Hackeo: [{codigo_parcial}]")
    
    print("""Acciones:")
    1. Forzar cerradura (-20 E, -2 T)
    2. Hackear panel (-10 E, -3 T)
    3. Descansar (+15 E, -1 T)""")
    
    opcion=input("Elegir acción: ")
    while not (opcion.isdigit() and "1" <= opcion <= "3"):
        opcion=input("Error. Elija 1, 2 o 3: ")
    if opcion == "1":
        energia -= 20
        tiempo -= 2
        forzar_seguidos += 1
        if forzar_seguidos == 3:
            print("¡La cerradura se trabó por insistir tanto! Alarma activada.")
            alarma=True
        else:
            if energia < 40:
                print("¡CUIDADO! Energía baja, riesgo de activar alarma.")
                n_riesgo = input("Elija un número de seguridad (1-3): ")
                while not (n_riesgo.isdigit() and "1" <= n_riesgo <= "3"):
                    n_riesgo = input("Error. Ingrese 1, 2 o 3: ")
                if n_riesgo == "3":
                    alarma = True
                    print("¡ACTIVASTE LA ALARMA!")
            
            if not alarma:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta con éxito!")

    elif opcion == "2": 
        energia -= 10
        tiempo -= 3
        forzar_seguidos = 0 
        
        print("Hackeando...")
        for i in range(1, 5):
            codigo_parcial += "A"
            print(f"Paso {i}/4 - Progreso: {codigo_parcial}")
        
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡El hackeo abrió una cerradura!")

    elif opcion == "3":
        tiempo -= 1
        forzar_seguidos = 0
        recuperacion = 15
        if alarma:
            recuperacion -= 10
            print("Es difícil descansar con la alarma sonando...")
        energia += recuperacion
        if energia > 100: energia = 100
        print(f"Has descansado. Energía actual: {energia}")
        
if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! El Agente {nombre} ha abierto la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print(f"DERROTA: Te quedaste sin {'energía' if energia <= 0 else 'tiempo'}.")
else:
    print("DERROTA: El sistema se encuentra bloqueado.")

