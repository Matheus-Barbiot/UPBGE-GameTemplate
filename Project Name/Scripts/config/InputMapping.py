#icon=FONT_DATA
# Input Mapping system.
# Created by: Guilherme Teres Nunes
# Visit: youtube.com/UnidayStudio
import bge

class __InputController():
    def __init__(self, inpList):
        self.inputList = inpList
    
    def __checkInputs(self):
        val = [False, 0.0, False]
        for input in self.inputList:
            origin = None
            if input[0] == "Keyboard":
                origin = bge.logic.keyboard.inputs
            elif input[0] == "Mouse":
                origin = bge.logic.mouse.inputs
            else:
                origin = bge.logic.joysticks[0].inputs
            
            out = origin[ getattr(bge.events, input[1]) ]
            
            if out.active:
                val[1] = input[2]
            if out.activated:
                val[0] = True
            elif out.released:
                val[2] = True
        return val
    
    def value(self):
        return self.__checkInputs()[1]
    
    def getValue(self):
        return self.value()
    
    def pressed(self):
        return self.__checkInputs()[0]
    
    def released(self):
        return self.__checkInputs()[2]
            
            
Player_Y = __InputController([['Keyboard', 'WKEY', 1.0], ['Keyboard', 'SKEY', -1.0]])
Player_X = __InputController([['Keyboard', 'DKEY', 1.0], ['Keyboard', 'AKEY', -1.0]])
Player_Jump = __InputController([['Keyboard', 'SPACEKEY', 1.0]])

Global_Keys = __InputController([['Keyboard', 'ENTERKEY', 1.0], ['Keyboard', 'ESCKEY', 2.0]])
