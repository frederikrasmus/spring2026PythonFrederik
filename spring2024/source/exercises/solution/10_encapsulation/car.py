# car.py (solution)

# 1. Car object
# Create a Car class. 
# When instanciated the object should be able to take 4 attributes (Make, Model, bhp, mph).
# They all 4 should be properties.

db = {
    "Audi": {"A3", "A4", "A6", "Q5", "Q7"},
    "BMW": {"3 Series", "5 Series", "7 Series", "X3", "X5"},
    "Mercedes-Benz": {"C-Class", "E-Class", "S-Class", "GLC", "GLE"},
    "Volkswagen": {"Golf", "Passat", "Polo", "Tiguan", "Arteon"},
    "Volvo": {"S60", "S90", "V60", "XC60", "XC90"},
    "Toyota": {"Corolla", "Camry", "RAV4", "Prius", "Hilux"},
    "Honda": {"Civic", "Accord", "CR-V", "Fit", "HR-V"},
    "Ford": {"Focus", "Fiesta", "Mustang", "Escape", "Explorer"},
    "Nissan": {"Altima", "Rogue", "Sentra", "Maxima", "Murano"},
    "Mazda": {"Mazda3", "Mazda6", "CX-5", "CX-9", "MX-5"}
}


class Car:
    def __init__(self, make, model, bhp, mph):
        self.make = make
        self.model = model
        self.bhp = bhp
        self.mph = mph

    # make
    @property 
    def make(self):
        return self._make
    
    @make.setter
    def make(self, make):
        if make not in db.keys():
            raise ValueError('Make is not in valid list')
        self._make = make

    # model
    @property 
    def model(self):
        return self._model
    
    @model.setter
    def model(self, model):
        if model not in db[self.make]: 
            raise ValueError(f'No model named {model} belongs to {self.make}')
        self._model = model
    
    # bhp
    @property 
    def bhp(self):
        return self._bhp
    
    @bhp.setter
    def bhp(self, bhp):
        if bhp < 0:
            raise ValueError('bhp can not be negative')
        self._bhp = bhp

    # mph
    @property 
    def mph(self):
        return self._mph
    
    @mph.setter
    def mph(self, mph):
        if mph < 0:
            raise ValueError('mph can not be negative')
        self._mph = mph

