---

**ACTIVIDAD PREPARATORIA — PRIMER PARCIAL**
**Asignatura: Pruebas de Software | Semestre V**
**Tiempo estimado: 1 hora 45 minutos**
**Entrega: Repositorio GitHub público**

---

**CONTEXTO DEL CASO**

La Universidad Regional del Sur necesita un módulo de **registro de notas académicas**. El Product Owner entregó estos requerimientos. No existe ningún código todavía.

1. Un estudiante puede registrar una nota para una materia. La nota debe estar entre 0.0 y 5.0.
2. El sistema determina si el estudiante aprueba o reprueba una materia. Aprueba con nota mayor o igual a 3.0.
3. El sistema calcula el promedio de todas las notas registradas de un estudiante.
4. No se puede registrar dos notas para la misma materia en el mismo semestre. Si se intenta, el sistema debe lanzar un error claro.

Tu trabajo es construir este sistema desde cero aplicando todo lo visto en clase.

---

**TECNOLOGÍA**

Usa el lenguaje y las herramientas de tu preferencia. Lo que importa es que apliques correctamente las metodologías. Algunas opciones válidas:

- Python con `uv` + `pytest` + `pytest-bdd`
- Java con Maven + JUnit 5 + Cucumber
- JavaScript con npm + Jest + Cucumber.js

Cualquier otra combinación es válida siempre que permita hacer TDD, BDD con Gherkin y un pipeline CI/CD en GitHub Actions. Documenta en el README qué tecnología elegiste y por qué.

---

**ESTRUCTURA DEL REPOSITORIO**

La estructura debe ser coherente con la tecnología elegida, pero el repositorio debe contener obligatoriamente:

- El código de producción en una carpeta separada de los tests
- Un archivo con los tests unitarios TDD
- Un archivo `.feature` con los escenarios en Gherkin
- Los step definitions del BDD
- El archivo de workflow de GitHub Actions
- El README completo

Haz un primer commit con solo la estructura y configuración antes de escribir cualquier lógica. Ese commit muestra que entiendes cómo organizar un proyecto.

---

**PARTE 1 — Análisis escrito en el README (15 minutos)**

Antes de escribir cualquier test o código, documenta tu análisis en el README. Este análisis es evidencia de que pensaste como tester antes de teclear.

**1.1 — Particiones de equivalencia**

Para el requerimiento 1 (nota entre 0.0 y 5.0) construye una tabla con todas las particiones que identificas: nombre de la partición, rango que cubre, el valor representativo que usarías para probarla y el resultado que esperas. Debe haber particiones tanto válidas como inválidas.

**1.2 — Análisis de valores límite**

Para el mismo requerimiento construye una tabla con los valores críticos en cada borde del rango. Para cada valor indica si está dentro o fuera del rango y qué resultado esperas. Recuerda la regla: el valor justo antes del límite, el límite exacto y el valor justo después.

**1.3 — Preguntas al Product Owner**

Para el requerimiento 4 (no duplicar nota), escribe mínimo dos preguntas que le harías al Product Owner antes de diseñar cualquier prueba. Explica brevemente por qué cada pregunta impacta el diseño de los casos de prueba. Una pregunta sin justificación no cuenta.

Haz commit de este análisis con un mensaje descriptivo antes de continuar.

---

**PARTE 2 — Diseño formal de casos de prueba (20 minutos)**

Diseña los casos de prueba usando el formato estándar visto en clase. Estos casos son el documento que le entregarías a cualquier tester del equipo para que ejecute las pruebas manualmente, independientemente del código.

Construye la tabla con los siguientes campos para cada caso:

```
ID | Requerimiento | Descripción | Precondición | Datos de entrada | Pasos | Resultado esperado | Tipo
```

El campo Tipo puede ser: Positivo, Negativo o Borde.

Debes diseñar mínimo 12 casos de prueba distribuidos así:

- Al menos 3 casos para el requerimiento 1, cubriendo particiones válidas, inválidas y valores límite
- Al menos 3 casos para el requerimiento 2, cubriendo el límite de aprobación desde ambos lados
- Al menos 3 casos para el requerimiento 3, incluyendo el caso de estudiante sin notas
- Al menos 3 casos para el requerimiento 4, incluyendo el caso de misma materia en semestre diferente

Esta tabla va en el README del repositorio. Haz commit cuando esté completa.

---

**PARTE 3 — Ciclo TDD completo (35 minutos)**

Implementa los 4 requerimientos usando el ciclo Red-Green-Refactor que practicamos. El historial de commits de Git debe evidenciar que seguiste el proceso. Se revisan los commits, no solo el resultado final.

El flujo esperado es este: escribes los tests para un requerimiento sin implementar nada, haces commit indicando que es la fase RED. Luego escribes el código mínimo para que los tests pasen, haces commit indicando GREEN. Luego mejoras el código sin romper los tests, haces commit indicando REFACTOR. Repites para cada requerimiento.

Sobre los tests: los casos de prueba que diseñaste en la Parte 2 son tu guía. Cada caso de prueba de la tabla debe tener su test automatizado correspondiente. Los tests deben tener nombres que describan qué verifican. Cada test debe probar una sola cosa.

Sobre la implementación: diseña la clase o las funciones que consideres necesarias. No hay una estructura impuesta pero el código debe ser limpio, con responsabilidades claras y sin lógica mezclada.

Al terminar ejecuta el reporte de cobertura y pega el output en el README. La cobertura debe superar el 85%.

---

**PARTE 4 — BDD en Gherkin (20 minutos)**

Escribe el archivo `.feature` con escenarios en Gherkin para los requerimientos 2, 3 y 4.

El archivo debe cumplir lo siguiente:

- La declaración `Feature` debe incluir el contexto del usuario en lenguaje de negocio, explicando quién usa el sistema y para qué
- Usar `Background` si hay una precondición que se repite en varios escenarios
- Mínimo 6 escenarios en total entre los tres requerimientos
- Al menos un `Scenario Outline` con tabla `Examples` que pruebe múltiples combinaciones de datos
- Al menos un escenario que pruebe el camino de error con resultado esperado claro
- Tags en todos los escenarios usando `@smoke`, `@critical` o `@regression` según corresponda

Los escenarios deben estar escritos en lenguaje de negocio. Si alguien sin conocimientos técnicos no puede entenderlos, no están bien escritos.

Implementa los step definitions conectando cada paso del Gherkin con el código ya construido en la parte anterior. Los steps deben manejar tanto los casos exitosos como los de error.

Ejecuta los tests BDD y verifica que todos pasen antes de hacer commit.

---

**PARTE 5 — Pipeline CI/CD (10 minutos)**

Configura GitHub Actions para que los tests corran automáticamente en cada push a la rama principal.

El pipeline debe instalar las dependencias, ejecutar los tests unitarios y los tests BDD juntos, generar el reporte de cobertura y fallar si algún test no pasa o si la cobertura baja del 80%.

Haz push y entra a la pestaña Actions de tu repositorio. El pipeline debe quedar en verde. Si queda en rojo, corrige antes de entregar. Un pipeline en rojo al momento de la revisión descuenta puntos directamente.

---

**PARTE 6 — Reflexión en el README (5 minutos)**

Al final del README incluye dos párrafos cortos respondiendo lo siguiente:

Primero: ¿qué diferencia notaste entre diseñar los casos de prueba en la tabla antes de escribir código versus simplemente ponerte a programar directamente?

Segundo: ¿qué fue lo más difícil de seguir el ciclo TDD y en qué momento sentiste la tentación de saltarte algún paso?

---

**LO QUE SE REVISARÁ**

El repositorio debe tener mínimo 10 commits con mensajes claros que muestren la evolución del trabajo. Se verificará que los commits de RED no tengan código de producción, que los de GREEN tengan implementación mínima y que los de REFACTOR mejoren sin romper nada.

El pipeline debe estar en verde. Todos los tests deben pasar. La cobertura debe superar el 85%. La tabla de casos de prueba debe estar completa y bien estructurada. El archivo `.feature` debe estar en lenguaje natural comprensible. El análisis del README debe demostrar pensamiento de tester antes que de desarrollador.

---

**ENTREGA**

Comparte el link del repositorio GitHub público en el foro del curso antes de que termine la sesión. El repositorio debe ser público para que se pueda revisar el historial de commits, el pipeline y el código.

---

**CRITERIOS DE EVALUACIÓN**

| Criterio | Puntos |
|---|---|
| Análisis en README: particiones, límites, preguntas al PO | 10 |
| Tabla de casos de prueba: mínimo 12, bien estructurados y distribuidos | 20 |
| Ciclo TDD evidenciado en commits 🔴🟢🔵 por cada requerimiento | 15 |
| Tests automatizados completos con cobertura ≥ 85% | 15 |
| Implementación correcta, limpia y con responsabilidades claras | 10 |
| Archivo Gherkin con mínimo 6 escenarios bien escritos en lenguaje de negocio | 15 |
| Step definitions funcionando y conectados al código | 10 |
| Pipeline en verde en GitHub Actions | 5 |
| **Total** | **100** |