import numpy as np
import streamlit as st
import PIL
from PIL import Image
import qrcode

st.title("QR code Genator")
st.text("Content provide by user is directly encode in the image to generate QR-Code. Make sure everything you enter is correct because you can’t change the content once your QR code is printed.")

text = st.text_input('Enter the Text')


click = st.button("Generate")


if click:

    # st.write(text)

    img = qrcode.make(text)
    image = img.save("QR.png")
    output = Image.open("QR.png")
    st.image(output)
