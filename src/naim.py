import os
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Filename
from time import time
class MyApp(ShowBase):
    def __init__(self):
        super().__init__()
        self.setBackgroundColor(0, 0, 0)
        model_path = os.path.join("assets", "model", "12221_Cat_v1_l3.obj")
        texture_path = os.path.join("assets", "model", "Cat_diffuse.jpg")
        self.obj = self.loader.loadModel(Filename(model_path))
        self.obj.reparentTo(self.render)
        self.obj.setScale(0.4, 0.4, 0.4)
        texture = self.loader.loadTexture(Filename(texture_path))
        self.obj.setTexture(texture)
        self.obj.setPos(0, 0, 0)  
        self.camera.setPos(0, -70, 35)  
        self.camera.lookAt(self.obj)  
        self.disableMouse()
        self.taskMgr.add(self.spin_task, "spin_task")
        sound_path = os.path.join("assets", "Cat_sounds.mp3")
        self.background_sound = self.loader.loadSfx(Filename(sound_path))  
        self.last_played_time = time()
        self.taskMgr.add(self.sound_loop_task, "sound_loop_task")
    def spin_task(self, task):
        self.obj.setH(self.obj.getH() + 2)  
        self.obj.setP(self.obj.getP() + 0.9)  
        self.obj.setR(self.obj.getR() + 0.7)  
        return task.cont  
    def sound_loop_task(self, task):
        if time() - self.last_played_time >= 0.6:
            if not self.background_sound.status() == self.background_sound.PLAYING:
                self.background_sound.play()  
            self.last_played_time = time()  
        return task.cont  

app = MyApp()
app.run()
