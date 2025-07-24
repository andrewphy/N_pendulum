# Nombre del archivo original y del nuevo
for j in [10,13]:
    archivo_entrada = f"DATOS\\datos_{j}masas_2metro.txt"
    archivo_salida = f"DATOS\\datos_{j}masas_2metroMODIFY.txt"

    # Leer el contenido del archivo original
    with open(archivo_entrada, "r", encoding="latin-1") as f:
        contenido = f.read()

# Reemplazar comas por puntos
    contenido_modificado = contenido.replace(",", ".")

# Guardar el contenido modificado en un nuevo archivo
    with open(archivo_salida, "w", encoding="utf-8") as f:
        f.write(contenido_modificado)

    print("Reemplazo completado. Archivo guardado como:", archivo_salida)
    
    with open(f"DATOS\\datos_{j}masas_2metroMODIFY.txt", "r") as f:
        for i, linea in enumerate(f):
            if i < 34:  # saltar cabecera si usás skiprows=34
                continue
            columnas = linea.strip().split()
            if len(columnas) != 4:
                print(f"⚠️  Línea {i+1} tiene {len(columnas)} columnas: {linea.strip()}")
print(j)    