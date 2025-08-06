#icon=SYNTAX_ON
import bge

class Menu():
    def __init__(self, home='', previous='', next=''):
        # Lista com todas as cenas do jogo
        self.scenes = bge.logic.getSceneList() + bge.logic.getInactiveSceneNames()
        
        # Verificação
        for menu in [home, previous, next]:
            if menu and menu not in self.scenes:
                return print(f'Menu "{menu}" não identificado.')

        
        # Pega o nome das cenas 
        self.current = bge.logic.getCurrentScene()
        
        self.home = home
        self.previous = previous
        self.next = next
    
    
    # voltar
    def back(self):
        if not self.previous:
            print('Nenhum menu anterior definido')
            return False
        
        self.current.replace(self.previous)
        return True

    # avançar
    def advance(self):
        if not self.next:
            print('Nenhum próximo menu definido')
            return False
        
        self.current.replace(self.next)
        return True
        
        
    # mudar
    def change(self, scene=''):
        if not scene in self.scenes:
            print(f'Cena {scene} não identificada')
            return False
        
        self.current.replace(scene)
        return True


    # voltar ao menu principal
    def return_home(self):
        if not self.home:
            print(f'Nenhum menu principal definido')
            return False
        
        self.current.replace(self.home)
        return True