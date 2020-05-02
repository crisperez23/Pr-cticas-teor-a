palabra=raw_input("Inserte la operacion: ") + ";"
estado="q0"
numero= ""
numero1 = ""
operaciones= ""

for entrada in palabra:
    if estado == "q0":
        if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9":
            estado="q1"
            numero+= entrada
        if entrada== ";" or entrada=="+" or entrada=="-" or entrada=="*" or entrada=="/":
            print "sintax error "
            salir
            estado="qR"
            
    elif estado == "q1":
        if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9":
            estado="q1"
            numero += entrada
            
		if  entrada=="+" or entrada=="-" or entrada=="*" or entrada=="/":
            estado="q2"
            operaciones += entrada
        if entrada == ";":
            print "sintax error"
            salir
            estado="qR"
                
    elif estado == "q2":
        if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or en=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9":
			estado="q3"
			numero1 += entrada
        if entrada=="+" or entrada=="-" or entrada=="*" or entrada=="/" or entrada==";":
           estado="qR"
           print "sintax error"
           salir
           
           
    elif estado == "q3":
        if entrada=="0" or entrada=="1" or entrada=="2" or entrada=="3" or entrada=="4" or entrada=="5" or entrada=="6" or entrada=="7" or entrada=="8" or entrada=="9":
           estado="q3"
           numero1 += entrada
        if entrada=="+" or entrada=="-" or entrada=="*" or entrada=="/":
           estado="q2"
        if entrada==";":
           estado="qA"
    
           

           
if estado=="qA":
    numero=int(numero)
    numero1=int(numero1)
    operaciones=(operaciones)

    if operaciones=="+" or operaciones=="-" or operaciones=="*" or operaciones=="/":
        if operaciones=="+":
            resultado=numero+numero1
                      
        elif operaciones=="-":
            resultado=numero-numero1
           
        elif operaciones=="/":
            resultado=numero/numero1
            
        elif operaciones=="*":
            resultado=numero*numero1


            
    print estado
    print ("el resultado de tu operacion es")

