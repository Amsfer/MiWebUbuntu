import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="/favicon.ico"),
        rx.link(
            f"Este es un Proyecto con Derechos reservados-{datetime.date.today().year}",
        href="https://www.google.com/",
        is_external=True),
        rx.text(" - copyrigth Williams Fernandez"),
        
    )
