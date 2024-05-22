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
                        src="https://lh3.googleusercontent.com/a/ACg8ocI_paO-FEM-CnlP-Z0O9pPb9KXiZTQ3uh93Ghi73I4FU1oOZXk=s288-c-no",
                        width="35px",
                        height="auto",
                        border_radius="20px 60px",
                        border="2px solid #555",
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
