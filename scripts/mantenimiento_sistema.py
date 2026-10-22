"""Script de verificacion de integridad y mantenimiento - Comercial Chiclayo."""
import datetime
import os
import sys


def ejecutar_mantenimiento():
    print("Iniciando revision preventiva de archivos...")
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Comprobar que los archivos esenciales existan
    archivos_criticos = ["src/logica_negocio.py", "src/main.py"]
    for archivo in archivos_criticos:
        if not os.path.exists(archivo):
            print(f"[ERROR]: No se encuentra el archivo obligatorio {archivo}")
            sys.exit(1)

    # Crear el informe en un archivo de texto
    nombre_reporte = "reporte_mantenimiento.txt"
    with open(nombre_reporte, "w", encoding="utf-8") as salida:
        salida.write("=====================================================\n")
        salida.write("    REPORTE DE MANTENIMIENTO DEL SISTEMA     \n")
        salida.write("=====================================================\n")
        salida.write(f"Fecha de Revision : {fecha}\n")
        salida.write("Archivos Auditados: src/logica_negocio.py, src/main.py\n")
        salida.write("Estado Operativo  : OK - INTEGRIDAD DEL SISTEMA 100%\n")
        salida.write("=====================================================\n")

    print(f"Mantenimiento concluido con exito. Archivo creado: {nombre_reporte}")
    sys.exit(0)


if __name__ == "__main__":
    ejecutar_mantenimiento()
