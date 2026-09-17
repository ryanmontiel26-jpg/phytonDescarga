import tkinter as tk

# 1. Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("300x200")  # Tamaño de la ventana (ancho x alto)

# 2. Función que se ejecutará al hacer clic en el botón
def saludar():
    etiqueta.config(text="¡Hola! Has presionado el botón.")

# 3. Agregar un texto (etiqueta)
etiqueta = tk.Label(ventana, text="¡Hola, mundo!", font=("Arial", 12))
etiqueta.pack(pady=20)  # .pack() sirve para colocar el elemento en la ventana

# 4. Agregar un botón
boton = tk.Button(ventana, text="Haz clic aquí", command=saludar)
boton.pack()

# 5. Mantener la ventana abierta ejecutando el bucle principal
ventana.mainloop()