import json
import os

class StockInvalidoError(Exception):
    """Excepción personalizada para impedir asignación de stock negativo."""
    pass

class DispositivoEcológico:
    """Clase base que encapsula las propiedades generales de un dispositivo."""
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.set_stock(stock)
        
    def get_stock(self):
        return self._stock
        
    def set_stock(self, stock):
        if stock < 0:
            raise StockInvalidoError(f"Error: El stock ({stock}) no puede ser un valor negativo.")
        self._stock = stock
        
    stock = property(get_stock, set_stock)
    
    def ficha_tecnica(self):
        return f"Dispositivo: {self.nombre} | Stock Disponible: {self._stock}"
        
    def to_dict(self):
        return {
            "tipo": "Generico",
            "nombre": self.nombre,
            "stock": self._stock
        }

class PanelSolar(DispositivoEcológico):
    """Clase especializada que hereda de DispositivoEcológico aplicando polimorfismo."""
    def __init__(self, nombre, stock, potencia_w):
        super().__init__(nombre, stock)
        self.potencia_w = potencia_w
        
    def ficha_tecnica(self):
        return f"[Panel Solar] {self.nombre} - Potencia: {self.potencia_w}W - Stock: {self._stock} unidades"
        
    def to_dict(self):
        data = super().to_dict()
        data["tipo"] = "PanelSolar"
        data["potencia_w"] = self.potencia_w
        return data

class GestorInventario:
    """Gestiona la persistencia del catálogo en disco."""
    @staticmethod
    def guardar_catalogo_json(lista_dispositivos, ruta_archivo="catalogo_ecotech.json"):
        datos = [d.to_dict() for d in lista_dispositivos]
        with open(ruta_archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print(f"Catálogo guardado exitosamente en '{ruta_archivo}'.")


if __name__ == "__main__":
    catalogo_valido = []
    
    # Prueba 1: Captura controlada de StockInvalidoError
    print("--- Probando validación de stock negativo ---")
    try:
        panel_defectuoso = PanelSolar("Solar 200W", -5, 200)
    except StockInvalidoError as e:
        print(f"Excepción capturada correctamente: {e}")
        
    p1 = PanelSolar("EcoSolar 400W Pro", 15, 400)
    p2 = PanelSolar("NanoSolar 150W", 30, 150)
    
    catalogo_valido.extend([p1, p2])
    
    print("\n--- Fichas Técnicas (Polimorfismo) ---")
    for dispositivo in catalogo_valido:
        print(dispositivo.ficha_tecnica())
        
    GestorInventario.guardar_catalogo_json(catalogo_valido, "catalogo_ecotech.json")