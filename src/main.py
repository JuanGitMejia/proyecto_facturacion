# <--- Habilita los códigos de salida de la terminal (0 para éxito, 1 para error)
import sys
from logica_negocio import validar_numero_positivo, procesar_factura


def ejecutar_interfaz_cajero():
    print("=== SISTEMA DE FACTURACIÓN COMERCIAL ===")
    monto_input = input("Ingrese el subtotal bruto de la compra (S/): ")

    # Evaluamos la entrada usando el validador
    if validar_numero_positivo(monto_input):
        subtotal_ingresado = float(monto_input)
        cliente_input = input("Ingrese tipo de cliente (VIP / REGULAR): ")

        # Enviamos los datos al cerebro (logica_negocio.py)
        factura = procesar_factura(subtotal_ingresado, cliente_input)

        print("\n--- RESUMEN DE COMPROBANTE DE VENTA ---")
        print(f"Subtotal Bruto : S/ {factura['subtotal_bruto']:.2f}")
        print(f"Descuento      : S/ {factura['descuento']:.2f}")
        print(f"Subtotal Neto  : S/ {factura['subtotal_neto']:.2f}")
        print(f"IGV (18%)      : S/ {factura['igv']:.2f}")
        print(f"TOTAL A PAYAR  : S/ {factura['total_pagar']:.2f}")

        sys.exit(0)  # <--- ÉXITO: El programa termina perfectamente en la consola
    else:
        print(
            "\n[ERROR CRÍTICO]: El monto ingresado debe ser un número decimal positivo.")
        # <--- ERROR: Le avisa a la consola que el usuario rompió las reglas
        sys.exit(1)


if __name__ == "__main__":
    ejecutar_interfaz_cajero()
