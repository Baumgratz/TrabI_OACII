def parser(lista):
    string=[]

    #classe J
    if(lista[:6]=='000010'):
        string.append('j ')
        string.append(hex(int(lista[6:],2)))
    elif(lista[:6]=='000011'):
        string.append('jal ')
        string.append(hex(int(lista[6:],2)))

    #classe I
    elif(lista[:6]=='100000'):
        string.append('lb')
        string.append(padraoI1(lista))
    elif(lista[:6]=='101000'):
        string.append('sb')
        string.append(padraoI1(lista))
    elif(lista[:6]=='100011'):
        string.append('lw')
        string.append(padraoI1(lista))
    elif(lista[:6]=='101011'):
        string.append('sw')
        string.append(padraoI1(lista))
    elif(lista[:6]=='000001'):
        string.append('bgez')
        string.append(padraoI2(lista))
    elif(lista[:6]=='000111'):
        string.append('bgtz')
        string.append(padraoI2(lista))
    elif(lista[:6]=='001000'):
        string.append('bgt')
        string.append(padraoI2(lista))

    # classe R
    if(lista[:6]=='000000'):
        if(lista[26:]=='001000'):
            string.append('jr')
            string.append(' $')
            string.append(regMIPs(lista[6:11]))
        elif(lista[26:]=='100000'):
            string.append('add')
            string.append(padraoR1(lista))
        elif(lista[26:]=='100010'):
            string.append('sub')
            string.append(padraoR1(lista))
        elif(lista[26:]=='100101'):
            string.append('or')
            string.append(padraoR1(lista))
        elif(lista[26:]=='101010'):
            string.append('slt')
            string.append(padraoR1(lista))
        elif(lista[26:]=='010100'):
            string.append('li')
    	    string.append(' $')
            string.append(regMIPs(lista[16:21]))
            string.append(', ')
            string.append(regMIPs(lista[6:11]))
        elif(lista[26:]=='010101'):
            string.append('la')
    	    string.append(' $')
            string.append(regMIPs(lista[16:21]))
            string.append(', ')
            string.append(hex(int(lista[6:11],2)))
        elif(lista[26:]=='010110'):
            string.append('move')
            string.append(' $')
            string.append(regMIPs(lista[16:21]))
            string.append(', $')
            string.append(regMIPs(lista[6:11]))

    string = ''.join(string)
    return string

def padraoI1(lista):
    string = []

    string.append(' $')
    string.append(regMIPs(lista[11:16]))
    string.append(', ')
    string.append(str(int(lista[16:],2)))
    string.append(' ($')
    string.append(regMIPs(lista[6:11]))
    string.append(')')

    string = ''.join(string)
    return string

def padraoI2(lista):
    string = []

    string.append(' $')
    string.append(regMIPs(lista[6:11]))
    string.append(', ')
    string.append(hex(int(lista[16:],2)))

    string = ''.join(string)
    return string

def padraoR1(lista):
    string = []

    string.append(' $')
    string.append(regMIPs(lista[16:21]))
    string.append(', $')
    string.append(regMIPs(lista[6:11]))
    string.append(', $')
    string.append(regMIPs(lista[11:16]))

    string = ''.join(string)
    return string

def regMIPs(reg):
    num = int(reg,2)
    string = []
    if(num == 0):
        string = '0'
    elif(num == 1):
        string = 'at'
    elif(num==2 or num ==3):
        num = num - 2
        string = 'v'+ (str(num))
    elif(num>3 and num<8):
        num = num - 4
        string = 'a'+ (str(num))
    elif(num>7 and num<16):
        num = num - 8
        string = 't'+ (str(num))
    elif(num>15 and num<24):
        num = num - 16
        string = 's'+ (str(num))
    elif(num==24 or num==25):
        num = num - 16
        string = 't'+ (str(num))
    elif(num ==26 or  num ==27):
        num = num - 26
        string = 'k'+ (str(num))
    elif(num==28):
        string = 'gp'
    elif(num==29):
        string = 'sp'
    elif(num==30):
        string = 'fp'
    elif(num==31):
        string = 'ra'
    return string
