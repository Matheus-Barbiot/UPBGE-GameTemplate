#icon=SOLO_OFF
import bge
from mathutils import Vector

class Mouse():
    def __init__(self, Visible=True):
        #Usado apenas para verificação em UI de HUD ou menus
        
        self.scene = bge.logic.getCurrentScene() 
        self.mouse = bge.logic.mouse
        
        #Atributos do mouse
        self.cam = self.scene.active_camera
        self.mouse.visible = Visible
        
    def hover(self): #Retorna o objeto em que o mouse está em cima
        mousePos = Vector(self.mouse.position)
        factor = 1920 / ((1080 / bge.render.getWindowHeight()) * bge.render.getWindowWidth())
        mousePos.y *= factor
        mousePos.y -= (factor - 1.0) / 2.0
        
        return self.cam.getScreenRay(mousePos[0], mousePos[1], 1000, "")
    
    def click(self): #Verifica clique com o mouse
        click = self.mouse.inputs[bge.events.LEFTMOUSE].activated
        
        return click
        