from widget.card import card
import flet as ft  


  


def main(page: ft.Page):  
    def show_drawer(e):
        page.drawer.open = True
        page.drawer.update() 

    page.appbar = ft.AppBar(
        title=ft.Text("My App Example"), 
        center_title=True,
        toolbar_height=40,
        leading=ft.IconButton(icon=ft.icons.MENU,on_click=show_drawer) 
        )
    page.drawer = ft.NavigationDrawer(
        elevation=100

    )

    page.scroll = True  
    page.title = 'my test app'
    print(page.height)
    for i in range(1):   
        opject = card
        opject.width  = page.width
        opject.height = page.height
        opject.anime_name = 'test_pos adasda dsad asda das das d '
        opject.img_src = 'https://image.tmdb.org/t/p/w300/4EFI8IdI7LOm9Q0BTT2FAdPwdeq.jpg'
        opject.episode = '1'
        opject.last_update = '1 day' 
        page.add(opject(width=page.width,height=page.height))  
        if i//20 == 0 :
            page.update
     
   
ft.app(target=main,view= ft.WEB_BROWSER)
                         
                                                            