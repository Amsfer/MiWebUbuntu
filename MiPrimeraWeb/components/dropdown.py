import reflex as rx

def dropdown(name: str, menu_items: list[tuple[str, dict]]) -> rx.Component:
       
    # Crear una lista de componentes rx.menu.item() para cada elemento en menu_items
    menu_items_components = []
    for item in menu_items:
        if isinstance(item, tuple):
            menu_items_components.append(rx.menu.item(item[0], **item[1]))
        elif item == "separator":
            menu_items_components.append(rx.menu.separator())

    return rx.flex(
        rx.menu.root(            
            rx.menu.trigger(                
                rx.hstack(
                    rx.image(
                        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSimsqX76hrhRfgKm77u7KxlRChxZiuJoYyojuOici27w&s",
                        width="40px",
                        height="auto",
                        border_radius="20px 60px",
                        border="1px solid #555",
                    ),
                    rx.text(name),
                    rx.icon("arrow-big-down-dash"),
                    align="center",
                ),
                style={"cursor": "pointer"},                
            ),
            rx.menu.content(
                *menu_items_components  # Usar * para desempaquetar la lista de componentes de items
            ),
        ),
    )
