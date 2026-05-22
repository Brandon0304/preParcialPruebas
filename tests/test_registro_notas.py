import pytest
from src.sistema_notas import SistemaNotas

def test_registrar_nota_minima_valida():
    sistema = SistemaNotas()
    # CP01: Registro de nota 0.0
    resultado = sistema.registrar_nota("Juan", "Matemáticas", "2024-1", 0.0)
    assert resultado == True

def test_registrar_nota_superior_limite_invalida():
    sistema = SistemaNotas()
    # CP03: Registro de nota 5.1 (Debe fallar)
    with pytest.raises(ValueError, match="Nota fuera de rango"):
        sistema.registrar_nota("Juan", "Matemáticas", "2024-1", 5.1)

def test_determinar_aprobacion_limite_exacto():
    sistema = SistemaNotas()
    # CP04: Nota 3.0 es APROBADO
    sistema.registrar_nota("Juan", "Matemáticas", "2024-1", 3.0)
    estado = sistema.obtener_estado("Juan", "Matemáticas", "2024-1")
    assert estado == "APROBADO"

def test_calcular_promedio_varias_notas():
    sistema = SistemaNotas()
    # CP07: Promedio de 3.0, 4.0, 5.0 es 4.0
    sistema.registrar_nota("Juan", "Matemáticas", "2024-1", 3.0)
    sistema.registrar_nota("Juan", "Física", "2024-1", 4.0)
    sistema.registrar_nota("Juan", "Química", "2024-1", 5.0)
    assert sistema.calcular_promedio("Juan") == 4.0

def test_calcular_promedio_sin_notas():
    sistema = SistemaNotas()
    # CP08: Estudiante sin notas
    assert sistema.calcular_promedio("Pedro") == 0.0

def test_error_registrar_duplicado_misma_materia_semestre():
    sistema = SistemaNotas()
    # CP10: Registro duplicado misma materia/semestre
    sistema.registrar_nota("Juan", "Matemáticas", "2024-1", 4.0)
    with pytest.raises(ValueError, match="La nota para esta materia ya fue registrada en este semestre"):
        sistema.registrar_nota("Juan", "Matemáticas", "2024-1", 3.5)

def test_registrar_misma_materia_diferente_semestre():
    sistema = SistemaNotas()
    # CP11: Misma materia en diferente semestre
    sistema.registrar_nota("Juan", "Matemáticas", "2023-2", 4.0)
    resultado = sistema.registrar_nota("Juan", "Matemáticas", "2024-1", 3.5)
    assert resultado == True
