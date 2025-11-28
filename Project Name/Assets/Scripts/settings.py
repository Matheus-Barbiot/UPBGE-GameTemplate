#icon=SCRIPTWIN
import bge

class Settings():
    def __init__(self):
        # Tamanhos de tela
        self.sizes_list = [
            (640, 480),
            (800, 600),
            (1280, 720),
            (1366, 768)
        ]
        
        # Pega o tamanho de tela padrão da tela informada na cena de INTRO
        self.max_size = bge.logic.globalDict.get('Max Screen Size')
        
        # Coloca ela na lista de tamanh
        if self.max_size and not self.max_size in self.sizes_list:
            self.sizes_list.append(self.max_size)
        
        # Configurações padrão
        self.default = {
        'Video': {
            'Screen Size':  len(self.sizes_list)-1, 
            'Display Mode': True, 
            'Vsync':        True,
            },
            
        'Audio': {
            'General':  2.0,
            'Music':    1.0, 
            'Fx':   1.0
            } 
        }
 
        
#=========================== Funções de VIDEO =========================
        
    def set_screen_size(self, index):
        #pega o tamanho cosrrespondente ao index na lista de tamanhos
        size = self.sizes_list[index]
        
        #Aplica no jogo
        bge.render.setWindowSize(*size)
        return
        
    
    def set_display_mode(self, mode):
        # Altera entre modo janela e tela cheia
        
        # Reseta o tamanho para aplicar o modo
        bge.render.setWindowSize(*self.sizes_list[-1])
        # Altera
        bge.render.setFullScreen(mode)
        
        # Volta para o tamanho atual
        self.set_screen_size(bge.logic.globalDict['Settings']['Video']['Screen Size'])
    
    
    def set_vsync_mode(self, mode):
        num = 0 if mode == True else 1
        bge.render.setVsync(mode)
        
      
#============================================================================  

    # Aplica configurações de vídeo
    def apply_video(self):
        video = bge.logic.globalDict['Settings']['Video']
        
        #aplica as configurações
        self.set_display_mode(video['Display Mode'])
        self.set_screen_size(video['Screen Size'])
        self.set_vsync_mode(video['Vsync'])


    
        
    