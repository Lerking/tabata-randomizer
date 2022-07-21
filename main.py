from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem

from tabata_randomizer import TabataRandomizer as TR
import playsound

KV = '''
ScrollView:

    MDList:
        id: container
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.tabata = TR()
        self.exercises = self.tabata.get_training_plan()
        for i in self.exercises:
            self.root.ids.container.add_widget(
                OneLineListItem(text=i['name'], on_release=self.play_audio)
            )
    
    def play_audio(self, instance):
        for i in self.exercises:
            if i['name'] == instance.text:
                playsound.playsound('audio/'+i['speak'], False)
                break
        
if __name__ == '__main__':
    MainApp().run()