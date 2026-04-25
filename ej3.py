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