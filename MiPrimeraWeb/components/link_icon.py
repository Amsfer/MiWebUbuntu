import reflex as rx
import MiPrimeraWeb.styles.styles as styles

def link_icon(url: str)-> rx.Component:
    return rx.link(
        rx.icon(
            tag="moon"
        ),
        href=url,
        is_external= True,
    )