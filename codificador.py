
regs = { '$0':'00000','$at':'00001','$v0':'00010','$v1':'00011','$a0':'00100',
		'$a1':'00101','$a2':'00110','$a3':'00111','$t0':'01000','$t1':'01001',
		'$t2':'01010','$t3':'01011','$t4':'01100','$t5':'01101','$t6':'01110',
		'$t7':'01111','$s0':'10000','$s1':'10001','$s2':'10010','$s3':'10011',
		'$s4':'10100','$s5':'10101','$s6':'10110','$s7':'10111','$t8':'11000',
		'$t9':'11001','$k0':'11010','$k1':'11011','$gp':'11100','$sp':'11101',
		'$fp':'11110','$ra':'11111'}

fun = {'add':'100000','sub':'100010',
	   'and':'100100', 'or':'100101',
	   'slt':'101010', 'jr':'001000'}

opI = {'beq':'000100','bne':'000101','addi':'001000','lw':'100011','sw':'101011'}

tam = {'beq':3,'bne':3,'addi':4,'lw':2,'sw':2}

opJ = {'j':'000010','jal':'000011'}

def extend(num, tam) :
	b = str(bin(num))[2:]
	n = len(b)
	for i in range(0,tam-n) :
		b = '0' + b
	return b

def parser(lista):
	ls = lista.replace('(',' ').replace(')','').replace(',','').split()
	string = []
	try :
		return parserI(ls)
	except KeyError :
		try :
			return parserR(ls)
		except KeyError:
			return parserJ(ls)

def parserJ(ls):
	op = opJ[ls[0]]
	j = extend(int(ls[1],16),26)
	return op + j

def parserR(ls):
	string = '000000'
	shamt = '00000'
	f = fun[ls[0]]
	if ls[0] == 'jr' :
		r = regs[ls[1]]
		a = extend(0,15)
		return string + r + a + f
	rd = regs[ls[1]]
	rs = regs[ls[2]]
	rt = regs[ls[3]]
	return string + rs + rt + rd + shamt + f

def parserI(ls) :
	string = opI[ls[0]]
	if(tam[ls[0]] == 2) :
		rt = regs[ls[1]]
		address = extend(int(ls[2],10),16)
		rs = regs[ls[3]]
		return string + rs + rt + address
	if(tam[ls[0]] == 4) :
		rt = regs[ls[1]]
		rs = regs[ls[2]]
		imt = extend(int(ls[3],16),16)
		return string + rs + rt + imt

	rs = regs[ls[1]]
	rt = regs[ls[2]]
	address = extend(int(ls[3],16),16)
	return string + rs + rt + address
	# subi ?????

# lw = 'lw $t0, 10($t1)'
# addi = 'addi $a1, $a2, 0x100'
# beq = 'beq $zero, $s7, 0x60'
# jr = 'jr $ra'
# add = 'add $a1, $a2, $t9'
# j = 'j 0x1000'
# orr = 'or $a1, $a2, $t9'
# print parser(jr)
