import pytest
from pytest_bdd import scenario, given, when, then, parsers
from src.sistema_notas import SistemaNotas

@scenario('../registro_notas.feature', 'Registro exitoso de una nota aprobatoria')
def test_registro_exitoso():
    pass

@scenario('../registro_notas.feature', 'Error al registrar nota fuera de rango')
def test_registro_error_rango():
    pass

@pytest.fixture
def sistema():
    return SistemaNotas()

@given('el sistema de notas está inicializado', target_fixture='sistema_inst')
def sistema_inst(sistema):
    return sistema

@when(parsers.parse('registro la nota {nota:f} para el estudiante "{estudiante}" en "{materia}" semestre "{semestre}"'))
def registrar_nota(sistema_inst, estudiante, materia, semestre, nota):
    sistema_inst.registrar_nota(estudiante, materia, semestre, nota)

@when(parsers.parse('intento registrar la nota {nota:f} para el estudiante "{estudiante}" en "{materia}" semestre "{semestre}"'))
def registrar_nota_invalida(sistema_inst, estudiante, materia, semestre, nota):
    try:
        sistema_inst.registrar_nota(estudiante, materia, semestre, nota)
        pytest.fail("Debería haber lanzado un ValueError")
    except ValueError as e:
        pytest.error_msg = str(e)

@then(parsers.parse('el promedio de "{estudiante}" debe ser {promedio:f}'))
def verificar_promedio(sistema_inst, estudiante, promedio):
    assert sistema_inst.calcular_promedio(estudiante) == promedio

@then(parsers.parse('el estado de "{estudiante}" en "{materia}" debe ser "{estado}"'))
def verificar_estado(sistema_inst, estudiante, materia, estado):
    # Nota: Aquí usamos un valor por defecto para el semestre ya que el feature no lo escala, 
    # pero en una implementación real este step debería ser más preciso.
    assert sistema_inst.obtener_estado(estudiante, materia, "2024-1") == estado

@then('el sistema debe lanzar un error de rango')
def verificar_error_rango():
    assert pytest.error_msg == "Nota fuera de rango"
