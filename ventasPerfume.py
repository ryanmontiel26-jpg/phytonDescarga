import tkinter as tk
from tkinter import messagebox

class RyanShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ryan.ShopMx — Haute Parfumerie System")
        self.root.geometry("750x550")
        self.root.config(bg="#121212")

        # Catálogo extendido con categorías
        self.catalogo = {
            "Xerjoff Erba Pura (Nicho)": 185.00,
            "Tom Ford Black Orchid (Nicho)": 145.00,
            "Dior Sauvage Elixir (Diseñador)": 125.50,
            "Jean Paul Gaultier Le Male (Diseñador)": 95.00,
            "Decant 10ml - Afnan 9pm": 18.00,
            "Decant 10ml - Lattafa Asad": 16.00
        }

        self.carrito = []
        self.crear_interfaz()

    def crear_interfaz(self):
        # Título / Header
        lbl_header = tk.Label(
            self.root, 
            text="✨ RYAN.SHOPMX | HIGH PERFUMERY ✨", 
            font=("Helvetica", 16, "bold"), 
            bg="#121212", 
            fg="#d4af37"
        )
        lbl_header.pack(pady=15)

        # Marco Principal dividido en dos columnas (Izquierda: Catálogo, Derecha: Carrito)
        frame_principal = tk.Frame(self.root, bg="#121212")
        frame_principal.pack(fill="both", expand=True, padx=20, pady=5)

        # --- Columna Izquierda: Catálogo ---
        frame_catalogo = tk.LabelFrame(
            frame_principal, 
            text=" Catálogo Exclusivo ", 
            font=("Helvetica", 11, "bold"), 
            bg="#1b1b1b", 
            fg="#e0e0e0", 
            bd=1, 
            relief="solid"
        )
        frame_catalogo.pack(side="left", fill="both", expand=True, padx=(0, 10))

        self.perfume_var = tk.StringVar(value=list(self.catalogo.keys())[0])

        for perfume, precio in self.catalogo.items():
            rb = tk.Radiobutton(
                frame_catalogo, 
                text=f"{perfume} — ${precio:.2f}", 
                variable=self.perfume_var, 
                value=perfume, 
                font=("Helvetica", 10), 
                bg="#1b1b1b", 
                fg="#f5f5f5", 
                selectcolor="#2a2a2a",
                activebackground="#1b1b1b",
                activeforeground="#d4af37",
                anchor="w"
            )
            rb.pack(anchor="w", padx=15, pady=8)

        btn_agregar = tk.Button(
            frame_catalogo, 
            text="Agregar al Carrito", 
            command=self.agregar_al_carrito, 
            font=("Helvetica", 10, "bold"), 
            bg="#d4af37", 
            fg="#121212", 
            relief="flat",
            cursor="hand2",
            padx=10, 
            pady=5
        )
        btn_agregar.pack(pady=15, padx=15)

        # --- Columna Derecha: Resumen de Carrito ---
        frame_carrito = tk.LabelFrame(
            frame_principal, 
            text=" Resumen de Orden ", 
            font=("Helvetica", 11, "bold"), 
            bg="#1b1b1b", 
            fg="#e0e0e0", 
            bd=1, 
            relief="solid"
        )
        frame_carrito.pack(side="right", fill="both", expand=True, padx=(10, 0))

        self.txt_carrito = tk.Text(
            frame_carrito, 
            height=12, 
            width=30, 
            font=("Consolas", 10), 
            bg="#0f0f0f", 
            fg="#00ffcc", 
            insertbackground="white",
            relief="flat"
        )
        self.txt_carrito.pack(padx=15, pady=10, fill="both", expand=True)

        btn_finalizar = tk.Button(
            frame_carrito, 
            text="Finalizar Venta", 
            command=self.finalizar_venta, 
            font=("Helvetica", 10, "bold"), 
            bg="#28a745", 
            fg="white", 
            relief="flat",
            cursor="hand2",
            padx=10, 
            pady=5
        )
        btn_finalizar.pack(pady=(0, 15), padx=15)

        # Barra de Estado Inferior (Estilo Toast)
        self.lbl_toast = tk.Label(
            self.root, 
            text="Sistema listo. Seleccione sus fragancias.", 
            font=("Helvetica", 9, "italic"), 
            bg="#1b1b1b", 
            fg="#888888", 
            anchor="w", 
            padx=15, 
            pady=5
        )
        self.lbl_toast.pack(fill="x", side="bottom")

    def agregar_al_carrito(self):
        seleccion = self.perfume_var.get()
        precio = self.catalogo[seleccion]
        self.carrito.append((seleccion, precio))
        
        # Actualizar vista de texto del carrito
        self.txt_carrito.delete("1.0", tk.END)
        total = 0
        for item, precio in self.carrito:
            self.txt_carrito.insert(tk.END, f"• {item}\n  ${precio:.2f}\n\n")
            total += precio
        
        self.txt_carrito.insert(tk.END, f"--------------------\nTOTAL PARCIAL: ${total:.2f}")
        self.lbl_toast.config(text=f"Agregado al carrito: {seleccion}", fg="#d4af37")

    def finalizar_venta(self):
        if not self.carrito:
            messagebox.showwarning("Carrito Vacío", "No hay productos seleccionados en la orden.")
            return
        
        total = sum(precio for _, precio in self.carrito)
        messagebox.showinfo("Éxito", f"¡Venta registrada con éxito!\nTotal cobrado: ${total:.2f}")
        self.carrito.clear()
        self.txt_carrito.delete("1.0", tk.END)
        self.lbl_toast.config(text="Venta procesada correctamente. Nuevo ticket iniciado.", fg="#28a745")

if __name__ == "__main__":
    root = tk.Tk()
    app = RyanShopApp(root)
    root.mainloop()