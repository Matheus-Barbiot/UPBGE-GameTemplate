#icon=OUTLINER_DATA_CAMERA
import bge
from InputMapping import Game
from config_mouse import Mouse
from collections import OrderedDict

class Menu(bge.types.KX_PythonComponent):
    args = OrderedDict([
        ('Play', "Play"),
        ('Options', "Options"),
        ('Quit', "Quit"),
    ])
    
    def start(self, args): #Atributos iniciais
        self.scene = bge.logic.getCurrentScene()
        self.mouse = Mouse(True)
        self.input = Game
        
        #Nomes de botões
        self.play = args['Play']
        self.options = args['Options']
        self.quit = args['Quit']
        
        #Declaração de ultima cena acessada
        bge.logic.globalDict['lastMenu'] = 'Menu'
        
    def update(self):
        #Funções por teclado:
        if self.input.pressed():
            if self.input.value() == 1.0: #tecla ENTER - Entra no jogo
                self.scene.replace('Game')
        
        #Funções por mouse
        elif self.mouse.click():
            hovered = self.mouse.hover()
            
            if hovered and not 'GradintDisplay' in hovered.name:
                #Entra no jogo
                if self.play in hovered.name:
                    self.scene.replace('Game')
                        
                #Entra no options
                elif self.options in hovered.name:
                    self.scene.replace('Options')
                    
                #Salva e sai do jogo
                elif self.quit in hovered.name:
                    bge.logic.saveGlobalDict()
                    bge.logic.endGame()
    
