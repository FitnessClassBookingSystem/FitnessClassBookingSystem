from models.class_model import FitnessClass
from repositories.class_repository import ClassRepository

class ClassService:

    def __init__(self, class_repository):
        self.class_repository = class_repository

    def create_class(self, id, title, instructor, capacity):
        fitness_class = FitnessClass(
            id, title, instructor, capacity)

        self.class_repository.save(fitness_class)

        return fitness_class

    def get_all_classes(self):
        return self.class_repository.find_all()