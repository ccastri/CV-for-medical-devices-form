from tkinter import *
from tkinter import filedialog
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib import colors

class TablePage:
    def __init__(self, win, title, table_data):
        self.win = win
        self.title = title
        self.table_data = table_data
        
        # Create the frame for the table
        self.table_frame = Frame(self.win)
        self.table_frame.pack(pady=10)

        # Create the table
        self.create_table()

    def create_table(self):
        # Create title label
        title_label = Label(self.table_frame, text=self.title, padx=10, pady=5)
        title_label.grid(row=0, columnspan=2, sticky=NSEW)

        # Create table headers and rows
        for row, data in enumerate(self.table_data):
            label = Label(self.table_frame, text=data[0], padx=10, pady=5)
            label.grid(row=row+1, column=0, sticky=NSEW)

            entry = Entry(self.table_frame, relief=RIDGE)
            entry.insert(END, data[1])
            entry.grid(row=row+1, column=1, sticky=NSEW, ipadx=10, ipady=5)

    def get_table_data(self):
        headers = [data[0] for data in self.table_data]
        data = [entry.get() for entry in self.table_frame.winfo_children() if isinstance(entry, Entry)]
        return headers, data

# Create the main window
win = Tk()
win.title('Table Example')

# Create a list to store table pages
table_pages = []

# Function to save all tables as a single PDF
def save_as_pdf():
    save_file_path = filedialog.asksaveasfilename(defaultextension=".pdf")
    if save_file_path:
        doc = SimpleDocTemplate(save_file_path, pagesize=letter)

        # Define table style
        table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.blue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])

        # Build table elements for all tables
        elements = []
        for i, table_page in enumerate(table_pages):
            # Add spacer between tables
            if i > 0:
                elements.append(Spacer(1, 30))  # Adjust the spacing as needed

            headers, data = table_page.get_table_data()
            table_data = [headers] + [data]
            table_data.insert(0, [table_page.title])
            table = Table(table_data, style=table_style)
            elements.append(table)

        # Build PDF document
        doc.build(elements)

# Create TablePages and add them to the table_pages list
table_pages.append(TablePage(win, "Table 1", [["Header 1", ""], ["Header 2", ""], ["Header 3", ""]]))
table_pages.append(TablePage(win, "Table 2", [["Header A", ""], ["Header B", ""], ["Header C", ""]]))
# Add more TablePage instances for additional tables

# Create a button for saving all tables as PDF
save_pdf_button = Button(win, text="Save as PDF", command=save_as_pdf)
save_pdf_button.pack(pady=10)

win.mainloop()
