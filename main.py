from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.utils import platform
import yt_dlp
import os

class YTDownloader(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        self.label = Label(text="YouTube Music Downloader", font_size='20sp')
        self.layout.add_widget(self.label)
        self.url_input = TextInput(multiline=False, hint_text="Lipește link-ul aici...", size_hint_y=None, height='50dp')
        self.layout.add_widget(self.url_input)
        self.btn = Button(text="DESCARCĂ", size_hint_y=None, height='60dp', background_color=(0, 0.7, 0, 1))
        self.btn.bind(on_press=self.download_music)
        self.layout.add_widget(self.btn)
        return self.layout

    def download_music(self, instance):
        url = self.url_input.text.strip()
        if not url:
            self.label.text = "Eroare: Introdu un URL!"
            return

        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
            path = '/storage/emulated/0/Download/%(title)s.%(ext)s'
        else:
            path = '%(title)s.%(ext)s'

        self.label.text = "Descărcare începută..."
        ydl_opts = {
            'format': 'bestaudio[ext=m4a]/bestaudio/best',
            'outtmpl': path,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            self.label.text = "GATA! Verifică folderul Downloads."
        except Exception as e:
            self.label.text = f"Eroare: {str(e)}"

if __name__ == '__main__':
    YTDownloader().run()
