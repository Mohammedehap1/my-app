import flet as ft
class card(ft.Card):
    img_src = ''
    episode = ''
    anime_name =''
    last_update  ='' 
    card_height = 0
    card_width = 0
    
    def __init__(self,width,height,*args): 
        super().__init__(*args) 
        self.height = height
        self.width = width
        self.card_height = self.height/6 
        self.card_width = self.width
        
        self.image = ft.Image(  
            src=self.img_src, 
            left= True,
            width=self.card_width/4,
            height= self.card_height,
            fit=ft.ImageFit.COVER,
            border_radius=ft.border_radius.all(10),
                            ) 
        
        
        self.content = ft.Container(

height= self.card_height,
width= self.card_width,
border_radius = 10,
content=ft.Row([
    self.image,
    ft.Column(
        spacing=40,   
        controls=[
        ft.Container(
            
            width=(self.card_width - self.card_width/4) - 38.5,
            height=self.card_height/3,
            border_radius = 10,
            content=ft.Text(value=self.anime_name,size= 18,max_lines=1), 
            alignment= ft.alignment.center_left),
        ft.Row([
            ft.Container(
                bgcolor=ft.colors.YELLOW_700,
                width=self.card_width /5,
                height=self.card_height/3, 
                border_radius = 20, 
                content=ft.Text(value=self.episode,size= 18), 
                alignment= ft.alignment.center),
            ft.Container(
                
                width=self.card_width /2.501, 
                height=self.card_height/3, 
                 
                content=ft.Text(value=self.last_update,size= 18), 
                alignment= ft.alignment.bottom_right),
                ])
            ]),
    

                ])
                                    )

      
 
        