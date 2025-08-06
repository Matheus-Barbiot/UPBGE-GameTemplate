#icon=COLOR
import bge
from Settings import Settings
from collections import OrderedDict

class VisualSettings(bge.types.KX_PythonComponent):
    args = OrderedDict([
    ])

    def start(self, args):
        bge.logic.loadGlobalDict()
        self.screen_list = Settings().sizes_list
        
        self.text_objects = {
            'screen': self.object.scene.objects.get('Txt_size'),
            'display': self.object.scene.objects.get('Txt_display'),
            'vsync': self.object.scene.objects.get('Txt_vsync'),
            'volume': [
                {'object': self.object.scene.objects.get('Txt_general'), 'key': 'General'},
                {'object': self.object.scene.objects.get('Txt_music'), 'key': 'Music'},
                {'object': self.object.scene.objects.get('Txt_fx'), 'key': 'Fx'},
            ]
        }
        
        self.visual_funcs = {            
            'screen': self.set_screen_text,
            'display': self.set_display_text,
            'vsync': self.set_vsync_text,
            'volume': self.set_volume_text,
            'all': self.set_visuals
        }

        
            
        self.set_visuals()

        pass

    def set_screen_text(self):
        obj = self.text_objects['screen']
        index = bge.logic.globalDict['Settings']['Video']['Screen Size']
        current = self.screen_list[index]
        
        string = f'{current[0]}x{current[1]}'
        obj['Text'] = string

    def set_display_text(self):
        obj = self.text_objects['display']
        value = bge.logic.globalDict['Settings']['Video']['Display Mode']
        obj['Text'] = 'FullScreen' if value else 'WideScreen'

    def set_vsync_text(self):
        obj = self.text_objects['vsync']
        value = bge.logic.globalDict['Settings']['Video']['Vsync']
        obj['Text'] = 'Vsync on' if value else 'Vsync off'

    def set_volume_text(self):
        for item in self.text_objects['volume']:
            value = bge.logic.globalDict['Settings']['Audio'][item['key']]
            percent = int((value * 100) // 2)
            item['object']['Text'] = f'{percent}%'

    def set_visuals(self):
        for key, func in self.visual_funcs.items():
            if key == 'all':
                return
            
            func()
        
    def update(self):
        visual = self.object.get('set visual')
        if not visual or visual == '':
            return
        
        for key, func in self.visual_funcs.items():
            if visual == key:
                func()
                self.object['set visual'] = ''
                return
        
        print(visual, 'não entendido')
        pass

