import flet as ft
from pytube import YouTube
import os
def main(page: ft.Page):
    
    def close_infoBanner(e):
        page.banner.open = False
        page.update()
    def DownbtnFunc(e):
        if inputArea.value:
            paraApasta = os.getcwd()+os.sep+'Downloads'
            ytObj = YouTube(inputArea.value)
            ytObj = ytObj.streams.get_highest_resolution()
            try:
                ytObj.download(output_path=paraApasta)
                res.value = 'Download Concluido'
                page.update()
            except:
                res.value = 'houve um erro'
                page.update()


    


    text1 = ft.Text('Coloque o link aqui')
    inputArea = ft.TextField()
    
    btnDown = ft.FilledButton('Donwload', on_click=DownbtnFunc)
    res = ft.Text('')
    page.add(
        text1,
        ft.Row(
            [
            ft.Container(
                content=inputArea,
                
                alignment=ft.alignment.center,
                

            ),
            ft.Container(
                content=btnDown,
                
                alignment=ft.alignment.center,
                

            ),
        ]),
        res,
    )


ft.app(target=main)