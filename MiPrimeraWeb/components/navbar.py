import reflex as rx
from MiPrimeraWeb.styles.styles import Size as Size
from MiPrimeraWeb.components.dropdown import dropdown

def navbar() -> rx.Component:
    return rx.hstack(
        rx.image(
            src="/leectorOnline.ico",
            width="35px",
            height="auto",
            border_radius="50px",
            border="2px solid #555",
        ),
        rx.text("Leector Online"),
        rx.spacer(),
        rx.hstack(            
            rx.spacer(),#espacio para alinear text y/o modificaciones unicas
            rx.center(
                rx.input(
                rx.input.slot(
                    rx.icon(tag="search"),
                    ),
                placeholder="Busca aquí...",            
                ),         
                
            ),        
            rx.spacer(),
            rx.icon("eye"),
            rx.switch("Switched", name="switch",style={"cursor": "pointer"}),
            rx.spacer(),
            dropdown(
                "Fernandez",
                menu_items = [
                    ("Perfil", {"shortcut": "#item1"}),
                    ("Ajustes", {"shortcut": "#item2","href": "#item2"}),
                    "separator",                
                    ("Salir", {"shortcut": "#item3","color": "red"}),
                ]
            ),            
            align="center",
        ),
        position="sticky",
        bg="teal",
        padding_x=Size.DEFAULT.value,#espacio en el texto x
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",#mantener la el nabvar constante en vista sin perderse
        align="center",
    )