import taichi as ti
import numpy as np
import time

ti.init(arch=ti.gpu)
ti.init(device_memory_GB=0.1)

gui = ti.GUI("TaichiGUI", res=(800, 800), background_color=0x00456B)

# 添加滑块
slider_value = gui.slider("slide", 0, 300, 1)
slider_value.value = 50

while True:
    if gui.get_event(ti.GUI.ESCAPE):
        break
    gui.circle(pos=(0.5, 0.5), color=0xFF0000, radius=slider_value.value)
    gui.show()