#icon=OUTLINER_DATA_CAMERA
import bge
from config_user import UserConfig
from collections import OrderedDict

class Intro(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ('Timer', 0.0),
    ])

    def start(self, args):
        #Atualiza o globalDict.
        bge.logic.loadGlobalDict()
        
        #Define a resolução do dispositivo como a padrão.
        bge.logic.globalDict['defaultSize'] = bge.render.getDisplayDimensions()
        
        #Aplica as configurações de video.
        video = UserConfig(bge.logic.globalDict['defaultSize']) 
        video.applyVideoOptions(bge.logic.globalDict.get('options'))

        #Tempo de carregamento
        self.timer = 0.0
        self.target = args['Timer']
        pass

    def update(self):
        #Aplica o carregamento
        if self.timer >= self.target:
            bge.logic.getCurrentScene().replace('Menu')
        else:
            self.timer += 1
        pass






#Direciona para o menu

