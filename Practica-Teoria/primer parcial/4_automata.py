palabra = raw_input("ingresar la cedena:") + "*"
estado = "q0"
for entrada in palabra:
	if estado == "q0":
		if entrada == "1":
			estado = "q1"
		if entrada == "0":
			estado = "q0"
		if entrada == "*":
			estado = "qr"
	elif estado == "q1":
		if entrada == "1":
			estado = "q2"
		if entrada == "0":
			estado = "q1"
		if entrada == "*":
			estado = "qr"
	elif estado == "q2":
		if entrada == "1":
			estado = "q3"
		if entrada == "0":
			estado = "q2"
		if entrada == "*":
			estado = "qr"
	elif estado == "q3":
		if entrada =="1":
			estado = "q1"
		if entrada == "0":
			estado = "q3"
		if entrada =="*":
			estado = "qa"
	#elif estado =="qa":#
		#break#
print estado
