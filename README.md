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

## 🧾 Function Signature

```python
def hasCircularDependency(n: int, edges: List[List[int]]) -> bool
