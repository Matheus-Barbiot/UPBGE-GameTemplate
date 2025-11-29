#icon=OUTLINER_DATA_CAMERA
import bge
from collections import OrderedDict

import config_mouse
import config_menu


class Menu(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ('Game scene', 'Game'),
    ('Main Menu', 'Menu'),
    ('Previous scene (optional)', ''),
    ])
    
    def start(self, args): 
        # Carrega o globalDict
        bge.logic.loadGlobalDict()
        
        # Pega o nome do meu principal e a cena do jogo
        self.home = args['Main Menu']
        self.game = args['Game scene']
        
        # Pega a cena anterior definida OU a do globalDict
        self.previous = args['Previous scene (optional)'] or bge.logic.globalDict.get('Previous menu')
        
        
        # Objetos do mouse e do menu: importantes para a logica funcionar
        self.mouse = config_mouse.Mouse(visible=True)
        self.menu = config_menu.Menu(self.home, self.previous)
        
        # Funções pre definidas de cada botão
        self.commands_dict = {
            'play'    : self.play,
            'restart' : self.play,
            'quit'    : self.quit,
            'resume'  : self.resume,
            'back'    : self.menu.back,
            'home'    : self.menu.return_home,
        }
        
#======================= Funções genéricas de menu ==============================
    
    def update_previous(self):   
        # Define a cena atual como a anterior e salva
        bge.logic.globalDict['Previous menu'] = self.object.scene.name
        bge.logic.saveGlobalDict()
        
        
    def play(self):
        # Dá play no jogo
        self.menu.change(self.game)
        
        
    def quit(self):
        # Sai do jogo
        bge.logic.globalDict['Previous menu'] = ''
        bge.logic.saveGlobalDict()
        bge.logic.endGame()
    
    
    def resume(self):
        # Volta para o jogo atual
        # Verifica se há algum jogo atual
        for scene in bge.logic.getSceneList():
            if scene.name == self.game:
                scene.resume()
                self.object.scene.end()
                return
        
        return print('Nenhuma cena de game achada')

#===============================================================================#
        
    def update(self):             
        # Verificação:
        hovered = self.mouse.hover()
        if not self.mouse.click() or not hovered:
            return
        
        # Verifica se o objeto é um botão,importante para não confundir com outros objetos na cena
        if not 'button' in hovered:
            return
            
        # verifica se é um objeto de grupo: Importante porque a maioria dos botões dos menus serão instãncias de grupo
        if hovered.groupObject:
            button = hovered.groupObject
            
        if 'setting' in button:
            return
        
        # propriedades necessárias
        command = button.get('command')
        set_scene = button.get('set scene')
        
        # salva o globalDict
        self.update_previous()
        
        if command:
            #aplica o comando especificado
            command = command.lower()
            if command in self.commands_dict:
                self.commands_dict[command]()
        
        elif set_scene:
            #muda a cena específicada
            scene = set_scene.title()
            self.menu.change(scene)
                
        else:
            print(f'{button.name}: Nenhum comando encontrado para esse botão:\n defina um "command" com o comando ou \n "set scene" com a cena que deseja acessar.')
                
                