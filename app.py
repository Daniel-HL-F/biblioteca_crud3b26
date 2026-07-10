import flet as ft

from ui.main_window import main_Window
from dao.libro_dao import LibroDAO
from models.libro import Libro
from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario

def ver_libros():
    try:
        libro_dao = LibroDAO()
        libros = libro_dao.obtener_todo()

        if len(libros) == 0:
            print("No hay libros registrado")

        else:
            for libro in libros:
                print(f"{libro.id} {libro.titulo} {libro.autor} {libro.isbn} {libro.disponible}")

            print("\n Conexion establecida con la base de datos")        

    except Exception as e: 
        print("Error")
        print(e)

def insertar_libro():
    print("INCERTAR UN NUEVO LIBRO")
    titulo = input("Escribe el titulo: ")
    autor = int(input("Escribe el id del autor: "))
    isbn = input("Escribe el isbn: ")
    disponible = True


    try:
        libro_dao = LibroDAO()
        ultimo_id = libro_dao.obtener_ultimo_id() + 1
        libro = Libro(ultimo_id, titulo, autor, isbn, disponible)
        libro_dao.insertar(libro)
        print("Insercion del nuevo libro fue exitosa")
    except Exception as e:
        print("Error al insertar el libro")
        print(e)

def actualizar_libro():
    try:
        libro_dao = LibroDAO()
        print("Lista de libros disponibles")
        ver_libros()
        id = int(input("Seleccione el id del libro a actualizar"))
        titulo = input("Escribe el titulo: ")
        autor = int("Escribe el id autor: ")
        isbn = input("Escribe el isbn")
        disponible = bool(input("Escribe si esta disponible: "))
        libro = Libro(id, titulo, autor, isbn, disponible)
        libro_dao.actualizar(libro)
        print("El libro fue actualizado con exito")
    except Exception as e:
        print("Error al actualizar el libro")
        print(e)

def eliminar_libro():
    try:
        libro_dao = LibroDAO()
        print("Lista de libros diaponibles")
        ver_libros()
        id = int(input("Escribe el id del libro a eliminar: "))
        libro_dao.eliminar(id)
        print(f"El libro {id} ha sido eliminado")
    except Exception as e:
        print("Error al eliminar el libro")
        print(e)

def menu_libros():
    print("=== BIBLIOTECA UNIVERCITARIA ===")
    print("1. Ver todos los libros")
    print("2. Incertar un nuevo libro")
    print("3. Actualizar un libro")
    print("4. Eliminar un libro existente")
    opcion = int(input("Selecciona una opción (1-4):"))

    match opcion:
        case 1: 
            ver_libros()
        case 2:
            insertar_libro()
        case 3:
            actualizar_libro()
        case 4:
            eliminar_libro()

    

def menu_usuarios():
    print("=== BIBLIOTECA UNIVERCITARIA ===")
    print("1. Ver todos los usuarios")
    print("2. Incertar un nuevo usuario")
    print("3. Actualizar un usuario")
    print("4. Eliminar un usuario existente")
    opcion = int(input("Selecciona una opción (1-4):"))

    match opcion:
        case 1: 
            ver_usuario()
        case 2:
            insertar_usuario()
        case 3:
            actualizar_usuario()
        case 4:
            eliminar_usuario()
#===============================================================================
ft.app(target=main_Window)




# def main():
#     print("=== BIBLIOTECA UNIVERCITARIA ===")
#     print("Menu de opciones: ")
#     print("1. libros")
#     print("2. usuarios")
#     opcion = int(input("Escribe tu opcion: "))
#     match opcion:
#          case 1: menu_libros()
#          case 2: menu_usuarios()
#     print("Saliendo del sistema de Biblioteca universitaria ...")  


# def ver_usuario():
#     try:
#         usuario_dao = UsuarioDAO()
#         usuarios = usuario_dao.obtener_todo()

#         if len(usuarios) == 0:
#             print("No hay usuarios registrados")

#         else:
#             for usuario in usuarios:
#                 print(f"{usuario.id} {usuario.nombre} {usuario.matricula} {usuario.carrera} {usuario.correo} {usuario.activo}")

#             print("\n Conexion establecida con la base de datos")        

#     except Exception as e: 
#         print("Error")
#         print(e)


# def insertar_usuario():
#     print("INCERTAR UN NUEVO USUARIO")
#     nombre = input("Escribe el nombre: ")
#     matricula = input("Escribe la matricula: ")
#     carrera = input("Escribe la carrera: ")
#     correo = input("Escribe el correo: ")
#     activo = True


#     try:
#         usuario_dao = UsuarioDAO()
#         ultimo_id = usuario_dao.obtener_ultimo_id() + 1
#         usuario = Usuario(ultimo_id, nombre, matricula, carrera, correo, activo)
#         usuario_dao.insertar(usuario)
#         print("Insercion del nuevo usuario fue exitosa")
#     except Exception as e:
#         print("Error al insertar el usuario")
#         print(e)

# def actualizar_usuario():
#     try:

#         usuario_dao = UsuarioDAO()

#         print("Lista de usuarios disponibles")

#         ver_usuario()


#         id = int(input("Seleccione el id del usuario a actualizar: "))
#         nombre = input("Escribe el nombre: ")
#         matricula = input("Escribe la matricula: ")
#         carrera = input("Escribe la carrera: ")
#         correo = input("Escribe el correo: ")

#         activo = True


#         usuario = Usuario(
#             id,
#             nombre,
#             matricula,
#             carrera,
#             correo,
#             activo
#         )


#         usuario_dao.actualizar(usuario)


#         print("El usuario fue actualizado con exito")


#     except Exception as e:

#         print("Error al actualizar el usuario")

#         print(e)

# def eliminar_usuario():
#     try:
#         usuario_dao = UsuarioDAO()
#         print("Lista de usuario diaponibles")
#         ver_usuario()
#         id = int(input("Escribe el id del usuario a eliminar: "))
#         usuario_dao.eliminar(id)
#         print(f"El usuario {id} ha sido eliminado")
#     except Exception as e:
#         print("Error al eliminar el usuario")
#         print(e)
 
    

    

# if __name__ == "__main__":
#     main()       
