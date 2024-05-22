import reflex as rx
from MiPrimeraWeb.components.navbar import navbar
from MiPrimeraWeb.views.header.header import header
from MiPrimeraWeb.views.links.links import links
from MiPrimeraWeb.components.footer import footer
import MiPrimeraWeb.styles.styles as styles


class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            header(),
            rx.hstack(
                rx.vstack(
                    rx.text("--------------Propagandas---------------"),
                    width="150px"
                ),
                rx.vstack(           
                    links(),
                    #max_width=styles.MAX_WIDTH,
                    width="100%", #redimencionamiento
                    margin_y=styles.Size.DEFAULT.value,
                    align="center",
                ),
                rx.vstack(
                    rx.text("----------------Propagandas------------"),
                    width="150px"
                ),
            ),            
            margin=styles.Size.DEFAULT.value,
            align="center",
        ),
        rx.vstack(
            footer(),
            align="center",
        ),       
    )

app = rx.App(
    style=styles.BASE_STYLES
)
app.add_page(index)