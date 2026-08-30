import unittest

from models.class_model import FitnessClass
from repositories.class_repository import ClassRepository
from services.class_service import ClassService


class MyTestCase(unittest.TestCase):

    def test_to_create_class_service(self):
        repository = ClassRepository()
        service = ClassService(repository)

        fitness_class = service.create_class(
            1,
            "Morning Yoga",
            "Fitness Master",
            30
        )

        self.assertEqual(fitness_class.title, "Morning Yoga")
        self.assertEqual(fitness_class.instructor, "Fitness Master")
        self.assertEqual(fitness_class.capacity, 30)

    def test_get_all_classes_service(self):
        repository = ClassRepository()
        service = ClassService(repository)

        class1 = FitnessClass(
            1,
            "Morning Yoga",
            "Fitness Master",
            35
        )

        class2 = FitnessClass(
            2,
            "Evening Yoga",
            "Fitness Mistress",
            15
        )

        repository.save(class1)
        repository.save(class2)

        classes = service.get_all_classes()

        self.assertIn(class1, classes)
        self.assertIn(class2, classes)


if __name__ == '__main__':
    unittest.main()