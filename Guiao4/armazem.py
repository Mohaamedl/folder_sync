class Armazem:
    def __init__(self,local):
        self._local = local
        self._listaMercadorias = []
    
    def __str__(self):
        s = 'Armazem: '+str(self._local)+'\n'
        if len(self._listaMercadorias)==0:
            s+='Vazio'
        else:
            for e in self._listaMercadorias:
                s+=str(e)+'\n'
        
        return s
    def receber(self,merc):
        self._listaMercadorias.append(merc)
    def getListaMercadorias(self):
        return self._listaMercadorias
    def setListaMercadorias(self,lista):
        self._listaMercadorias = lista