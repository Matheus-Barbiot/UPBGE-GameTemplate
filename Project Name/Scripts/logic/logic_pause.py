#icon=OUTLINER_DATA_CAMERA
import bge
from InputMapping import Game
from config_mouse import Mouse # Função de mouseOver 
from collections import OrderedDict


class Pause(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ('Resume', "Resume"),
    ('Options', "Options"),
    ('Quit', "Quit"),
    ])
    
    def start(self, args): #Atriutos iniciais
        self.scene = bge.logic.getCurrentScene()
        self.mouse = Mouse()
        self.input = Game
        
        #Nomes dos Botões
        self.resume = args['Resume']
        self.options = args['Options']
        self.quit = args['Quit']
        
        self.lastGameScene = bge.logic.getSceneList()[0] #Pega a cena de jogo atual
    
    
    def update(self):
        #Função por teclado: ESC ou ENTER - volta para o jogo
        if self.input.pressed(): 
            self.lastGameScene.resume() 

        #Funções por mouse
        if self.mouse.click():
            hovered = self.mouse.hover()
            
            #
            if hovered and not 'GradintDisplay' in hovered.name:
                #Voltar para o jogo
                if self.resume in hovered.name:
                    self.lastGameScene.resume()
                    self.scene.replace('Hud')
                        
                #Entrar em options
                elif self.options in hovered.name:
                    bge.logic.globalDict['lastMenu'] = 'Pause'
                    bge.logic.saveGlobalDict()
                    self.scene.replace('Options')
                    
                #Voltar para o menu
                elif self.quit in hovered.name:
                    for scene in bge.logic.getSceneList():
                        self.scene.replace('Menu')
                        if scene.name !='Menu':
                            scene.end()
                        



