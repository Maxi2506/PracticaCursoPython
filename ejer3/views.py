from .emisiones import calcular_emisiones_carbono

def obtener_metricas_consumo(registros):
    """
    Procesa un historial de consumos por planta industrial para determinar
    el total global de emisiones y la planta de mayor consumo.
    """
    if not registros:
        return 0.0, None
        
    total_emisiones = 0.0
    max_consumo = -1.0
    planta_mayor_consumo = None
    
    for reg in registros:
        planta = reg.get("planta", "Desconocida")
        consumo = reg.get("consumo_kwh", 0.0)
        
        emisiones = calcular_emisiones_carbono(consumo)
        total_emisiones += emisiones
        
        if consumo > max_consumo:
            max_consumo = consumo
            planta_mayor_consumo = planta
            
    return total_emisiones, planta_mayor_consumo


def vista_panel_sustentabilidad(request):
    """
    Función de vista en Django que procesa las métricas y renderiza 'sustentabilidad/panel.html'.
    """
    registros_plantas = [
        {"planta": "Planta Norte", "consumo_kwh": 3400.0},
        {"planta": "Planta Sur", "consumo_kwh": 5120.0},
        {"planta": "Planta Este", "consumo_kwh": 2150.0}
    ]
    
    total_emisiones, planta_top = obtener_metricas_consumo(registros_plantas)
    
    contexto = {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_top,
        "registros": registros_plantas
    }
    
    # -------------------------------------------------------------
    # Cumplimiento con Django:
    # -------------------------------------------------------------
    try:
        from django.shortcuts import render
        return render(request, 'sustentabilidad/panel.html', contexto)
    except (ImportError, Exception):
        # Si no estamos corriendo en un servidor Django activo,
        # retornamos el contexto para poder verificarlo en consola.
        return contexto