from widget.card import card
import flet as ft  


  


def main(page: ft.Page):  
    page.appbar = ft.AppBar(
        title=ft.Text("My App Example"), 
        center_title=True,
        toolbar_height=40)  
    page.scroll = True  
    page.title = 'my test app'
    print(page.height)
    for i in range(6):  
        opject = card
        
        opject.width  = page.width
        opject.height = page.height
        
        opject.anime_name = 'test_pos adasda dsad asda das das d '
        opject.img_src = 'https://image.tmdb.org/t/p/w300/4EFI8IdI7LOm9Q0BTT2FAdPwdeq.jpg'
        opject.episode = '1'
        opject.last_update = '1 day' 
        page.add(opject(width=page.width,height=page.height))  
        
     
   
ft.app(target=main)
                         
                                                            