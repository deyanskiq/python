alphabet={0:'a',1:'b',2:'c',3:'d',
	4:'e',5:'f',6:'g',7:'h',
	8:'i',9:'j',10:'k',11:'l',
	12:'m',13:'n',14:'o',15:'p',
	16:'q',17:'r',18:'s',19:'t',
	20:'u',21:'v',22:'w',23:'x',
	24:'y',25:'z'	
}
def ceaser(string,n):
	new_list=list(string)
	last_list=[]
	for var in new_list:
		for p in alphabet:
			if var.lower()==alphabet[p]:
				while n>25:
					n=n-26
				if p+n>25:
					if var==var.lower():
						last_list.append(alphabet[n+p-26])
					else:
						last_list.append(alphabet[n+p-26].upper())
				else:
					if var==var.lower():
						last_list.append(alphabet[n+p])
					else:
						last_list.append(alphabet[n+p].upper())
	print ("".join(last_list))
ceaser("ABCdefg",27)