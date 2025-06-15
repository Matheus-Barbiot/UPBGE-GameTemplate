#icon=OUTLINER_DATA_CAMERA
import bge
from config_mouse import Mouse
from InputMapping import Game
from user_config import UserConfig
from collections import OrderedDict

class Options(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])
    
    def start(self, args):
        self.scene = bge.logic.getCurrentScene()
        self.mouse = Mouse()
        self.input = Game
        self.video = UserConfig(bge.logic.globalDict.get('defaultSize'))
        
        bge.logic.loadGlobalDict()
        
        self.Txt_Resolution = self.scene.objects['Txt_Resolution']
        self.Txt_Screen = self.scene.objects['Txt_Screen']
        self.Txt_Vsync = self.scene.objects['Txt_Vsync']
        self.Txt_Music = self.scene.objects['Txt_Music']
        self.Txt_Sounds = self.scene.objects['Txt_Sounds']
        
        if not bge.logic.globalDict.get('options'):
            bge.logic.globalDict['options'] = self.defaultOptions.copy()
        self.loadOptions(bge.logic.globalDict['options'])

        self.updateVisualValues()
  
    
    def update(self):
        if self.mouse.click():
            hovered = self.mouse.hover()

            ####### VIDEO:
            #fullscreen
            if hovered and not 'GradintDisplay' in hovered.name:
                
                #Modo de tela
                if hovered.name == 'Btn_FullScreen':
                    self.object['fullscreen'] = not self.object['fullscreen']
                    
                #Resolução
                if hovered.name == 'Btn_ScreenSize+':
                    if self.object['screenSize'] < 4:
                        self.object['screenSize'] += 1
                            
                if hovered.name == 'Btn_ScreenSize-':
                    if self.object['screenSize'] > 0:
                        self.object['screenSize'] -= 1 
                
                #Vsync
                if hovered.name == 'Btn_Vsync':
                    self.object['vsync'] = 0 if self.object['vsync'] == 1 else 1
                
                ####### AUDIO:
                #mute
                if hovered.name == 'Btn_Mute':
                    self.object['music'] = 0.0
                    self.object['sounds'] = 0.0
                
                #music
                if hovered.name == 'Btn_Music+':
                    if self.object['music'] < 2.0:
                        self.object['music'] += 0.1
                        
                if hovered.name == 'Btn_Music-':
                    if self.object['music'] >= 0.0:
                        self.object['music'] -= 0.1
                    
                #sounds
                if hovered.name == 'Btn_Sounds+':
                    if self.object['sounds'] < 2.0:
                        self.object['sounds'] += 0.1
                    
            
                if hovered.name == 'Btn_Sounds-':
                    if self.object['sounds'] >= 0.0:
                        self.object['sounds'] -= 0.1
                
                ######## OUTROS:
                if hovered.name == 'Btn_Apply':
                    self.saveOptions()
                
                if hovered.name == 'Btn_Cancel':
                    self.loadOptions(bge.logic.globalDict.get('options'))
                    self.saveOptions()
                    
                if hovered.name == 'Btn_Back':
                    self.scene.replace(bge.logic.globalDict.get('lastMenu'))
                
                if hovered.name == 'Btn_Reset':
                    bge.logic.globalDict['options'] = self.video.defaultOptions
                    self.loadOptions(self.video.defaultOptions)
                
                self.updateVisualValues()
            
        #saida:
        elif self.input.pressed():
            if self.input.value() == 1.0:
                self.saveOptions()
            else:
                self.scene.replace(bge.logic.globalDict.get('lastMenu'))
            
        
    def saveOptions(self):
        #salva as configurações no globalDict
        options = dict()
        for prop_name in self.object.getPropertyNames():
            options[prop_name] = self.object[prop_name]
            
        self.video.applyVideoOptions(options)
        
    def loadOptions(self, options):
        #Carrega as configurações no globalDict
        self.updateVisualValues()
        if options:
            for prop, value in options.items():
                self.object[prop] = value
            
            
    def updateVisualValues(self):
        #Função que irá atualizar os textos e seus valores:
        #Resolução da tela
        index = self.object['screenSize']
        size = self.video.sizeList[index]
        self.Txt_Resolution['Text'] = f'{size[0]}x{size[1]}'
        
        #Modo de tela
        screen = 'FullScreen' if self.object['fullscreen'] == True else 'WideScreen'
        self.Txt_Screen['Text'] = screen
        
        #Vsync
        vsync = 'Vsync on' if self.object['vsync'] == 0 else 'Vsync off'
        self.Txt_Vsync['Text'] = vsync
        
        #audio
        musicValue = int(self.object['music'] * 50)
        soundValue = int(self.object['sounds'] * 50)
        
        self.Txt_Music['Text'] = f'Music: {musicValue}%'
        self.Txt_Sounds['Text'] = f'Sounds: {soundValue}%'
