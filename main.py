import flet as ft
from pytube import YouTube
import os
def main(page: ft.Page):
    page.title = 'BEVY'
    
    def close_infoBanner(e):
        page.banner.open = False
        page.update()
    def DownbtnFunc(e):
        if inputArea.value:
           
            try:
                
                arquivoFormat = ''
                if checkBoxMp4.value == True and checkBoxMp3.value == True:
                    arquivoFormat = 'mp4'
                    
                if checkBoxMp4.value == False and checkBoxMp3.value == False:
                    arquivoFormat = 'mp4'
                    
                if checkBoxMp4.value == True and checkBoxMp3.value == False:
                    arquivoFormat = 'mp4'
                    
                if checkBoxMp4.value == False and checkBoxMp3.value == True:
                    arquivoFormat = 'mp3'
                    
                paraApasta = os.getcwd()+os.sep+'Downloads'
                
                if arquivoFormat == 'mp4':
                    
                    ytObj = YouTube(inputArea.value)
                    ytObj = ytObj.streams.get_highest_resolution()
                    ytObj.download(output_path=paraApasta)
                else:
                    
                    yt = YouTube(inputArea.value)
                    ytObj = yt.streams.filter(only_audio=True).first()
                    ytObj.download(filename=f'{yt.title}.mp3', output_path=paraApasta)
                page.banner.bgcolor = ft.colors.GREEN_100
                page.banner.leading = ft.Icon(ft.icons.CHECK_CIRCLE_OUTLINED,color=ft.colors.GREEN_200, size = 40)
                page.banner.content = ft.Text("Download feito com sucesso!", color='black',size=18)
                page.banner.open = True
                page.update()
            except:
                
                page.banner.bgcolor =  ft.colors.RED_100
                page.banner.leading = ft.Icon(ft.icons.ERROR_OUTLINE_SHARP,color=ft.colors.RED_200, size = 40)
                page.banner.content = ft.Text("Houve algum erro, desculpe.",color='black',size=18)
                page.banner.open = True
                page.update()

    page.banner = ft.Banner(
        
        actions=[
            
            ft.FilledButton("Fechar", on_click=close_infoBanner, icon_color='black'),
        ],
    )
   
    


    text1 = ft.Text('Coloque o link aqui')
    inputArea = ft.TextField(label='Seu Link', border_color=ft.colors.PURPLE_800)
    checkBoxMp4 = ft.Checkbox(label="MP4", active_color=ft.colors.PURPLE_700, check_color='white')
    checkBoxMp3 = ft.Checkbox(label="MP3",active_color=ft.colors.PURPLE_700, check_color='white')
    btnDown = ft.FilledButton('Donwload',on_click=DownbtnFunc,  style=ft.ButtonStyle(
        bgcolor={
            ft.MaterialState.HOVERED: ft.colors.PURPLE_800,
            ft.MaterialState.FOCUSED: ft.colors.PURPLE_700,
            ft.MaterialState.DEFAULT: ft.colors.PURPLE_900,
        },
        color={
            
            ft.MaterialState.DEFAULT: ft.colors.WHITE,
        }
        
        ))

   
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
        ft.Text('Formato do arquivo', size=25),
        ft.Row(
            [
            ft.Container(
                content=checkBoxMp4,
                
                alignment=ft.alignment.center,
                

            ),
            ft.Container(
                content=checkBoxMp3,
                
                alignment=ft.alignment.center,
                

            ),
        ]),
    )


ft.app(target=main)