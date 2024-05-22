import reflex as rx
from MiPrimeraWeb.components.link_button import link_button
from MiPrimeraWeb.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("CONTENIDO DE PELICULAS :","5"),
        link_button("Accion","contenido","https://www.google.com/"),
        link_button("Comedia","contenido","https://www.google.com/"),
        link_button("Terror","contenido","https://www.google.com/"),
        title("CONTENIDO DE SERIES :","5"),
        link_button("Hora de Aventura","contenido","https://www.google.com/"),
        link_button("Los Caballeros del Zodiaco","contenido","https://www.google.com/"),
        link_button("Casa de Papel","contenido","https://www.google.com/"),
    )