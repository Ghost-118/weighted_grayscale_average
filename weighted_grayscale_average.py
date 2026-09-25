# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 15:28:36 2024

@author: jose ochoa
"""

import cv2 

# Lista de archivos a procesar
imagenes = ["img1", "img2", "img3"]

# Pesos de luminancia para conversión a escala de grises
wr = 0.299
wg = 0.587
wb = 0.114

for ruta in imagenes:
    img = cv2.imread(f"{ruta}.jpg")
    
    # Separación de canales de color (OpenCV usa BGR)
    r = img[:,:,2]
    g = img[:,:,1]
    b = img[:,:,0]
   
    # Promedio ponderado y conversión a enteros
    n_img = (wr*r + wg*g + wb*b)/3
    n_img = n_img.astype(int)
    
    # Guardar imagen generada
    cv2.imwrite(f"{ruta}_E9.jpg", n_img)
