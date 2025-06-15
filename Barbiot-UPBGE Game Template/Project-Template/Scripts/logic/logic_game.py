#icon=OUTLINER_DATA_CAMERA
import bge
from InputMapping import Game as Gm
from collections import OrderedDict

class Game(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ('Mouse Visible', False),
    ])

    def start(self, args):
        self.input = Gm
        self.scene = bge.logic.getCurrentScene()
        bge.logic.mouse.visible = args['Mouse Visible']
        
        bge.logic.addScene('Hud', 1)
        pass

    def update(self):
        if len(bge.logic.getSceneList()) > 1:
            self.hud = bge.logic.getSceneList()[1]
        if self.input.pressed() and self.input.value() == 2.0:
            bge.logic.addScene('Pause', 1)
            self.hud.suspend()
            self.scene.suspend()
            
                
                
                
