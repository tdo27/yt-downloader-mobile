Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import yt_dlp
import os

class YTDownloader(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.label = Label(text="Introduceți link-ul YouTube Music:")
...         self.layout.add_widget(self.label)
...         
...         self.url_input = TextInput(multiline=False, hint_text="https://music.youtube.com/...")
...         self.layout.add_widget(self.url_input)
...         
...         self.btn = Button(text="Descarcă MP3", size_hint_y=None, height=50)
...         self.btn.bind(on_press=self.download_music)
...         self.layout.add_widget(self.btn)
...         
...         return self.layout
... 
...     def download_music(self, instance):
...         url = self.url_input.text
...         if not url:
...             self.label.text = "Te rog introdu un URL!"
...             return
... 
...         # Folderul de descarcare pe Android (cale specifica)
...         download_path = '/storage/emulated/0/Download/%(title)s.%(ext)s'
...         
...         ydl_opts = {
            'format': 'bestaudio[ext=m4a]/bestaudio/best', # Caută m4a mai întâi
            'outtmpl': path,
            # Am scos postprocessors (care cereau ffmpeg)
        }
... 
...         try:
...             with yt_dlp.YoutubeDL(ydl_opts) as ydl:
...                 ydl.download([url])
...             self.label.text = "Descărcare reușită în folderul Downloads!"
...         except Exception as e:
...             self.label.text = f"Eroare: {str(e)}"
... 
... if __name__ == '__main__':


