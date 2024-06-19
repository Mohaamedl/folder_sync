from Guiao3.Stack import Stack
from armazem import Armazem
class Comboio:
    def __init__(self,list):
        self._origem = ''
        self._destino = ''
        self._locomotiva = Locomotiva()
        self._listaVagoes = Stack()
        for i in list:
            self._listaVagoes.push(Vagao(i))
    def __str__(self):
        s = 'Comboio com ' + str(self._listaVagoes.size())+' vagoes\n'
        l =Stack()
        j=self._listaVagoes.size()
        for i in range(j):
            vagao = self._listaVagoes.top()
            l.push(vagao)
            s += vagao.__str__() +'\n'
            self._listaVagoes.pop()
        self._listaVagoes = l
        return s
    def carregar(self,armz): # processo de carregamento começa 
        lista = armz.getListaMercadorias()
        listaVag = []
        j=self._listaVagoes.size()
        for i in range(j): # lista com vagoes listados com o primeiro sendo o mais proximo da locomotiva
            listaVag.insert(0,self._listaVagoes.top())
            self._listaVagoes.pop()
            
        self._listaVagoes.clear()
        l = lista.copy()
        for vagao in listaVag:
            for item in lista:
                if vagao._capAt >= item._peso:# se o vagao estiver cheio quebra para seguir ao proximo
                    vagao.addItem(item) # se nao, adiciona e remove da lista do que ha para adicionar
                    l.remove(item)
            lista = l.copy()
            self._listaVagoes.push(vagao) # cola-se o vagao ao comboio
        armz.setListaMercadorias(l) # nova lista de mercadorias, com o que sobrou





    def fazerViagem(self,origem,destino):
        self._origem = origem
        #... vrom vromm
        self._destino = destino
    
    
    
    def descarregar(self):
        arm = Armazem(self._destino)
        #print(self._listaVagoes.size())
        while self._listaVagoes.size()!=0:
            vagao = self._listaVagoes.top() # pega o ultimo vagao do comboio
            for it in vagao._items:
                arm._listaMercadorias.append(it)
            vagao.vagClear() # tira os itens
            self._listaVagoes.pop() # e o desconecta do comboio para pegar o proximo
        print(arm) # mostra

class Vagao:
    _id = 10000
    def __init__(self,capMax):
        self._items = []
        self._capMax = capMax*1000
        self._capAt = self._capMax
        self._id = Vagao._id
        Vagao._id +=1

    def __str__(self):
        s=''
        for i in self._items:
            s+=i.__str__()+' ; '
        return f'Vagao {self._id}: capacidade max : {self._capMax} kg: capacidade atual: {self._capAt} kg: Mercadorias: {s}'

    def addItem(self,item):
        t = True
        if self._capAt >= item._peso:
            self._items.append(item)
            self._capAt-= item._peso
            t = False
        return t
    

    def vagClear(self):
        self._items = []
        self._capAt = self._capMax






class Locomotiva:
    _id  = 10090
    def __init__(self):
        self._cor = ''
        self._matricula = '' # pode-se se desencolver ou usar um metodo para verificar se essa matricula existe como nas classes dos veiculos
        self._id = Locomotiva._id
        Locomotiva._id +=1
        # ...etc
    def __str__(self):
        return f'Locomotiva  {self._id}: cor - {self._cor}: matricula: {self._matricula}'