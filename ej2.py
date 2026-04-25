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

