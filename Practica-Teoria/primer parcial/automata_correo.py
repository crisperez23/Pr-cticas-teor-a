palabra = raw_input("ingrese la cedena:") + "*"
estado = "q0"
for entrada in palabra:
	if estado == "q0":
		if entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="0" or entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or  entrada=="j" or  entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z" or entrada==".":

			estado = "q1"

		if entrada == "*":
			estado = "qr"

	elif estado == "q1":
		if entrada == "@":
			estado = "q2"
	        if entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="0" or entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or  entrada=="j" or  entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z":
            		estado = "q1"

		if entrada == "*":
			estado = "qr"

	elif estado == "q2":
		if entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="0" or entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or  entrada=="j" or  entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z" or entrada==".":
			estado = "q3"

		if entrada == "*" or entrada=="@" or entrada==".":
			estado = "qr"

	elif estado == "q3":
		if entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or  entrada=="j" or  entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z":
			estado = "q3"
		if entrada == ".":
			estado = "q4"
        if entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="0":
            estado = "qr"

	elif estado == "q4":
        	if entrada == "." or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="0" or entrada == "@":
            		estado = "qr"
        	if entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or  entrada=="j" or  entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z":
            		estado = "q5"

	elif estado == "q5":
        	if entrada == "*":
            		estado = "qa"
        	if entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9" or entrada=="0" or entrada=="a" or entrada=="b" or entrada=="c" or entrada=="d" or entrada=="e" or entrada=="f" or entrada=="g" or entrada=="h" or entrada=="i" or  entrada=="j" or  entrada=="k" or entrada=="l" or entrada=="m" or entrada=="n" or entrada=="o" or entrada=="p" or entrada=="q" or entrada=="r" or entrada=="s" or entrada=="t" or entrada=="u" or entrada=="v" or entrada=="w" or entrada=="x" or entrada=="y" or entrada=="z":
			estado = "q5"
		if entrada == "@" or entrada == ".":
                	estado ="qr"

print estado