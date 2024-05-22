import reflex as rx
import MiPrimeraWeb.styles.styles as styles

def link_button(texto: str,body: str,url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="calendar",
                    width=styles.Size.BIG.value,
                    heigth=styles.Size.DEFAULT.value
                ),
                
            ),
            rx.vstack(
                rx.text(
                    texto,
                    style=styles.Button_title_styles
                ),
                rx.text(
                    body,
                    style=styles.Button_body_style
                ),
            ),
        ),
        href=url,
        is_external= True,
        width="100%",
    )