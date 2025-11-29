#icon=SYNTAX_ON
import bge

class Menu:
    """
    Componente de funções gerais de menu.
    Permite navegar entre cenas: anterior, próxima, principal ou qualquer outra.
    """

    def __init__(self, home='', previous='', next=''):
        # Cena atual
        self.current = bge.logic.getCurrentScene()
        
        # Definições
        self.home = self._validate_scene(home)
        self.previous = self._validate_scene(previous)
        self.next = self._validate_scene(next)

    # ---------------- Funções de navegação ---------------- #

    def back(self):
        if not self.previous:
            print('Nenhum menu anterior definido')
            return False
        return self._replace(self.previous)


    def advance(self):
        if not self.next:
            print('Nenhum próximo menu definido')
            return False
        return self._replace(self.next)


    def change(self, scene=''):
        if not scene or scene not in self.scenes:
            print(f'Cena "{scene}" não identificada')
            return False
        return self._replace(scene)


    def return_home(self):
        if not self.home:
            print('Nenhum menu principal definido')
            return False
        return self._replace(self.home)

    # ---------------- Funções privadas ---------------- #

    def _replace(self, scene_name):
        try:
            self.current.replace(scene_name)
            return True
        except Exception as e:
            print(f'Erro ao trocar para cena "{scene_name}": {e}')
            return False