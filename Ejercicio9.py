# Directorio del alumnado en formato de cadena de texto
directorio_texto = "nif;nombre;email;teléfono;nota\n01234567L;Pedro González;pedrogonzalez@mail.com;656343576;8.5\n71476342J;Candela Costa;candela@mail.com;692839321;8\n63823376M;Juan Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carolina Sánchez;carolina@mail.com;667677855;5.7"

# Dividir el directorio en líneas
lineas = directorio_texto.split('\n')

# Obtener los nombres de los campos
campos = lineas[0].split(';')

# Inicializar el diccionario del directorio
directorio = {}

# Recorrer las líneas desde la segunda (índice 1)
for linea in lineas[1:]:
    # Dividir la línea en valores
    valores = linea.split(';')

    # Inicializar el diccionario del alumno
    alumno = {}

    # Recorrer los campos y asignar los valores al diccionario del alumno
    for i in range(len(campos)):
        alumno[campos[i]] = valores[i]

    # Agregar el diccionario del alumno al directorio con el nif como clave
    directorio[alumno['nif']] = alumno

# Mostrar el diccionario del directorio
print(directorio)

# Calcular la nota media de los alumnos
notas = [float(alumno['nota']) for alumno in directorio.values()]
nota_media = sum(notas) / len(notas)

# Mostrar la nota media
print(f"Nota media de los alumnos: {nota_media}")
