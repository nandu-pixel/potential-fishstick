import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
from particle_system import ParticleSystem

def main():
    glfw.init()
    window = glfw.create_window(800, 600, "GPU Particle System", None, None)
    glfw.make_context_current(window)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE)  # Additive blending

    ps = ParticleSystem(1000)
    last_time = glfw.get_time()

    def mouse_callback(window, button, action, mods):
        if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
            x, y = glfw.get_cursor_pos(window)
            ps.spawn_burst(x, y)

    glfw.set_mouse_button_callback(window, mouse_callback)

    while not glfw.window_should_close(window):
        current_time = glfw.get_time()
        delta = current_time - last_time
        last_time = current_time

        glClear(GL_COLOR_BUFFER_BIT)
        ps.update(delta)
        ps.render()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
