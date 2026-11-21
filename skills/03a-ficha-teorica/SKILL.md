---
name: 03a-ficha-teorica
description: Desarrolla la Ficha Teorica de una sesion con conceptos clasificados por nivel de desarrollo, bibliografia academica y continuidad curricular.
stage_id: "03.A"
version: "1.12"
status: stable
---

# Ficha Teórica (03a) — Versión cerrada v1.12

## Posición en el flujo

Esta skill alimenta a **03d (Composición Dual)** y a **03e (Capítulo de Libro Autónomo)**. Su salida —la Ficha Teórica— es consumida directamente en la Fase 1 y Fase 3 de 03d, y en la Fase 2 de 03e para:

- alimentar los slides de teoría y de aplicación;
- nutrir la articulación curricular;
- aportar mini-fichas para el refuerzo inicial;
- alimentar la categoría A (bibliografía académica) del 60/20/20;
- clasificar cada concepto en un nivel de desarrollo (Núcleo / Panorama / Propedéutico / Contexto / Reservado);
- categorizar los conceptos Reservado según su continuidad curricular y **fundamentar su exclusión cuando aplica**;
- elevar a Panorama los Reservados que pertenecen al campo de acción del subtema actual;
- priorizar fuentes en español y de origen mexicano o latinoamericano;
- reportar lagunas y advertencias al docente;
- aportar el peso heredado de cada concepto para trazabilidad con el Brief;
- **verificar la suficiencia conceptual de los eslabones de competencia que el Brief declara (NUEVO en v1.12)**.

**Nota de compatibilidad:** esta skill requiere que el Brief sea **v2.8** (o superior) y que el Doc Maestro sea **v1.5** (o superior). Si el Brief es v2.7, se acepta, y el campo `Eslabones de competencia cubiertos` se marca como `no declarado`. Si el Brief es v2.6 o anterior, se declara `no declarado` en el campo de alcance y se reporta al usuario.

**Versión autocontenida.** Esta versión no depende de versiones anteriores. Todo el contenido vigente está expandido literalmente.

### Resumen de capacidades por versión

- **v1.7:** bloque L reformulado como "Articulación curricular".
- **v1.8:** regla de calibración por verbo y nivel educativo (§1.6.7).
- **v1.9:** regla de elevación Reservado→Panorama por campo de acción (§1.6.2 bis).
- **v1.10:** regla de fundamento obligatorio de exclusión (§1.6.2 ter).
- **v1.11:** consolidación autocontenida + referencias a Brief v2.7 y Doc Maestro v1.5.
- **v1.12:** regla de suficiencia conceptual por eslabón de competencia (§1.6.8) + campo `Eslabones de competencia cubiertos` en metadatos + reglas 85–92 + verificaciones y criterios nuevos.

---

## Propósito

Esta skill toma el **Brief v2.8** y produce la **Ficha Teórica** de la sesión: el conjunto de conceptos, corrientes teóricas, fuentes verificables, articulación curricular y lagunas declaradas que sostienen la clase.

Esta skill **no investiga el tema al azar**. Su trabajo es descomponer el subtema oficial con **expansión conceptual controlada**: identificar los conceptos nucleares que el alumno debe dominar, los conceptos panorámicos que debe reconocer sin dominar todavía, los conceptos **propedéuticos** que se introducen ahora porque una competencia posterior los requiere, los conceptos de contexto que aportan marco, y los conceptos reservados que corresponden a sesiones posteriores o quedan fuera del curso.

**Calibración por contexto curricular:** la amplitud de la expansión no es universal. Depende de **seis factores** que se leen desde el Brief y el Doc Maestro:

1. El temario oficial: qué permite y qué reserva.
2. La articulación curricular: qué materias anteceden y qué materias siguen.
3. El perfil profesional de la carrera.
4. El nivel académico del alumno (cuatrimestre).
5. El verbo del objetivo de aprendizaje y el nivel educativo del programa.
6. La pertenencia al campo de acción del subtema.

**Verificación de suficiencia conceptual (v1.12):** además, la skill verifica que el desarrollo conceptual sea suficiente para cubrir los eslabones de competencia que el Brief declara (introduce / desarrolla / aplica / evalúa).

**Prioridad idiomática y geográfica:** al buscar fuentes, se prefieren las de origen mexicano o latinoamericano en español. Solo se expande a fuentes españolas o extranjeras cuando no hay opción nacional o regional (§1.7).

**No investiga teoría** fuera del tema. **No busca normativa** (eso es 03b). **No busca imágenes** (eso es 03c). **No compone la sesión** (eso es 03d y 03e). Solo clasifica, jerarquiza, articula, verifica suficiencia y cita.

---

## Cuándo activar esta skill

Actívala cuando el usuario:

- Tenga ya generados el **Brief v2.8** y el Doc Maestro v1.5.
- Pida "ficha teórica de la sesión N", "conceptos de la sesión", "marco teórico de la sesión", o similar.
- Quiera alimentar la composición de 03d y el capítulo de 03e con conceptos clasificados por nivel.

No la actives si falta el Brief v2.8. Si falta, remite a la skill 02.

---

## Estructura final de la skill

```
A.  Metadatos
B.  Bloques conceptuales (5 niveles + categoría de reserva + fundamento de exclusión)
C.  Fuentes académicas (categoría A — 60% ponderado)
C.bis Fuentes científicas e institucionales (categoría C — 20%)
D.  Fuentes web confiables (categoría B — 20%)
E.  Fuentes de contraste y actualización
F.  Citas textuales autorizadas
G.  Conceptos que requieren aplicación práctica
H.  Lagunas declaradas
I.  Advertencias para composición
J.  Derivaciones a otras skills
K.  Mini-fichas de refuerzo
L.  Articulación curricular
```

---

## A. Metadatos (siempre)

| Campo | Ejemplo |
|---|---|
| Asignatura | Topografía |
| Clave | LIA0525 |
| Cuatrimestre | 5° |
| Sesión | 4 |
| Subtemas cubiertos | 1.4 |
| Nivel de profundidad | Heredado literal del Brief |
| Tipo de sesión | Heredado literal del Brief |
| **Alcance conceptual del subtema** | **literal con extensión propedéutica** |
| **Verbo principal del objetivo** | **utilizar / realizar** |
| **Nivel educativo del programa** | **licenciatura** |
| **Piso mínimo de exigencia** | **Núcleo para conceptos operativos** |
| **Nivel académico del alumno** | **5° cuatrimestre** |
| **Contexto curricular — materias antecedentes** | **Matemáticas aplicadas, Dibujo de representación, Geometría II** |
| **Contexto curricular — materias consecuentes** | **Modelación digital, Diseño Arquitectónico IV, Topografía** |
| **Perfil profesional de la carrera** | **Ingeniero-Arquitecto, contexto Mérida, Yucatán** |
| **Pesos por subtema heredados** | **1.4=medio** |
| **Modo de composición** | **operativo** |
| **Eslabones de competencia cubiertos** | **C2=desarrolla** (NUEVO en v1.12) |
| **Corriente teórica dominante** | **Sistémica (enfoque técnico-metrórico)** |
| **Área disciplinar** | **Representación** |
| **Contexto geográfico** | **Mérida, Yucatán** |
| Brief origen (versión y fecha) | v2.8, YYYY-MM-DD |
| Doc Maestro (versión) | v1.5, YYYY-MM-DD |
| Ficha versión | v1.12 |
| Fecha de generación | YYYY-MM-DD |

**Reglas:**

- Los campos `Alcance conceptual`, `Verbo principal del objetivo`, `Nivel educativo`, `Piso mínimo de exigencia`, `Nivel académico`, `Contexto curricular`, `Perfil profesional` y `Eslabones de competencia cubiertos` son obligatorios. Gobiernan la calibración de la expansión conceptual y la verificación de suficiencia.
- Si el Brief es v2.7 o anterior, el campo `Eslabones de competencia cubiertos` se marca como `no declarado` y se reporta al usuario. No se aplica §1.6.8.
- Si el Brief es v2.6 o anterior, el campo `Alcance conceptual` se marca como `no declarado` y se reporta.
- Si el Doc Maestro no declara nivel educativo, se infiere del nombre del programa (bachillerato / técnico / licenciatura / posgrado) y se reporta.

---

## 1.6 Regla de expansión conceptual controlada

### 1.6.1 Test de denominación amplia

**Señales de denominación amplia (aplica expansión):**
- El subtema usa términos como "sistemas de", "fundamentos de", "introducción a", "principios de", "métodos de", "tipos de".
- El temario no enumera los subconceptos que la disciplina reconoce bajo esa denominación.
- La disciplina reconoce múltiples subconceptos bajo esa denominación.

**Señales de denominación literal (no aplica expansión por defecto):**
- El subtema nombra una técnica, procedimiento o producto específico.
- Se puede enseñar como unidad autocontenida sin depender de subconceptos.
- El temario enumera explícitamente los subconceptos.

**Correspondencia con el campo `Alcance conceptual` del Brief:**

| Alcance declarado en Brief | Comportamiento de 03.A |
|---|---|
| `literal` | No expande por defecto. **Excepción 1:** si hay competencia posterior documentada que requiere conceptos propedéuticos, se activan como Propedéutico (§1.6.3). **Excepción 2:** si hay conceptos de la misma familia del subtema que pertenecen a sesiones posteriores, se elevan a Panorama (§1.6.2 bis). |
| `literal con extensión propedéutica` | Expande solo para introducir conceptos propedéuticos. **Excepción v1.8:** si el verbo es operativo y el nivel educativo es licenciatura o superior, los Propedéuticos que el verbo requiera suben a Núcleo (§1.6.7). **Excepción v1.9:** los Reservados de la misma familia conceptual suben a Panorama (§1.6.2 bis). |
| `amplio` | Expande en 5 niveles. |
| `panorámico` | Expande con énfasis en Panorama y Propedéutico. Núcleo reducido. |

### 1.6.2 Clasificación de 5 niveles + categoría de reserva

Cada concepto derivado recibe uno de cinco niveles. Si el nivel es Reservado, además recibe una **categoría de reserva**.

| Nivel | Definición | Profundidad | Fuentes requeridas | Consumo downstream |
|---|---|---|---|---|
| **Núcleo** | Central. Se enseña, se aplica, se evalúa. | Completa según peso. | Base + contraste (2+ fuentes). | 03d: minutos completos. 03e: prosa completa + ejemplos + aplicación + ejercicios. |
| **Panorama** | Pertenece al tema pero su técnica se verá después. Se presenta conceptualmente. | Definición + ejemplo + relación con el resto. Sin ejercicios ni cálculo. | 1 fuente. | 03d: 2–3 min máximo. 03e: 3–6 párrafos agrupados. |
| **Propedéutico** | Se introduce ahora porque una competencia posterior documentada lo requiere. No se practica. | Definición + ejemplo breve + remisión al momento donde se retoma. | 1 fuente (o 0 si es conceptual). | 03d: 2–4 min. 03e: 2–4 párrafos. |
| **Contexto** | Antecedente o referencia. Ayuda a entender el tema. | Mención breve (1–2 líneas). | 1 fuente o ninguna. | 03d: mención dentro de otro bloque. 03e: 1–2 líneas. |
| **Reservado** | No se desarrolla ahora. Requiere categoría de reserva. | Solo remisión por nombre. | Ninguna. | 03d: transición. 03e: remisión en E.5. |

**Categorías de reserva (solo para nivel Reservado):**

| Categoría | Definición | Requiere mención de destino |
|---|---|---|
| **Continuidad explícita** | Existe un capítulo posterior identificado en la colección. | Sí (nombre del capítulo) |
| **Aplicación posterior** | Se retomará dentro de prácticas o uso de instrumentos. | Sí (momento donde se retoma) |
| **Fuera del curso** | No existe desarrollo previsto en el programa. | **Sí (fundamento obligatorio, §1.6.2 ter)** |

**Distinción clave entre Panorama y Reservado con Continuidad explícita:**

| Aspecto | Panorama | Reservado con Continuidad explícita |
|---|---|---|
| ¿Pertenece al campo de acción del subtema actual? | **Sí** | **No** |
| ¿Recibe definición? | Sí | No |
| ¿Recibe ejemplo? | Sí | No |
| ¿Recibe fuente académica? | Sí (1 fuente) | No |
| ¿Recibe remisión al destino? | Sí | Sí |
| ¿Consume tiempo en 03d? | 2–3 min | 0 min |
| ¿Aparece en capítulo 03e? | Sí (3–6 párrafos) | Solo remisión en E.5 |

### 1.6.2 bis Regla de elevación de Reservado a Panorama por campo de acción

**Propósito:** evitar que conceptos que pertenecen al campo de acción del subtema actual queden como Reservados sin descripción.

**Cuándo se aplica:**

Un concepto clasificado como **Reservado con Continuidad explícita** debe elevarse a **Panorama** si cumple **los cuatro criterios**:

1. **Pertenece a la misma familia conceptual del subtema actual.**
2. **La disciplina reconoce el concepto como parte natural del tema.**
3. **Desarrollarlo operativamente ahora no corresponde.**
4. **Presentarlo conceptualmente completa el campo del subtema sin invadir la sesión posterior.**

**Efectos de la elevación:**

| Elemento | Antes (Reservado) | Después (Panorama) |
|---|---|---|
| Nivel | Reservado | Panorama |
| Categoría de reserva | Continuidad explícita | No aplica |
| Definición | No | Sí (breve) |
| Ejemplo | No | Sí (mínimo) |
| Relación con el tema | No | Sí (explícita) |
| Remisión al destino | Sí | Sí (mantenida) |
| Fuente académica | No | Sí (1 fuente) |
| Ejercicios / Operación / Evaluación | No | No |
| Consumo en 03d | 0 min | 2–3 min |
| Consumo en 03e | Solo remisión | 3–6 párrafos agrupados |
| Cuenta para proporción Panorama | No | Sí |

**Declaración:** en bloque I con el formato:

> **Elevación Reservado→Panorama por campo de acción:** el concepto [X] estaba clasificado como Reservado con Continuidad explícita. Por §1.6.2 bis, se eleva a Panorama porque pertenece a la misma familia conceptual del subtema [Y]. Se presenta conceptualmente sin operar con él; se retoma en [destino].

En la tabla B marcar `Elevado a Panorama` con `Sí`.

**Regla de límite:** la elevación **no autoriza operación**.

**Regla de no elevación:** no se eleva si:
- Es de familia conceptual distinta al subtema.
- La disciplina no lo reconoce como parte del tema.
- Desarrollarlo conceptualmente implicaría operar con él.
- El destino es "Fuera del curso".

### 1.6.2 ter Regla de fundamento obligatorio de exclusión

**Propósito:** evitar que conceptos que pertenecen al campo de la disciplina o que se retoman más adelante en el curso se clasifiquen como "Fuera del curso" sin justificación.

**Los tres fundamentos universales de exclusión:**

| Fundamento | Definición | Aplica cuando |
|---|---|---|
| **Fuera por alcance curricular** | El curso no lo toca en ninguna sesión del programa. | No aparece en ninguna otra parte del temario ni se retoma en ningún capítulo o sesión. |
| **Fuera por nivel** | El curso lo toca conceptualmente, pero no lo desarrolla porque exige un nivel académico superior. | Sería pertinente al tema pero su tratamiento formal excede el nivel del programa. |
| **Fuera por especialidad** | El concepto pertenece a otra profesión o especialidad. | Es competencia de otro perfil profesional (metrólogo, geodesta, abogado especialista, etc.). |

**Procedimiento:**

1. Antes de clasificar como Reservado / Fuera del curso, verificar si alguno de los tres fundamentos aplica.
2. Si **ningún fundamento aplica**, el concepto **no puede clasificarse como Fuera del curso**. Debe reclasificarse como:
   - Continuidad explícita hacia la sesión donde se retoma, o
   - Aplicación posterior si se retoma en práctica profesional posterior, o
   - Panorama si pertenece al campo del subtema actual (§1.6.2 bis).
3. Si **al menos un fundamento aplica**, se clasifica como Reservado / Fuera del curso y **se declara cuál fundamento aplica** en la columna `Fundamento de exclusión` de la tabla B.

**Ejemplos universales:**

| Disciplina | Concepto | Fundamento |
|---|---|---|
| Topografía | Tolerancias formales | **No aplica** → Continuidad explícita |
| Topografía | Incertidumbre metrológica formal | Nivel |
| Topografía | Calibración de instrumentos | Especialidad |
| Topografía | Geodesia satelital avanzada | Alcance curricular |
| Derecho | Procedimiento ante tribunales internacionales | Alcance curricular |
| Derecho | Contabilidad forense | Especialidad |
| Medicina | Cirugía mayor | Especialidad |
| Medicina | Farmacología avanzada | Nivel |
| Biología | Análisis filogenético bayesiano | Nivel |
| Arquitectura | Cálculo estructural avanzado | Especialidad |
| Arquitectura | Normativa de seguridad industrial | Alcance curricular |

**Regla de límite:** el fundamento **no autoriza desarrollo** del concepto.

**Regla de reporte:** si un concepto fue clasificado previamente como Fuera del curso y al aplicar §1.6.2 ter se descubre que ningún fundamento aplica, se reclasifica y se reporta en el bloque I.

### 1.6.3 Activación del nivel Propedéutico

Un concepto se clasifica como **Propedéutico** cuando se cumplen **las tres condiciones**:

1. **Hay una competencia posterior documentada.**
2. **No es núcleo del tema actual.**
3. **Introducirlo ahora prepara mejor al alumno.**

**Reglas del Propedéutico:**

- No lleva aplicación práctica.
- No lleva ejercicios.
- No lleva fuentes de contraste.
- Sí lleva remisión al momento donde se retoma.
- Extensión: 2–4 párrafos.
- No cuenta para la proporción Núcleo 70–80%.
- **Excepción v1.8:** si el verbo es operativo y el nivel educativo es licenciatura o superior, un Propedéutico que el verbo requiera para operar sube a Núcleo (§1.6.7).

### 1.6.4 Reglas de asignación de nivel

1. Todo concepto del bloque B debe tener un nivel asignado.
2. Un concepto con peso alto debe ser Núcleo.
3. Un concepto Núcleo no puede tener peso bajo.
4. Un concepto Panorama puede tener peso medio o bajo.
5. Un concepto Propedéutico puede tener peso bajo o sin peso.
6. Un concepto Contexto o Reservado no tiene peso.
7. La suma de conceptos Núcleo debe corresponder a los subtemas oficiales.
8. Los conceptos Reservado requieren categoría de reserva.
9. Los conceptos Reservado / Fuera del curso requieren fundamento de exclusión (§1.6.2 ter).
10. El verbo del objetivo y el nivel educativo ajustan el piso mínimo (§1.6.7).
11. Los Reservados que pertenecen al campo de acción del subtema se elevan a Panorama (§1.6.2 bis).
12. La elevación Reservado→Panorama solo aplica a Reservados con categoría Continuidad explícita.
13. Si ningún fundamento de exclusión aplica, el concepto no puede ser Fuera del curso. Se reclasifica como Continuidad explícita, Aplicación posterior o Panorama.

### 1.6.5 Calibración por contexto curricular

**Factor 1 — El temario oficial:** determina qué se menciona antes/después.

**Factor 2 — La articulación curricular:** antecedente / consecuente / concurrente.

**Factor 3 — El perfil profesional:** aplicación directa → Núcleo o Panorama.

**Factor 4 — El nivel académico y educativo:** cuatrimestre + nivel del programa.

**Factor 5 — El verbo del objetivo:** reconocimiento / operación / análisis / producción.

**Factor 6 — La pertenencia al campo de acción del subtema:** misma familia conceptual → Panorama; familia distinta → Reservado; ajeno al curso → Reservado con fundamento (§1.6.2 ter).

### 1.6.6 Ejemplo completo

**Subtema oficial:** "1.4 Unidades de medida"
**Verbo del objetivo:** "Utilizar... realizar... reconociendo..."
**Nivel educativo:** licenciatura

| Concepto | Nivel | Cat. reserva | Fundamento exclusión | Recalibrado | Elevado a Panorama | Justificación |
|---|---|---|---|---|---|---|
| Unidades de longitud | Núcleo | — | — | No | No | Central |
| Unidades de superficie | Núcleo | — | — | No | No | Central |
| Conversiones | Núcleo | — | — | No | No | Central |
| Consistencia dimensional | Núcleo | — | — | No | No | Necesaria |
| Cifras significativas y criterio de reporte | **Núcleo** | — | — | **Sí** | No | Verbo operativo en licenciatura |
| Error de medición absoluto/relativo | **Núcleo** | — | — | **Sí** | No | Verbo operativo en licenciatura |
| Resolución de una medición | Propedéutico | — | — | No | No | Prerrequisito de S6 |
| Precisión vs exactitud | Propedéutico | — | — | No | No | Prerrequisito de S6 |
| Sistema inglés | Contexto | — | — | No | No | Nota contextual |
| **Unidades angulares** | **Panorama** | — | — | No | **Sí** | Misma familia; se opera en 2.7 |
| **Tolerancias formales** | **Reservado** | **Continuidad explícita** | — | No | No | Se retoman en 2.6 / 2.7 |
| Incertidumbre metrológica formal | Reservado | Fuera del curso | **Nivel** | No | No | Excede el nivel introductorio |
| Calibración / trazabilidad | Reservado | Fuera del curso | **Especialidad** | No | No | Competencia del metrólogo |

**Verificación:** 6 Núcleo, 1 Panorama, 2 Propedéutico, 1 Contexto, 3 Reservado (1 continuidad explícita + 2 fuera del curso con fundamento).

### 1.6.7 Regla de calibración por verbo del objetivo y nivel educativo

**Propósito:** determinar el **piso mínimo de exigencia** de cada concepto según dos señales que ya existen en el Brief y el Doc Maestro.

**Procedimiento:**

1. Extraer el verbo principal del objetivo.
2. Clasificar el verbo según taxonomía operativa.
3. Leer el nivel educativo del programa.
4. Aplicar el piso mínimo.
5. Ajustar niveles de conceptos.

#### 1.6.7.1 Clasificación operativa de verbos

| Verbo del objetivo | Categoría operativa |
|---|---|
| Reconocer / Identificar / Describir / Enunciar / Mencionar | Reconocimiento |
| Aplicar / Utilizar / Realizar / Resolver / Calcular / Ejecutar | Operación |
| Analizar / Comparar / Justificar / Diferenciar / Evaluar | Análisis |
| Diseñar / Integrar / Proponer / Sintetizar / Crear | Producción |

#### 1.6.7.2 Tabla de pisos mínimos por verbo × nivel educativo

| Categoría operativa | Bachillerato / Técnico | Licenciatura | Posgrado |
|---|---|---|---|
| **Reconocimiento** | Contexto o Reservado | Propedéutico | **Núcleo** mínimo |
| **Operación** | Propedéutico | **Núcleo** | **Núcleo** |
| **Análisis** | No aplica | **Núcleo** | **Núcleo con crítica** |
| **Producción** | No aplica | **Núcleo con producción** | **Núcleo con propuesta** |

#### 1.6.7.3 Regla de lectura de verbos compuestos

**Orden de jerarquía:** Producción > Análisis > Operación > Reconocimiento.

#### 1.6.7.4 Regla de recalibración de Propedéuticos

| Situación | Acción |
|---|---|
| Verbo = Reconocimiento | Se mantiene como Propedéutico |
| Verbo = Operación y nivel = licenciatura o superior | **Sube a Núcleo** |
| Verbo = Operación y nivel = bachillerato | Se mantiene como Propedéutico |
| Verbo = Análisis y nivel = licenciatura o superior | **Sube a Núcleo** |
| Verbo = Producción y nivel = licenciatura o superior | **Sube a Núcleo con producción** |

#### 1.6.7.5 Regla de trazabilidad

Toda recalibración se declara en el bloque I.

#### 1.6.7.6 Regla de límite

La regla §1.6.7 **no autoriza expansión conceptual**. Solo recalibra conceptos existentes.

### 1.6.8 Regla de suficiencia conceptual por eslabón de competencia (NUEVA en v1.12)

**Propósito:** garantizar que el desarrollo conceptual de la ficha sea suficiente para cubrir los eslabones de competencia que el Brief v2.8 declara. Cierra la brecha entre "ficha teórica completa" y "ficha teórica responsable del eslabón que declara cubrir".

#### 1.6.8.1 Procedimiento

1. Leer del Brief v2.8, bloque B, el campo **`Eslabones de competencia cubiertos`**.
2. Para cada eslabón declarado (`C1=introduce`, `C2=desarrolla`, `C3=aplica`, `C4=evalúa`), aplicar el criterio de suficiencia correspondiente (§1.6.8.2).
3. Si un eslabón **no puede cubrirse** con el desarrollo conceptual disponible, registrar la insuficiencia y reportarla en bloque I como **insuficiencia teórica**.
4. Si el Brief es v2.7 o anterior, el campo se marca como `no declarado` y **no se aplica la regla**.

#### 1.6.8.2 Criterios de suficiencia por eslabón

| Eslabón | Criterio de suficiencia | Evidencia esperada en la ficha |
|---|---|---|
| **introduce** | Al menos un concepto (de cualquier nivel: Núcleo, Panorama, Propedéutico o Contexto) relacionado con la competencia. | Un concepto identificado en bloque B con definición breve. |
| **desarrolla** | Al menos un concepto **Núcleo** con desarrollo completo: definición, ejemplo, aplicación, fuente. | Un concepto en bloque B con nivel Núcleo, peso alto o medio, y fuente asignada. |
| **aplica** | Al menos un concepto **Núcleo** que aparezca en bloque G (conceptos que requieren aplicación práctica). | Un concepto en bloque G con tipo de aplicación declarado. |
| **evalúa** | Al menos un concepto **Núcleo** que aparezca vinculado a la **evidencia declarada por el Brief** (bloque G del Brief). | Correspondencia entre la evidencia del Brief (bloque G) y un concepto Núcleo en bloque B. |

#### 1.6.8.3 Reglas de declaración

En el bloque I, cada eslabón verificado se declara con el formato:

> **Suficiencia conceptual — C2=desarrolla:** verificada. El concepto [X] en nivel Núcleo con peso [alto/medio] y fuente [ref] sostiene el desarrollo de la competencia C2.

Si la suficiencia falla:

> **Insuficiencia teórica — C2=desarrolla:** no se cumple. El Brief declara el eslabón `desarrolla` para C2, pero la ficha no dispone de un concepto Núcleo con desarrollo completo en el subtema [X.Y]. Acción sugerida: revisar Brief (¿el eslabón fue mal asignado?) o revisar Maestro (¿la competencia C2 no debería aplicarse en esta sesión?).

#### 1.6.8.4 Reglas duras

- **No se inventan conceptos** para cubrir eslabones. Si falta el concepto, se reporta la insuficiencia.
- **No se modifica el nivel** de un concepto para cumplir un criterio. Si un concepto es Panorama y el eslabón requiere Núcleo, se reporta la insuficiencia en lugar de forzar la elevación.
- **No se modifica el Brief** desde esta skill. Las discrepancias se reportan al usuario.
- **Si el Brief declara un eslabón pero el subtema no tiene conceptos suficientes**, se registra como **brecha teórica del Brief** y se remite a la skill 02.
- **Si el Brief no declara eslabones** (caso v2.7 o anterior), la regla no se aplica y se declara `no verificado`.
- **La suficiencia se verifica por eslabón, no globalmente.** Un eslabón puede estar cubierto y otro no.

#### 1.6.8.5 Coherencia con §1.6.7

Si la sesión cubre un eslabón `aplica` o `evalúa`, el piso mínimo de exigencia (§1.6.7.2) ya debería haber elevado los conceptos correspondientes a Núcleo. Si la verificación de §1.6.8 detecta que no fue así, se reporta como **inconsistencia interna de la ficha** y se revisa §1.6.7 antes de cerrar.

#### 1.6.8.6 Universalidad

La regla aplica a cualquier disciplina. En disciplinas interpretativas, `aplica` significa construir una interpretación fundamentada; en disciplinas creativas, producir una obra o propuesta. El criterio de suficiencia se ajusta al tipo de disciplina, pero la lógica de "el desarrollo conceptual debe sostener el eslabón declarado" es universal.

---

## 1.7 Regla de prioridad idiomática y geográfica

### 1.7.1 Jerarquía geográfica

1. México (español)
2. Latinoamérica (español)
3. España (español)
4. Otros idiomas

### 1.7.2 Qué cuenta como "fuente mexicana"

Autor mexicano, editorial mexicana, institución mexicana, o contenido aplicable al contexto mexicano. Los criterios son acumulativos.

### 1.7.3 Excepción por calidad superior

Se puede usar fuente extranjera si se declara en bloque I y se conserva la nacional como secundaria o contraste.

### 1.7.4 Fuentes normativas (puente a 03b)

La búsqueda de NOM, NMX o reglamentos mexicanos corresponde a 03b.

### 1.7.5 Relación con el 60/20/20

La regla geográfica **no modifica la proporción 60/20/20**.

---

## B. Bloques conceptuales (núcleo)

### Tabla del bloque B

| Columna | Notas |
|---|---|
| # | Referencia |
| Subtema | Del Brief |
| Concepto | Nombre |
| **Nivel** | Núcleo / Panorama / Propedéutico / Contexto / Reservado |
| **Categoría de reserva** | Solo si Reservado |
| **Fundamento de exclusión** | Solo si Fuera del curso: Alcance curricular / Nivel / Especialidad |
| **Recalibrado por §1.6.7** | Sí / No |
| **Elevado a Panorama** | Sí / No |
| **Suficiencia para eslabón** | Introduce / Desarrolla / Aplica / Evalúa / No aplica (NUEVO en v1.12) |
| Tipo de concepto | Ver catálogo expandido |
| Definición breve | 2-3 líneas |
| Nivel de consenso | Ver 6 matices |
| Profundidad | introductorio / aplicado / técnico-profesional |
| Peso heredado | alto / medio / bajo (Núcleo y Panorama) |
| Fuente principal | Ref [n] |
| Fuentes de contraste | Ref [n] (solo Núcleo) |
| Aplica a evidencia | Sí / No |
| Requiere aplicación práctica | Sí / No (solo Núcleo) |
| Articulación curricular | Ver bloque L |

**Ejemplo lleno (Sesión 4 — Topografía, licenciatura):**

| # | Subtema | Concepto | Nivel | Cat. reserva | Fundamento exclusión | Recalibrado | Elevado a Panorama | Suficiencia para eslabón | Tipo | Peso | Ref |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1.4 | Unidades de longitud | Núcleo | — | — | No | No | desarrolla | Definición | alto | [1] |
| 2 | 1.4 | Unidades de superficie | Núcleo | — | — | No | No | desarrolla | Definición | alto | [1] |
| 3 | 1.4 | Conversiones | Núcleo | — | — | No | No | desarrolla | Procedimiento | alto | [1] |
| 4 | 1.4 | Consistencia dimensional | Núcleo | — | — | No | No | desarrolla | Principio | alto | [1] |
| 5 | 1.4 | Cifras significativas | **Núcleo** | — | — | **Sí** | No | desarrolla | Criterio | medio | [2] |
| 6 | 1.4 | Error de medición (abs./rel.) | **Núcleo** | — | — | **Sí** | No | desarrolla | Concepto técnico | medio | [2] |
| 7 | 1.4 | Resolución de una medición | Propedéutico | — | — | No | No | — | Concepto técnico | — | [2] |
| 8 | 1.4 | Precisión vs exactitud | Propedéutico | — | — | No | No | — | Comparación | — | [2] |
| 9 | 1.4 | Sistema inglés | Contexto | — | — | No | No | — | Definición | — | [3] |
| 10 | 1.4 | **Unidades angulares** | **Panorama** | — | — | No | **Sí** | — | Concepto | bajo | [4] |
| 11 | 1.4 | **Tolerancias formales** | **Reservado** | **Continuidad explícita** | — | No | No | — | Criterio técnico | — | — |
| 12 | 1.4 | Incertidumbre metrológica | Reservado | Fuera del curso | **Nivel** | No | No | — | Concepto | — | — |
| 13 | 1.4 | Calibración / trazabilidad | Reservado | Fuera del curso | **Especialidad** | No | No | — | Concepto | — | — |

**Nota sobre la columna `Suficiencia para eslabón`:** solo se marca para los conceptos que sostienen algún eslabón declarado en el Brief. En el ejemplo, el Brief declara `C2=desarrolla`, y los conceptos 1–6 sostienen ese eslabón. Los demás conceptos se marcan con `—`.

### Catálogo expandido de `Tipo de concepto`

| Tipo | Ejemplo |
|---|---|
| **Principio** | "El aire caliente asciende" |
| **Definición** | "¿Qué es un arco?" |
| **Clasificación** | "Tipos de cimentación" / "Tipos de contratos" |
| **Proceso** | "Cómo se elabora un adobe" / "Cómo se redacta una demanda" |
| **Comparación** | "Muro de carga vs. estructura aporticada" / "Dolo vs. culpa" |
| **Modelo teórico** | "Modelo concéntrico de Burgess" |
| **Criterio de diseño** | "Orientación óptima según latitud" |
| **Procedimiento técnico** | "Cálculo de zapata aislada" / "Técnica de sutura" |
| **Fórmula / relación cuantitativa** | "Fórmula de Euler para pandeo" |
| **Concepto histórico** | "El Barroco americano como estilo" |
| **Concepto filosófico / ético** | "Ética ambiental" / "Consentimiento informado" |
| **Concepto actitudinal** | "Proactividad" / "Empatía clínica" |
| **Concepto interdisciplinar** | "Sustentabilidad como cruce de áreas" |
| **Concepto proyectual** | "Partido arquitectónico" |
| **Concepto normativo derivado** | "Coeficiente de uso de suelo" |

### 6 matices de `Nivel de consenso`

| Matiz | Significado |
|---|---|
| **Estable** | Aceptado sin debate activo |
| **Aceptado con matices** | Varía según contexto |
| **En debate activo** | Escuelas divergentes |
| **Emergente** | Reciente, no consolidado |
| **Controvertido** | Posiciones encontradas |
| **Obsoleto pero en circulación** | Superado, aún usado |

---

## C. Fuentes académicas (categoría A — 60% ponderado)

| Columna | Notas |
|---|---|
| Ref | [n] |
| Autor | Apellido, Nombre |
| Año | Edición usada |
| Título | — |
| Tipo | Libro / Capítulo / Manual / Tratado |
| Editorial | — |
| Páginas | pp. XX–XX |
| ISBN / DOI | — |
| **Procedencia geográfica** | México / Latinoamérica / España / Otro |
| **Idioma original** | Español / Inglés / Francés / Portugués / Otro |
| Aplica a concepto(s) | 1, 3 |
| Fuente base o de contraste | Base / Contraste |
| URL | Solo si es de acceso abierto |

### Regla del 60% con ponderación diferenciada

| Nivel | Ponderación |
|---|---|
| Núcleo | 1.0 |
| Panorama | 0.5 |
| Propedéutico | 0.5 |
| Contexto | 0.5 |
| Reservado | 0.0 |

**Fórmula:**

```
Peso total = (Núcleo × 1.0) + (Panorama × 0.5) + (Propedéutico × 0.5) + (Contexto × 0.5)

Peso sostenido = suma ponderada de conceptos con fuente académica

Proporción = Peso sostenido / Peso total
```

**Umbrales:**
- Si ≥ 60% → sin advertencia.
- Si < 60% → advertencia visible en bloque I.

**Nota:** los conceptos elevados a Panorama sí cuentan (0.5).

---

## C.bis. Fuentes científicas e institucionales (categoría C — 20%)

| Columna | Ejemplo |
|---|---|
| Ref | [12] |
| Autor / Institución | UADY / INAH / CINVESTAV / CONACYT |
| Título | ... |
| Tipo | Artículo revisado / Reporte técnico / Tesis / Documento institucional |
| Año | 2022 |
| **Procedencia geográfica** | México / Latinoamérica / España / Otro |
| **Idioma original** | Español / Inglés / Francés / Portugués / Otro |
| DOI o URL | — |
| Aplica a concepto(s) | 3 |

---

## D. Fuentes web confiables (categoría B — 20%)

| Columna | Ejemplo |
|---|---|
| Ref | [7] |
| Autor / Institución | ArchDaily / Arup / IAT |
| Título | ... |
| Tipo | Artículo web / Documentación técnica / Portal educativo |
| Año | 2022 |
| **Procedencia geográfica** | México / Latinoamérica / España / Otro |
| **Idioma original** | Español / Inglés / Francés / Portugués / Otro |
| URL | — |
| Verificado | Sí / No |
| Aplica a concepto(s) | 2 |

---

## E. Fuentes de contraste y actualización (automático)

Se activa si al menos un concepto Núcleo tiene consenso en debate activo, emergente o controvertido.

| Columna | Ejemplo |
|---|---|
| Ref de contraste | [15] |
| Concepto en debate | 1 — Regionalismo crítico |
| Fuente base | Frampton (1983) |
| Fuente de contraste | Koolhaas (1995) |
| Naturaleza del contraste | Defensa del lugar vs. globalización |
| Postura base | El lugar debe informar la forma |
| Postura de contraste | La globalización es inevitable |
| Recomendación para slide | Presentar ambas |

---

## F. Citas textuales autorizadas (condicional)

| Columna | Ejemplo |
|---|---|
| Ref | [1] |
| Cita textual | "La arquitectura es el juego sabio, correcto y magnífico de los volúmenes bajo la luz." |
| Autor | Le Corbusier |
| Obra | Vers une architecture |
| Año | 1923 |
| Página | p. 16 |
| Idioma original | Francés |
| Traducción propuesta | — |
| Concepto al que aplica | 4 |

Máximo 2-3 líneas.

---

## G. Conceptos que requieren aplicación práctica

**Solo aplica a conceptos Núcleo.**

| Columna | Ejemplo |
|---|---|
| Concepto (ref) | 3 — Cálculo de zapata aislada |
| Tipo de aplicación | Ejercicio / Caso / Problema / Simulación |
| Descripción breve | ... |
| Insumo necesario | ... |
| Derivación a 03b | Sí — NTC concreto |
| Derivación a 03c | Sí — diagrama |
| Tiempo estimado | 20 min |
| **Eslabón sostenido** | **C2=aplica** (NUEVO en v1.12) |

---

## H. Lagunas declaradas (siempre)

| Columna | Ejemplo |
|---|---|
| Subtema / concepto | 3.4 — Comportamiento del chukum |
| Tipo de laguna | Sin fuente / Fuente débil / En disputa / Idioma / Pago |
| Razón | No hay bibliografía revisada por pares |
| Impacto para composición | Reportar al docente |
| Fuente alternativa | Entrevista con maestro (no verificable) |
| Acción sugerida | Presentar como práctica regional |

**Nota:** las lagunas aplican a Núcleo, Panorama y Propedéutico.

**Nota v1.8:** si §1.6.7 sugiere un concepto que no está en el bloque B, se registra como laguna de expansión. No se introduce.

**Nota v1.12:** si §1.6.8 detecta que un eslabón declarado no puede cubrirse por falta de conceptos suficientes, se registra como **laguna de suficiencia** en este bloque además del bloque I.

---

## I. Advertencias para composición (siempre)

Incluye:
- Advertencia 60% ponderada cuando aplique
- Concepto con cita sensible
- Concepto en debate (remite a bloque E)
- Concepto que requiere contraste normativo (deriva a 03b)
- Concepto que requiere imagen (deriva a 03c)
- Concepto con nomenclatura regional
- Concepto que cambió en edición reciente
- Concepto que no debe profundizarse todavía
- Si algún subtema no tiene peso heredado declarado
- Si el modo de composición no está declarado
- Si el alcance conceptual del Brief es `no declarado`
- Si hay inversión de proporciones
- Fuente extranjera con equivalente nacional disponible
- Laguna idiomática
- **Recalibración por verbo y nivel educativo (v1.8)**
- **Elevación Reservado→Panorama por campo de acción (v1.9)**
- **Reclasificación por fundamento de exclusión (v1.10)**
- **Suficiencia conceptual por eslabón (v1.12)**
- **Insuficiencia teórica para eslabón (v1.12)**
- **Brecha teórica del Brief (v1.12)**
- **Inconsistencia interna entre §1.6.7 y §1.6.8 (v1.12)**

### Formato de la Advertencia 60% ponderada

> ⚠️ **Advertencia 60% ponderada:** la sesión tiene [N] conceptos ponderados. De ellos, [X] están sostenidos por bibliografía académica, lo que representa [%]. El umbral requerido es 60%. Los conceptos que no cumplen son: [lista].

### Formato de la Suficiencia conceptual (v1.12)

> ✓ **Suficiencia conceptual — C[N]=[eslabón]:** verificada. El concepto [X] en nivel Núcleo con peso [alto/medio] y fuente [ref] sostiene el [eslabón] de la competencia C[N].

### Formato de la Insuficiencia teórica (v1.12)

> ⚠️ **Insuficiencia teórica — C[N]=[eslabón]:** no se cumple. El Brief declara el eslabón `[eslabón]` para C[N], pero la ficha no dispone de un concepto Núcleo con desarrollo completo en el subtema [X.Y]. Acción sugerida: revisar Brief o Maestro.

### Formato de la Brecha teórica del Brief (v1.12)

> ⚠️ **Brecha teórica del Brief:** el Brief v2.8 declara el eslabón `[eslabón]` para C[N] en esta sesión, pero el subtema [X.Y] no contiene conceptos suficientes para sostenerlo. Se remite a la skill 02 para revisar la asignación del eslabón.

---

## J. Derivaciones a otras skills (condicional)

| Columna | Ejemplo |
|---|---|
| Concepto (ref) | 5 — Coeficiente U |
| Nivel | Núcleo |
| Skill destino | 03b |
| Razón | NOM-020-ENER-2011 |
| Acción esperada | 03b trae valor normativo vigente |
| Estado | Pendiente / Resuelto |

**Regla:** Núcleo, Panorama y Propedéutico pueden derivar.

---

## K. Mini-fichas de refuerzo (siempre proactivas)

Hasta **3 mini-fichas** para los prerrequisitos más críticos.

**Estructura:**

```markdown
### Mini-ficha K.1 — [Concepto a reforzar]

- **Origen:** sesión [N], unidad [X.Y]
- **Razón:** prerrequisito del concepto [Z] de la sesión actual
- **Duración sugerida:** 8–12 min
- **Definición breve:** [2 líneas]
- **Ejemplo mínimo:** [1 ejemplo concreto]
- **Error frecuente:** [qué confunde el alumno]
- **Pregunta de verificación:** [1 pregunta]
- **Fuente:** reutiliza [ref] de bloque C
```

---

## L. Articulación curricular

**Fuentes de alimentación:**

| Fuente | Qué aporta |
|---|---|
| Brief v2.8, bloque F | Articulación prioritaria + Materia de aplicación concurrente principal |
| Doc Maestro v1.5, sección de articulación | Relaciones documentadas del curso |
| Ficha Teórica, bloque A | Contexto curricular general |

**Estructura:**

```markdown
## L. Articulación curricular

[Prosa breve: 2–3 líneas.]

| Asignatura | Tipo de relación | Concepto vinculado | Cómo se aplica |
|---|---|---|---|
| [Asignatura 1] | Antecedente / Aplicación concurrente / Consecuente / Contexto disciplinar | [concepto] | [cómo se manifiesta] |

**Materia de aplicación concurrente principal:** [asignatura + cómo se aplica / no aplica]
```

**Reglas:**

- Máximo 4 materias en la tabla.
- Cada relación debe tener trazabilidad documental (Brief bloque F o Doc Maestro).
- Si no hay articulación documentada: el bloque se declara como `sin articulación documentada` y se omite la tabla.
- La materia de aplicación concurrente principal se declara en la tabla y además se destaca aparte.
- No se inventan relaciones.
- El lenguaje es neutral.
- El bloque aplica a cualquier disciplina.

**Ejemplo (Ing-Arq):**

| Asignatura | Tipo de relación | Concepto vinculado | Cómo se aplica |
|---|---|---|---|
| Matemáticas aplicadas a la arquitectura | Antecedente | Equivalencias y proporcionalidad | Soporte del procedimiento de conversión |
| Dibujo de representación | Antecedente | Cotas y unidades en documentación gráfica | Interpretación de planos |
| Geometría II | Antecedente | Longitud, superficie y relaciones dimensionales | Interpretación dimensional |
| Diseño Arquitectónico IV | Aplicación concurrente | Consistencia dimensional | Análisis y documentación del sitio |

**Ejemplo (Derecho):**

| Asignatura | Tipo de relación | Concepto vinculado | Cómo se aplica |
|---|---|---|---|
| Introducción al Derecho | Antecedente | Nociones de norma y sanción | Base conceptual |
| Teoría del Delito | Antecedente | Tipicidad, antijuridicidad, culpabilidad | Estructura del análisis |
| Derecho Procesal Penal | Consecuente | Etapas del proceso | Aplicación procesal |
| Clínica Jurídica | Aplicación concurrente | Análisis de casos reales | Redacción de escritos |

---

## Reglas de operación de la skill 03a

### Reglas generales

1. **Siempre** genera bloques A, B, C, C.bis, G, H, I, K, L.
2. **Bloque D** se genera si hay fuentes web complementarias.
3. **Bloque E** se activa automáticamente si algún concepto Núcleo tiene consenso en debate, emergente o controvertido.
4. **Bloque F** se genera solo si el compositor solicitó citas textuales.
5. **Bloque J** se activa si hay conceptos que derivan a otras skills.
6. **Bloque K** genera siempre hasta 3 mini-fichas proactivas.
7. **Bloque L** declara solo los conceptos con aplicación práctica directa.
8. **Corriente teórica dominante** es obligatoria.
9. **Nunca inventes citas, páginas, editoriales, ISBN/DOI ni URLs.**
10. **Regla 60% declarativa con ponderación diferenciada.**
11. **Citas breves** (`Autor, año, pág.`).
12. **No invadas territorio de 03b ni 03c.**
13. **Contexto disciplinar y geográfico** siempre presente.
14. **No mezcles corrientes teóricas incompatibles.**

### Reglas de expansión conceptual

15. **Nivel de profundidad, tipo de sesión, pesos por subtema y modo de composición se heredan literal del Brief.**
16. **Los pesos por subtema del bloque A y del bloque B deben coincidir literalmente con los del Brief, bloque B.**
17. **Si el Brief es v2.4 o el Doc Maestro es v1.3**, se declara `sin ponderar`.
18. **El modo de composición se hereda literal del Brief, bloque A.**

### Reglas de niveles y categorías

19. **Todo concepto del bloque B debe tener un nivel asignado.**
20. **Peso alto → Núcleo.** Núcleo no puede tener peso bajo.
21. **Suma de Núcleo = subtemas oficiales.**
22. **La expansión se calibra por 6 factores.**
23. **Si el Brief declara `literal` pero el test da positivo, se reporta.**
24. **Los Reservados solo se mencionan como remisión.**
25. **El bloque G solo incluye Núcleo.**

### Reglas del nivel Propedéutico

26. **El Propedéutico se activa solo si hay competencia posterior documentada.**
27. **No lleva aplicación práctica.**
28. **No lleva ejercicios.**
29. **No lleva fuentes de contraste.**
30. **Sí lleva remisión al momento donde se retoma.**
31. **Extensión: 2–4 párrafos.**
32. **No cuenta para la proporción Núcleo 70–80%.**

### Reglas de las categorías de reserva

33. **Todo Reservado debe tener una categoría de reserva.**
34. **Reservado con Continuidad explícita declara el capítulo.**
35. **Reservado con Aplicación posterior declara el momento.**
36. **Reservado con Fuera del curso declara el fundamento (§1.6.2 ter).**

### Reglas de prioridad idiomática y geográfica

37. **Prioridad México > Latinoamérica > España > Otros.**
38. **Cada fuente tiene procedencia geográfica e idioma.**
39. **Se agotan fuentes mexicanas y latinoamericanas antes de usar extranjeras.**
40. **Fuente extranjera se declara en bloque I si hay equivalente nacional disponible.**
41. **La regla geográfica no modifica la proporción 60/20/20.**

### Reglas de articulación curricular

42. **El bloque L se llama "Articulación curricular".**
43. **Máximo 4 materias.**
44. **Cada relación declara asignatura, tipo, concepto y aplicación.**
45. **Se declara `Materia de aplicación concurrente principal`.**
46. **La materia de aplicación concurrente principal debe estar también en la tabla.**
47. **Si no hay articulación, se declara `sin articulación documentada`.**
48. **No se inventan relaciones.**
49. **Lenguaje neutral (sin "taller" salvo que sea nombre oficial).**
50. **Trazabilidad documental con Brief bloque F o Doc Maestro.**
51. **El bloque aplica a cualquier disciplina.**

### Reglas de calibración por verbo y nivel educativo (v1.8)

52. **El verbo principal del objetivo se extrae del Brief, bloque B.**
53. **El nivel educativo se extrae del Doc Maestro, metadatos.**
54. **El piso mínimo se aplica según la tabla §1.6.7.2.**
55. **Si el objetivo tiene varios verbos, gobierna el verbo operativo más alto.**
56. **Los Propedéuticos que el verbo requiera para operar suben a Núcleo.**
57. **Toda recalibración se declara en el bloque I.**
58. **§1.6.7 no autoriza expansión conceptual.**
59. **El campo `Recalibrado por §1.6.7` se marca `Sí` para los conceptos afectados.**
60. **Si el Doc Maestro no declara nivel educativo, se infiere del nombre del programa y se reporta.**

### Reglas de elevación Reservado→Panorama (v1.9)

61. **Un concepto Reservado con Continuidad explícita se eleva a Panorama** si cumple los cuatro criterios de §1.6.2 bis.
62. **Un concepto Reservado con categoría "Fuera del curso" no se eleva.**
63. **Un concepto Reservado con categoría "Aplicación posterior" solo se eleva si cumple los cuatro criterios.**
64. **La elevación se declara en el bloque I con el formato de §1.6.2 bis.**
65. **El campo `Elevado a Panorama` se marca `Sí` para los conceptos afectados.**
66. **El concepto elevado a Panorama recibe definición breve + ejemplo + relación con el tema + remisión al destino.**
67. **El concepto elevado a Panorama NO recibe ejercicios, NO se opera con él, NO se evalúa.**
68. **El concepto elevado a Panorama recibe 1 fuente académica.**
69. **El concepto elevado a Panorama cuenta en la proporción Panorama 15–20%.**
70. **La elevación no autoriza operación** ni modifica el nivel educativo esperado.
71. **Si el destino es "Fuera del curso", no se eleva.**
72. **Si el concepto elevado a Panorama contradice la clasificación del Brief, se reporta la discrepancia.**
73. **La elevación se declara en el bloque B** con la columna `Elevado a Panorama`.
74. **La elevación Reservado→Panorama aplica a cualquier disciplina.**

### Reglas de fundamento de exclusión (v1.10)

75. **Todo concepto Reservado / Fuera del curso debe declarar cuál de los tres fundamentos aplica:** alcance curricular, nivel o especialidad (§1.6.2 ter).
76. **Si ningún fundamento aplica, el concepto no puede clasificarse como Fuera del curso.**
77. **Un concepto que se retoma más adelante en el curso NO puede clasificarse como Fuera del curso.** Debe ser Continuidad explícita o Aplicación posterior.
78. **Un concepto que pertenece al campo de acción del subtema actual NO puede clasificarse como Fuera del curso.** Debe ser Panorama (§1.6.2 bis).
79. **Los tres fundamentos son universales** y aplican a cualquier disciplina: derecho, medicina, arquitectura, biología, contaduría, historia, etc.
80. **El fundamento se declara en la columna `Fundamento de exclusión` de la tabla B.**
81. **La reclasificación por fundamento se declara en el bloque I** cuando corrige una clasificación previa.
82. **El fundamento no autoriza desarrollo del concepto.** Solo justifica su exclusión.
83. **Si un concepto fue clasificado previamente como Fuera del curso y se descubre que ningún fundamento aplica, se reclasifica y se reporta.**
84. **Ejemplos de aplicación universal:**
    - Topografía: tolerancias formales → **no aplica exclusión** → Continuidad explícita.
    - Topografía: incertidumbre metrológica formal → **fundamento: nivel**.
    - Topografía: calibración de instrumentos → **fundamento: especialidad**.
    - Derecho: procedimiento ante tribunales internacionales → **fundamento: alcance curricular**.
    - Medicina: cirugía mayor → **fundamento: especialidad**.
    - Biología: análisis filogenético bayesiano → **fundamento: nivel**.

### Reglas de suficiencia conceptual por eslabón (v1.12)

85. **La ficha hereda el campo `Eslabones de competencia cubiertos` del Brief v2.8, bloque B.** Si el Brief es v2.7 o anterior, se marca como `no declarado`.
86. **Si el Brief es v2.7 o anterior, no se aplica §1.6.8.** El campo se marca `no declarado` y se reporta al usuario.
87. **La suficiencia conceptual se verifica por eslabón** según los criterios de §1.6.8.2.
88. **El eslabón `introduce` requiere al menos un concepto de cualquier nivel relacionado con la competencia.**
89. **El eslabón `desarrolla` requiere al menos un concepto Núcleo con desarrollo completo.**
90. **El eslabón `aplica` requiere al menos un concepto Núcleo que aparezca en bloque G.**
91. **El eslabón `evalúa` requiere al menos un concepto Núcleo vinculado a la evidencia declarada en el Brief.**
92. **Las insuficiencias teóricas se declaran en bloque I** con el formato de §1.6.8.3.
93. **No se inventan conceptos para cubrir eslabones.** Si falta, se reporta la insuficiencia.
94. **No se modifica el nivel de un concepto** para cumplir un criterio de suficiencia.
95. **No se modifica el Brief desde esta skill.** Las discrepancias se reportan al usuario.
96. **Si el Brief declara un eslabón pero el subtema no tiene conceptos suficientes**, se registra como **brecha teórica del Brief** y se remite a la skill 02.
97. **La suficiencia se verifica por eslabón, no globalmente.** Un eslabón puede estar cubierto y otro no.
98. **Si §1.6.8 detecta inconsistencia con §1.6.7**, se reporta y se revisa §1.6.7 antes de cerrar.
99. **La columna `Suficiencia para eslabón` en bloque B se llena para los conceptos que sostienen eslabones declarados.**
100. **La regla §1.6.8 es universal** y aplica a cualquier disciplina.

---

## Archivos que produce la skill 03a

| Archivo | Contenido | Frecuencia |
|---|---|---|
| `ficha_teorica_sesion_N.md` | Ficha completa | Por sesión |
| `corrientes_teoricas_[asignatura].md` | Catálogo de escuelas | Una vez |
| `fuentes_academicas_[asignatura].md` | Acumulado de referencias | Cada sesión |
| `mini_fichas_refuerzo_sesion_N.md` | Hasta 3 mini-fichas | Por sesión |

---

## Checklist interno antes de entregar

### Verificaciones de suficiencia conceptual (v1.12)

- ¿Se heredó el campo `Eslabones de competencia cubiertos` del Brief v2.8?
- ¿Si el Brief es v2.7 o anterior, se declaró `no declarado` y se reportó?
- ¿Se aplicó la regla de suficiencia por eslabón según §1.6.8.2?
- ¿Cada eslabón declarado tiene su verificación de suficiencia?
- ¿Las insuficiencias teóricas se declararon en bloque I?
- ¿Las brechas teóricas del Brief se reportaron?
- ¿Se evitó inventar conceptos para cubrir eslabones?
- ¿Se evitó modificar niveles para cumplir criterios?
- ¿Se verificó coherencia con §1.6.7?
- ¿La columna `Suficiencia para eslabón` está llena en bloque B?
- ¿La columna `Eslabón sostenido` está llena en bloque G?

### Verificaciones de fundamento de exclusión (v1.10)

- ¿Todo concepto Fuera del curso declara cuál de los tres fundamentos aplica?
- ¿Algún concepto Fuera del curso debería reclasificarse como Continuidad explícita?
- ¿Algún concepto Fuera del curso debería reclasificarse como Panorama?
- ¿Algún concepto Fuera del curso debería reclasificarse como Aplicación posterior?
- ¿Los fundamentos declarados son verificables?
- ¿La columna `Fundamento de exclusión` está llena para todos los Fuera del curso?
- ¿La reclasificación se declaró en el bloque I cuando corrigió?

### Verificaciones de elevación Reservado→Panorama (v1.9)

- ¿Se revisaron los Reservados con Continuidad explícita?
- ¿Se aplicaron los cuatro criterios de §1.6.2 bis?
- ¿Los elevados reciben definición, ejemplo y remisión?
- ¿Los elevados NO reciben ejercicios ni operación?
- ¿Los elevados reciben 1 fuente académica?
- ¿Ningún Fuera del curso fue elevado?

### Verificaciones de calibración por verbo y nivel educativo (v1.8)

- ¿Se extrajo el verbo principal del Brief?
- ¿Se extrajo el nivel educativo del Doc Maestro?
- ¿Se aplicó la tabla de pisos mínimos?
- ¿Los Propedéuticos que el verbo requiere subieron a Núcleo?
- ¿La recalibración se declaró en el bloque I?

### Verificaciones de articulación curricular

- ¿El bloque L se llama "Articulación curricular"?
- ¿Máximo 4 materias?
- ¿Cada relación declara asignatura, tipo, concepto y aplicación?
- ¿Se declara `Materia de aplicación concurrente principal`?
- ¿Lenguaje neutral?
- ¿No se inventaron relaciones?

### Verificaciones de prioridad idiomática y geográfica

- ¿Cada fuente tiene procedencia geográfica e idioma?
- ¿Se agotaron fuentes mexicanas y latinoamericanas?
- ¿Se declaró en bloque I el uso de fuente extranjera habiendo nacional?

### Verificaciones del nivel Propedéutico

- ¿Cumplen las tres condiciones de §1.6.3?
- ¿No llevan aplicación, ejercicios ni fuentes de contraste?
- ¿Sí llevan remisión?
- ¿No cuentan para la proporción Núcleo?

### Verificaciones de las categorías de reserva

- ¿Todo Reservado tiene categoría?
- ¿Continuidad explícita declara el capítulo?
- ¿Aplicación posterior declara el momento?
- ¿Fuera del curso declara el fundamento?

### Verificaciones de expansión conceptual

- ¿El Brief es v2.8 o superior?
- ¿Se aplicó el test de denominación amplia?
- ¿Cada concepto tiene nivel?
- ¿Los pesos altos son Núcleo?
- ¿La expansión se calibró por los 6 factores?

### Verificaciones de ponderación 60%

- ¿Se aplicó la ponderación diferenciada?
- ¿Proporción ≥ 60%?
- Si < 60%, ¿advertencia emitida?

### Verificaciones generales

- ¿Bloque A con todos los metadatos, incluido `Eslabones de competencia cubiertos`?
- ¿Bloque B con columnas `Nivel`, `Categoría de reserva`, `Fundamento de exclusión`, `Recalibrado por §1.6.7`, `Elevado a Panorama`, `Suficiencia para eslabón`?
- ¿Bloque C.bis presente?
- ¿Bloque H declara lagunas, incluidas lagunas de suficiencia?
- ¿Bloque I incluye advertencias, recalibración, elevación, reclasificación y suficiencia conceptual?
- ¿Bloque K hasta 3 mini-fichas?
- ¿Bloque L declara articulación?
- ¿No se inventaron fuentes ni URLs?

---

## Criterio final de calidad

La skill 03a cumple si:

### Criterios de suficiencia conceptual (v1.12)

- **el campo `Eslabones de competencia cubiertos` fue heredado del Brief v2.8**;
- **si el Brief es v2.7 o anterior, se declaró `no declarado`**;
- **la suficiencia se verificó por eslabón**;
- **cada eslabón declarado tiene su verificación correspondiente**;
- **las insuficiencias teóricas se reportaron en bloque I**;
- **las brechas teóricas del Brief se reportaron y se remitieron a skill 02**;
- **no se inventaron conceptos para cubrir eslabones**;
- **no se modificaron niveles para cumplir criterios**;
- **la columna `Suficiencia para eslabón` está llena**;
- **la columna `Eslabón sostenido` está llena en bloque G**;
- **hay coherencia entre §1.6.7 y §1.6.8**;
- **la regla aplica universalmente a cualquier disciplina**.

### Criterios de fundamento de exclusión (v1.10)

- **todo concepto Fuera del curso declara cuál de los tres fundamentos aplica**;
- **ningún concepto Fuera del curso es en realidad Continuidad explícita**;
- **ningún concepto Fuera del curso es en realidad Panorama**;
- **ningún concepto Fuera del curso es en realidad Aplicación posterior**;
- **los fundamentos declarados son verificables**;
- **la columna `Fundamento de exclusión` está llena**;
- **la reclasificación se declaró en el bloque I cuando corrigió**;
- **los tres fundamentos son universales**.

### Criterios de elevación Reservado→Panorama (v1.9)

- **los Reservados con Continuidad explícita fueron revisados**;
- **los cuatro criterios de §1.6.2 bis se aplicaron**;
- **los elevados reciben definición, ejemplo, remisión, 1 fuente**;
- **los elevados no reciben ejercicios ni operación**;
- **ningún Fuera del curso fue elevado**.

### Criterios de calibración por verbo y nivel educativo (v1.8)

- **el verbo se extrajo del Brief**;
- **el nivel educativo se extrajo del Doc Maestro**;
- **la tabla de pisos mínimos se aplicó**;
- **los Propedéuticos que el verbo requiere subieron a Núcleo**;
- **la recalibración se declaró**.

### Criterios de articulación curricular

- **bloque L se llama "Articulación curricular"**;
- **máximo 4 materias**;
- **cada relación declara asignatura, tipo, concepto y aplicación**;
- **se declara `Materia de aplicación concurrente principal`**;
- **lenguaje neutral**;
- **no se inventaron relaciones**.

### Criterios de prioridad idiomática y geográfica

- **todas las fuentes clasificadas por procedencia e idioma**;
- **se agotaron fuentes mexicanas y latinoamericanas**;
- **proporción 60/20/20 intacta**.

### Criterios del nivel Propedéutico

- **cumplen las tres condiciones**;
- **no llevan aplicación, ejercicios ni contraste**;
- **llevan remisión**;
- **no cuentan para Núcleo**.

### Criterios de las categorías de reserva

- **todo Reservado tiene categoría**;
- **Continuidad explícita declara el capítulo**;
- **Aplicación posterior declara el momento**;
- **Fuera del curso declara el fundamento**.

### Criterios generales

- Brief v2.8 o superior (v2.7 con campo `no declarado`);
- test de denominación amplia aplicado;
- todo concepto con nivel;
- pesos altos son Núcleo;
- ningún Núcleo con peso bajo;
- suma de Núcleo = subtemas oficiales;
- Reservados sin desarrollo, peso ni fuentes (salvo Panorama elevado);
- bloque G solo Núcleo;
- expansión calibrada por 6 factores;
- ponderación 60% diferenciada;
- advertencia visible si < 60%;
- bloque A con metadatos, incluidos eslabones de competencia;
- bloque B con las 6 columnas nuevas;
- bloque K hasta 3 mini-fichas;
- bloque L con articulación;
- ficha declara versiones (v1.12, Brief v2.8, Doc Maestro v1.5);
- trazabilidad verificable con Brief y Maestro;
- suficiencia conceptual verificada y declarada.

---

## Changelog de consolidación v1.11 → v1.12

**Propósito:** incorporar la capa de suficiencia conceptual por eslabón de competencia. Cerrar la brecha entre "ficha teórica completa" y "ficha teórica responsable del eslabón que declara cubrir".

**Contenido normativo preservado del v1.11 (sin cambios):**

- §1.6.1 a §1.6.7 (incluidas las reglas v1.8, v1.9 y v1.10).
- §1.7 (prioridad idiomática).
- Bloques A–L (con extensiones en A, B, G, H, I).
- Reglas de operación 1–84.
- Checklist interno (ampliado).
- Criterio final de calidad (ampliado).
- Changelog anterior v1.10 → v1.11.

**Contenido nuevo en v1.12:**

- **§1.6.8** Regla de suficiencia conceptual por eslabón de competencia.
- **Campo nuevo en bloque A:** `Eslabones de competencia cubiertos` (heredado del Brief v2.8).
- **Columna nueva en bloque B:** `Suficiencia para eslabón`.
- **Columna nueva en bloque G:** `Eslabón sostenido`.
- **Bloque H ampliado:** lagunas de suficiencia.
- **Bloque I ampliado:** formatos de suficiencia conceptual, insuficiencia teórica, brecha teórica del Brief, inconsistencia interna §1.6.7–§1.6.8.
- **Reglas 85–100** (suficiencia conceptual por eslabón).
- **Verificaciones nuevas** en el checklist.
- **Criterios nuevos** en el criterio final.

**Cambios de empaquetado:**

- Se amplió el contrato de metadatos con un campo nuevo.
- Se amplió el bloque B con una columna nueva.
- Se amplió el bloque G con una columna nueva.
- Se amplió el bloque I con cuatro tipos nuevos de advertencia.
- Se ampliaron las reglas de operación de 84 a 100.
- Se amplió el checklist con un bloque nuevo (suficiencia conceptual).
- Se amplió el criterio final con un bloque nuevo (suficiencia conceptual).

**Actualizaciones de compatibilidad:**

- Brief consumidor: **v2.8** (antes v2.7). Cambio crítico: la v2.8 introduce el campo `Eslabones de competencia cubiertos`, sin el cual la v1.12 no puede cumplir su verificación.
- Doc Maestro consumidor: **v1.5** (sin cambios).
- 03.D consumidor: v1.8 (implícito).
- 03.E consumidor: v2.2 (implícito).
- 04 Auditor: v3.9 (implícito).

---

## Changelog de consolidación v1.10 → v1.11 (conservado)

**Propósito:** confirmar autocontención y actualizar referencias a skills consolidadas.

**Verificación de autocontención:**

- Se auditó v1.10 contra las versiones históricas v1.0 a v1.9.
- **No se encontraron referencias `[Igual que vX]` ni `[Sin cambios respecto a vX]`.**
- v1.10 ya estaba completamente autocontenida.

**Cambios aplicados en v1.11:**

1. **Título:** v1.10 → v1.11.
2. **Referencias al Brief:** v2.6 → **v2.7** (consolidado en la conversación previa).
3. **Referencias al Doc Maestro:** v1.4 → **v1.5** (consolidado en la conversación previa).
4. **Nota de compatibilidad:** actualizada a Brief v2.7 y Doc Maestro v1.5.
5. **Bloque A (metadatos):** ejemplo actualizado a v2.7 / v1.5.
6. **Reglas y checklist:** todas las referencias `Brief v2.6` → `Brief v2.7`.
7. **Añadido resumen de capacidades por versión** para trazabilidad histórica.
8. **Changelog de consolidación** (este bloque).

---

**Guía de uso del flujo completo:** consulta `guia_uso_flujo_skills.md`.