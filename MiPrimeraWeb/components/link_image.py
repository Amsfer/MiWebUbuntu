import reflex as rx
import MiPrimeraWeb.styles.styles as styles

def link_image(url: str,image: str)-> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width="150px",
            height="auto",
        ),
        href=url,
        is_external= True,
    )