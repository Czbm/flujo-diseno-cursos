---
name: 00p-extractor-perfil-estilo
description: Extrae, calibra o consolida el perfil semántico y de estilo editorial de un docente a partir de corpus real, entrevista guiada o dos extracciones previas, produciendo un perfil compatible con 03.D, 03.E y 04.B.
stage_id: "00.P"
version: "1.0"
status: stable
---

# Skill: Extractor de Perfil Semántico y de Estilo Docente (00.P) — v1.0

## Posición en el flujo

Esta skill es una **pre-etapa persistente y reutilizable** del ecosistema. No sustituye ninguna etapa curricular (`01`–`05`); su función es construir el **Perfil de Estilo y Semántica Docente** (`profiles/perfil-estilo-<id>.md`) que consumen:

- **03.D (Composición Dual):** para conservar la voz didáctica y técnica del docente en la presentación proyectable y la guía docente.
- **03.E (Capítulo de Libro Autónomo):** para redactar capítulos con la semántica, estructura argumentativa y registro documental propios del docente, evitando prosa genérica de IA.
- **04.B (Implementación de Mejoras):** para aplicar correcciones editoriales downstream sin desviar la voz original del autor.

Un mismo perfil puede reutilizarse en **todas las asignaturas** de un docente, independientemente del grado académico o disciplina.

---

## Principios rectores

1. **Evidencia sobre invención:** cada rasgo declarado debe respaldarse en muestras reales o respuestas explícitas del docente. Si un rasgo no tiene evidencia suficiente, se marca como `Bajo / pendiente de validar`.
2. **Separación estricta entre voz espontánea y voz documental:** la forma en que un docente escribe en chats, correos o instrucciones rápidas (*voz espontánea*) **no** se traslada literalmente a documentos finales (*voz documental*). La voz documental conserva la lógica, precisión, vocabulario y estructura del docente, pero eleva el registro lingüístico.
3. **Semántica antes que cosmética:** importa más cómo el docente delimita conceptos, qué distinciones conceptuales defiende, qué ambigüedades rechaza y cómo argumenta, que simples adornos de estilo.
4. **Privacidad y saneamiento:** nunca incluir en el perfil datos confidenciales, nombres de alumnos, información institucional sensible ni citas literales extensas de documentos privados. Los ejemplos de la sección §12 deben ser **reconstrucciones representativas** basadas en patrones observados.

---

## Modos de operación

Al iniciar, identifica qué insumos proporciona el usuario y selecciona el modo correspondiente:

### Modo A — Extracción desde corpus (recomendado)
**Cuándo usarlo:** el docente proporciona 3 o más textos suyos (apuntes de clase, reportes técnicos, correos, guías, artículos, transcripciones o historiales de conversación).

**Procedimiento:**
1. Clasificar cada muestra por tipo (`técnico`, `didáctico`, `conversacional/operativo`, `narrativo`).
2. Extraer patrones recurrentes de tono, formalidad, ritmo, longitud de frases, léxico disciplinar/operativo, conectores, puntuación, argumentación y cierres.
3. Separar explícitamente los marcadores de **voz espontánea** frente a los de **voz documental**.
4. Identificar **distinciones conceptuales fuertes** y **fórmulas de corrección** (qué errores o ambigüedades rechaza el docente).
5. Asignar nivel de confianza (`Alto`, `Medio`, `Bajo`) a cada campo según la cantidad y variedad del corpus.

### Modo B — Entrevista guiada de calibración
**Cuándo usarlo:** el docente no tiene textos a la mano o quiere construir su perfil desde cero de forma interactiva.

**Procedimiento:**
Realizar una entrevista breve (en 1 o 2 rondas máximo) cubriendo:
1. Área disciplinar, grados académicos habituales y relación con el estudiante (`tú` / `usted` / plural).
2. Preferencia entre explicar primero el *por qué funcional/aplicado* o la *definición teórica formal*.
3. Nivel de formalidad deseado en presentaciones vs. capítulos de libro.
4. Tres términos técnicos o distinciones conceptuales que siempre cuida en clase.
5. Qué le molesta o evita en textos generados por IA (relleno, adjetivación vacía, tono motivacional, metáforas forzadas, etc.).
6. Uso de humor y analogías (nulo, ocasional técnico, frecuente cotidiano).
7. Estilo de cierre preferido (síntesis operativa, reto aplicado, pregunta reflexiva).
8. **Mini-prueba de contraste:** mostrar un párrafo técnico-didáctico neutro de 4 líneas y pedirle que diga *"qué le cambiaría o corregiría"* para capturar su patrón real de corrección.

Marcar los campos derivados únicamente de entrevista como confianza `Medio` y listar en §13.13 los textos sugeridos para validación futura.

### Modo C — Consolidación o actualización de perfil (`vN` → `vN+1`)
**Cuándo usarlo:** existen dos extracciones independientes del mismo docente, o se desea calibrar un perfil previo con nuevos textos o después de 5–10 sesiones generadas.

**Procedimiento:**
1. Comparar coincidencias y divergencias campo por campo.
2. Resolver cada divergencia distinguiendo si corresponde a **contextos/registros distintos** (por ejemplo, voz espontánea vs. voz documental) o a una evolución real del estilo.
3. Documentar explícitamente las resoluciones en la **sección §14** y actualizar el número de versión y el registro de cambios al final del archivo.

---

## Contrato de salida fijo (`profiles/perfil-estilo-<id>.md`)

El perfil generado **debe** respetar esta estructura de 14 secciones (puedes tomar [`profiles/crc-referencia.md`](../../profiles/crc-referencia.md) como referencia de formato completo):

```markdown
# Perfil de estilo — [Nombre o identificador del docente]

**Docente:** [Nombre o alias]
**Extraído:** [YYYY-MM-DD]
**Versión:** v1.0
**Modo de extracción:** [Corpus / Entrevista guiada / Consolidación]
**Nivel de confianza global:** [Alto / Medio / Bajo]

---

## 1. Tono
- General, Técnico, Didáctico, Narrativo.
- Tabla de diferencia clave entre **Voz espontánea** y **Voz documental**.

## 2. Nivel de formalidad
- Predominante, modulaciones por tipo de documento y regla de aplicación.

## 3. Ritmo
- Tipo, marcadores estructurales y secuencia habitual de exposición.

## 4. Longitud de frases
- Predominante, distribución (cortas vs. largas/compuestas) y patrón frecuente.

## 5. Vocabulario
- Registro general.
- Palabras recurrentes agrupadas por área (disciplinar, operativa/metodológica, transversal).
- Lista explícita de qué evita (muletillas de IA, ambigüedades, relleno).

## 6. Muletillas y conectores
- Conectores habituales, fórmulas de control, restricciones negativas (si aplican) e imperativos de trabajo (acotados solo a voz espontánea).

## 7. Puntuación
- Comas, punto y coma, dos puntos, guiones, paréntesis y reglas de énfasis/formato en documentos finales.

## 8. Estructura de argumentación
- Tipo (deductiva, inductiva, por casos, por capas), organización de ideas, criterios de defensa, patrón característico de corrección y distinciones conceptuales fuertes.

## 9. Humor
- Presencia, tipo, dosis, contextos permitidos y contextos donde debe estar ausente.

## 10. Metáforas y analogías
- Presencia, tipo, preferencia estructural y regla de uso.

## 11. Cierres
- Tipo, longitud, recursos, qué evita y diferencia entre cierre espontáneo y cierre documental.

## 12. Ejemplos de prosa (reconstrucciones representativas)
- 3 a 5 ejemplos breves (técnico, didáctico, explicativo/operativo, narrativo) con los rasgos que ilustran y nota aclaratoria de reconstrucción.

## 13. Reglas operativas de aplicación
- Principios dominantes del estilo (ej. precisión sobre elegancia, control de alcance, enfoque modular).
- Jerarquía de prioridades estilísticas (orden explícito).
- Regla práctica en 8–10 puntos para imitar el estilo.
- Fórmula sintética del estilo (1 frase).
- **Tabla de aplicación en `03.D` y `03.E`** (elemento → voz a aplicar) + listas explícitas de **Prohibido** y **Permitido y esperado** en entregables finales.
- **Nivel de confianza por campo** (`Alto`, `Medio`, `Bajo`).
- **Validación pendiente** (qué textos faltan para subir confianza).

## 14. Divergencias resueltas y control de versión
- Coincidencias y divergencias resueltas (si aplica Modo C; si es primera extracción en Modo A/B, indicar "Primera extracción base").
- Versión anterior, cambios realizados y fecha o hito sugerido de próxima revisión.
```

---

## Checklist de verificación antes de entregar

- [ ] Se distingue claramente **voz espontánea** de **voz documental**.
- [ ] Existen listas explícitas de **Prohibido** y **Permitido y esperado** para `03.D` y `03.E`.
- [ ] Cada grupo de campos tiene declarado su **nivel de confianza** (`Alto / Medio / Bajo`).
- [ ] Los ejemplos de §12 son reconstrucciones representativas sin datos privados ni institucionales sensibles.
- [ ] El archivo se guarda en `profiles/perfil-estilo-<id>.md` (sin sobrescribir `profiles/template-perfil-estilo.md`).
