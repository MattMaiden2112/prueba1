print("Aqui crearemos su tarjeta de contacto, por favor ingrese los datos que le iremos pidiendo:")
apellido=input("Ingrese su apellido: "); nombres=input("Ahora ingrese sus nombres: "); nacimiento=input("Ahora, ingrese su año de nacimiento: ")
ciudad=input("Ingrese la ciudad donde vive: ")
print("Se le creara un correo electronico con los datos ingresados."); print("He aqui su tarjeta de contacto:")
sep_nombres=[nombres.capitalize() for nombres in nombres.split()]
nombres_comp=" ".join(sep_nombres)
sep_ciudad=[ciudad.capitalize() for ciudad in ciudad.split()]
ciudad_comp=" ".join(sep_ciudad)
nacimiento=int(nacimiento)
import datetime
year_act=int(datetime.datetime.now().year)
edad=int(year_act-nacimiento)
print("")
cadena1="▓"; cadena2=" DATOS PERSONALES "; cadena3="░"
print(cadena1.center(50, cadena1)); print(cadena2.center(50, "▒")); print(cadena3.center(50, cadena3)); print("▀"*50)
print("║ Apellido y nombres:", apellido.upper(), end=(", ")); print(nombres_comp)
print("║ Año de nacimiento: ", nacimiento)
print("║ Correo electronico:", nombres[0], end=("")); print(apellido.lower(), end=(".")); print(nacimiento, end=("@empresa.com.ar")); print()
print("║ Ciudad:", ciudad_comp)
print("║ Edad aproximada:", edad)
print("▄"*50); print(cadena3.center(50, cadena3)); print(cadena1.center(50, cadena1))