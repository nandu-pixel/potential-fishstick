import numpy as np
from OpenGL.GL import *
import OpenGL.GL.shaders
import random
import os

VERT_SHADER = os.path.join("shaders", "vertex.glsl")
FRAG_SHADER = os.path.join("shaders", "fragment.glsl")

class ParticleSystem:
    def __init__(self, max_particles):
        self.max_particles = max_particles
        self.positions = np.zeros((max_particles, 2), dtype=np.float32)
        self.velocities = np.zeros((max_particles, 2), dtype=np.float32)
        self.colors = np.ones((max_particles, 4), dtype=np.float32)
        self.lifetimes = np.zeros(max_particles, dtype=np.float32)

        self.shader = self.load_shader(VERT_SHADER, FRAG_SHADER)
        self.vbo = glGenBuffers(1)

        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.positions.nbytes, self.positions, GL_DYNAMIC_DRAW)

    def load_shader(self, vert_path, frag_path):
        with open(vert_path) as v, open(frag_path) as f:
            vs = OpenGL.GL.shaders.compileShader(v.read(), GL_VERTEX_SHADER)
            fs = OpenGL.GL.shaders.compileShader(f.read(), GL_FRAGMENT_SHADER)
        return OpenGL.GL.shaders.compileProgram(vs, fs)

    def spawn_burst(self, x, y):
        for i in range(self.max_particles):
            self.positions[i] = [(x / 400.0 - 1.0), -(y / 300.0 - 1.0)]
            angle = random.uniform(0, 2 * np.pi)
            speed = random.uniform(0.2, 1.0)
            self.velocities[i] = [np.cos(angle) * speed, np.sin(angle) * speed]
            self.colors[i] = [random.random(), random.random(), random.random(), 1.0]
            self.lifetimes[i] = random.uniform(1.5, 3.0)

    def update(self, dt):
        alive = self.lifetimes > 0
        self.positions[alive] += self.velocities[alive] * dt
        self.lifetimes[alive] -= dt
        self.colors[alive, 3] = self.lifetimes[alive] / 3.0  # Fade out

    def render(self):
        glUseProgram(self.shader)
        glEnableVertexAttribArray(0)

        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferSubData(GL_ARRAY_BUFFER, 0, self.positions.nbytes, self.positions)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, None)

        glDrawArrays(GL_POINTS, 0, self.max_particles)

        glDisableVertexAttribArray(0)
        glUseProgram(0)
