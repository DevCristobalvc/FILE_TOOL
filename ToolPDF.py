import PyPDF2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tkinter as tk
from tkinter import filedialog
import os

def combine_pdfs_and_convert_images():
    # Abre el diálogo de selección de archivos PDF y JPG
    filetypes = [("Archivos PDF", "*.pdf"), ("Imágenes JPG", "*.jpg")]
    files = filedialog.askopenfilenames(filetypes=filetypes)

    if files:
        pdf_files = [file for file in files if file.lower().endswith('.pdf')]
        jpg_files = [file for file in files if file.lower().endswith('.jpg')]

        # Crea un objeto PdfMerger
        pdf_merger = PyPDF2.PdfMerger()

        # Combina los archivos PDF seleccionados en uno solo
        for pdf_file in pdf_files:
            pdf_merger.append(pdf_file)

        # Abre el cuadro de diálogo para seleccionar la ubicación y nombre del archivo de salida
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")])

        # Verifica si se seleccionó una ubicación de salida
        if output_file:
            if jpg_files:
                # Combina las imágenes JPG en el PDF de salida
                c = canvas.Canvas(output_file, pagesize=letter)
                for jpg_file in jpg_files:
                    c.drawImage(jpg_file, 100, 100, width=400, height=400)
                    c.showPage()
                c.save()
            else:
                # Guarda el archivo PDF combinado en la ubicación de salida
                with open(output_file, 'wb') as output_pdf:
                    pdf_merger.write(output_pdf)

            print(f'Archivos PDF y JPG combinados exitosamente en {output_file}')
        else:
            print('No se seleccionó una ubicación de salida.')
    else:
        print('No se seleccionaron archivos PDF ni imágenes JPG.')

# Configura la ventana de la interfaz gráfica
root = tk.Tk()
root.title("Combinar PDFs y Convertir Imágenes a PDF")
root.geometry("350x150")

# Botón para iniciar la combinación de archivos PDF y conversión de imágenes
combine_button = tk.Button(root, text="Combinar PDFs y Convertir Imágenes", command=combine_pdfs_and_convert_images)
combine_button.pack()

# Ejecuta la interfaz gráfica
root.mainloop()
