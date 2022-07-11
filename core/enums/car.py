import enum


class CarType(enum.Enum):
    SEDAN = 'Sedan'
    COUPE = 'Coupe'
    CROSSOVER = 'Crossover'
    HATCHBACK = 'Hatchback'
    MINIVAN = 'Minivan'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)