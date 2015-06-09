nombre = print("INFORME DE COMISIONES: ")
vend = input("Nombre del Vendedor: ")
vent1 = int(input("Ingrese VENTA 1: "))
vent2 = int(input("Ingrese VENTA 2: "))
vent3 = int(input("Ingrese VENTA 3: "))

promvts = (vent1 + vent2 + vent3)
comis = (promvts*12.5)/100

print("\nINFORME DE COMISIONES"+"\nVendedor"+"\t\tVentas"+"\t\tComision"+"\n"+(vend)+ "\t\t\t"+str(promvts)+ "\t\t"+ str(comis))
