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
        
        self.next_scene = args['Next Scene']
        self.setting = Settings()
        

        pass

    def update(self):
        if not bge.logic.globalDict.get('Settings'):
            bge.logic.globalDict['Settings'] = self.setting.default
            self.setting.apply_video()
        else:
            self.object.scene.replace(self.next_scene)
            
        pass
