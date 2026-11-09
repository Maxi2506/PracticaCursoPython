def limpiar_registro_sensor(registro_raw):
    """
    Procesa un diccionario con datos crudos de un sensor, normalizando
    el ID, extrayendo la temperatura numérica y asignando una ubicación por defecto.
    """
    sensor_id = str(registro_raw.get("sensor_id", "")).strip()
    
    temp_raw = str(registro_raw.get("temperatura", "0"))
    temp_clean_str = "".join([c for c in temp_raw if c.isdigit() or c == '.'])
    temperatura = float(temp_clean_str) if temp_clean_str else 0.0
    
    # 3. Validar ubicación con valor por defecto seguro
    ubicacion = registro_raw.get("ubicacion")
    if not ubicacion or not str(ubicacion).strip():
        ubicacion = "Planta Desconocida"
    else:
        ubicacion = str(ubicacion).strip()
        
    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }

def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    """
    Toma una lista de sensores limpios y un umbral térmico.
    Retorna una tupla: (lista_sensores_alerta, promedio_temperatura).
    """
    if not lista_sensores_limpios:
        return [], 0.0
        
    lista_sensores_alerta = []
    suma_temperaturas = 0.0
    total = len(lista_sensores_limpios)
    
    for sensor in lista_sensores_limpios:
        temp = sensor["temperatura"]
        suma_temperaturas += temp
        if temp > umbral_temperatura:
            lista_sensores_alerta.append(sensor["sensor_id"])
            
    promedio_temperatura = suma_temperaturas / total
    return lista_sensores_alerta, promedio_temperatura


if __name__ == "__main__":
    registros_crudos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": "SENSOR-002", "temperatura": " 31.8 °C ", "ubicacion": " "},
        {"sensor_id": " SENSOR-003", "temperatura": "19.2", "ubicacion": "Planta Sur"}
    ]
    

    sensores_limpios = [limpiar_registro_sensor(reg) for reg in registros_crudos]
    

    umbral = 28.0
    alertas, promedio = generar_resumen_sensores(sensores_limpios, umbral)
    
    print("=== REPORTE CONSOLIDADO DE SENSORES ===")
    print(f"Temperatura Promedio Global: {promedio:.2f} °C")
    print(f"Dispositivos en Alerta (> {umbral} °C): {alertas}")
    print("Registros Sanitizados:", sensores_limpios)