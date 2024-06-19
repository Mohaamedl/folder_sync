from armazem import Armazem
from mercadorias import Mercadoria
from comboio import Comboio

# imports random module
import random
import numpy as np

def main():
    origem = "Aveiro"
    destino = "Lisboa"
    armazem_origem = Armazem(origem)
    
    # receber mercadorias - Mercadoria tem designação, peso (Kg) e proprietário
    armazem_origem.receber(Mercadoria("Mercedes 200",3000,"Automotor"))   
    armazem_origem.receber(Mercadoria("Renault Twingo",2000,"XPTZ"))
    armazem_origem.receber(Mercadoria("BMW",4000,"XPTZ"))
    armazem_origem.receber(Mercadoria("Peças auto",7000,"XPTZ"))
    armazem_origem.receber(Mercadoria("Parafusos",4000,"CP CARGO"))
    armazem_origem.receber(Mercadoria("Cereais",4000,"CP CARGO"))
    armazem_origem.receber(Mercadoria("Motos",5000,"APRILIA"))
    print(armazem_origem)

    # criar comboio com 3 vagões, todos com carga máxima de 10 toneladas
    #comboio = Comboio([10, 10, 10])
    
    # outro comboio
    comboio = Comboio([12, 11,11])
    
    # comboio com configuração aleatória (até 20 carruagens de 2 a 15 toneladas)
    #num_vagoes = random.randint(3,7)
    #lista = np.random.randint(13, size=(num_vagoes)).__add__(3).tolist()
    #comboio = Comboio(lista)

    # carregar comboio com o que está em armazém
    comboio.carregar(armazem_origem)
    
    # descomentar para mostra comboio (chama __str__())
    print(comboio)

    # fazer viagem 
    comboio.fazerViagem(origem, destino)
    
    # descarregar no destino
    comboio.descarregar()  # descarrega e mostra
 
    # mostrar o que ficou por enviar
    print(armazem_origem)


if __name__ == "__main__":

    main()
