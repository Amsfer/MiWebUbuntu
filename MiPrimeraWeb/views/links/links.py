import reflex as rx
from MiPrimeraWeb.components.link_button import link_button
from MiPrimeraWeb.components.title import title
from MiPrimeraWeb.components.link_image import link_image

def links() -> rx.Component:
    return rx.vstack(
        title("COMICS MAS POPULARES:","5"),
        rx.hstack(
            link_image("https://www.google.com/","https://cdn.oldskull.net/wp-content/uploads/2014/03/infinite-crisis-superman.jpg"),
            link_image("https://www.google.com/","https://sm.ign.com/t/ign_es/screenshot/b/bthe-aveng/bthe-avengers-vol-1-223bbrbrbdrawn-byb-ed-hanniganbrbrthe-no_3rxt.1080.jpg"),
            link_image("https://www.google.com/","https://hablandodecomics.wordpress.com/wp-content/uploads/2013/01/uncanny-x-men-137.jpg"),
            link_image("https://www.google.com/","https://sm.ign.com/t/ign_es/screenshot/b/bsilver-su/bsilver-surfer-vol-1-4bbrbrbdrawn-byb-john-buscemabrbrwhen-i_uyby.1080.jpg"),
            link_image("https://www.google.com/","https://i0.wp.com/www.universomarvel.com/wp-content/uploads/2023/01/AM_SM_23_D100_VAR-scaled.jpg?ssl=1"),
            link_image("https://www.google.com/","https://cloudfront-eu-central-1.images.arcpublishing.com/prisa/KBXMELGIMFJFVDCBMKIWZ2RZZU.jpg"),
            spacing="4",
        ),
        rx.hstack(
            link_image("https://www.google.com/","https://cdn.oldskull.net/wp-content/uploads/2014/03/infinite-crisis-superman.jpg"),
            link_image("https://www.google.com/","https://sm.ign.com/t/ign_es/screenshot/b/bthe-aveng/bthe-avengers-vol-1-223bbrbrbdrawn-byb-ed-hanniganbrbrthe-no_3rxt.1080.jpg"),
            link_image("https://www.google.com/","https://hablandodecomics.wordpress.com/wp-content/uploads/2013/01/uncanny-x-men-137.jpg"),
            link_image("https://www.google.com/","https://sm.ign.com/t/ign_es/screenshot/b/bsilver-su/bsilver-surfer-vol-1-4bbrbrbdrawn-byb-john-buscemabrbrwhen-i_uyby.1080.jpg"),
            link_image("https://www.google.com/","https://i0.wp.com/www.universomarvel.com/wp-content/uploads/2023/01/AM_SM_23_D100_VAR-scaled.jpg?ssl=1"),
            link_image("https://www.google.com/","https://cloudfront-eu-central-1.images.arcpublishing.com/prisa/KBXMELGIMFJFVDCBMKIWZ2RZZU.jpg"),
            spacing="4",
        ),
        rx.hstack(
            link_image("https://www.google.com/","https://cdn.oldskull.net/wp-content/uploads/2014/03/infinite-crisis-superman.jpg"),
            link_image("https://www.google.com/","https://sm.ign.com/t/ign_es/screenshot/b/bthe-aveng/bthe-avengers-vol-1-223bbrbrbdrawn-byb-ed-hanniganbrbrthe-no_3rxt.1080.jpg"),
            link_image("https://www.google.com/","https://hablandodecomics.wordpress.com/wp-content/uploads/2013/01/uncanny-x-men-137.jpg"),
            link_image("https://www.google.com/","https://sm.ign.com/t/ign_es/screenshot/b/bsilver-su/bsilver-surfer-vol-1-4bbrbrbdrawn-byb-john-buscemabrbrwhen-i_uyby.1080.jpg"),
            link_image("https://www.google.com/","https://i0.wp.com/www.universomarvel.com/wp-content/uploads/2023/01/AM_SM_23_D100_VAR-scaled.jpg?ssl=1"),
            link_image("https://www.google.com/","https://cloudfront-eu-central-1.images.arcpublishing.com/prisa/KBXMELGIMFJFVDCBMKIWZ2RZZU.jpg"),
            spacing="4",
        ),
        rx.hstack(
            link_image("https://www.google.com/","https://cdn.oldskull.net/wp-content/uploads/2014/03/infinite-crisis-superman.jpg"),
            link_image("https://www.google.com/","https://sm.ign.com/t/ign_es/screenshot/b/bthe-aveng/bthe-avengers-vol-1-223bbrbrbdrawn-byb-ed-hanniganbrbrthe-no_3rxt.1080.jpg"),
            link_image("https://www.google.com/","https://hablandodecomics.wordpress.com/wp-content/uploads/2013/01/uncanny-x-men-137.jpg"),
            link_image("https://www.google.com/","https://sm.ign.com/t/ign_es/screenshot/b/bsilver-su/bsilver-surfer-vol-1-4bbrbrbdrawn-byb-john-buscemabrbrwhen-i_uyby.1080.jpg"),
            link_image("https://www.google.com/","https://i0.wp.com/www.universomarvel.com/wp-content/uploads/2023/01/AM_SM_23_D100_VAR-scaled.jpg?ssl=1"),
            link_image("https://www.google.com/","https://cloudfront-eu-central-1.images.arcpublishing.com/prisa/KBXMELGIMFJFVDCBMKIWZ2RZZU.jpg"),
            spacing="4",
        ),        
        rx.vstack(
            title("CATEGORIAS DE COMICS:","5"),
            rx.center(
                rx.vstack(
                    rx.hstack(
                        link_button(
                            "Superhéroes",
                            "https://www.google.com/",
                            "https://qph.cf2.quoracdn.net/main-qimg-5a067b31835f902a9afee336ecef783d-pjlq"
                        ),
                        link_button(
                            "Ciencia Ficción",
                            "https://www.google.com/",
                            "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyiwuw5YK9QLbanmXh40T3LLSLS6-dM_Zeq_LC38HCDV7ipCxXfb5BeghEP4heDYQsasiJbEPpSqvUJ_NVYkTa-PiuL8x6J_TdAI6BM6raDpAblu2By31Odr7EZ78Q9eoYHLE1k6Xr5rA/s1600/comics-de-ciencia-ficcion.jpg"
                        ),
                        link_button(
                            "Humor",
                            "https://www.google.com/",
                            "https://rialta.org/wp-content/uploads/2019/11/Portada-definitiva-para-publicar.jpg"
                        ),
                        width="100%",
                    ),
                    rx.hstack(                        
                        link_button(
                            "Aventuras",
                            "https://www.google.com/",
                            "https://texlibris.lib.utexas.edu/wp-content/uploads/2019/11/backdrop-912x576.jpg"
                        ),
                        link_button(
                            "Fantasia",
                            "https://www.google.com/",
                            "https://i.etsystatic.com/7705291/r/il/3bb416/484833926/il_1080xN.484833926_57na.jpg"
                        ),
                        link_button(
                            "Historia",
                            "https://www.google.com/",
                            "https://www.zonanegativa.com/imagenes/2020/07/Revistas-de-c%C3%B3mics-de-los-80ZN.jpg"
                        ),
                        width="100%",
                    ),
                    width="100%",
                ),
                
                border_radius="15px",
                border_width="thick",
                width="100%",
            ),
            align="center",
            
        ),
        align="center",
            
    )