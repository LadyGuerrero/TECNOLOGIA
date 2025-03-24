def calcular_descuento(monto_total, porcentaje_descuento=10):
    """Calcula el descuento de una compra"""
    return monto_total * (porcentaje_descuento / 100)

# Primera llamada - con valor por defecto (10%)
compra1 = 1000
desc1 = calcular_descuento(compra1)
print(f"Compra: ${compra1}, Descuento: ${desc1}, Total a pagar: ${compra1 - desc1}")

# Segunda llamada - con porcentaje específico
compra2 = 1500
desc2 = calcular_descuento(compra2, 15)
print(f"Compra: ${compra2}, Descuento: ${desc2}, Total a pagar: ${compra2 - desc2}")