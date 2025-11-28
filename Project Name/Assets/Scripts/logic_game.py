#icon=OUTLINER_DATA_CAMERA
import bge
from InputMapping import Global_Keys
from collections import OrderedDict

class Game(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):
        self.keyboard = Global_Keys
        pass

    def update(self):
        if self.keyboard.pressed() and self.keyboard.value() == 2.0:

            bge.logic.addScene('Pause', 1)
            self.object.scene.suspend()
        
                
