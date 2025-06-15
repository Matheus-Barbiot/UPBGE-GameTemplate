#icon=MESH_CUBE
import bge
import InputMapping as Input
from mathutils import Vector
from collections import OrderedDict

class Player(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ('speed', 0.0)
    ])

    def start(self, args):
        self.character = bge.constraints.getCharacter(self.object)
        
        self.speed = args['speed']
        self.Y = Input.Player_Y
        self.X = Input.Player_X
        self.jump = Input.Player_Jump
        pass
    
    def movement(self):
        vetor = self.object.localOrientation * Vector([self.X.value(), self.Y.value(), 0])
        self.character.walkDirection = vetor.normalized() * self.speed

    def update(self):
        if self.X  or self.Y:
            self.movement()
        if self.jump.pressed():
            self.character.jump()
        
        pass
