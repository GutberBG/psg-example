class FondosInsuficientesError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

saldo_disponible = 500

try:
    monto = float(input("Ingrese el monto a retirar: "))

    if monto > 1000:
        raise Exception("❌ El monto excede el límite permitido por transacción (máx. 1000).")

    if monto > saldo_disponible:
        raise FondosInsuficientesError("❌ Fondos insuficientes para realizar el retiro.")

    saldo_disponible -= monto
    print(f"✅ Retiro exitoso. Su nuevo saldo es: {saldo_disponible}")

except FondosInsuficientesError as e:
    print(e)
except Exception as e:
    print(e)
