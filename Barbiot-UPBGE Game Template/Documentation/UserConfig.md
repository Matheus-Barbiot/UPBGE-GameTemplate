# Introdução
#script
videoConfig é um objeto responsável por aplicar as configurações de video, utilizando um dicionário pronto.

## Importação e uso
```
from video import VideoConfig

videoController = VideoConfig(size)
```

### Parâmetros

- `size`
	- **Descrição:** Resolução padrão do dispositivo.
	- **Tipo:** tuple (width, height)

*Dica* Você pode pegar a resolução padrão utilizando `bge.render.getDislayDimensions()` 

### Atributos

`self.defaultSize` 
- **Descrição:** Recebe o valor de `size` 
- **Tipo:** Tupla (width, height)

`self.sizeList`
- **Descrição:** Lista de resoluções pré definidas do objeto, com `self.defaultSize` incluso.
- **Tipo:** Lista de tuplas:
```
[(640, 480), 
(800, 600), 
(1280, 720), 
(1366, 768), 
self.defaultSize]
```

### Métodos

`self.setScreenSize(index)`
**Descrição:**
	Aplica alguma das resoluções definidas no `self.sizeList`
**Parâmetros:** 
	*index* - Index referente à resolução que será usada do `self.sizeList` 
		**Tipo:** int 


`self.setFullScreen(full)`
**Descrição:**
	Ativa ou desativa o modo de tela cheia
**Parâmetros:**
	*full* - `True` ativa e `False` desativa
		**Tipo:** Bool


`self.applyVideoOptions(options)`
**Descrição:** 
	Aplica as configurações acima a partir de um dicionário. Além de aplicar configurações no Vsync também, ativando ou desativando.
**Parâmetros**
	*options* - ``{'screenSize': int, 'fullScreen': bool, 'vsync':int}``

---
# Código

```
#icon=SOLO_OFF
import bge

class VideoConfig():
    def __init__(self, size):
        self.defaultSize = size
        
        self.sizeList = [
            (640, 480),
            (800, 600),
            (1280, 720),
            (1366, 768),
            self.defaultSize,  # resolução da tela cheia
        ]
        
        
    def setScreenSize(self, index):
        #muda a relosução da tela
        
        size = self.sizeList[index]
        bge.render.setWindowSize(*size)
        
    
    def setFullScreen(self, full):
        # Ajusta a resolução do monitor
        if bge.render.getFullScreen() != full:
            bge.render.setWindowSize(*self.defaultSize)
            bge.render.setFullScreen(full)  # Ajusta a resolução da janela
        

    def applyVideoOptions(self, options):
        if options:
            index = options['screenSize']
            fullscreen = options['fullscreen']
            vsync = options['vsync']
            
            
            self.setFullScreen(fullscreen)
            self.setScreenSize(index)
            bge.render.setVsync(vsync)
            
            bge.logic.globalDict['options'] = options
            bge.logic.saveGlobalDict()
```