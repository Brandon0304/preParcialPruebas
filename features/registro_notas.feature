Feature: Registro de notas académicas
  As a professor
  I want to register student grades
  So that I can track their academic performance

  Scenario: Registro exitoso de una nota aprobatoria
    Given el sistema de notas está inicializado
    When registro la nota 4.5 para el estudiante "Carlos" en "Matemáticas" semestre "2024-1"
    Then el promedio de "Carlos" debe ser 4.5
    And el estado de "Carlos" en "Matemáticas" debe ser "APROBADO"

  Scenario: Error al registrar nota fuera de rango
    Given el sistema de notas está inicializado
    When intento registrar la nota 6.0 para el estudiante "Carlos" en "Física" semestre "2024-1"
    Then el sistema debe lanzar un error de rango
