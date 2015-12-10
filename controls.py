ULAfunct = {'100000':'0010','100010':'0110',
            '100100':'0000','100101':'0001',
            '101010':'0111'}

bancReg = {}

def preencheMemReg() :
    for i in range(0,32) :
        bancReg[i] = '00000000000000000000000000000000'
        # print str(i) + ' = ' + str(bancReg[i])
    return bancReg

def mux2(i0,i1,cod) :
    if(int(cod,2) == 0) :
        return i0
    return i1

def mux4(i0,i1,i2,i3,cod) :
    if(int(cod,2) == 0) :
        return i0
    if(int(cod,2) == 1) :
        return i1
    if(int(cod,2) == 2) :
        return i2
    return i3

def mux3(i0,i1,i2,cod) :
    return mux4(i0,i1,i2,0,cod)

def extend(num, tam) :
	b = str(bin(num))[2:]
	n = len(b)
	for i in range(0,tam-n) :
		b = '0' + b
	return b

def shift2(address):
    return address + '0' + '0'

def Add(i0,i1) :
    return i0 + i1

def ULAcontrol(funct, ULAop) :
    if(ULAop == '00') :
        return '0000'
    if(ULAop == '01') :
        return '0110'
    if(ULAop == '10') :
        return ULAfunct[funct]

def andB(i0,i1) :
    result = ''
    i = 31
    while i >= 0 :
        if (i0[i] == '0') | (i1[i] == '0') :
            result = '0' + result
        else :
            result = '1' + result
        i = i - 1
    return result

def orB(i0,i1) :
    result = ''
    i = 31
    while i >= 0 :
        if (i0[i] == '0') & (i1[i] == '0') :
            result = '0' + result
        else :
            result = '1' + result
        i = i - 1
    return result
