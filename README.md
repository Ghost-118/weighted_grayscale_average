# 🖼️ Weighted Grayscale Average in Python

Este repositorio contiene una implementación en **Python** para convertir imágenes a escala de grises mediante la aplicación de pesos de luminancia sobre los canales de color (BGR) utilizando **OpenCV**.

El algoritmo extrae individualmente los canales Rojo ($R$), Verde ($G$) y Azul ($B$), aplica una ponderación personalizada ($w_r = 0.299$, $w_g = 0.587$, $w_b = 0.114$) y guarda las imágenes resultantes en formato entero.

---

## 🚀 Características

- 🎨 **Ponderación de Luminancia:** Aplica coeficientes específicos para cada canal de color:
  $$\text{Gris} = \frac{0.299 \cdot R + 0.587 \cdot G + 0.114 \cdot B}{3}$$
- 🔄 **Procesamiento por Lote:** Procesa iterativamente múltiples imágenes (`img1.jpg`, `img2.jpg`, `img3.jpg`).
- 💾 **Exportación:** Guarda cada imagen procesada agregando el sufijo `_E9.jpg`.

---

## 🛠️ Requisitos e Instalación

### Requisitos previos
- **Python 3.x**
- **OpenCV (`opencv-python`)**

### Instalación

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/Ghost-118/weighted_grayscale_average.git](https://github.com/Ghost-118/weighted_grayscale_average.git)
   cd weighted_grayscale_average
