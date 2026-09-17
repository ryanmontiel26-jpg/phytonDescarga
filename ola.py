print(" CALCULADORA DE CUENTAS ")
print("------------------------------")

# 1. Pedimos los datos al usuario
total_cuenta = float(input("¿Cuánto fue el total de la cuenta? $"))
personas = int(input("¿Entre cuántas personas se va a dividir? "))
porcentaje_propina = float(input("¿Qué porcentaje de propina quieren dejar? (ejemplo: 10, 15): "))

# 2. Hacemos las matemáticas
dinero_propina = total_cuenta * (porcentaje_propina / 100)
total_a_pagar = total_cuenta + dinero_propina
pago_por_persona = total_a_pagar / personas

# 3. Mostramos el resultado en pantalla
print("\n--- EL RESULTADO ---")
print(f"La propina será de: ${dinero_propina:.2f}")
print(f"El total final a pagar es: ${total_a_pagar:.2f}")
print(f"👉 Cada persona debe poner: ${pago_por_persona:.2f}")