from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image as pillow_Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image
from reportlab.lib import colors
from openpyxl import Workbook


class Window1:
    imagen= ""
    departamento = ""
    municipio = ""
    entidad=""
    correo=""
    direccion=""
    telefono=""

    def __init__(self, parent):
        self.parent = parent
        self.create_form()

    def create_form(self):
        departments = [
            'Select department',
            'Antioquia',
            'Arauca',
            'Atlántico',
            'Bolívar',
            'Boyacá',
            'Caldas',
            'Caquetá',
            'Casanare',
            'Cauca',
            'Cesar',
            'Chocó',
            'Córdoba',
            'Cundinamarca',
            'Guainía',
            'Guaviare',
            'Huila',
            'La Guajira',
            'Magdalena',
            'Meta',
            'Nariño',
            'Norte de Santander',
            'Putumayo',
            'Quindío',
            'Risaralda',
            'San Andrés y Providencia',
            'Santander',
            'Sucre',
            'Tolima',
            'Valle del Cauca',
            'Vaupés',
            'Vichada'
        ]
        cities = [
            'Select city',
            'Arauca',
            'Armenia',
            'Barranquilla',
            'Bogotá',
            'Bucaramanga',
            'Cali',
            'Cartagena',
            'Cúcuta',
            'Florencia',
            'Ibagué',
            'Leticia',
            'Manizales',
            'Medellín',
            'Mitú',
            'Mocoa',
            'Montería',
            'Neiva',
            'Pasto',
            'Pereira',
            'Popayán',
            'Puerto Carreño',
            'Puerto Inírida',
            'Quibdó',
            'Riohacha',
            'San Andrés',
            'San José del Guaviare',
            'Santa Marta',
            'Sincelejo',
            'Tunja',
            'Valledupar',
            'Villavicencio',
            'Yopal'
        ]

        # Create the frame for the section
        form_frame = LabelFrame(self.parent, text="Ubicacion geografica", fg='white', bg='lightgray',
                                font=("Helvetica", 12, "bold italic"), padx=10, pady=10)
        form_frame.pack(pady=10)

        # Create the grid frame within the form frame
        grid_frame = Frame(form_frame, bg='lightgray')
        grid_frame.grid(row=0, column=0, padx=10, pady=5, sticky='nsew')

        # Labels
        label_ubicacion_dep = Label(grid_frame, text="Departamento")
        label_ubicacion_municipio = Label(grid_frame, text="Municipio")
        label_entidad = Label(grid_frame, text="Entidad")
        label_correo = Label(grid_frame, text="Correo")
        label_direccion = Label(grid_frame, text="Direccion")
        label_telefono = Label(grid_frame, text="Telefonos")

        # Entry fields
        var_ubicacion_dep = StringVar(grid_frame)
        var_ubicacion_dep.set(self.departamento)
        optionmenu_ubicacion_dep = ttk.Combobox(grid_frame, textvariable=var_ubicacion_dep, values=departments)
        var_ubicacion_municipio = StringVar(grid_frame)
        var_ubicacion_municipio.set(self.municipio)
        optionmenu_ubicacion_municipio = ttk.Combobox(grid_frame, textvariable=var_ubicacion_municipio, values=cities)
        entry_entidad = Entry(grid_frame)
        entry_correo = Entry(grid_frame)
        entry_direccion = Entry(grid_frame)
        entry_telefono = Entry(grid_frame)

        # Set the previously entered values
        entry_entidad.insert(0, self.entidad)
        entry_correo.insert(0, self.correo)
        entry_direccion.insert(0, self.direccion)
        # self.imagen.insert(0, self.image_label['text'])

        # Load the image file
        # Create a label to display the image
        self.image_label = Label(form_frame, text="Drag and drop or click to add an image", bg="white", relief="solid", cursor="hand2")

        # Grid layout
        label_ubicacion_dep.grid(row=0, column=0, sticky=W, padx=10, pady=5)
        label_ubicacion_municipio.grid(row=1, column=0, sticky='news', padx=10, pady=5)
        label_entidad.grid(row=2, column=0, sticky='news', padx=10, pady=5)
        label_correo.grid(row=3, column=0, sticky='ew', padx=10, pady=5)
        label_direccion.grid(row=4, column=0, sticky='ew', padx=10, pady=5)
        label_telefono.grid(row=5, column=0, sticky='ew', padx=10, pady=5)
        optionmenu_ubicacion_dep.grid(row=0, column=1, padx=10, pady=5)
        optionmenu_ubicacion_municipio.grid(row=1, column=1, padx=10, pady=5)
        entry_entidad.grid(row=2, column=1, padx=10, pady=5, sticky='news')
        entry_correo.grid(row=3, column=1, padx=10, pady=5, sticky='news')
        entry_direccion.grid(row=4, column=1, padx=10, pady=5, sticky='news')
        entry_telefono.grid(row=5, column=1, padx=10, pady=5, sticky='news')
        self.image_label.grid(row=0, column=4, ipady=20, padx=10)

        self.image_label.bind("<Button-1>", self.open_image)
        # Next button
        next_button = Button(form_frame, text="Siguiente", command=lambda: self.save_values(entry_entidad.get(), entry_correo.get(), entry_direccion.get(), entry_telefono.get(), var_ubicacion_dep.get(), var_ubicacion_municipio.get()))
        next_button.grid(row=3, columnspan=4, pady=10)

    def open_image(self, event):
        # Open a file dialog to select an image file
        filetypes = [("Image Files", "*.png *.jpg *.jpeg *.gif")]
        filepath = filedialog.askopenfilename(filetypes=filetypes)
        if filepath:
            self.imagen = filepath
            # Update the image placeholder with the selected image
            image = pillow_Image.open(filepath)
            image = image.resize((180, 200))  # Resize the image as needed
            self.photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=self.photo)
            self.image_label.image = self.photo

    def save_values(self, departamento, municipio, entidad, correo, direccion, telefono):
        self.departamento = departamento
        self.municipio = municipio
        self.entidad = entidad
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono

        # Create a PDF file
        pdf_file = "form_data.pdf"
        doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    
        elements = []
    
        # Add the image
        if self.imagen:
            image = Image(self.imagen, width=180, height=200)
            elements.append(image)
    
        # Create the table data
        table_data = [
            ["Departamento", "Municipio", "Entidad", "Correo", "Dirección", "Teléfonos"],
            [departamento, municipio, entidad, correo, direccion, telefono].sort(reverse=True)
        ]
    
        # Define table style
        table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),  # Header text color
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font style
            ('FONTSIZE', (0, 0), (-1, 0), 12),  # Header font size
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 12),
            ('LEFTPADDING', (0, 0), (-1, -1), 5),  # Left padding for header and data cells
            ('RIGHTPADDING', (0, 0), (-1, -1), 5),  # Right padding for header and data cells
            ('TOPPADDING', (0, 0), (-1, -1), 5),  # Top padding for header and data cells
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),  # Bottom padding for header and data cells
        ])

        # Create the table and apply the style
        table = Table(table_data)
        table.setStyle(table_style)

        # Add the image and table to the elements list
        elements.append(table)

        # Build the PDF document
        doc.build(elements)

        print("PDF generated successfully.")

    def save_values_xls(self, departamento, municipio, entidad, correo, direccion, telefono):
        self.departamento = departamento
        self.municipio = municipio
        self.entidad = entidad
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono

        # Create an Excel workbook
        wb = Workbook()
        ws = wb.active

        # Add the data to the worksheet
        header = ["Departamento", "Municipio", "Entidad", "Correo", "Dirección", "Teléfonos"]
        data = [telefono, direccion, correo, entidad, municipio, departamento]

        ws.append(header)
        ws.append(data)

        # Save the Excel workbook
        excel_file = "form_data.xlsx"
        wb.save(excel_file)

    print("Excel file generated successfully.")
class Window2:
    equipo = ""
    forma_adquisicion = ""

    def __init__(self, parent):
        self.parent = parent
        self.create_form()

    def create_form(self):
        # Create the frame for the section
        form_frame = Frame(self.parent)
        form_frame.pack(pady=10)

        # Labels
        label_equipo = Label(form_frame, text="Equipo")
        label_forma_adquisicion = Label(form_frame, text="Forma de Adquisición")

        # Entry fields
        entry_equipo = Entry(form_frame)
        var_forma_adquisicion = StringVar(form_frame)
        var_forma_adquisicion.set(self.forma_adquisicion)
        optionmenu_forma_adquisicion = ttk.Combobox(form_frame, textvariable=var_forma_adquisicion, values=["Opcion de adquisicion", "1. Compra", "2. Donación", "3. Incautación"])

        # Set the previously entered values
        entry_equipo.insert(0, self.equipo)

        # Save the values when the Submit button is clicked
        submit_button = Button(form_frame, text="Submit", command=lambda: self.save_values(entry_equipo.get(), var_forma_adquisicion.get()))

        # Grid layout
        label_equipo.grid(row=0, column=0, sticky=W, padx=10, pady=5)
        label_forma_adquisicion.grid(row=1, column=0, sticky=W, padx=10, pady=5)
        entry_equipo.grid(row=0, column=1, padx=10, pady=5)
        optionmenu_forma_adquisicion.grid(row=1, column=1, padx=10, pady=5)
        submit_button.grid(row=2, column=1, pady=10)

    def save_values(self, equipo, forma_adquisicion):
        self.equipo = equipo
        self.forma_adquisicion = forma_adquisicion

class Window3:
    marca = ""
    documento = ""

    def __init__(self, parent):
        self.parent = parent
        self.create_form()

    def create_form(self):
        # Create the frame for the section
        form_frame = Frame(self.parent)
        form_frame.pack(pady=10)

        # Labels
        label_marca = Label(form_frame, text="Marca")
        label_documento = Label(form_frame, text="Documento")

        # Entry fields
        entry_marca = Entry(form_frame)
        entry_documento = Entry(form_frame)

        # Set the previously entered values
        entry_marca.insert(0, self.marca)
        entry_documento.insert(0, self.documento)

        # Save the values when the Submit button is clicked
        submit_button = Button(form_frame, text="Submit", command=lambda: self.save_values(entry_marca.get(), entry_documento.get()))

        # Grid layout
        label_marca.grid(row=0, column=0, sticky=W, padx=10, pady=5)
        label_documento.grid(row=1, column=0, sticky=W, padx=10, pady=5)
        entry_marca.grid(row=0, column=1, padx=10, pady=5)
        entry_documento.grid(row=1, column=1, padx=10, pady=5)
        submit_button.grid(row=2, column=1, pady=10)

    def save_values(self, marca, documento):
        self.marca = marca
        self.documento = documento


win = Tk()
win.title('Formulario Hoja de Vida')
win.geometry('720x900')

# Create a notebook widget to hold the different windows
notebook = ttk.Notebook(win)
notebook.pack(fill=BOTH, expand=True)

# Create the three frames for the windows
frame1 = Frame(notebook)
frame2 = Frame(notebook)
frame3 = Frame(notebook)

# Create the three windows and associate them with the frames
window1 = Window1(frame1)
window2 = Window2(frame2)
window3 = Window3(frame3)

# Add the frames as tabs to the notebook
notebook.add(frame1, text="Window 1")
notebook.add(frame2, text="Window 2")
notebook.add(frame3, text="Window 3")

win.mainloop()
