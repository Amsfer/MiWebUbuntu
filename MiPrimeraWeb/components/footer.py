import reflex as rx
import datetime
import MiPrimeraWeb.styles.styles as styles
from MiPrimeraWeb.components.link_icon import link_icon

def footer() -> rx.Component:
    return rx.vstack(
        rx.spacer("5"),
        rx.hstack(
            rx.image(
                src="/leectorOnline.ico",
                width="35px",
                height="auto",
                border_radius="35px 35px",
                border="1px solid #555",
            ),
            rx.link(
                f"Este es un Proyecto con Derechos reservados-{datetime.date.today().year}",
                href="https://www.google.com/",
                is_external=True
            ),
            rx.text(" - copyrigth Williams Fernandez"),
            align="center",            
        ),
        rx.hstack(
            link_icon("instagram","#EF8840","https://www.instagram.com"),
            link_icon("facebook","blue","http://www.facebook.com"),
            link_icon("twitter","linghtblue","http://www.twitter.com"),
            link_icon("twitch","indigo","http://www.twitch.com"),
            align="center",
            
        ),
        rx.spacer("5"),
        margin=styles.Size.DEFAULT.value,
        bg="#C6BAB3",
        width="100%",
        align="center",        
    )
