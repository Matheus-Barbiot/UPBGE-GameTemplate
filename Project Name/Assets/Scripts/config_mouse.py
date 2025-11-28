#icon=RESTRICT_SELECT_OFF
import bge
from mathutils import Vector

class Mouse():
    def __init__(self, visible=True):
        #Usado apenas para verificação em UI de HUD ou menus
        
        self.scene = bge.logic.getCurrentScene() 
        self.mouse = bge.logic.mouse
        
        #Atributos do mouse
        self.cam = self.scene.active_camera
        self.mouse.visible = visible
        
    

    def hover(self): #Retorna o objeto em que o mouse está em cima
        mousePos = Vector(self.mouse.position)
        factor = 1920 / ((1080 / bge.render.getWindowHeight()) * bge.render.getWindowWidth())
        mousePos.y *= factor
        mousePos.y -= (factor - 1.0) / 2.0
        
        return self.cam.getScreenRay(mousePos[0], mousePos[1], 1000, "")
    
    
    # Funções genéricas:
    def click(self):
        event = self.mouse.inputs[bge.events.LEFTMOUSE].activated
        return event
    
    def hold(self):
        event = self.mouse.inputs[bge.events.LEFTMOUSE].active
        return event
    
    
    

