import os
import random
import tempfile

import streamlit as st
from PIL import Image, ImageDraw, ImageFont

from giger.services.image import ImageService
from giger.services.prompt import PromptService

COLORS = [
    "red",
    "orange",
    "yellow",
    "chartreuse green",
    "green",
    "spring green",
    "cyan",
    "azure",
    "blue",
    "violet",
    "magenta",
    "rose",
]

WIDTH = 768
HEIGHT = 432


def controlnet_image():
    img = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)
    ttf = ImageFont.truetype(
        os.path.join(
            os.path.dirname(__file__),
            "fonts",
            "{0}.ttf".format(font.replace(" ", "")),
        ),
        300,
    )
    draw.text((WIDTH / 2, HEIGHT / 2), tag, font=ttf, fill="black", anchor="mm")
    return img


def prompt():
    text = ["Graffiti on"]

    if background == "Wall":
        text.append("a wall,")
    elif background == "Train":
        text.append("a train,")
    elif background == "Blackbook":
        text.append("black background,")

    text.append("in the colors")
    text.append(color1)
    text.append("and")
    text.append(color2)

    if artist != "None":
        text[-1] = "{0},".format(text[-1])
        text.append("by {0}".format(artist))

    return PromptService().generate(
        " ".join(text),
        rendering_engine="Octane Render",
        lightning_style="Cinematic",
        resolution="8k",
        compel_style="subtle",
    )


def render():
    with st.spinner(text="Rendering"):
        tmp_dir = tempfile.gettempdir()
        seed = random.randint(0, 1000000)
        tag_path = os.path.join(tmp_dir, "tag-{0}.png".format(str(seed)))
        controlnet_image().save(tag_path)

        ImageService().controlnet(
            "Lykon/DreamShaper",
            prompt(),
            "",
            tmp_dir,
            WIDTH,
            HEIGHT,
            "artificialhoney/graffiti",
            0.75,
            0,
            1,
            tag_path,
            loras=[
                {
                    "model": "OedoSoldier/detail-tweaker-lora",
                    "filename": "add_detail.safetensors",
                    "scale": 0.75,
                }
            ],
            seed=seed,
            count=1,
            steps=30,
            name="controlnet",
        )
        st.image(
            os.path.join(tmp_dir, "controlnet-000-" + str(seed).rjust(6, "0") + ".png")
        )


st.header("Graffiti")

col1, col2, col3, col4, col5, col6 = st.columns(6)

tag = col1.text_input("Tag", max_chars=5, value="PARIS")

color1 = col2.selectbox("Color 1", COLORS, index=1)
color2 = col3.selectbox("Color 2", COLORS, index=9)

background = col4.selectbox("Background", ["Blackbook", "Wall", "Train"])
artist = col5.selectbox(
    "Artist",
    [
        "None",
        "Banksy",
        "David Choe",
        "Eduardo Kobra",
        "Blek le Rat",
        "Os Gemeos",
        "Vhils",
        "Lady Pink",
        "Seen UA",
        "Blu",
        "Lee Quiñones",
    ],
)
font = col6.selectbox(
    "Font",
    [
        "Another Tag",
        "Marsneveneksk",
        "Most Wasted",
    ],
)

trigger = st.button("Render", on_click=render, use_container_width=True)
