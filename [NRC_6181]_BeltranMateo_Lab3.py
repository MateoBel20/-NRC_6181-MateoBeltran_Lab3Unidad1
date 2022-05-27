#Se define la clase cliente 
class cliente:

#Se define el méetodo constructor con cada uno de sus objetos y tipo de datos
    def __init__(self, nombre, telefono, estado):
        self.nombre=nombre
        self.telefono=telefono
        self.estado=estado

#Se define el método para registrarse en el sistema, tiene como objetos usuario y contraseña
    def RegistrarseSistema(self,usuario,contrasena):
        self.usuario=usuario
        self.contrasena=contrasena

#Se define el método para iniciar la sesión
    def IniciarSesion(self, usuario, contrasena):
        self.usuario=usuario
        self.contrasena=contrasena

#Se define el método para registrarse en una tienda
    def RegistroTienda(self,dia, mes, año):
        self.dia=dia
        self.mes=mes
        self.año=año

#Se define el método para ver el estado de salud del cliente 
    def VerEstado(self):
        if (self.mes!="Julio"):
            print("Caso")
        else:
             print("Normal")

#Datos para la instanciar la clase cliente
print("Estimado usuario, tenga la bondad de llenar los siguientes campos: ")
nombre=str(input("Ingrese su nombre por favor: "))
telefono=str(input("Ingrese su número de teléfono: "))
estado=str(input("Ingrese su estado clínico, puede ser normal, caso o cercano: "))
estadoMinuscula=estado.lower()
while(estadoMinuscula!= "normal") and (estadoMinuscula!="caso") and (estadoMinuscula!="cercano"):
    print("Ingrese bien uno de los casos, nótese que solo existen TRES casos: ")
    estadoMinuscula=str(input("Ingrese su estado clínico, puede ser normal, caso o cercano: "))

#Instanciar la clase con datos dinámicos
persona=cliente(nombre,telefono,estado)
persona.usuario=persona.nombre + "_2022_"
persona.contrasena=''.join(reversed(persona.nombre))
print("Bienvenido mi estimado: ", nombre)
print("Sus dato telefónico registrado es: ", telefono)
print("Su estado clínico es: ", estado)
print("Su usuario es: ", persona.usuario)
print("Su contraseña: ", persona.contrasena)

#Datos para el método RegistroTienda
persona.dia=str(input("Ingrese el día de su ingreso a la tienda (04): "))
persona.mes=str(input("Ingrese el mes en el formato (Enero): "))
persona.año=str(input("Ingrese el año respectivo(2000): "))

#Inicio de sesión
print("INICIO DE SESIÓN")
user=str(input("Ingrese su usuario facilitado: "))
#Condicional while para poder ingresar de manera correcta el usuario
while (user!=persona.usuario):
    print("Ingrese bien su usuario por favor: ")
    user=str(input("Ingrese su usuario facilitado: "))
password=str(input("Ingrese su contraseña facilitada: "))
#Condicional while para poder ingresar de manera correcta la contraseña
while (password!=persona.contrasena):
    print("Ingrese bien su usuario por favor: ")
    password=str(input("Ingrese su contraseña facilitada: "))

#Definir la clase tienda
class tienda:
    #Método constructor
    def __init__(self, nombre, telefono, estado, gerente):
        self.nombre=nombre
        self.telefono=telefono
        self.estado=estado
        self.gerente=gerente
#Método para saber si el paciente tiene un estado de salud normal
    def ValorNormal(self):
#Se construye condicionales para darle un diagnóstico rápido
        if ("caso"==persona.estado):
            print("Se recomienda el aislamiento total")
        else: 
            if("cercano"==persona.estado):
                print("Tome su distanciamiento prudente")
            else:
                print("Uste se encuentra sin COVID-19")


#Registro en una tienda
print("REGISTRARSE EN UNA TIENDA")
estado1=str(input("Ingrese el estado de la tienda: "))
#Instanciar clase tienda
SANATE=tienda("SANATE", 3789546, estado1, "Luis")
#Método para el admin


print("EL HISTORIAL DE VISITA A UNA TIENDA ES EL SIGUIENTE: ")
print("El nombre de la tienda es: ", SANATE.nombre)
print("El número telefónico para cualquier novedad es: ", SANATE.telefono)
print("El estado de la tienda es: ", estado1)
print("Para cualquier novedad o queja comuníquese con el siguiente gerente: ", SANATE.gerente)
print("La fecha de su registro es: ", persona.dia, persona.mes, persona.año)
print("ESTADO DE SALUD")
print(persona.nombre,  SANATE.ValorNormal())
print("INFORME SEMANAL PARA EL ADMINISTRADOR")
print("Cliente: ", persona.nombre, " estado del cliente: " , persona.estado)