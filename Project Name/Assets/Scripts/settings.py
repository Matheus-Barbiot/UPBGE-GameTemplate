#icon=SCRIPTWIN
import bge

class Settings:
    """
    Classe Settings (configurações)
    Aplica as configurações do usuário ou usa valores padrão.
    """

    def __init__(self):
        # ------------------------ configurações de resolução ----------------
        self.display_modes = [
            (640, 480),
            (800, 600),
            (1280, 720),
            (1366, 768)
        ]

        # Pega resolução salva ou padrão
        self.resolution = bge.logic.globalDict.get(
            'resolution',
            bge.render.getDisplayDimensions()
        )

        if not self.resolution:
            print('Resolução padrão não identificada, uso de padrão do jogo')
        elif self.resolution not in self.display_modes:
            self.display_modes.append(self.resolution)

        # ------------------------ configurações padrão ----------------
        self.default_config = {
            'Video': {
                'Resolution Index': len(self.display_modes) - 1,
                'Display Mode': "fullscreen",  # "windowed" ou "fullscreen"
                'Vsync': True,
            },
            'Audio': {
                'Master': 1.0,  # Volume geral normalizado
                'Music': 1.0,
                'SFX': 1.0
            }
        }

    # ---------------- Muda o tamanho da área de renderização -------------------
    def set_display_size(self, index: int):
        size = self.display_modes[index]
        bge.render.setWindowSize(*size)

    # ---------------- Muda o modo da área de renderização -------------------
    def set_display_mode(self, fullscreen: bool):
        # Aplica modo fullscreen ou windowed
        bge.render.setFullScreen(fullscreen)

    # ----------------- Altera o modo do Vsync ----------------------
    def set_vsync_mode(self, enabled: bool):
        bge.render.setVsync(int(enabled))

    # ------ Aplica TODAS configurações de video ---------------
    def apply_video(self):
        try:
            video = bge.logic.globalDict['Settings']['Video']

            # aplica as configurações na seguinte ordem SEMPRE
            self.set_display_mode(video['Display Mode'] == "fullscreen")
            self.set_display_size(video['Resolution Index'])
            self.set_vsync_mode(video['Vsync'])

        except KeyError as e:
            print(f'Configuração de vídeo não encontrada: {e}')
            bge.logic.endGame()
