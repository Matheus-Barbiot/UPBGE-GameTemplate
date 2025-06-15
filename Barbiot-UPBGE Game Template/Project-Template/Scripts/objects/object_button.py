#icon=MESH_CUBE
import bge
from config_mouse import Mouse
from collections import OrderedDict
            
class Button(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ('Default mesh', 'Button_Default'),
    ('Hovered mesh', 'Button_Hovered'),
    ('Text name', ''),
    ('Text color', (0,0,0,1)),
    ])

    def start(self, args):
        self.mouse = Mouse()
        
        
        #Nomes das malhas do botão
        self.default = args['Default mesh']
        self.hovered = self.default if not args['Hovered mesh'] else args['Hovered mesh']
            
        #Objeto de texto pertencente ao botão:
        self.textObject = None
        self.textColorDefault = None
        self.textColorHovered = None

        
        if args['Text name']:
            self.textObject = self.object.children.get(args['Text name'])
            if self.textObject != None:
                self.textColorDefault = self.textObject.color.copy()
                self.textColorHovered = args['Text color']
    
            
        #variaveis
        

    def replaceButtonForm(self, mesh="", color=(0,0,0,0)):
        #Função para atualizar a forma do self.object e self.textObject
        if self.object:
            if not mesh in self.object.meshes:
                self.object.replaceMesh(mesh, True, False)
                
        if self.textObject:
            if not color == self.textObject.color:
                self.textObject.color = color

                

    def update(self):
        #Verificação do mouse
        try:
            if self.mouse.hover() == self.object:
                #atualização da forma para quando o mouse estiver em cima
                self.replaceButtonForm(self.hovered, self.textColorHovered)

            else:
                #atualização da forma para o padrão
                self.replaceButtonForm(self.default, self.textColorDefault)
        except:
            print('ERRO', self.object.name)

