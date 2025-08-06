#icon=SOLO_OFF
import bge

class UserConfig():
    def __init__(self, size):
        self.defaultSize = size
        self.sizeList = [
            (640, 480),
            (800, 600),
            (1280, 720),
            (1366, 768),
            self.defaultSize,  # resolução da tela cheia
        ]
        self.defaultOptions = {'screenSize':len(self.sizeList)-1, 'fullscreen':True, 'vsync':0, 'music':1.0, 'sounds':1.0} 
        
        
        
    def setScreenSize(self, index):
        #muda a relosução da tela
        
        size = self.sizeList[index]
        bge.render.setWindowSize(*size)
        
    
    def setFullScreen(self, full):
        # Ajusta a resolução do monitor
        if bge.render.getFullScreen() != full:
            bge.render.setWindowSize(*self.defaultSize)
            bge.render.setFullScreen(full)  # Ajusta a resolução da janela
        

    def applyVideoOptions(self, options):
        if not options:
            options = self.defaultOptions
            
        index = options['screenSize']
        fullscreen = options['fullscreen']
        vsync = options['vsync']
        
        
        self.setFullScreen(fullscreen)
        self.setScreenSize(index)
        bge.render.setVsync(vsync)
        
        bge.logic.globalDict['options'] = options
        bge.logic.saveGlobalDict()