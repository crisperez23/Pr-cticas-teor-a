palabra = raw_input("ingresar la cadena:") + ";"

numero1 = ""
numero2 = ""
operacion =""

estado = "q0"
for entrada in palabra:
	if estado == "q0":
		if entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="0":
			estado = "q1"
			numero1 += entrada
		if entrada == "*" or entrada == "+" or entrada == "-" or entrada == "/" or entrada == "." or entrada == ";":
			estado = "qr"
			print "caracter invalido::.  " + entrada

	elif estado == "q1":
		if entrada == ";":
			estado = "qr"
			print "caracter invalido::.  " + entrada
       		if entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="0" or entrada ==",":
            		estado = "q1"
			numero1 += entrada

		if entrada == "*" or entrada == "+" or entrada == "-" or entrada == "/":
			estado = "q2"
			operacion += entrada
        	if entrada == ";":
            		estado = "qr"
			print "caracter invalido::.  " +  entrada

	elif estado == "q2":
		if entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="0":
			estado = "q3"
			numero2 += entrada

		if entrada == "*" or entrada == "+" or entrada == "-" or entrada == "/":
			estado = "qr"
			print "caracter invalido::.  " + entrada

	elif estado == "q3":
        	if entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="0" or entrada == "*" or entrada == "+" or entrada == "-" or entrada == "/":
            		estado = "q3"
		if entrada=="*" or entrada == "/" or entrada == "+" or entrada == "-":
			estado ="qr"
		if entrada == ";":
			estado = "qa"
			numero1 = int(numero1)
			numero2= int(numero2)
			if operacion== "*":
				resultado = numero1 * numero2
			if operacion=="/":
				resultado=numero1/numero2
			if operacion=="+":
				resultado=numero1+numero2
			if operacion == "-":
				resultado=numero1-numero2
			print "tu resultado es ::.  " + str(resultado)

	
print estado
