import reflex as rx
import datetime
import MiPrimeraWeb.styles.styles as styles

def footer() -> rx.Component:
    return rx.hstack(
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
        is_external=True),
        rx.text(" - copyrigth Williams Fernandez"),
        align="center",
        margin=styles.Size.BIG.value,
    )
