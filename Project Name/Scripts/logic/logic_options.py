#icon=OUTLINER_DATA_CAMERA
import bge
import Settings as Set
from collections import OrderedDict
from config_mouse import Mouse


class Settings(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])
    
    def start(self, args):
        # Carrega o globalDict
        bge.logic.loadGlobalDict()
        
        # Carrega a classe com as funções de configurações
        self.setting = Set.Settings()
        self.mouse = Mouse(True)
        
        # Funções da cena
        self.set_funcs = {
            'Screen': self.set_screen_size,
            'Display': self.set_display_mode,
            'Vsync': self.set_vsync,
            'Volume': self.set_volume,
        }
        
        self.gd_funcs = {
            'save': self.save_settings,
            'cancel': self.cancel_settings,
            'reset': self.reset_settings
        }
        


#===================================
    # Funções de Configurações
#===================================

    # Tamanho da tela
    def set_screen_size(self, num):
        max = len(self.setting.sizes_list) - 1
        func = self.setting.set_screen_size
        
        value = self.__to_int_func('Screen Size', 'Video', num, max, func)
        self.object['set visual'] = 'screen'
        
        return(value)
        
        
    # Modo de tela
    def set_display_mode(self, mode):
        value = self.__to_bool_func('Display Mode', mode, self.setting.set_display_mode)
        self.object['set visual'] = 'display'
        return value


    # Vsync
    def set_vsync(self, mode):
        value = self.__to_bool_func('Vsync', mode, self.setting.set_vsync_mode)
        self.object['set visual'] = 'vsync'
        return value
    
        
    def set_volume(self, key, num):        
        value = self.__to_int_func(key, 'Audio', num, max=2)
        self.object['set visual'] = 'volume'
        
        return(value)
    
#====================================================
#       Funções de globalDict
#====================================================

    def reset_settings(self):
        bge.logic.globalDict['Settings'] = self.setting.default
        self.setting.apply_video()
        
        self.object['set visual'] = 'all'
        print('algo')
        
    def cancel_settings(self):
        bge.logic.loadGlobalDict()
        self.setting.apply_video()
        
        self.object['set visual'] = 'all'
    
    def save_settings(self):
        bge.logic.saveGlobalDict()
        
#====================================================

    def update(self):
        # Pega o objeto que o mouse está em cima
        hovered = self.mouse.hover()
        
        #Verifica se é um botão válido ou nada
        if not self.mouse.click() or not hovered or 'button' not in hovered:
            return
        
        # Verifica se é um objeto de grupo
        button = hovered.groupObject if hovered.groupObject else hovered
        if 'setting' in button:
            if button['setting'] == 'gd':
                print(button.name)
                for key, func in self.gd_funcs.items():
                    if key in button:
                        func()
                        print(key, button.name)
            
            elif button['setting'] == 'set':
                # aplica a função correspondente á cada chave no self.funcs se alguma da propriedade tiver o mesmo nome.
                for key, func in self.set_funcs.items():
                    if key in button:
                        # verifica se é um volume para aplicar configurações de volume
                        if key == 'Volume':
                            value = func(button['Type'], button[key])
                            self.object[button['Type']] = value
                        else:
                            # se não aplicar configurações de 
                            value = func(button[key])
                            print(key, button.name)
                            self.object[key] = value
                            
                        #Se for um valor boleano, atriubui o valor para a propriedade do botão também.
                        if isinstance(button[key], bool):
                            button[key] = value

#################################################
# Funções privadas
#################################################

    def __to_bool_func(self, key, mode, func):
        # Pega o valor atual no globalDict
        current_mode = bge.logic.globalDict['Settings']['Video'][key]
        
        # Verifica se o inverso do parãmetro passado não é a mesma coisa do valor atual
        new_mode = not mode
        if current_mode == new_mode:
            return new_mode
        
        # Aplica a função e salva no globalDict
        func(new_mode)
        bge.logic.globalDict['Settings']['Video'][key] = new_mode
        return new_mode
    
    
    
    def __to_int_func(self, key, category, num, max, func=None):
        # Pega o valor atual
        current = bge.logic.globalDict['Settings'][category][key]
        
        # Faz o calculo
        new = current + num
        
        # Verifica
        if new > max or new < 0.0:
            return current
        
        #Se tiver função, ativa. Atualza o globalDict
        if func:
            func(new)
        bge.logic.globalDict['Settings'][category][key] = new
        
        return new