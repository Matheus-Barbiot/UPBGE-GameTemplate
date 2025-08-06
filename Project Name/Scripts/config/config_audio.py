#icon=SPEAKER
import bge
from collections import OrderedDict

class Audio(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):   
        self.sound = bge.logic.globalDict['options']['sounds']
        self.music = bge.logic.globalDict['options']['music']
        
        self.soundAct = [act for act in self.object.actuators if 'sound' in act.name]
        self.musicAct = [act for act in self.object.actuators if 'music' in act.name]
        
        self.verifyVolume()
        
        
        pass
    
    def verifyVolume(self):    
        for sound in self.soundAct:
            sound.volume = self.sound
        
        for music in self.musicAct:
            music.volume = self.music
        
        
    def update(self):
        atualSound = bge.logic.globalDict['options']['sounds']
        atualMusic = bge.logic.globalDict['options']['music']
        

        
        if self.music != atualMusic or self.sound != atualSound:
            self.music = atualMusic
            self.sound = atualSound
            
            self.verifyVolume()
        pass
