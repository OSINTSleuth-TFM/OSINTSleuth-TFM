import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from subprocess import Popen, PIPE

# Definir un diccionario con los nombres de los scripts y sus rutas
scripts = {
    "Generador de Alias": "./Scripts/alias_generator.sh",
    "Fierce": "./Scripts/fierce.sh",
    "Holehe": "./Scripts/holehe.sh",
    "Maryam": "./Scripts/maryam.sh",
    "Pagodo": "./Scripts/pagodo.sh",
    "Maltego": "./Scripts/maltego.sh",
    "Sherlock": "./Scripts/sherlock.sh",
    "Git Recon": "./Scripts/gitrecon.sh",
    "ProtOSINT": "./Scripts/ProtOSINT.sh",
    "DNSenum": "./Scripts/dnsenum.sh",
    "Spiderfoot": "./Scripts/Spiderfoot.sh",
    "Exiftool": "./Scripts/exiftool.sh",
    "Mediainfo": "./Scripts/mediainfo.sh",
    "Reconftw": "./Scripts/reconftw.sh",
    "Infoga": "./Scripts/Infoga.sh",
    "OSINTool": "./Scripts/OSINTool.sh",
    "Recon-ng": "./Scripts/recon-ng.sh"
}

def ejecutar_script(nombre_script):
    ruta_script = scripts.get(nombre_script, None)
    if ruta_script is None:
        messagebox.showerror("Error", "El script seleccionado no tiene una ruta válida.")
        return

    # Ejecutar el script seleccionado en una nueva ventana de terminal
    proceso = Popen(["./{}".format(ruta_script)], stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = proceso.communicate()
    if proceso.returncode == 0:
        messagebox.showinfo("Éxito", f"Script {nombre_script} ejecutado correctamente.")
    else:
        messagebox.showerror("Error", f"Hubo un error al ejecutar el script {nombre_script}. Error: {stderr.decode()}")

def al_seleccionar_script(event):
    script_seleccionado = combobox_scripts.get()
    ejecutar_script(script_seleccionado)

# Crear la interfaz gráfica
ventana_principal = tk.Tk()
ventana_principal.title("Ejecutar Scripts")
ventana_principal.geometry("600x400")  # Cambiar el tamaño de la ventana principal a 600x400
ventana_principal.configure(bg='black')  # Cambiar el color de fondo a negro

# Crear una etiqueta
etiqueta = ttk.Label(ventana_principal, text="Selecciona un script para ejecutar:", foreground='green', background='black', font=('Arial', 12))
etiqueta.pack(pady=20)  # Ajustar el espacio vertical alrededor de la etiqueta

# Crear el desplegable (combobox) para seleccionar el script
combobox_scripts = ttk.Combobox(ventana_principal, values=list(scripts.keys()))
combobox_scripts.pack(pady=10)  # Ajustar el espacio vertical alrededor del combobox
combobox_scripts.bind("<<ComboboxSelected>>", al_seleccionar_script)

# Cambiar los colores del desplegable (combobox)
estilo = ttk.Style()
estilo.configure('TCombobox', foreground='green', background='black')

# Ejecutar el estilo personalizado para toda la aplicación
ventana_principal.estilo = estilo

# Manejador de eventos para el cierre de la ventana principal
def al_cerrar():
    if messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?"):
        ventana_principal.destroy()

ventana_principal.protocol("WM_DELETE_WINDOW", al_cerrar)

ventana_principal.mainloop()

