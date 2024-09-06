class Usuario:
    def __init__(self, nombrec, nickname, clave, tipo, creacion):
        self.datos = {
            "nombrec": nombrec,
            "nickname": nickname,
            "clave": clave,
            "tipo": tipo,
            "creacion": creacion
        }

    def buscar(self, valorbuscar):
        for key, value in self.datos.items():
            if value == valorbuscar:
                return value
        return None

    def eliminar(self, valoreliminar):
        for key, value in self.datos.items():
            if value == valoreliminar:
                self.datos.pop(key)
                return value
        return None


def menu():
    usuarios = []
    while True:
        print("1. Registrar usuario")
        print("2. Buscar usuario")
        print("3. Eliminar usuario")
        print("4. Salir")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            nombrec = input("Ingrese nombre completo: ")
            nickname = input("Ingrese nickname: ")
            clave = int(input("Ingrese clave: "))
            tipo = input("Ingrese tipo: ")
            creacion = int(input("Ingrese fecha de creación: "))
            usuario = Usuario(nombrec, nickname, clave, tipo, creacion)
            usuarios.append(usuario)
        if opcion == 2:
            valorbuscar = input("Ingrese el usuario a buscar: ")
            for usuario in usuarios:
                resultado = usuario.buscar(valorbuscar)
                if resultado is not None:
                    print("Usuario encontrado:", resultado)
                else:
                    print("Usuario no encontrado")
        if opcion == 3:
            valoreliminar = input("Ingrese el usuario a eliminar: ")
            for usuario in usuarios:
                resultado = usuario.eliminar(valoreliminar)
                if resultado is not None:
                    print("Usuario eliminado:", resultado)
                    break
                else:
                    print("Usuario no encontrado")
        if opcion == 4:
            break
        



menu()
