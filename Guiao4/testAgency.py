from agency import *
from accommodation import *
from cars import *

'''Criação  dos  diversos  objetos  referidos  acima
   Simulação de algumas  operações  de  reserva  e  entrega 
   Impressão, no final, da informação atual sobre a agência '''
def main():

    # criar uma agência
    agencia = Agency("MyTravel","Aveiro")

    # adcionar alguns apartamentos   
    apartamentos = [Apartment("T4","Aveiro",1500,5,4), Apartment ("T3","Albufeira",900,5,3), Apartment ("T3","Lisboa",1000,5,3) ] # adicionei avaliação (4º argumento)
    apartamentos[0].checkIn()
    for ap in apartamentos:
        agencia.addAccomodation(ap) 
        

    # adicionar alguns quartos de hotel
    quartos  = [Room ("Quarto 23","Hotel Américas (Aveiro)",200,5,"double"), Room ("Quarto 2","Hotel Imperial (Aveiro)",100,5,"single")]
    quartos[1].checkIn()
    for quarto in quartos:
        agencia.addAccomodation(quarto) 
    
    # adicionar algumas viaturas
    viaturas = [EletricVehicle("Tesla", "X","OF-04-90",200), DieselVehicle("VW", "Golf", "AA-11-AA", 100), GasolineVehicle("VW", "Golf", "AA-12-AA", 120)] 
    for viatura in viaturas:
        agencia.addVehicle(viatura)

    # processamento ao nível da agência do aluguer de viaturas
    agencia.rentVehicle("Tesla","X","OF-04-90")
    agencia.rentVehicle("Tesla","Y","FF-14-09")
    
    
    # processamento ao nível da agência do aluguer de alojamentos
    agencia.rentAccomodation("T4","Aveiro")
    agencia.rentAccomodation("Quarto 23","Hotel Américas (Aveiro)")
    agencia.rentAccomodation("Quarto 24","Hotel Américas (Aveiro)")

    # processamento ao nível da agência do ckeckout de um alojamento
    agencia.checkoutAccomodation("T4","Aveiro")
    
    # processamento ao nível da agência da devolução de um carro que se encontrava alugado
    agencia.devolutionVehicle("Tesla", "X","OF-04-90")
    
    # mostrar informação sobre todos alojamentos e viaturas da agência
    print("\n----------------------")
    print(agencia)

 

if __name__ == "__main__":
    main()
