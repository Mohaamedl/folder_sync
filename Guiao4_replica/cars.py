from abc import ABC

class Vehicle(ABC):
    def __init__(self,brand:str,model:str,plateNum:str,maxSpeed:int):
        self._brand = brand 
        self._model = model
        self._maxSpeed = maxSpeed
        self._plateNum = plateNum # acrescentar um metodo de verificação de validade de matricula
        self._available = True
    
    def __str__(self):
        return f'Brand : {self._brand} {self._model}, plate number : {self._plateNum} '
    def rent(self):
        try:
            if self._available == False:
                raise Exception('Not available')
            self._available = False

        except Exception as e:
            print(self.getBrand(),self.getModel,e)
    def devolution(self):
        try:
            if self._available == True:
                raise Exception('already available')
            self._available = True

        except Exception as e:
            print(self.getBrand(),self.getModel,e)
    def detType(self):
        pass


    def getBrand(self):
        return self._brand
    

    def getModel(self):
        return self._Model
    

    def getPlateNum(self):
        return self._plateNum




class EletricVehicle(Vehicle):
    def __init__(self,brand:str,model:str,plateNum:str,maxSpeed:int):
        super().__init__(brand,model,plateNum,maxSpeed)
        self._type = "Eletric"


    def getType(self):
        return self._type



class DieselVehicle(Vehicle):
    def __init__(self,brand:str,model:str,plateNum:str,maxSpeed:int):
        super().__init__(brand,model,plateNum,maxSpeed)
        self._type = "Diesel"


    def getType(self):
        return self._type




class GasolineVehicle(Vehicle):
    def __init__(self,brand:str,model:str,plateNum:str,maxSpeed:int):
        super().__init__(brand,model,plateNum,maxSpeed)
        self._type = "Gasoline"

    
    def getType(self):
        return self._type
    
