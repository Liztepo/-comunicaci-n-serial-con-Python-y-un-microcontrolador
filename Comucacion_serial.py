import tkinter as tk
from tkinter import ttk
import serial

baudrates = [9600, 115200] # Listado de posibles baudrates

def conectar_puerto():
    global ser
    puerto = 'COM1' # Puerto serie a conectar
    baudrate = baundrate_combobox.get()
    ser = serial.Serial(port=puerto, baudrate=baudrate, timeout=1)
    conectar_button['state'] = 'disabled'
    desconectar_button['state'] = 'normal'

def desconectar_puerto():
    ser.close()
    conectar_button['state'] = 'normal'
    desconectar_button['state'] = 'disabled'

def leer_datos():
    opcion = operacion_combobox.get()
    if opcion == 'Leer el adc':
        ser.write(b'1') # Envía el comando para leer el ADC al microcontrolador
        # Leer y procesar la respuesta del microcontrolador
        data = ser.readline().decode().strip()
        # Mostrar el dato en la interfaz
        print(data)
    elif opcion == 'Establecer PWM':
        porcentaje_pwm = int(pwm_entry.get())
        # Enviar el porcentaje de PWM al microcontrolador
        ser.write(str(porcentaje_pwm).encode())

# Crear la ventana principal
root = tk.Tk()
root.title("Comunicación con microcontrolador")

# Combobox para seleccionar la operación
operacion_label = ttk.Label(root, text="Seleccione una operación:")
operacion_label.pack()
operaciones = ['Leer el adc', 'Establecer PWM', 'Activar relevador', 'Mover motor', 'Recibir saludo']
operacion_combobox = ttk.Combobox(root, values=operaciones)
operacion_combobox.pack()


# Botones para conectar y desconectar el puerto serie
conectar_button = ttk.Button(root, text="Conectar puerto", command=conectar_puerto)
conectar_button.pack()
desconectar_button = ttk.Button(root, text="Desconectar puerto", command=desconectar_puerto, state='disabled')
desconectar_button.pack()

# Combobox para seleccionar el baudrate
baundrate_label = ttk.Label(root, text="Seleccione el baudrate:")
baundrate_label.pack()
baundrate_combobox = ttk.Combobox(root, values=baudrates)
baundrate_combobox.pack()

# Entry para ingresar el porcentaje de PWM
pwm_label = ttk.Label(root, text="Ingrese el porcentaje de PWM:")
pwm_label.pack()
pwm_entry = ttk.Entry(root)
pwm_entry.pack()

# Botón para enviar el comando al microcontrolador
enviar_button = ttk.Button(root, text="Enviar comando", command=leer_datos)
enviar_button.pack()

root.mainloop()