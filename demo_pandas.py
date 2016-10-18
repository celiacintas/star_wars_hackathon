#!/usr/bin/env python2


from panda3d.core import WindowProperties, TextNode
from direct.task.TaskManagerGlobal import taskMgr
from direct.gui.OnscreenText import OnscreenText
from direct.task import Task
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Filename, AmbientLight, DirectionalLight

import sys

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.base = self
        self.setup()

    def setup(self):
        self.model = self.loader.loadModel("models/tyderium.egg")
        self.model.setScale(0.001)
        self.model.reparentTo(self.render)

        self.cam.setPos(0, -5, 0)
        self.cam.lookAt(0, 0, 0)

        self.ambientLight = AmbientLight("ambientLight")
        self.ambientLight.setColor((.2, .2, .3, 1))
        self.directionalLight = DirectionalLight("directionalLight")
        self.directionalLight.setDirection((-5, -5, -5))
        self.directionalLight.setColor((1, 1, 1, 1))
        self.directionalLight.setSpecularColor((1, 1, 1, 1))
        self.render.setLight(self.render.attachNewNode(self.ambientLight))
        self.render.setLight(self.render.attachNewNode(self.directionalLight))

app = App()
app.run()
