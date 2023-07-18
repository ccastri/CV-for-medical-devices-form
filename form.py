from tkinter import*

win=Tk()
win.title('Registro de equipo')
win.geometry('350x700')
# win.configure(bg='blue')
def crear():
    print('Ingresa la informacion relevante del nuevo equipo')
    
    
name= Label(win, text="Ingrese el nombre del equipo")
name.grid(row=0, column=0)
name.config(padx=10, pady=10)
input_field_name= Entry(win)
input_field_name.grid(row=0,column=1)
but1=Button(win, text="Crear", fg="blue", command=crear)
but1.grid(row=1, column=0, pady=10, columnspan=2)
but2=Button(win, text="Eliminar", fg="red", command=win.quit)
but2.grid(row=2, column=0, pady=10, columnspan=2)
win.mainloop()