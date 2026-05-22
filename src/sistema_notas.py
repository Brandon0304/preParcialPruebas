class SistemaNotas:
    def __init__(self):
        # almacenamiento simple: { (estudiante, materia, semestre): nota }
        self.notas = {}

    def registrar_nota(self, estudiante, materia, semestre, nota):
        if nota < 0.0 or nota > 5.0:
            raise ValueError("Nota fuera de rango")
        
        clave = (estudiante, materia, semestre)
        self.notas[clave] = nota
        return True

    def obtener_estado(self, estudiante, materia, semestre):
        clave = (estudiante, materia, semestre)
        nota = self.notas.get(clave)
        
        if nota is None:
            return None
        
        return "APROBADO" if nota >= 3.0 else "REPROBADO"

    def calcular_promedio(self, estudiante):
        notas_estudiante = [nota for (est, mat, sem), nota in self.notas.items() if est == estudiante]
        
        if not notas_estudiante:
            return 0.0
            
        return sum(notas_estudiante) / len(notas_estudiante)
