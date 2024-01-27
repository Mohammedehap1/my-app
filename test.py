from flet import *
from widget.card import card
def main(page :Page):
    page.add(card())
app(target=main,view=WEB_BROWSER)
