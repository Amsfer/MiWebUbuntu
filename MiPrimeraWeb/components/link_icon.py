import reflex as rx
import MiPrimeraWeb.styles.styles as styles

def link_icon(icon: str,color: str ,url: str)-> rx.Component:
    return rx.link(
        rx.icon(
            tag=icon,
            color=color,
        ),
        href=url,
        is_external= True,
    )