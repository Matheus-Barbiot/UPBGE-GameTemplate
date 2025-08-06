#icon=OUTLINER_DATA_CAMERA
import bge
from Settings import Settings
from collections import OrderedDict

class Intro(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ('Next Scene', ""),
    ])

    def start(self, args):
        bge.logic.loadGlobalDict()
        bge.logic.globalDict['Max Screen Size'] = bge.render.getDisplayDimensions()
    
        
        setting = Settings()
        
        if not bge.logic.globalDict.get('Settings'):
            bge.logic.globalDict['Settings'] = setting.default
            
        setting.apply_video()
        
        self.object.scene.replace(args['Next Scene'])
        pass

    def update(self):
        pass
