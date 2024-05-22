import reflex as rx
from MiPrimeraWeb.components.link_icon import link_icon

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="JW",
                  color_scheme="orange",
                  variant="solid",
                  size="5"),
            rx.text("Willimasfer1998@gmail.com",size="2"),
            rx.vstack(
                rx.heading("Williams Fernandez",size="3"),
                rx.text("Ing.Sistemas"),
            ),
            rx.vstack(
                link_icon("http://www.google.com"),
                link_icon("http://www.google.com"),
            ),
        ),
        rx.text("""Este es un Blog que vende Peliculas y/o Series"""),
        align="center",
        
    )