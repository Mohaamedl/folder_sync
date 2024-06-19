class Accommodation:
    _id = 101
    def __init__(self,name:str,local:str,pricePerNight:float,evaluation:float,availability=True):
        try:
            if pricePerNight<0:
                raise ValueError('No negative price')
            elif 0 > evaluation or evaluation>5 :
                raise Exception('Evaluation not valid') 
            self._id = self.__class__._id
            self.__class__._id +=1
            self._name = name
            self._local = local
            self._pricePerNight = pricePerNight
            self._evaluation = evaluation
            self._availability = availability
        except Exception as e:
            print(e)
        except ValueError as va:
            print(va)
    
    def __str__(self):
        return f'id : {self._id}, name : {self._name}, local : {self._local}, Price per night : {self._pricePerNight}, evaluation : {self._evaluation}, available : '+("Yes" if self._availability else 'No')
    
    
    def getId(self):
        return self._id
    
    def getName(self):
        return self._name
    
    def getLocal(self):
        return self._local
    
    def getPricePerNight(self):
        return self._pricePerNight
    
    def getEvaluation(self):
        return self._evaluation
    
    def getAvailability(self):
        return self._availability
    

    #def setPricePerNight(self,newPrice):
        #self._pricePerNight = newPrice

    def setAvailability(self,newStatus):
        self._availability = newStatus 

    #def setName(self,newName): #pode mudar de nome(?)
        #self._name = newName

    #def setEvaluation(self,newEV):
        #self._evaluation = newEV
    
    def checkIn(self):
        try:
            if self._availability==False:
                raise Exception("Not available")
            self._availability = False
        except Exception as e :
            print(self.getName,e)
    
    def checkOut(self):
        try:
            if self._availability==True :
                raise Exception("Already available")
            self._availability = True
        except Exception as e :
            print(self.getName,e)
    


class Apartment(Accommodation):
    def __init__(self,name:str,local:str,pricePerNight:float,evaluation:float,numRooms:int,availability=True):
        try:
            if numRooms <0:
                raise Exception('Negative number of rooms not exist. (yet)')
            super().__init__(name,local,pricePerNight,evaluation,availability)
            self._numRooms = numRooms
        except Exception as e:
            print(e)
    def __str__(self):
        return f'Apartment with {self._numRooms} rooms, Details: '+super().__str__()
    def getNumRooms(self):
        return self._numRooms
class Room(Accommodation):
    
    _typeList = ['single','double','twin','triple']
    
    def __init__(self,name:str,local:str,pricePerNight:float,evaluation:float,type:str,availability=True):
        try:
            if not self.__class__._typeList.__contains__(type):
                raise Exception("This type of room do not exist here.")
            super().__init__(name,local,pricePerNight,evaluation,availability)
            self._type = type

        except Exception as e:
            print(e)
    def __str__(self):
        return f'{self._type} Room, Details: ' +super().__str__()
    def getType(self):
        return self._type