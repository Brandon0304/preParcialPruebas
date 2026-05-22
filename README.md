# Sistema de Registro de Notas Académicas

Este proyecto es una solución para la Universidad Regional del Sur, construida como parte de la actividad preparatoria para el primer parcial de Pruebas de Software.

## Tecnologías Elegidas

- **Lenguaje:** Python 3.x
- **Gestor de paquetes:** pip (o uv)
- **Framework de Pruebas:** `pytest` (para TDD y pruebas unitarias)
- **Pruebas BDD:** `pytest-bdd` (para escenarios Gherkin)
- **CI/CD:** GitHub Actions

### Justificación
Se eligió Python por su sintaxis clara y legible, ideal para demostrar ciclos de TDD (Red-Green-Refactor). `pytest` es un estándar en la industria para pruebas robustas, y `pytest-bdd` permite una integración nativa de escenarios Gherkin con el código de prueba, facilitando el cumplimiento de los requerimientos de comportamiento (BDD).

---

## Estructura del Proyecto

- `src/`: Código de producción.
- `tests/`: Pruebas unitarias para el ciclo TDD.
- `features/`: Archivos `.feature` (Gherkin) y definiciones de pasos (BDD).
- `.github/workflows/`: Configuración del pipeline de CI.

---

## Análisis Escrito (Parte 1)

### 1.1 — Particiones de equivalencia
Para el requerimiento 1 (nota entre 0.0 y 5.0), identificamos las siguientes particiones:

| Nombre de la Partición | Rango | Valor Representativo | Resultado Esperado |
| :--- | :--- | :--- | :--- |
| **Nota válida (Reprobación)** | 0.0 ≤ nota < 3.0 | 1.5 | Nota registrada (Reprueba) |
| **Nota válida (Aprobación)** | 3.0 ≤ nota ≤ 5.0 | 4.2 | Nota registrada (Aprueba) |
| **Nota inválida (Inferior)** | nota < 0.0 | -1.0 | Error: Nota fuera de rango |
| **Nota inválida (Superior)** | nota > 5.0 | 5.5 | Error: Nota fuera de rango |
| **Entrada No Numérica** | No numérico | "A" | Error: Tipo de dato inválido |

### 1.2 — Análisis de valores límite
Para el mismo requerimiento, los valores críticos en los bordes son:

| Valor Crítico | ¿Está dentro del rango? | Resultado Esperado | Explicación |
| :--- | :--- | :--- | :--- |
| **-0.1** | No | Error | Justo debajo del límite inferior (0.0). |
| **0.0** | Sí | Válido (Reprueba) | Límite inferior exacto. |
| **0.1** | Sí | Válido (Reprueba) | Justo encima del límite inferior (0.0). |
| **2.9** | Sí | Válido (Reprueba) | Justo debajo del límite de aprobación (3.0). |
| **3.0** | Sí | Válido (Aprueba) | Límite exacto de aprobación. |
| **3.1** | Sí | Válido (Aprueba) | Justo encima del límite de aprobación (3.0). |
| **4.9** | Sí | Válido (Aprueba) | Justo debajo del límite superior (5.0). |
| **5.0** | Sí | Válido (Aprueba) | Límite superior exacto. |
| **5.1** | No | Error | Justo encima del límite superior (5.0). |

### 1.3 — Preguntas al Product Owner
Respecto al requerimiento 4 (no duplicar notas en el mismo semestre):

1. **¿Qué formato exacto define un "semestre" (ej. "2024-1", o un rango de fechas) y cómo se asocia al estudiante?**
   - *Justificación:* Impacta el diseño de los casos de prueba porque determina qué datos de entrada necesito para probar registros en diferentes semestres. Sin esto, no puedo validar si el sistema distingue correctamente entre un duplicado inválido y un registro legítimo en un periodo distinto.
2. **¿El sistema debe permitir la edición de una nota si hubo un error en el primer registro, o el bloqueo por duplicidad es absoluto?**
   - *Justificación:* Esto define si debo diseñar casos de prueba para "Actualización de nota" o si el resultado esperado siempre debe ser un error ante cualquier segundo intento. Afecta directamente la lógica de negocio y los flujos alternos.

---

## Diseño Formal de Casos de Prueba (Parte 2)

| ID | Requerimiento | Descripción | Precondición | Datos de entrada | Pasos | Resultado esperado | Tipo |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **CP01** | R1 | Registro de nota mínima válida | Estudiante existe | nota: 0.0 | Registrar nota | Nota guardada exitosamente | Borde |
| **CP02** | R1 | Registro de nota máxima válida | Estudiante existe | nota: 5.0 | Registrar nota | Nota guardada exitosamente | Borde |
| **CP03** | R1 | Registro de nota superior al límite | Estudiante existe | nota: 5.1 | Registrar nota | Error: Nota fuera de rango | Negativo |
| **CP04** | R2 | Aprobación en límite exacto | Estudiante con nota 3.0 | nota: 3.0 | Consultar estado | Estado: "APROBADO" | Borde |
| **CP05** | R2 | Reprobación justo bajo el límite | Estudiante con nota 2.9 | nota: 2.9 | Consultar estado | Estado: "REPROBADO" | Borde |
| **CP06** | R2 | Aprobación con nota alta | Estudiante con nota 4.5 | nota: 4.5 | Consultar estado | Estado: "APROBADO" | Positivo |
| **CP07** | R3 | Promedio con varias notas | Estudiante con notas: 3, 4, 5 | notas: [3.0, 4.0, 5.0] | Calcular promedio | Promedio: 4.0 | Positivo |
| **CP08** | R3 | Promedio de estudiante sin notas | Estudiante nuevo | - | Calcular promedio | Error o 0.0 (según definición) | Negativo |
| **CP09** | R3 | Promedio con nota decimal | Estudiante con notas: 3.5, 4.5 | notas: [3.5, 4.5] | Calcular promedio | Promedio: 4.0 | Positivo |
| **CP10** | R4 | Registro duplicado misma materia/semestre | Nota ya registrada | materia: "Matemáticas", semestre: "2024-1" | Intentar registrar misma materia/semestre | Error: Nota duplicada | Negativo |
| **CP11** | R4 | Misma materia en diferente semestre | Nota previa en "2023-2" | materia: "Matemáticas", semestre: "2024-1" | Registrar materia en nuevo semestre | Nota guardada exitosamente | Positivo |
| **CP12** | R4 | Diferentes materias mismo semestre | Estudiante con nota en "Física" | materia: "Química", semestre: "2024-1" | Registrar nueva materia | Nota guardada exitosamente | Positivo |

---

## Guía de ejecución

Para probar el sistema, primero instalé las dependencias necesarias:

```bash
pip install pytest pytest-bdd
```

### Ejecutar pruebas
Para correr todos los tests que hice (tanto los de TDD como los de BDD), usé estos comandos:

- **Tests unitarios (TDD):**
  ```bash
  pytest tests/
  ```

- **Escenarios BDD (Gherkin):**
  ```bash
  pytest features/
  ```

Con esto se verifica que todos los requerimientos del Product Owner funcionan como se espera.
