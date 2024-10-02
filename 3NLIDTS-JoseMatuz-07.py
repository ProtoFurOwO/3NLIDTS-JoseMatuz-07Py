# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 23:34:17 2024

@author: ProtofurOwO
"""

import tkinter as tk
import serial

port = 'COM3'
baudrate = 9600
ser = serial.Serial(port, baudrate)

def encender_led():
    ser.write(b'b')
    print("LED Encendido")
    
def apagar_led():
    ser.write(b'a')
    print("LED Apagado")
    
ventana = tk.Tk()
ventana.title("Control de LED")

btn_encender = tk.Button(ventana, text="Encender LED", command=encender_led)
btn_encender.pack(pady=10)
btn_apagar = tk.Button(ventana, text="Apagar LED", command=apagar_led)
btn_apagar.pack(pady=10)

ventana.mainloop()

ser.close()