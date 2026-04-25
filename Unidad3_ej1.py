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


