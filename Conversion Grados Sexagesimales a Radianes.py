import math

class ConversorAngulos:
    def grados_a_radianes(self, grados: float) -> float:
        return math.radians(grados)

    def radianes_a_grados(self, radianes: float) -> float:
        return math.degrees(radianes)


if __name__ == "__main__":
    # Ejemplo de uso
    conversor = ConversorAngulos()

    # Convertir de grados a radianes
    grados = float(input("Ingrese el ángulo en grados sexagesimales: "))
    radianes = conversor.grados_a_radianes(grados)
    print(f"{grados} grados son {radianes:.4f} radianes")

    # Convertir de radianes a grados
    radianes = float(input("Ingrese el ángulo en radianes: "))
    grados = conversor.radianes_a_grados(radianes)
    print(f"{radianes:.4f} radianes son {grados:.4f} grados sexagesimales")