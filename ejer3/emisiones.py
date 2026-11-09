def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):
    """
    Calcula las emisiones de carbono industriales.
    Eleva ValueError si el consumo recibido es negativo.
    """
    if consumo_kwh < 0:
        raise ValueError("El consumo en kWh no puede ser un valor negativo.")
    return consumo_kwh * factor_emision