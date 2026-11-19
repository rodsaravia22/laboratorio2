"""Interfaz gráfica Tkinter para la calculadora."""

import tkinter as tk
from tkinter import messagebox, ttk


def iniciar_interfaz(calcular, agregar, listar, limpiar):
    """Construye y ejecuta la ventana usando las funciones inyectadas."""
    root = tk.Tk()
    root.title("Calculadora")
    root.geometry("480x560")
    root.minsize(420, 500)
    root.configure(background="#f3f6fb")

    style = ttk.Style(root)
    if "clam" in style.theme_names():
        style.theme_use("clam")
    style.configure("TFrame", background="#f3f6fb")
    style.configure("TLabel", background="#f3f6fb", foreground="#1e293b", font=("Segoe UI", 10))
    style.configure("Title.TLabel", font=("Segoe UI", 22, "bold"), foreground="#172554")
    style.configure("Result.TLabel", font=("Segoe UI", 18, "bold"), foreground="#2563eb")
    style.configure("TButton", font=("Segoe UI", 10), padding=8)

    frame = ttk.Frame(root, padding=24)
    frame.pack(fill="both", expand=True)
    ttk.Label(frame, text="Calculadora", style="Title.TLabel").pack(anchor="w")
    ttk.Label(frame, text="Operaciones sencillas, resultados claros").pack(anchor="w", pady=(2, 18))

    form = ttk.Frame(frame)
    form.pack(fill="x")
    ttk.Label(form, text="Primer número").grid(row=0, column=0, sticky="w", pady=(0, 5))
    first = ttk.Entry(form, font=("Segoe UI", 12))
    first.grid(row=1, column=0, sticky="ew", padx=(0, 8), ipady=5)
    ttk.Label(form, text="Segundo número").grid(row=0, column=1, sticky="w", pady=(0, 5))
    second = ttk.Entry(form, font=("Segoe UI", 12))
    second.grid(row=1, column=1, sticky="ew", ipady=5)
    form.columnconfigure(0, weight=1)
    form.columnconfigure(1, weight=1)

    ttk.Label(frame, text="Operación").pack(anchor="w", pady=(16, 5))
    operation = tk.StringVar(value="+")
    selector = ttk.Combobox(frame, textvariable=operation, values=("+", "-", "*", "/", "**", "raiz"), state="readonly")
    selector.pack(fill="x", ipady=4)
    result = ttk.Label(frame, text="Resultado: —", style="Result.TLabel")
    result.pack(anchor="w", pady=(18, 12))

    ttk.Label(frame, text="Historial reciente").pack(anchor="w", pady=(4, 6))
    history_box = tk.Listbox(frame, height=6, font=("Segoe UI", 10), relief="flat", background="white", foreground="#334155", activestyle="none", highlightthickness=1, highlightbackground="#dbe3ef")
    history_box.pack(fill="both", expand=True)
    history = []

    def refresh_history():
        history_box.delete(0, tk.END)
        for item in listar(history):
            history_box.insert(tk.END, item)

    def run_calculation():
        try:
            a = float(first.get())
            op = operation.get()
            if op == "raiz":
                value = calcular(op, a)
                description = f"√({a:g}) = {value:g}"
            else:
                b = float(second.get())
                value = calcular(op, a, b)
                description = f"{a:g} {op} {b:g} = {value:g}"
        except ValueError as exc:
            messagebox.showerror("No se pudo calcular", str(exc) or "Introduce números válidos.", parent=root)
            return
        except (OverflowError, TypeError) as exc:
            messagebox.showerror("No se pudo calcular", f"Revisa los números introducidos: {exc}", parent=root)
            return
        result.configure(text=f"Resultado: {value:g}")
        agregar(history, description)
        refresh_history()

    def clear_history():
        limpiar(history)
        refresh_history()

    ttk.Button(frame, text="Calcular", command=run_calculation).pack(fill="x", pady=(0, 8))
    ttk.Button(frame, text="Borrar historial", command=clear_history).pack(fill="x")
    root.bind("<Return>", lambda _event: run_calculation())
    first.focus_set()
    root.mainloop()
