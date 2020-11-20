import sys
#provee acceso a funciones y objetos mantenidos por del intérprete.
import sqlite3
from sqlite3 import Error
#para hacer conexión a la base de datos
import pandas as pd
#para un anlisis de datos
from tkinter import *
from tkinter import ttk
#para crear las ventanas del usuario
from tkinter import messagebox as MessageBox
#para mandar un mensaje al usuario
from PIL import ImageTk,Image
#para poner una imagen en una ventana
 

#Creamos la ventana del login y le damos medidas
ventana_login = Tk()
ventana_login.title ("Seguridad - Ventana Acceso ")
ventana_login.geometry ("320x400")
ventana_login.resizable(0, 0)

#Acomodamos el cuadro de texto del usuario
usuario_label = Label(ventana_login, text = "Usuario:")
usuario_label.grid(row=1, column=0, padx=85, pady=5)
usuario_entry = Entry(ventana_login)
usuario_entry.grid(row=2, column=0, padx=85)

#Acomodamos el cuadro de texto de la contraseña
contraseña_label = Label(ventana_login, text = "Contraseña:")
contraseña_label.grid(row=3, column=0, padx=85, pady=5)
contraseña_entry = Entry(ventana_login, show = "*")
contraseña_entry.grid(row=4, column=0, padx=85)

#Ponemos una imagen para identificar a la empresa
imagen=Image.open("Simbolo.png")                      
imagen=imagen.resize((200,200),Image.ANTIALIAS)     
photoImg=ImageTk.PhotoImage(imagen)                 
panel=ttk.Label(ventana_login,image=photoImg).grid(row=0, column=0, padx=10, pady=5)

#Hacemos la función del logian  
def login():
    #Nos conectamos a la base de datos y la tabla usuario para poder logearnos
    connection = sqlite3.connect('PIA.db')
    c = connection.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Usuario(Usuario TEXT NOT NULL, Pass TEXT NOT NULL, Nombre TEXT NOT NULL, Apellido Paterno TEXT NOT NULL);")
    
    usuario = usuario_entry.get()
    contra = contraseña_entry.get()
    
    c.execute('SELECT * FROM Usuario WHERE Usuario = ? AND Pass = ?', (usuario, contra))

    if c.fetchall():
        MessageBox.showinfo(title = "Login correcto", message = "Usuario Correcto")
        c.close()
        ventana_login.destroy()
        #Creamos la clase producto para poder crear las tablas y la manipulacion de los datos
        class Producto:
            
#********************************************************************************************************************************************************************************

            #Creación de la base de datos en SQLite3 con sus tablas correspondientes
            try:
                with sqlite3.connect("PIA.db") as conn:
                    c = conn.cursor()
                    c.execute("CREATE TABLE IF NOT EXISTS Producto(ID_P INTEGER PRIMARY KEY, Nombre TEXT NOT NULL, Precio INTEGER NOT NULL, Descripcion TEXT, Categoria TEXT);")
                    c.execute("CREATE TABLE IF NOT EXISTS Venta(ID_V INTEGER PRIMARY KEY, Monto INTEGER NOT NULL, Fecha TEXT NOT NULL, Categoria TEXT);")
                    print("--Carga de datos exitosamente-- \n")
            except Error as e:
                print(e)

#********************************************************************************************************************************************************************************
            #Abrimos la conexion a la base de datos para poder hacer el CRUD
            def abrirBD(self):
                conexion=sqlite3.connect("PIA.db")
                return conexion
            #Funcion que regsitra un usuario
            def InsertarUsuario(self, datos):
                enlace=self.abrirBD()
                cursor=enlace.cursor()
                sql="INSERT INTO Usuario(Usuario, Pass, Nombre, Apellido) VALUES (?,?,?,?)"
                cursor.execute(sql, datos)
                enlace.commit()
                enlace.close()
            #Funcion que regsitra un producto
            def InsertarDatos(self, datos):
                enlace=self.abrirBD()
                cursor=enlace.cursor()
                sql="INSERT INTO Producto(ID_P, Nombre, Precio, Descripcion, Categoria) VALUES (?,?,?,?,?)"
                cursor.execute(sql, datos)
                enlace.commit()
                enlace.close()
            #Funcion que modifica un producto
            def Modificar_Datos(self, datos):
                try:
                    enlace=self.abrirBD()
                    cursor=enlace.cursor()
                    sql="UPDATE Producto SET Nombre = ?, Precio = ?, Descripcion = ?, Categoria = ? WHERE ID_P = ?"
                    cursor.execute(sql, datos)
                    enlace.commit()
                    return cursor.rowcount
                except:
                    enlace.close()
            #Funcion para eliminar un producto
            def baja(self, datos):
                try:
                    enlace=self.abrirBD()
                    cursor=enlace.cursor()
                    sql="DELETE FROM Producto WHERE ID_P = ?"
                    cursor.execute(sql, datos)
                    enlace.commit()
                    return cursor.rowcount
                except:
                    enlace.close()
            #Funcion para consultar un producto
            def consulta(self, datos):
                try:
                    enlace=self.abrirBD()
                    cursor=enlace.cursor()
                    sql="SELECT Nombre, Precio, Descripcion, Categoria FROM Producto WHERE ID_P = ?"
                    cursor.execute(sql, datos)
                    return cursor.fetchall()
                finally:
                    enlace.close()
#*********************************************************************************************************************************************************
        #Definir la ventana de menu
        ventana = Tk()
        gasto1 = Producto()
        ventana.minsize(450, 500)
        ventana.title("Empresa Computadoras Premium | PIA")
        ventana.resizable(0, 0)

        #Funcion para salir de la aplicación 
        def salir():
            opción = MessageBox.askquestion("Salir", "¿Seguro que quieres salir de la aplicación?")
            if opción == "yes":
                ventana.destroy()

        #Ventana de inicio de la aplicación y darle la medida, y el color  
        def inicio():
            home_label.config(
                fg="white",
                bg="dark cyan",
                font=("Times New Roman", 40),
                padx=270,
                pady=20)
            home_label.grid(row=0, column=0)
            home_frame.grid(row=1)
            
            #Botones para desplazarse dentro del menu a la opción que elija el usuario
            boton_agregar.grid(row=1, column=0, padx=15, pady=30, sticky=NW)
            boton_editar.grid(row=1, column=1, padx=15, pady=30, sticky=NE)
            boton_eliminar.grid(row=2, column=0, padx=15, pady=30, sticky=SW)
            boton_consulta.grid(row=2, column=1, padx=15, pady=30, sticky=SE)
            home_separator.grid(row=3, column=0)
            home_separator2.grid(row=3, column=1)
            boton_venta.grid(row=4, column=0, padx=15, pady=30, sticky=SW)
            boton_usuario.grid(row=4, column=1, padx=15, pady=30, sticky=SE)
            barra_status.grid(row=6, column=0,padx=150, ipadx=10, ipady=10)
            #Darle colores a los botones y el tipo de letra
            boton_agregar.config(bg="#008B8B", fg="white", font=("Times New Roman", 14, "bold"), bd=5,)
            boton_editar.config(bg="#000000", fg="white", font=("Times New Roman", 14, "bold"), bd=5,)
            boton_eliminar.config(bg="#000000", fg="white", font=("Times New Roman", 14, "bold"), bd=5,)
            boton_consulta.config(bg="#008B8B", fg="white", font=("Times New Roman", 14, "bold"), bd=5,)
            boton_venta.config(bg="#008B8B", fg="white", font=("Times New Roman", 14, "bold"), bd=5,)
            boton_usuario.config(bg="#000000", fg="white", font=("Times New Roman", 14, "bold"), bd=5,)
            home_separator.config(font=("Arial", 14))
            home_separator2.config(font=("Arial", 14))
            barra_status.config(bg="dark cyan", fg="white", font=("Times New Roman", 12, "bold"), borderwidth=6)

            #Esconder las ventanas y poder dezplazarnos entre ellas 
            agregar_label.grid_remove()
            agregar_frame.grid_remove()
            editar_label.grid_remove()
            editar_frame.grid_remove()
            eliminar_label.grid_remove()
            eliminar_frame.grid_remove()
            consulta_label.grid_remove()
            consulta_frame.grid_remove()
            venta_label.grid_remove()
            venta_frame.grid_remove()
            usuario_label.grid_remove()
            usuario_frame.grid_remove()
            return True
#**************************************************************************************************************************************
        #Ventana de registrar y darle la medida, y el color  
        def agregar():
            agregar_label.config(
                fg="white",
                bg="dark cyan",
                font=("Times New Roman", 30),
                padx=150,
                pady=20)
            
            #Posicion de los recuadros de textos a la hora de registrar un prodcuto
            agregar_label.grid(row=0, column=0, columnspan=10)
            agregar_frame.grid(row=1)

            agregar_id_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
            agregar_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

            agregar_name_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
            agregar_name_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

            agregar_price_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
            agregar_price_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

            agregar_description_label.grid(row=4, column=0, padx=5, pady=5, sticky=NE)
            agregar_description_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)
            agregar_description_entry.config(width=30, height=1, font=("Arial", 12), padx=15, pady=15)

            agregar_category.place(x=40, y=180)

            guardar.grid(row=6, column=1, padx=5, pady=30, sticky=E)
            guardar.config(padx=15, pady=5, bg="#008B8B", fg="white", font=("Arial", 10, "bold"))

            #Esconder las ventanas y poder dezplazarnos entre ellas
            home_label.grid_remove()
            home_frame.grid_remove()
            editar_label.grid_remove()
            editar_frame.grid_remove()
            eliminar_label.grid_remove()
            eliminar_frame.grid_remove()
            consulta_label.grid_remove()
            consulta_frame.grid_remove()
            venta_label.grid_remove()
            venta_frame.grid_remove()
            usuario_label.grid_remove()
            usuario_frame.grid_remove()
            return True
#******************************************************************************************************************************************
        #Ventana de actualizar y darle la medida, y el color 
        def editar():
            editar_label.config(
                fg="white",
                bg="dark cyan",
                font=("Times New Roman", 30),
                padx=150,
                pady=20)
            
            #Posicion de los recuadros de textos a la hora de actualizar un prodcuto
            editar_label.grid(row=0, column=0, columnspan=10)
            editar_frame.grid(row=1)

            editar_id_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
            editar_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

            editar_name_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
            editar_name_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

            editar_price_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
            editar_price_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

            editar_description_label.grid(row=4, column=0, padx=5, pady=5, sticky=NE)
            editar_description_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)
            editar_description_entry.config(width=30, height=1, font=("Arial", 12), padx=15, pady=15)

            editar_category.place(x=50, y=180)

            actualizar.grid(row=6, column=1, padx=5, pady=30, sticky=E)
            actualizar.config(padx=15, pady=5, bg="#008B8B", fg="white", font=("Arial", 10, "bold"))

            #Esconder las ventanas y poder dezplazarnos entre ellas
            home_label.grid_remove()
            home_frame.grid_remove()
            agregar_label.grid_remove()
            agregar_frame.grid_remove()
            eliminar_label.grid_remove()
            eliminar_frame.grid_remove()
            consulta_label.grid_remove()
            consulta_frame.grid_remove()
            venta_label.grid_remove()
            venta_frame.grid_remove()
            usuario_label.grid_remove()
            usuario_frame.grid_remove()
            return True
#*******************************************************************************************************************************************
        #Ventana de consulta y darle la medida, y el color 
        def consulta():
            consulta_label.config(
                fg="white",
                bg="dark cyan",
                font=("Times New Roman", 30),
                padx=150,
                pady=20)
            
            #Posicion de los recuadros de textos a la hora de consultar un prodcuto
            consulta_label.grid(row=0, column=0)
            consulta_frame.grid(row=1)

            consulta_id_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
            consulta_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

            consulta_name_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
            consulta_name_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

            consulta_price_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
            consulta_price_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

            consulta_description_label.grid(row=4, column=0, padx=5, pady=5, sticky=NE)
            consulta_description_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)

            consulta_category.place(x=1, y=180)

            consultar.grid(row=6, column=1, padx=100, pady=30, sticky=E)
            consultar.config(padx=15, pady=5, bg="#008B8B", fg="white", font=("Arial", 10, "bold"))

            #Esconder las ventanas y poder dezplazarnos entre ellas
            home_label.grid_remove()
            home_frame.grid_remove()
            agregar_label.grid_remove()
            agregar_frame.grid_remove()
            editar_label.grid_remove()
            editar_frame.grid_remove()
            eliminar_label.grid_remove()
            eliminar_frame.grid_remove()
            venta_label.grid_remove()
            venta_frame.grid_remove()
            usuario_label.grid_remove()
            usuario_frame.grid_remove()
            return True        

#*******************************************************************************************************************************************
        #Ventana de eliminar y darle la medida, y el color 
        def eliminarr():
            eliminar_label.config(
                fg="white",
                bg="dark cyan",
                font=("Times New Roman", 30),
                padx=150,
                pady=20)
            
            #Posicion de los recuadros de textos a la hora de eliminar un prodcuto
            eliminar_label.grid(row=0, column=0)
            eliminar_frame.grid(row=1)

            eliminar_id_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
            eliminar_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

            eliminar.grid(row=1, column=5, padx=5, pady=30, sticky=E)
            eliminar.config(padx=20, pady=5, bg="#008B8B", fg="white", font=("Arial", 10, "bold"))

            #Esconder las ventanas y poder dezplazarnos entre ellas
            home_label.grid_remove()
            home_frame.grid_remove()
            agregar_label.grid_remove()
            agregar_frame.grid_remove()
            editar_label.grid_remove()
            editar_frame.grid_remove()
            consulta_label.grid_remove()
            consulta_frame.grid_remove()
            venta_label.grid_remove()
            venta_frame.grid_remove()
            usuario_label.grid_remove()
            usuario_frame.grid_remove()
            return True
#**************************************************************************************************************************************
        #Ventana de registar venta y darle la medida, y el color 
        def ventaa():
            venta_label.config(
                fg="white",
                bg="dark cyan",
                font=("Times New Roman", 30),
                padx=220,
                pady=20)
            
            #Posicion de los recuadros de textos a la hora de registar una venta
            venta_label.grid(row=0, column=0)
            venta_frame.grid(row=1)

            venta_id_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
            venta_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
            
            venta_idP_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
            venta_idP_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
            
            venta_monto_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
            venta_monto_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
            
            venta_fecha_label.grid(row=4, column=0, padx=5, pady=5, sticky=E)
            venta_fecha_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)

            #Esconder las ventanas y poder dezplazarnos entre ellas
            home_label.grid_remove()
            home_frame.grid_remove()
            agregar_label.grid_remove()
            agregar_frame.grid_remove()
            editar_label.grid_remove()
            editar_frame.grid_remove()
            eliminar_label.grid_remove()
            eliminar_frame.grid_remove()
            consulta_label.grid_remove()
            consulta_frame.grid_remove()
            usuario_label.grid_remove()
            usuario_frame.grid_remove()
            return True
#**************************************************************************************************************************************
        #Ventana de registar usuario y darle la medida, y el color
        def usuarios():
            usuario_label.config(
                fg="white",
                bg="dark cyan",
                font=("Times New Roman", 30),
                padx=150,
                pady=20)
            
            #Posicion de los recuadros de textos a la hora de registar un usuario
            usuario_label.grid(row=0, column=0)

            usuario_frame.grid(row=1)

            usuario_id_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
            usuario_id_entry.grid(row=1, column=1, padx=5, pady=5, sticky=S)

            usuario_pass_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
            usuario_pass_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

            usuario_name_label.grid(row=3, column=0, padx=5, pady=5, sticky=E)
            usuario_name_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

            usuario_apellido_label.grid(row=4, column=0, padx=5, pady=5, sticky=NE)
            usuario_apellido_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)

            agregar_usuario.grid(row=5, column=1, padx=5, pady=30, sticky=E)
            agregar_usuario.config(padx=15, pady=5, bg="#008B8B", fg="white", font=("Arial", 10, "bold"))

            #Esconder las ventanas y poder dezplazarnos entre ellas
            home_label.grid_remove()
            home_frame.grid_remove()
            editar_label.grid_remove()
            editar_frame.grid_remove()
            eliminar_label.grid_remove()
            eliminar_frame.grid_remove()
            consulta_label.grid_remove()
            consulta_frame.grid_remove()
            venta_label.grid_remove()
            venta_frame.grid_remove()
            return True
#**************************************************************************************************************************************
        #Funcion para el manejo de agreagar los productos teniendo la exepcion de un problema
        def agregar_product():
            try:
                datos = (id_data.get(), name_data.get(), price_data.get(), agregar_description_entry.get("1.0", "end-1c"), agregar_category.get())
                if id_data.get() == "" or name_data.get() == "" or price_data.get() == "" or agregar_description_entry.get("1.0", "end-1c") == "" or agregar_category.get() == "Categoria":
                    MessageBox.showwarning("Advertencia", "Complete el Formulario.")
                else:
                    gasto1.InsertarDatos(datos)
                    MessageBox.showinfo("Estatus de la aplicación", "Los datos fueron cargados")
                    id_data.set("")
                    name_data.set("")
                    price_data.set("")
                    agregar_description_entry.delete("1.0", END)
                    agregar_category.set("Categoria")
            except:
                MessageBox.showwarning("Advertencia", "El ID del producto ya esta en uso o Contiene letras el ID.")
        #Funciones para el manejo de agreagar a un usuario teniendo en cuenta a la que el administrador le asigne      
        def agregar_usuario():
            try:
                if usuario == "Administrador":
                    datos = (usuario_data.get(), pass_data.get(), name_data.get(), apellido_data.get())
                    if usuario_data.get() == "" or pass_data.get() == "":
                        MessageBox.showwarning("Advertencia", "Complete el Formulario.")
                    else:
                        gasto1.InsertarUsuario(datos)
                        MessageBox.showinfo("Estatus de la aplicación", "Los datos fueron cargados")
                        usuario_data.set("")
                        pass_data.set("")
                        name_data.set("")
                        apellido_data.set("")
                else:
                    MessageBox.showinfo("Estatus de la aplicación", "No cuentas con el permiso suficiente")
            except:
                MessageBox.showwarning("Advertencia", "Rellenar los campos vacios.")
        #Funcion para editar el producto teniendo la exepcion de un problema
        def editar_product():
            try:
                if usuario == "Administrador":
                    datos = (id_data.get(), name_data.get(), price_data.get(), editar_description_entry.get("1.0", "end-1c"), editar_category.get())
                    if id_data.get() == "" or name_data.get() == "" or price_data.get() == "" or editar_description_entry.get("1.0", "end-1c") == "" or editar_category.get() == "Categoria":
                        MessageBox.showwarning("Advertencia", "Complete el Formulario.")
                    else:
                        datos = (name_data.get(), price_data.get(), editar_description_entry.get("1.0", "end-1c"), category_data.get(), id_data.get())
                        cantidad = gasto1.Modificar_Datos(datos)
                        if cantidad == 1:
                            MessageBox.showinfo("Estatus de la aplicación", "Se Actualizo el Producto")
                        else:
                            MessageBox.showwarning("Estatus de la aplicación", "El ID del Producto no Existe")
                else:
                    MessageBox.showinfo("Estatus de la aplicación", "No cuentas con el permiso suficiente")
            except:
                MessageBox.showerror("Advertencia", "Rellenar los campos vacios.")
        #Funcion para eliminar un producto teniendo la restriccion de que solo el administrador puede elimnar el producto
        def eliminar_product():
                if usuario == "Administrador":
                    datos = (id_data.get(), )
                    cantidad = gasto1.baja(datos)
                    if id_data.get() == "":
                        MessageBox.showwarning("Advertencia", "Complete el Formulario.")
                    else:
                        if cantidad == 1:
                            MessageBox.showinfo("Estatus de la aplicación", "Se eliminó el prodcuto")
                        else:
                            MessageBox.showwarnin("Advertencia", "El ID del Producto no existe")
                else:
                    MessageBox.showinfo("Estatus de la aplicación", "No cuentas con el permiso suficiente")
        #Funcion para consultar un producto de la base de datos 
        def query_product():
            datos = (id_data.get(), )
            respuesta = gasto1.consulta(datos)
            if len(respuesta)>0:
                name_data.set(respuesta[0][0])
                price_data.set(respuesta[0][1])
                description_data.set(respuesta[0][2])
                category_data.set(respuesta[0][3])
                MessageBox.showinfo("Estatus de la aplicación", "Consulta terminada")
            else:
                name_data.set("")
                price_data.set("")
                category_data.set("Categoria")
                MessageBox.showwarning("Advertencia", "El ID del producto no existe o no lleno el campo ID")
#**************************************************************************************************************************************
        #Variables importantes
        id_data = StringVar()
        name_data = StringVar()
        apellido_data = StringVar()
        price_data = StringVar()
        description_data = StringVar()
        category_data = StringVar()
        agregar_status = StringVar()
        usuario_data = StringVar()
        pass_data = StringVar()
#**************************************************************************************************************************************
        #Definimos la pantalla del MENU
        home_frame = Frame(ventana)

        home_label = Label(ventana, text="Menú")
        boton_agregar = Button(home_frame, text="¡Registre un Producto!", command=agregar)
        boton_editar = Button(home_frame, text="¡Actualizar Producto!", command=editar)
        boton_eliminar = Button(home_frame, text="¡Eliminar Producto!", command=eliminarr)
        boton_consulta = Button(home_frame, text="¡Consultar Producto!", command=consulta)
        boton_venta = Button(home_frame, text="¡Regsitrar Venta!", command=ventaa)
        boton_usuario = Button(home_frame, text="¡Registrar Usuario!", command=usuarios)
        home_separator = Label(home_frame, text="**************************************")
        home_separator2 = Label(home_frame, text="*************************************")

        barra_status = Label(ventana, textvariable=agregar_status)
        agregar_status.set(f"Conectado en la sesion: {usuario}")
#**************************************************************************************************************************************
        #Definimos el recuadro del REGISTRO 
        agregar_label = Label(ventana, text="Ingrese un Producto")

        #Formulario para el REGISTRO
        agregar_frame = Frame(ventana)

        agregar_id_label = Label(agregar_frame, text="ID del Producto: ")
        agregar_id_entry = Entry(agregar_frame, textvariable=id_data)

        agregar_name_label = Label(agregar_frame, text="Nombre: ")
        agregar_name_entry = Entry(agregar_frame, textvariable=name_data)

        agregar_price_label = Label(agregar_frame, text="Precio: ")
        agregar_price_entry = Entry(agregar_frame, textvariable=price_data)

        agregar_description_label = Label(agregar_frame, text="Descripción: ")
        agregar_description_entry = Text(agregar_frame)

        agregar_category = ttk.Combobox(agregar_frame)
        agregar_category.set("Categoria")
        agregar_category['values'] = ('Laptop', 'Computadora de Escritorio')
        agregar_category.current()

        guardar = Button(agregar_frame, text="Guardar", command=agregar_product)
#**************************************************************************************************************************************
        #Definimos el recuadro del EDITAR
        editar_label = Label(ventana, text="Actualizar Producto")

        #Formulario para el EDITAR
        editar_frame = Frame(ventana)

        editar_id_label = Label(editar_frame, text="ID del Producto: ")
        editar_id_entry = Entry(editar_frame, textvariable=id_data)

        editar_name_label = Label(editar_frame, text="Nombre: ")
        editar_name_entry = Entry(editar_frame, textvariable=name_data)

        editar_price_label = Label(editar_frame, text="Precio: ")
        editar_price_entry = Entry(editar_frame, textvariable=price_data)

        editar_description_label = Label(editar_frame, text="Descripción: ")
        editar_description_entry = Text(editar_frame)

        editar_category = ttk.Combobox(editar_frame, textvariable=category_data)
        editar_category.set("Categoria")
        editar_category['values'] = ('Laptop', 'Computadora de Escritorio')
        editar_category.current()

        actualizar = Button(editar_frame, text="Actualizar", command=editar_product)
#**************************************************************************************************************************************
        #Definimos el recuadro del ELIMINAR 
        eliminar_label = Label(ventana, text="Eliminar producto")

        #Formulario para el ELIMINAR
        eliminar_frame = Frame(ventana)

        eliminar_id_label = Label(eliminar_frame, text="ID del producto: ")
        eliminar_id_entry = Entry(eliminar_frame, textvariable=id_data)

        eliminar = Button(eliminar_frame, text="Eliminar", command=eliminar_product)
#**************************************************************************************************************************************
        #Definimos el recuadro del CONSULTAR
        consulta_label = Label(ventana, text="Consultar productos")

        #Formulario para el CONSULTAR
        consulta_frame = Frame(ventana)

        consulta_id_label = Label(consulta_frame, text="ID del producto: ")
        consulta_id_entry = Entry(consulta_frame, textvariable=id_data)

        consulta_name_label = Label(consulta_frame, text="Nombre: ")
        consulta_name_entry = Entry(consulta_frame, textvariable=name_data)

        consulta_price_label = Label(consulta_frame, text="Precio: ")
        consulta_price_entry = Entry(consulta_frame, textvariable=price_data)

        consulta_description_label = Label(consulta_frame, text="Descripción: ")
        consulta_description_entry = Entry(consulta_frame, textvariable=description_data)

        consulta_category = ttk.Combobox(consulta_frame, textvariable=category_data)
        consulta_category.set("Categoria")
        consulta_category['values'] = ('Laptop', 'Computadora de Escritorio')
        consulta_category.current()

        consultar = Button(consulta_frame, text="Consultar", command=query_product)

#**************************************************************************************************************************************
        #Definimos el recuadro del REGISTRAR VENTA
        venta_label = Label(ventana, text="Registrar Venta")
        
        #Formulario para REGISTRAR VENTA
        venta_frame = Frame(ventana)
        
        venta_id_label = Label(venta_frame, text="ID de la Venta: ")
        venta_id_entry = Entry(venta_frame)
        
        venta_idP_label = Label(venta_frame, text="ID deL Producto: ")
        venta_idP_entry = Entry(venta_frame)
        
        venta_monto_label = Label(venta_frame, text="Monto total: ")
        venta_monto_entry = Entry(venta_frame)
        
        venta_fecha_label = Label(venta_frame, text="Fecha: ")
        venta_fecha_entry = Entry(venta_frame)
        
        venta = Button(venta_frame, text="Capturar Venta")
#*******************************************************************************************************************************       
        #Definimos el recuadro del REGISTRAR USUARIO
        usuario_label = Label(ventana, text="Registrar Usuario")

        #Formulario para REGISTRAR USUARIO
        usuario_frame = Frame(ventana)

        usuario_id_label = Label(usuario_frame, text="Usuario: ")
        usuario_id_entry = Entry(usuario_frame, textvariable=usuario_data)

        usuario_pass_label = Label(usuario_frame, text="Password: ")
        usuario_pass_entry = Entry(usuario_frame, show = "*", textvariable=pass_data)

        usuario_name_label = Label(usuario_frame, text="Nombre: ")
        usuario_name_entry = Entry(usuario_frame, textvariable=name_data)

        usuario_apellido_label = Label(usuario_frame, text="Apellido Paterno: ")
        usuario_apellido_entry = Entry(usuario_frame, textvariable=apellido_data)

        agregar_usuario = Button(usuario_frame, text="Guardar", command=agregar_usuario)
#**************************************************************************************************************************************
        #Cargar la pantalla del MENU
        inicio()

        #Menú superior
        menu_superior = Menu(ventana)
        menu_superior.add_command(label="Inicio", command=inicio)
        menu_superior.add_command(label="Registrar", command=agregar)
        menu_superior.add_command(label="Actualizar", command=editar)
        menu_superior.add_command(label="Eliminar", command=eliminarr)
        menu_superior.add_command(label="Consultar", command=consulta)
        menu_superior.add_command(label="Registrar Venta", command=ventaa)
        menu_superior.add_command(label="Registrar Usuario", command=usuarios)
        menu_superior.add_command(label="Salir", command=lambda: salir())

        #Cargar el Menú
        ventana.config(menu=menu_superior)

        #Cargar la ventana
        ventana.mainloop()


    else:
     MessageBox.showerror(title = "Login incorrecto", message = "Usuario o contraseña incorrecta")
    #Se cierra la conexion a la base de datos
    c.close()
#Boton para poder entrar en el login 
Logear = Button(ventana_login, text="Iniciar Sesión", command = login)
Logear.grid(row=5, column=0, pady=20)
Logear.config(padx=15, pady=5, bg="#000000", fg="white", font=("Arial", 10, "bold"))

ventana_login.mainloop()
