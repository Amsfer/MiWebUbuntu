import reflex as rx
import MiPrimeraWeb.styles.styles as styles

def title(text:str, title_size:str)-> rx.Component:
    return rx.heading(
        text,
        size=title_size,
        style=styles.title_style
    )