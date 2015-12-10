import controls

instrucao = {}

def preencheMemInst(lista) :
    for i in range(0,len(lista)-1) :
        lista[i] = lista[i].replace('\n','')
        instrucao[i*4] = lista[i]
    return instrucao

def pMI(lista):
    instrucao = preencheMemInst(lista)

def Reg(r1,r2,rw,dw,EscReg) :
    r1 = int(r1,2)
    r2 = int(r2,2)
    rw = int(rw,2)
    if(EscReg == 1) :
        bancReg[rw] = dw
    out1 = bancReg[r1]
    out2 = bancReg[r2]
    return [out1,out2]

def ULA(i0,i1,cod) :
    zero = '0'
    if(i0-i1 == 0) :
        zero = '1'
    if(cod == '0000') :
        result = andB(i0, i1)
        return [zero, result]
    if(cod == '0001') :
        result = orB(i0, i1)
        return [zero, result]
    if(cod == '0010') :
        result = i0 + i1
        return [zero, result]
    if(cod == '0110') :
        result = i0 - i1
        return [zero, result]
    if(cod == '0111') :
        result = i0 <= i1
        return [zero, result]

def memInst(pc) :
    # pc e mult de 4
    return instrucao[pc]
