from models.class_model import FitnessClass

class ClassRepository:

    def __init__(self):
        self.classes = []

    def save(self, fitness_class):
        self.classes.append(fitness_class)

    def find_all(self):
        return self.classes