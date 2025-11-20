#icon=BONE_DATA
import bge
from InputMapping import Player_Y, Player_X
from collections import OrderedDict

class PlayerRig(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):
        pass
    
    def set_direction(self):
        target_name = str()
        
        if Player_Y.value() == 1: #W
            if Player_X.value() == 1:
                target_name = 'Obj_WD'
            elif Player_X.value() == -1:
                target_name = 'Obj_WA'
            else:
                target_name = 'Obj_W'
            
        elif Player_Y.value() == -1:
            if Player_X.value() == 1:
                target_name = 'Obj_SD'
            elif Player_X.value() == -1:
                target_name = 'Obj_SA'
            else:
                target_name = 'Obj_S'
            
        elif Player_X.value() == 1:
            target_name = 'Obj_D'
        elif Player_X.value() == -1:
            target_name = 'Obj_A'

        target_obj = self.object.scene.objects.get(target_name)

        if target_obj:
            self.object.alignAxisToVect(-target_obj.localPosition, 1, 0.5)
            self.object.alignAxisToVect([0,0,5], 2, 1.0)
            
            
    def update(self):
        Move =  True if Player_X.value() or Player_Y.value() else False

        
        
        if Move: 
            self.set_direction()
            self.object.playAction('Player_Run', 1, 15, blendin=2)
        else: 
            self.object.playAction('Player_Idle', 1, 10, blendin=2)
        pass
