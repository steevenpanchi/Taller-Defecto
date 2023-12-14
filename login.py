# FALLOS
# FALLO 1: No se toma encuenta que el contador inicia en cero, por ende deberia existir como intentos 
# maximos 2, es por ello que se esta bloqueando al cuarto intento la cuenta

#FALLO 2: No se estan mostrando los mensajes de error para los distintos 
#casos, solo esta mostrando el error de la exepcion "Erros inesperado"


class ModuloInicioSesion:
    def __init__(self, usuarios, intentos_maximos=3):
        self.usuarios = usuarios
        self.intentos_maximos = intentos_maximos
        self.intentos_actuales = {}

    def iniciar_sesion(self, usuario, contrasena):
        try:
            if usuario in self.usuarios:
                if self.intentos_actuales.get(usuario, 0) < self.intentos_maximos:
                    if self.usuarios[usuario] == contrasena:
                        self.intentos_actuales[usuario] = 0  # Reiniciar los intentos al iniciar sesión exitosamente
                        return "Ingreso con éxito"
                    else:
                        self.intentos_actuales[usuario] += 1

                        if self.intentos_actuales[usuario] >= self.intentos_maximos:
                            self.bloquear_cuenta(usuario)
                            return "La cuenta ha sido bloqueada debido a múltiples intentos fallidos."
                        else:
                            return "Contraseña incorrecta"
                else:
                    return "La cuenta está bloqueada. Contacta al soporte para desbloquearla."
            else:
                return "Usuario incorrecto"
        except Exception as e:
            print(f"Fallo inesperado: {str(e)}")
            return "Error inesperado"

    def bloquear_cuenta(self, usuario):
        # Implementación de la lógica de bloqueo de cuenta
        print(f"La cuenta de {usuario} ha sido bloqueada.")
        # ...

# Datos quemados para usuarios y contraseñas
usuarios_registrados = {'Gustavo Venegas': 'gustavo123'}

# Crear instancia del módulo de inicio de sesión con los datos quemados
modulo_sesion = ModuloInicioSesion(usuarios_registrados)

# Intentos de inicio de sesión, se bloqueará después de 3 intentos fallidos
#En esta seccion existe el fallo ya que deberia tomarse como rango el numero 2
# puesto que ahi se tomaria en cuenta que  se bloquearia despues de 3 intentos fallidos
for _ in range(3):
    nombre_usuario = input("Introduce tu nombre de usuario: ")
    contrasena = input("Introduce tu contraseña incorrecta: ")

    resultado = modulo_sesion.iniciar_sesion(nombre_usuario, contrasena)
    print(resultado)

# Intento de inicio de sesión después de bloqueo
nombre_usuario = input("Introduce tu nombre de usuario: ")
contrasena = input("Introduce tu contraseña: ")

resultado = modulo_sesion.iniciar_sesion(nombre_usuario, contrasena)
print(resultado)

