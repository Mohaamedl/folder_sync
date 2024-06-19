
class Agency:
    
    def __init__(self,name:str,address:str,listAccommodation = [],listVehicles = []):
        self._name = name
        self._address = address
        self._listAccommodation = listAccommodation
        self._listVehicles = listVehicles

    def __str__(self):
        return f'{self._name} in {self._address} - accommodations: \n'+self.getAccommodations()+'Vehicles :\n'+self.getVehicles()

    def addAccomodation(self,acc):
        self._listAccommodation.append(acc)
    def addVehicle(self,veh):
        self._listVehicles.append(veh)
    def rentVehicle(self,brand,model,plateNum):
        for car in self._listVehicles:
            if car._brand == brand and car._model == model  and car._plateNum ==plateNum:
                car.rent()
    def devolutionVehicle(self,brand,model,plateNum):
        for car in self._listVehicles:
            if car._brand == brand and car._model == model  and car._plateNum ==plateNum:
                car.devolution()
    def rentAccomodation(self,name,address):
        for acc in self._listAccommodation:
            if acc._name == name and acc._local == address:
                acc.checkIn()
    def checkoutAccomodation(self,name,address):
        for acc in self._listAccommodation:
            if acc._name == name and acc._local == address:
                acc.checkOut()
    def getAccommodations(self):
        s = ''
        for e in self._listAccommodation:
            s+=e.__str__()+'\n'
        return s
        
    def getVehicles(self):
        s = ''
        for e in self._listVehicles:
            s+=e.__str__()+'\n'
        return s


