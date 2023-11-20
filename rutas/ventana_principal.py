from tkinter import *
from tkinter import ttk
from carga_libros import VentanaCarga
from carga_socios import VentanaCargaSocios
from biblioteca import Biblioteca
import time
biblioteca = Biblioteca()

class VentanaPrincipal():
    
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Biblioteca La Rioja")
        self.ventana.geometry("800x400")

        style = ttk.Style()
        style.configure("TButton",
                        padding=5,
                        relief="flat",
                        background="#E0E1DD",
                        foreground="black",
                        font=('Monserrat', 10, 'bold'))

        style.map("TButton",
                  background=[('active', '#2980b9')])

        # ppal
        contenedor_principal = Frame(self.ventana, bg='#778DA9')
        contenedor_principal.pack(expand=True, fill='both')

        # msjbienvenida
        self.mensaje_bienvenida = Label(contenedor_principal, text="Bienvenido usuario", font=('Monserrat', 12, 'bold'), bg='#778DA9')
        self.mensaje_bienvenida.place(x=400, y=15, anchor=NW)

        # Mostrar el horario actual
        self.label_horario = Label(contenedor_principal, text="", font=('Monserrat', 12, 'bold'), bg='#778DA9')
        self.label_horario.place(x=377, y=40, anchor=NW)

        # Iniciar la actualización del horario
        self.actualizar_horario()

        # botonera
        botonera = Frame(contenedor_principal, bg='#415A77', width=150)
        botonera.pack(side=LEFT, fill='y')

        # iconos
        self.books_icon = PhotoImage(file="images/libros.png").subsample(15, 15)
        self.reports_icon = PhotoImage(file="images/reporte.png").subsample(15, 15)
        self.users_icon = PhotoImage(file="images/usuario.png").subsample(15, 15)

        # botones
        ttk.Button(botonera, text="Administrar Libros", image=self.books_icon, compound="left", command=self.abrir_ventana_carga_libros).grid(row=0, column=0, pady=10, padx=10)
        ttk.Button(botonera, text="Administrar Socios", image=self.users_icon, compound="left", command=self.abrir_ventana_carga_socios).grid(row=1, column=0, pady=10)
        ttk.Button(botonera, text="Generar Reportes", image=self.reports_icon, compound="left").grid(row=2, column=0, pady=10)

    def abrir_ventana_carga_libros(self):
        ventana_carga = VentanaCarga(biblioteca)
        ventana_carga.mostrar()

    def actualizar_horario(self):
        horario_actual = time.strftime("%H:%M:%S")
        self.label_horario.config(text=f"Horario actual: {horario_actual}")
        self.ventana.after(1000, self.actualizar_horario)

    def abrir_ventana_carga_socios(self):
        ventana_carga = VentanaCargaSocios()
        ventana_carga.mostrar()
        
    def mostrar(self):
        self.ventana.mainloop()
        
