#ejercicio 1
nombre=input("Cliente: ")
while not nombre.isalpha():
    print("Error: El nombre debe contener solo letras y no estar vacio.")
    nombre=input("Cliente: ")
cant_prd=input("Cantidad de productos: ")
while not (cant_prd.isdigit() and int(cant_prd) > 0):
    print("Error: Ingrese un número entero mayor a 0.")
    cant_prd=input("Cantidad de productos: ")
cantidad_productos=int(cant_prd)
total_sin_desc=0
total_con_desc=0

for i in range(1, cantidad_productos + 1):
    precio_input=input(f"Producto {i} - Precio: ")
    while not precio_input.isdigit():
        print("Error: El precio debe ser un número entero.")
        precio_input=input(f"Producto {i} - Precio: ")
    precio=int(precio_input)
    total_sin_desc += precio
    tiene_desc=input("Descuento (S/N): ").lower()
    while tiene_desc not in ['s', 'n']:
        print("Error: Ingrese S(si) o N(no) ")
        tiene_desc=input("Descuento (S/N): ").lower()
    if tiene_desc == 's':
        precio_final=precio * 0.90
    else:
        precio_final=precio
    total_con_desc += precio_final
ahorro=total_sin_desc - total_con_desc
promedio=total_con_desc / cantidad_productos

print(f"Total sin descuentos: ${total_sin_desc}")
print(f"Total con descuentos: ${total_con_desc:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

#ejercicio 2
Usuario_correcto="alumno"
contraseña_correcta="python123"
intentos=1
acceso=False

while intentos <= 3:
    print(f"Intento {intentos}/3")
    usuario=input("Usuario: ")
    clave=input("Clave: ")
    if usuario == Usuario_correcto and clave == contraseña_correcta:
        print("Acceso concedido.")
        acceso=True
        break
    else:
        print("Error: credenciales inválidas.")
        intentos += 1

if not acceso:
    print("Cuenta bloqueada.")
else:
    opcion=""
    while opcion != "4":
        print("""--- MENÚ DEL CAMPUS ---
    1) Ver estado de inscripción
    2) Cambiar clave
    3) Mostrar mensaje motivacional
    4) Salir""")
        opcion=input("Opción:")
        
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
        elif int(opcion) < 1 or int(opcion) > 4:
            print("Error: opción fuera de rango.")
        else:
            
            if opcion == "1":
                print("Estado: Inscripto")
            
            elif opcion == "2":
                nueva_clave = input("Nueva clave: ")
                while len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres.")
                    nueva_clave=input("Nueva clave: ")
                confirmacion=input("Confirme nueva clave: ")
                if nueva_clave == confirmacion:
                    contraseña_correcta= nueva_clave
                    print("Clave cambiada con éxito.")
                else:
                    print("Error: las claves no coinciden.")
            elif opcion == "3":
                print("¡El éxito es la suma de pequeños esfuerzos repetidos día tras día!")
            elif opcion == "4":
                print("Saliendo del sistema...")

#ejercicio 3
l1 = l2 = l3 = l4 = "" 
m1 = m2 = m3 = ""      

operador=input("Nombre del operador: ")
while not operador.isalpha():
    print("Error: Solo letras.")
    operador=input("Nombre del operador: ")

opcion = ""
while opcion != "5":
    print(f"--- AGENDA (Operador: {operador}) ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    opcion=input("Opción: ")
    
    if opcion == "1":
        dia=input("Elegir día (1=Lunes, 2=Martes): ")
        if dia == "1":
            nombre=input("Nombre del paciente: ")
            while not nombre.isalpha():
                nombre=input("Error (solo letras). Nombre: ")
            if nombre == l1 or nombre == l2 or nombre == l3 or nombre == l4:
                print("Error: El paciente ya tiene un turno este día.")
            elif l1 == "": l1 = nombre; print("Turno 1 reservado.")
            elif l2 == "": l2 = nombre; print("Turno 2 reservado.")
            elif l3 == "": l3 = nombre; print("Turno 3 reservado.")
            elif l4 == "": l4 = nombre; print("Turno 4 reservado.")
            else: print("Lunes sin cupos.")
        elif dia == "2":
            nombre=input("Nombre del paciente: ")
            while not nombre.isalpha():
                nombre=input("Error (solo letras). Nombre: ")
            if nombre == m1 or nombre == m2 or nombre == m3:
                print("Error: Ya tiene turno este día.")
            elif m1 == "": m1 = nombre; print("Turno 1 reservado.")
            elif m2 == "": m2 = nombre; print("Turno 2 reservado.")
            elif m3 == "": m3 = nombre; print("Turno 3 reservado.")
            else: print("Martes sin cupos.")

    elif opcion == "2":
        dia=input("Elegir día para cancelar (1L/2M): ")
        nombre=input("Nombre del paciente a cancelar: ")
        if dia == "1":
            if l1 == nombre: l1 = ""; print("Cancelado.")
            elif l2 == nombre: l2 = ""; print("Cancelado.")
            elif l3 == nombre: l3 = ""; print("Cancelado.")
            elif l4 == nombre: l4 = ""; print("Cancelado.")
            else: print("No se encontró el paciente.")
        elif dia == "2":
            if m1 == nombre: m1 = ""; print("Cancelado.")
            elif m2 == nombre: m2 = ""; print("Cancelado.")
            elif m3 == nombre: m3 = ""; print("Cancelado.")
            else: print("No se encontró el paciente.")

    elif opcion == "3":
        dia=input("Ver día (1=Lunes, 2=Martes): ")
        if dia == "1":
            print(f"1: {l1 if l1!='' else '(libre)'}")
            print(f"2: {l2 if l2!='' else '(libre)'}")
            print(f"3: {l3 if l3!='' else '(libre)'}")
            print(f"4: {l4 if l4!='' else '(libre)'}")
        elif dia == "2":
            print(f"1: {m1 if m1!='' else '(libre)'}")
            print(f"2: {m2 if m2!='' else '(libre)'}")
            print(f"3: {m3 if m3!='' else '(libre)'}")

    elif opcion == "4":
        c_lunes=0
        if l1 != "": c_lunes += 1
        if l2 != "": c_lunes += 1
        if l3 != "": c_lunes += 1
        if l4 != "": c_lunes += 1
        
        c_martes=0
        if m1 != "": c_martes += 1
        if m2 != "": c_martes += 1
        if m3 != "": c_martes += 1
        
        print(f"Lunes: {c_lunes} ocupados, {4-c_lunes} libres.")
        print(f"Martes: {c_martes} ocupados, {3-c_martes} libres.")
        
        if c_lunes > c_martes: print("Día con más turnos: Lunes")
        elif c_martes > c_lunes: print("Día con más turnos: Martes")
        else: 
            print("Empate en cantidad de turnos.")

print("Sistema cerrado.")

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
