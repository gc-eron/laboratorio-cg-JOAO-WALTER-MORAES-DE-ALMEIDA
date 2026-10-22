import numpy as np
import streamlit as st

def ampliar(imagem, k=30):
 return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Bandeira da França")

bandeira = np.zeros((12, 18, 3), dtype=np.uint8)
bandeira[:, :6] = (0, 35, 149)
bandeira[:, 6:12] = (255, 255, 255)
bandeira[:, 12:] = (237, 41, 57)

st.image(ampliar(bandeira))