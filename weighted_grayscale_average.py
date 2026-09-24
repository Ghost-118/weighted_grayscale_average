# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 15:28:36 2024

@author: jose ochoa
"""

import cv2 

imagenes = ["img1", "img2", "img3"]

wr = 0.299
wg = 0.587
wb = 0.114

for ruta in imagenes:
    img = cv2.imread(f"{ruta}.jpg")
    r = img[:,:,2]
    g = img[:,:,1]
    b = img[:,:,0]
   
    n_img = (wr*r + wg*g + wb*b)/3
    n_img = n_img.astype(int)
    
    cv2.imwrite(f"{ruta}_E9.jpg", n_img)     
    
    