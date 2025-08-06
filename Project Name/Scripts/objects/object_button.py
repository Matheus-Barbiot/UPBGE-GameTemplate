#icon=COLOR
import bge
from mathutils import Vector
from config_mouse import Mouse
from collections import OrderedDict
            
class Button(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ('Hover Color', [1,1,1,1]),
    ])

    def start(self, args):
        self.mouse = Mouse()
        
        # Cores
        self.hov_color = args['Hover Color']
        self.def_color = self.object.color.copy()
        
        if self.object.groupObject:
            self.object.visible = self.object.groupObject.visible
        
        
    def update(self):
        if not self.object.visible:
            return
        
        hovered = self.mouse.hover()
        
        if self.object == hovered:
            self.object.color = self.hov_color

        else:
            self.object.color = self.def_color
