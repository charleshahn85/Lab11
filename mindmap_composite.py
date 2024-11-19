from mindmap_leaf import MindMapLeaf
import os

class MindMapComposite:
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def __str__(self):
        return self.get_shape_representation().format(self.name)

    def display(self, indent=0):
        print(" " * indent + str(self))
        for child in self.children:
            child.display(indent + 2)

    def get_shape_representation(self):
        shapes = {
            "circle": "(({}))",
            "oval": "({})",
            "square": "[{}]",
            "cloud": "){}(",
            "hexagon": "{{{{{}}}}}",
            "bang": ")){}(("
        }
        return shapes.get(self.shape, "{}")

