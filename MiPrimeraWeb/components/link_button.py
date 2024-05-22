import reflex as rx
import MiPrimeraWeb.styles.styles as styles

def link_button(title: str,url: str, image: str) -> rx.Component:
    return rx.link(
        rx.button(                  
            rx.hstack(
                rx.icon(
                    tag="library-big",
                    width=styles.Size.BIG.value,
                    heigth=styles.Size.DEFAULT.value
                ),
                rx.text(
                    title,
                    style=styles.Button_title_styles
                ),
                
            ),
            rx.vstack(                
                rx.image(
                    image,
                    width="250px",
                    height="150px",                                
                ),
                align="center"                
            ),            
            style={"cursor": "pointer"},                  
        ),
        href=url,
        is_external= True,
        width="100%",
    )
