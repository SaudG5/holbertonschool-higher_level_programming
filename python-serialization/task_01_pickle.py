import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

S1 = CustomObject("Jhon", 25, True)

def serialize(self, filename):
    with open(filename, "wb") as file:
        pickle.dump(self, file)


def deserialize(filename):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except Exception:
        return None
