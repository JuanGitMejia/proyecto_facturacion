"""Pruebas unitarias del sistema de facturacion."""

from src.logica_negocio import procesar_factura


def test_factura_cliente_vip():
    """Verifica el descuento y el total de una factura VIP."""
    factura = procesar_factura(1000.0, "VIP")

    assert factura["subtotal_bruto"] == 1000.0
    assert factura["descuento"] == 150.0
    assert factura["total_pagar"] == 850.0


def test_total_factura_es_positivo():
    """Verifica que el total de la factura sea positivo."""
    factura = procesar_factura(1000.0, "VIP")

    assert factura["total_pagar"] > 0


def test_factura_tiene_campos_requeridos():
    """Verifica que la factura contenga los campos necesarios."""
    factura = procesar_factura(1000.0, "VIP")

    assert "subtotal_bruto" in factura
    assert "descuento" in factura
    assert "total_pagar" in factura