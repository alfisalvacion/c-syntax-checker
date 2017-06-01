def init_typE1(): #var dec
	typE1 = [[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [1,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,1,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],
					 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0],
					 [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
					 [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0],
					 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
					 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
					 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0],
					 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0],
					 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0],
					 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0],
					 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,1,0,0],
					 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

	return typE1

def init_typE2(): #func dec
	typE2 = [[0,0,0,0,1,0,0,0,0,0,0,0,0],
					 [1,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,1,0,0,0,0,0,0,0,0,0,0,0],
					 [0,0,1,0,0,1,0,1,0,1,1,0,0],
					 [0,0,0,1,1,0,0,0,0,0,0,0,0],
					 [0,0,1,0,0,0,1,0,0,0,0,0,0],
					 [0,0,0,0,0,1,0,1,0,1,0,0,0],
					 [0,0,0,0,0,1,0,0,0,0,1,0,0],
					 [0,0,0,0,0,1,0,1,0,0,0,0,0],
					 [0,0,0,0,0,0,0,0,1,0,0,1,0],
					 [0,0,0,0,0,1,0,0,0,0,0,0,0],
					 [0,0,0,0,0,0,0,0,1,0,0,0,0],
					 [1,1,1,1,1,1,1,1,1,1,1,1,1]]

	return typE2

def init_typE3(): #func def
	typE3 = [[0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
					 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0],
					 [0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0],
					 [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0],
					 [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0],
					 [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
					 [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
					 [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
					 [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
					 [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
					 [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0],
					 [0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0],
					 [0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
					 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

	return typE3

def init_typE4(): #return 
	typE4 = [[0,0,0,0,0,0,0,0,0,0,0,0,0],
					 [1,1,1,0,0,1,0,0,1,0,0,1,0],
					 [1,0,0,0,1,0,0,0,0,1,0,0,0],
					 [0,0,0,0,0,0,0,0,0,0,1,0,0],
					 [0,0,1,0,0,1,0,0,1,0,0,0,0],
					 [1,0,0,0,1,0,0,0,0,1,0,0,0],
					 [1,0,0,0,1,0,0,0,0,1,0,0,0],
					 [0,0,0,0,0,0,1,0,0,0,0,0,0],
					 [0,0,0,0,0,0,0,1,0,0,0,0,0],
					 [0,0,1,0,0,0,0,0,0,0,0,1,0],
					 [0,0,1,0,0,0,0,0,0,0,0,0,0],
					 [0,0,0,1,0,0,0,0,0,0,0,0,0],
					 [1,1,1,1,1,1,1,1,1,1,1,1,1]]

	return typE4

def fileRead():
	from sys import argv
	script = argv

	data = []
	pas = False

	while not pas: 
		try:
			print "Enter input file name (input.in for default): "
			inp = raw_input()
			input_file = open(inp, 'r')

			data = input_file.read()
			input_file.close()
			pas = True

		except IOError:
			print "File does not exist. Try creating it first."

	return data

def execute():
	data = fileRead()

	print "Enter output file name: "
	out = raw_input()
	output_file = open(out, 'w')

	data = data.split('\n')
	writeStr = ""
	print '\n'
	testCases = int(data[0])
	ctr = 1
	testStr = 2
	while testCases > 0:
		dataStr = tokenize(data[testStr], int(data[ctr]))
		writeStr = "Yes" if isValid(int(data[ctr]), dataStr) else "No"
		print writeStr, '\n\n', '##############################################################################'
		output_file.write(writeStr + '\n') # filewrite

		ctr += 2
		testStr += 2
		testCases -= 1

	output_file.truncate()
	output_file.close()

def tokenize(data, typE):
	isValue = False
	isChar = 0
	isArray = False
	dataLen = len(data)
	snippetsArr = []
	snip = ""
	isIdent = False
	isFunc_Def = False

	for x in range(0, dataLen):
		if typE == 3 and data[x] == '{':
			snippetsArr.append(data[x])
			isFunc_Def = True
		elif typE == 3 and data[x] == '}':
			snippetsArr.append(snip)
			snippetsArr.append(data[x])
			isFunc_Def = False
			snip = ""
		elif isFunc_Def:
			snip += data[x]
			if data[x] == ';' and data[x + 1] != ';':
				snippetsArr.append(snip)
				snip = ""
		else:
			if isValue:
				if (data[x] == ';' or data[x] == ',' or data[x] == '}') or (data[x] in operators) and not isArray:
					snippetsArr.append(snip)
					snip = ""
					isValue = False
				else:
					if data[x] != ' ':
						if data[x] == '{':
							snippetsArr.append("{")
							snip = ''
							isArray = True
						elif data[x] == '}':
							snippetsArr.append(snip)
							snippetsArr.append("}")
							snip = ''
							isArray = False
						elif data[x] == "'":
							snippetsArr.append(snip)
							snippetsArr.append("'")
							snip = ''
						elif data[x] == ",":
							snippetsArr.append(snip)
							snippetsArr.append(",")
							snip = ''
						else:
							snip += data[x]

			if isIdent:
				if data[x] == ' ' or data[x] == '(' or data[x] == '=' or data[x] == ';' or data[x] == '[':
					snippetsArr.append(snip)
					if data[x] != ' ':
						snippetsArr.append(data[x])
					snip = ""
					isIdent = False
				else:
					snip += data[x]

			elif not isIdent and not isValue:
				if data[x] != " ":
					if not data[x].isalnum():
						if data[x] == '_':
							isIdent = True
							snip += data[x]
						else:
							if data[x] == '=':
								isValue = True
							snippetsArr.append(data[x])
					elif data[x].isalnum():
						snip += data[x]
						if x + 1 < dataLen and not data[x + 1].isalnum() and data[x + 1] != '_':
							snippetsArr.append(snip)
							snip = ""
				else:
					snippetsArr.append(snip)
					snip = ""

	snippetsArr.append(snip)

	return cleanArr(snippetsArr)

def cleanArr(snippet):
	snippTemp = []
	snippLen = len(snippet)
	for x in range(0, snippLen):
		if snippet[x] != "" and snippet[x] != "\t" and snippet[x] != "\n" and snippet[x] != "\r":
			snippTemp.append(snippet[x])
	return snippTemp

def isValid(typE, dataStr):
	print dataStr, '\n'
	if typE == 1:
		return isValid_varDec(dataStr, [], [])
	if typE == 2: 
		return isValid_funcDec(dataStr) 
	if typE == 3:	
		return isValid_funcDef(dataStr)

def isValid_varDec(dataStr, idents, pointers):
	deadState = 32
	currentState = -1
	datatypE = ""
	isArray = False

	identifiers = idents
	pointer_identifiers = pointers
	pointer_flag = False
	vardec = True

	arrLen = len(typE1[0]) 
	dataLen = len(dataStr)
	for x in range(0, dataLen):
		currentInput = dataStr[x]

		for i in range(0, arrLen):
			if currentState == -1:
				if currentInput in dataTypEs:
					currentState = 0
					datatypE = currentInput
					arrtypE = currentState
					break
				else:
					currentState = deadState
					break

			else:
				if typE1[i][currentState] == 1:
					if i == 0:
						if currentInput in dataTypEs:
							vardec = True
							currentState = i
							break
					elif i == 1:
						if isValid_identifier(currentInput):
							if vardec:
								if currentInput in identifiers or currentInput in reservedWords or currentInput in pointer_identifiers:
									currentState = deadState
								else:
									if pointer_flag:
										pointer_identifiers.append(currentInput)
										pointer_flag = False
									else:
										identifiers.append(currentInput)
									currentState = i
								vardec = False
							else:
								print identifiers
								if currentInput not in identifiers and currentInput not in pointer_identifiers:
									currentState = deadState
								else:
									currentState = i								
							break
					elif i == 2:
						if currentInput == ';':
							currentState = i
							isArray = False
							add_to_identifiers(identifiers, pointer_flag)
							add_to_identifiers(pointer_identifiers, pointer_flag)
							break 
					elif i == 3:
						if currentInput == '*':
							pointer_flag = True
							currentState = i
							break
					elif i == 4:
						if currentInput == ',':
							currentState = i
							isArray = False
							break
					elif i == 5:
						if currentInput == '[':
							isArray = True
							currentState = i
							break
					elif i == 6:
						if currentInput.isdigit():
							currentState = i
							break
					elif i == 7:
						if currentInput == ']':
							currentState = i
							break
					elif i == 8:
						if currentInput == '=':
							currentState = i
							break
					elif i == 9:
						if currentInput == '+':
							currentState = i
							break
					elif i == 10:
						if currentInput == '+':
							currentState = i
							break
					elif i == 11:
						if currentInput == '-':
							currentState = i
							break
					elif i == 12:
						if currentInput == '-':
							currentState = i
							break		
					elif i == 13:
						if currentInput == '+':
							currentState = i
							break
					elif i == 14:
						if currentInput == '+':
							currentState = i
							break
					elif i == 15:
						if currentInput == '-':
							currentState = i
							break
					elif i == 16:
						if currentInput == '-':
							currentState = i
							break		
					elif i == 17:
						try:
							num = float(currentInput)
							if isinstance(num, (int, long, float, complex)):
								currentState = i
								break
							else:
								currentState = deadState
						except ValueError:
							print
					elif i == 18:
						if currentInput in operators:
							currentState = i
							break
					elif i == 19:
						if currentInput in identifiers:
							currentState = i
							break
						else:
							currentState = deadState
					elif i == 20:
						if currentInput == "'":
							currentState = i
							break
					elif i == 21:
						if len(currentInput) == 1:
							currentState = i
							break
						else:
							currentState = deadState
					elif i == 22:
						if currentInput == "'":
							currentState = i
							break
					elif i == 23 and isArray:
						if currentInput == '{':
							currentState = i
							break
					elif i == 24:
						if currentInput == "'":
							currentState = i	
							break
					elif i == 25:
						if len(currentInput) == 1:
							currentState = i
							break
						else:
							currentState = deadState
					elif i == 26:
						if currentInput == "'":
							currentState = i	
							break		
					elif i == 27:
						if currentInput == ",":
							currentState = i
							break
					elif i == 28:
						try:
							val = float(currentInput)
							if isinstance(val, (int, long, float, complex)):
								currentState = i
								break
							else:
								currentState = deadState
						except ValueError:
							print
					elif i == 29:
						if currentInput in pointer_identifiers or currentInput in identifiers:
							currentState = i
							break
						else:
							currentState = deadState
					elif i == 30:
						if currentInput in operators:
							currentState = i
							break
					elif i == 31:
						if currentInput == "}":
							currentState = i	
							break
					elif i == 32:
						currentState = deadState

	return currentState == 2

def isValid_funcDec(dataStr):
	deadState = 12	
	currentState = -1
	isArray = False

	used_identifiers = []
	used_param_identifiers = []

	arrLen = len(typE2[0]) 
	dataLen = len(dataStr)
	for x in range(0, dataLen):
		currentInput = dataStr[x]

		for i in range(0, arrLen):
			if currentState == -1:
				if currentInput in returnTypEs:
					currentState = 0
					break
				else:
					currentState = deadState
					break

			else:
				if typE2[i][currentState] == 1:
					if i == 0:
						if currentInput in returnTypEs:
							currentState = i
							break
					elif i == 1:
						if isValid_identifier(currentInput):
							if currentInput in used_identifiers or currentInput in reservedWords:
								currentState = deadState
							else:
								used_identifiers.append(currentInput)
								currentState = i
							break
					elif i == 2:
						if currentInput == '(':
							currentState = i
							break 
					elif i == 3:
						if currentInput == ')':
							currentState = i 
							break
					elif i == 4:
						if currentInput == ';':
							used_param_identifiers = []
							currentState = i 
							break
					elif i == 5:
						if currentInput in dataTypEs:
							currentState = i 
							break
					elif i == 6:
						if currentInput == ',':
							currentState = i 
							break
					elif i == 7:
						if isValid_identifier(currentInput):
							if currentInput in used_param_identifiers or currentInput in reservedWords:
								currentState = deadState
							else:
								used_param_identifiers.append(currentInput)
								currentState = i
							break
					elif i == 8:
						if currentInput == '[':
							currentState = i 
							break
					elif i == 9:
						if currentInput == ']':
							currentState = i 
							break
					elif i == 10:
						if currentInput == '*':
							currentState = i
							break
					elif i == 11:
						if currentInput.isdigit():
							currentState = i
							break
					elif i == 12:
						currentState = deadState

	return currentState == 4

def isValid_funcDef(dataStr):
	deadState = 15	
	currentState = -1
	isArray = False

	used_param_identifiers = []
	used_function_identifiers = []

	arrLen = len(typE3[0]) 
	dataLen = len(dataStr)
	for x in range(0, dataLen):
		currentInput = dataStr[x]

		for i in range(0, arrLen):
			if currentState == -1:
				if currentInput in returnTypEs:
					currentState = 0
					break
				else:
					currentState = deadState
					break

			else:
				if typE3[i][currentState] == 1:
					if i == 0:
						if currentInput in returnTypEs:
							currentState = i
							break
					elif i == 1:
						if isValid_identifier(currentInput):
							if currentInput in used_function_identifiers or currentInput in reservedWords:
								currentState = deadState
							else:
								used_function_identifiers.append(currentInput)
								currentState = i
							break
					elif i == 2:
						if currentInput == '(':
							currentState = i
							break 
					elif i == 3:
						if currentInput == ')':
							currentState = i 
							break
					elif i == 4:
						if currentInput in dataTypEs:
							currentState = i 
							break
					elif i == 5:
						if isValid_identifier(currentInput):
							if currentInput in used_param_identifiers or currentInput in reservedWords:
								currentState = deadState
							else:
								used_param_identifiers.append(currentInput)
								funcDef_identifiers.append(currentInput)
								currentState = i
							break
					elif i == 6:
						if currentInput == ',':
							currentState = i 
							break
					elif i == 7:
						if currentInput == '[':
							currentState = i 
							break
					elif i == 8:
						if currentInput.isdigit():
							currentState = i
							break
					elif i == 9:
						if currentInput == ']':
							currentState = i 
							break
					elif i == 10:
						if currentInput == '*':
							currentState = i
							break
					elif i == 11:
						if currentInput == '{':
							currentState = i
							break
					elif i == 12:
						if currentInput == '}':
							currentState = i
							resetIdentifiers()
							break
					elif i == 13:
						snip = tokenize(currentInput, 1)
						if snip[0] == "return":
							if isValid_return(snip, funcDef_identifiers, funcDef_pointers):
								currentState = i
								break
						else:
							if isValid_varDec(snip, funcDef_identifiers, funcDef_pointers):
								currentState = i
								break
							else:
								currentState = deadState
							
					elif i == 14:
						if currentInput == ';':
							currentState = i 
							break
					elif i == 15:
						currentState = deadState

	if currentState == 12 or currentState == 14:
		return True
	return False

def isValid_return(dataStr, identifiers, pointers):
	# print "return"
	deadState = 12
	currentState = -1
	isArray = False

	used_identifiers = identifiers
	used_pointers = pointers

	arrLen = len(typE4[0]) 
	dataLen = len(dataStr)
	for x in range(0, dataLen):
		currentInput = dataStr[x]

		for i in range(0, arrLen):
			if currentState == -1:
				if currentInput == "return":
					currentState = 0
					break
				else:
					currentState = deadState
					break

			else:
				if typE4[i][currentState] == 1:
					if i == 1:
						if currentInput == ';':
							currentState = i
							break
					elif i == 2:
						if isValid_identifier(currentInput):
							if currentInput not in used_identifiers or currentInput in reservedWords:
								currentState = deadState
							else:
								currentState = i
							break
					elif i == 3:
						if currentInput.isdigit():
							currentState = i
							break
					elif i == 4:
						if currentInput in operators:
							currentState = i
							break
					elif i == 5:
						if currentInput.isdigit():
							currentState = i
							break
					elif i == 6:
						if currentInput == "'":
							currentState = i
							break
					elif i == 7:
						if len(currentInput) == 1:
							currentState = i
							break
					elif i == 8:
						if currentInput == "'":
							currentState = i
							break
					elif i == 9:
						if currentInput == '=':
							currentState = i
							break 
					elif i == 10:
						if currentInput == '[':
							currentState = i 
							break
					elif i == 11:
						if currentInput == ']':
							currentState = i 
							break
					elif i == 12:
						currentState = deadState

	return currentState == 1

def isValid_identifier(identifier):
	idenLen = len(identifier)
	for x in range(0, idenLen):
		if x == 0 and identifier[x].isdigit():
			return False
		if identifier[x] == '_':
			continue
		if not identifier[x].isalnum():
			return False
	return True

def add_to_identifiers(identifiers, pointer_flag):
	for item in identifiers:
		if item not in funcDef_identifiers and not pointer_flag:
			funcDef_identifiers.append(item)
		elif item not in funcDef_pointers and pointer_flag:
			funcDef_pointers.append(item)

def resetIdentifiers():
	global funcDef_pointers
	global funcDef_identifiers
	funcDef_pointers = []
	funcDef_identifiers = []

typE1 = init_typE1()
typE2 = init_typE2()
typE3 = init_typE3()
typE4 = init_typE4()
funcDef_identifiers = [] 
funcDef_pointers = []
dataTypEs = ["int", "float", "char", "double"]
returnTypEs = ["int", "float", "char", "double", "void"]
reservedWords = ["auto", "break", "case", "char", "const", "continue", 
								"default", "do", "int", "long", "register", "return", "short", "signed", "sizeof", 
								"static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while", 
								"double", "else", "enum", "extern", "float", "for", "goto", "if"]
operators = ['+','-','*','/','%']
execute()