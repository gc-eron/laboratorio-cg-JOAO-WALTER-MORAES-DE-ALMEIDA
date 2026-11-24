import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

foto = Image.open("imagens/foto.jpg")
img = np.array(foto)

# 1. Saturação
st.header("1. Saturação")

valor_sat = st.slider("Saturação", 0, 200, 100)

hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
sat = hsv.copy()

sat[:, :, 1] = np.clip(
    hsv[:, :, 1].astype(np.float32) * valor_sat / 100,
    0,
    255
).astype(np.uint8)

img_sat = cv2.cvtColor(sat, cv2.COLOR_HSV2RGB)

st.image(img_sat)

# 2. Brilho
st.header("2. Brilho")

valor_brilho = st.slider("Brilho", 0, 200, 100)

hsv2 = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
brilho = hsv2.copy()

brilho[:, :, 2] = np.clip(
    hsv2[:, :, 2].astype(np.float32) * valor_brilho / 100,
    0,
    255
).astype(np.uint8)

img_brilho = cv2.cvtColor(brilho, cv2.COLOR_HSV2RGB)

st.image(img_brilho)

# 8. Negativo
st.header("8. Negativo")

negativo = 255 - img

st.image(negativo)

# 11. Espelhamento
st.header("11. Espelhamento")

esp_h = np.fliplr(img)
esp_v = np.flipud(img)

col1, col2 = st.columns(2)

with col1:
    st.image(esp_h, caption="Horizontal")

with col2:
    st.image(esp_v, caption="Vertical")

# 19. Moldura
st.header("19. Moldura")

espessura = st.slider("Espessura", 1, 100, 20)

r = st.slider("R", 0, 255, 255)
g = st.slider("G", 0, 255, 0)
b = st.slider("B", 0, 255, 0)

moldura = img.copy()

moldura[:espessura, :] = [r, g, b]
moldura[-espessura:, :] = [r, g, b]
moldura[:, :espessura] = [r, g, b]
moldura[:, -espessura:] = [r, g, b]

st.image(moldura)
