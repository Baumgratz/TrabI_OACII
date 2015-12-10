import instrucoes
import codificador
import mips

nameArquivo = 'betaTeste.asm'

arquivo=open(nameArquivo,'r')

lista = arquivo.readlines()
mips.pMI(lista)
# for i in range(0,len(lista)-1) :
#     lista[i] = lista[i].replace('\n','')
#     ls = codificador.parser(lista[i])
    # ins = instrucoes.parser(ls)
    # print lista[i]
    # print ins
    # if lista[i] != ins :
    #     print 'ERRO!!!'
arquivo.close()
