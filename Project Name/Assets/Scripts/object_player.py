#icon=MESH_CUBE
import bge
import InputMapping as Input
from mathutils import Vector
from collections import OrderedDict

""" Código inicial de jogador, um template simples para iniciar os projetos no UPBGE. 
Possui:
    - movimentos com WASD
    - Pulo com SPACE
    - Colisão
"""
class Player(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ('speed', 0.0) # Parâmetro 'speed' no args que define a velocidade de movimento
    ])

# ================| Init |===============

    def start(self, args):
        # Componentes necessários para a lógica de jogador
        self.character = bge.constraints.getCharacter(self.object)
        self.object.collisionCallbacks.append(self.collision)
        
        # Parâmetros do ARGS
        self.speed = args['speed']
        
        # Entradas de teclado
        # para movimento:
        self.Y = Input.Player_Y # Teclas W e S
        self.X = Input.Player_X # Teclas A e D
        
        # para pulo:
        self.jump = Input.Player_Jump # Tecla SPACE
        pass
    
# ================| Movimento |===============
    
    # Função que aplica o movimento do personagem dependendo de qual tecla está sendo pressionada
    def movement(self):
        vetor = self.object.localOrientation * Vector([self.X.value(), self.Y.value(), 0])
        self.character.walkDirection = vetor.normalized() * self.speed

# ================| Colisão |===============

    # Função do CollisionCallback para verificar colisões
    def collision(self, obj, point, normal):
        # Colisão com o inimigo
        if 'enemy' in obj:
            self.scene.replace('Death')
            
# ================| Execução |===============
            
    # Atualiza a lógica por todos os quadros por segundo
    def update(self):
        self.movement()
            
        if self.jump.pressed():
            self.character.jump()
        pass

# ================| Final |===================
