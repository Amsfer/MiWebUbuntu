from enum import Enum
import reflex as rx

#constantes
MAX_WIDTH="600px"

#tamaños
class Size(Enum):
    SMALL="0.5em"    
    DEFAULT="1em" 
    MEDIUM="1.3em"   
    BIG="2em"
    
BASE_STYLES ={
    rx.button:{
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value
    },
    rx.link:{
        "text_decoration": "none"
    },
}

Button_title_styles = dict(
    font_size = Size.MEDIUM.value
)

Button_body_style = dict(
    font_size = Size.DEFAULT.value
)

title_style= dict(
    #sizeStyle="2",
    width="100%",
    padding_top=Size.DEFAULT.value
)