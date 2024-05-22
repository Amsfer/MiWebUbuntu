import reflex as rx
from MiPrimeraWeb.components.link_icon import link_icon

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="JW",
                  color_scheme="orange",
                  variant="solid",
                  size="5"),
            rx.text("Willimasfer1998@gmail.com",size="1"),
            rx.vstack(
                rx.heading("Williams Fernandez",size="2"),
                rx.text("Ing.Sistemas"),
            ),
            rx.hstack(
                rx.vstack(
                    link_icon("instagram","#EF8840","https://www.instagram.com"),
                    link_icon("facebook","blue","http://www.facebook.com"),                    
                ),
                rx.vstack(                    
                    link_icon("twitter","linghtblue","http://www.twitter.com"),
                    link_icon("twitch","indigo","http://www.twitch.com"),
                ),
            ),
            
        ),
        rx.text("""En Leector Online, 
                puedes leer tus comics favoritos en línea, 
                sin necesidad de descargarlos ni preocuparte por la espacio en tu dispositivo. 
                Nuestra biblioteca de comics incluye una variedad de géneros y estilos, 
                desde superhéroes y ciencia ficción hasta humor y aventuras. 
                ¡Explora nuestros títulos y descubre nuevos autores y series!"""),
        align="center",
        
    )