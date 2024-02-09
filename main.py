from datetime import date

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

class Paquete:
    def __init__(self, cliente):
        self.cliente = cliente

class CompaniaAerea:
    def __init__(self):
        self.paquetes_transportados = []
        self.total_recaudado = 0

    def transportar_paquete(self, paquete):
        self.paquetes_transportados.append(paquete)
        self.total_recaudado += 10

    def generar_reporte_diario(self, fecha):
        total_paquetes = len(self.paquetes_transportados)
        return f"Reporte del {fecha}:" \
               f"\nTotal de paquetes transportados:" \
               f" {total_paquetes}\nTotal recaudado:" \
               f" ${self.total_recaudado}"

# Ejemplo de uso
if __name__ == "__main__":
    cliente1 = Cliente("Cliente1")
    cliente2 = Cliente("Cliente2")

    compania = CompaniaAerea()

    paquete1 = Paquete(cliente1)
    paquete2 = Paquete(cliente2)

    # Simulación de transportar paquetes
    compania.transportar_paquete(paquete1)
    compania.transportar_paquete(paquete2)

    # Obtener la fecha actual (puede cambiar según tus necesidades)
    fecha_actual = date.today()

    # Generar y mostrar el reporte diario con la fecha actual
    reporte_diario = compania.generar_reporte_diario(fecha_actual)
    print(reporte_diario)



