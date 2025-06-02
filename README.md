# potential-fishstick
# N-Queens Solver

This repository contains a Python solution to the classic **n-Queens puzzle**, where the goal is to place `n` queens on an `n x n` chessboard so that no two queens attack each other.

## Problem Statement

Given an integer `n`, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration, where:
- `'Q'` indicates a queen
- `'.'` indicates an empty space

# Circular Dependency Checker

This project contains a Python solution to detect circular dependencies in a module dependency graph, which is crucial in large software systems for safe module loading.

##  Problem Statement

Given `n` modules and a list of dependency relationships between them, determine whether the dependency graph contains a cycle.

- Each module is labeled from `0` to `n - 1`.
- A directed edge from `a` to `b` means module `a` depends on module `b`.

A cycle in the dependency graph would mean circular loading dependencies, which must be avoided.



# 🎆 GPU-Accelerated Particle System (Python + OpenGL)

This project is a GPU-accelerated particle system implemented in Python using **PyOpenGL** and **GLFW**. It simulates a fireworks display or magical energy burst with real-time performance, using shaders and GPU buffers for efficient rendering.

## 🚀 Features

✅ **Particle System Basics**
- Particles spawn from a central point or burst area
- Each particle has:
  - Position
  - Velocity
  - Color (changes over time)
  - Lifetime (fades out)

✅ **Shader Usage**
- Uses vertex and fragment shaders (GLSL)
- Additive blending for glowing effects
- GPU-based rendering using point sprites

✅ **Animation**
- Particles move with velocity and optional gravity
- Smooth color and opacity transitions

✅ **Interactivity**
- Click to trigger a new particle burst at mouse position
- Easily customizable controls (e.g., for particle count, gravity)

✅ **Performance**
- Efficiently handles 1000+ particles
- Uses Vertex Buffer Objects (VBOs) for GPU acceleration

---

## 🧪 Demo Preview

> **Run the app** and click to trigger bursts of colorful particles.
> Handles hundreds of dynamic particles in real-time.

---

## 📦 Installation

### 🐍 Requirements

- Python 3.8+
- `PyOpenGL`
- `glfw`
- `numpy`

Install dependencies:

```bash
pip install PyOpenGL glfw numpy
