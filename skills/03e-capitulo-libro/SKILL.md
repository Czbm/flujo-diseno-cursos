---
name: 03e-capitulo-libro
description: Redacta el capitulo autocontenido del libro de la materia para estudio asincronico alineado con 02, 03.A, 03.B y 03.C.
stage_id: "03.E"
version: "2.4"
status: stable
---

# Skill: Capítulo de Libro Autónomo (03e) — v2.4

## Posición en el flujo

Esta skill es **paralela a 03d**, no secuencial. Ambas parten de los mismos insumos académicos y del mismo subsistema visual contractual, pero producen productos distintos:

- **03d** produce material sincrónico: presentación proyectable + guía docente.
- **03e** produce material asincrónico: **capítulo autocontenido del libro de la materia**.

```text
Brief v2.7/v2.8 ─────────────┐
Ficha Teórica v1.11/v1.12 ───┤
Ficha Normativa v1.4 ─────────┤
Perfil de estilo ──────────────┤
                               │
03.C-1 v1.2 ──────────────────┤
   │                           │
   ├─ EXTERNO → 03.C-3 ────────┤
   │                           │
   ├─ GENERATIVO               │
   │    03.C-2A                │
   │       ↓                   │
   │    03.C-2B PASS           │
   │       ↓                   │
   │    03Cbis ────────────────┤
   │                           │
   └─ HÍBRIDO → ambas ramas ───┤
                               ▼
                     03.E Capítulo de Libro
                               │
                               ▼
                     capitulo_N_[slug].md
```

**Nota de compatibilidad:** esta skill requiere Brief **v2.7 o v2.8**, Ficha Teórica **v1.11 o v1.12**, Ficha Normativa **v1.4**, Doc Maestro **v1.5 o v1.6**, perfil de estilo vigente y **03.C-1 v1.2**. Para recursos externos consume la salida vigente de 03.C-3. Mientras 03.C-3 permanezca en `BORRADOR v0.1`, su interfaz se considera provisional y debe declararse. Para recursos generativos exige evidencia de `PASS` de 03.C-2B v1.0 y producción trazable al RGE aprobado por medio de 03Cbis. No se acepta una antigua `subsistema visual 03.C` como sustituto contractual de este paquete visual.

**Compatibilidad extendida v2.4:** si el Brief es **v2.8 o superior** (con el campo `Eslabones de competencia cubiertos`), esta skill lo consume y aplica la política de audiencia de §0.10. Si el Brief es v2.7, funciona igual: la política de audiencia se aplica a los estados heredados de otras fuentes. En ningún caso la skill modifica el Brief.

**Versión autocontenida.** Esta versión no depende de versiones anteriores. Todo el contenido vigente está expandido literalmente.

### Resumen de capacidades por versión

- **v1.0–v1.3:** documento de estudio autónomo (nombre previo de la skill).
- **v1.4:** renombrada a "Capítulo de Libro Autónomo". Primera hoja identificadora, referencias por nombre de capítulo, formato `capitulo_N_[slug].md`.
- **v1.5:** desarrollo diferenciado por 4 niveles (Núcleo / Panorama / Contexto / Reservado) + Inclusión de imágenes + Reglas anti-presentación.
- **v1.6:** perfil de estilo del docente (bloque 0) para redactar en su voz.
- **v1.7:** bloque K reformulado como articulación curricular estructurada (K.1 antecedentes + K.2 conexión con taller).
- **v1.8:** nivel Propedéutico (E.4) + E.5 con 3 categorías de reserva + transiciones naturales.
- **v1.9:** K.3 actividad de aprendizaje vinculada.
- **v2.0:** K.2 renombrado a "Materia de aplicación concurrente" (lenguaje neutral).
- **v2.1:** K.3 dividida en K.3.a / K.3.b + referenciación interna de IDs + prohibición de metalenguaje.
- **v2.2:** consolidación autocontenida + referencias a Brief v2.7, Ficha Teórica v1.11, Ficha Normativa v1.4, subsistema visual 03.C, Doc Maestro v1.5.
- **v2.3:** política de audiencia (§0.10) + diccionario de expansión local (§0.11) + traducción de estados internos a prosa (§0.12) + reglas 116–143 + verificaciones de legibilidad editorial + criterios nuevos. El capítulo sale con lenguaje natural, sin códigos internos del pipeline visibles al alumno.
- **v2.4:** sustituye `subsistema visual 03.C` por el subsistema visual contractual `03.C-1 → [03.C-3 | 03.C-2A → 03.C-2B → 03Cbis]`; añade compuerta visual para destino `Capítulo`, integración editorial sin reinterpretación, identidad y atribución de figuras, control de PASS, bloqueo por NVD crítica no resuelta y protocolo de retorno upstream.

---

## Propósito

Esta skill toma el **Brief v2.7** (o v2.8), la Ficha Teórica, la Ficha Normativa, el perfil de estilo y el **paquete visual contractual resuelto** y produce un **capítulo autocontenido del libro de la materia** que permite al alumno profundizar los temas **sin la limitante de tiempo de clase y a su propio ritmo**.

**Marco conceptual:** el producto es un capítulo de un libro, no un documento de sesión. La información identificadora de la sesión vive **solo en la primera hoja**.

**Desarrollo diferenciado por nivel:** cada concepto tiene un **nivel** (Núcleo / Panorama / Propedéutico / Contexto / Reservado) que determina su extensión, profundidad, presencia de ejemplos y aplicación.

**Voz del docente:** el capítulo se redacta **imitando el estilo de prosa del docente** según el perfil de estilo (§0).

**Audiencia del capítulo:** el capítulo está dirigido al **alumno**. Los códigos internos del pipeline (`C1`, `U2`, `AC-01`, `AI-04`, `H11`, estados `introduce`/`desarrolla`/`aplica`/`evalúa`) **nunca aparecen sin expansión** en la prosa. Ver §0.10, §0.11 y §0.12.

**Articulación curricular:** el capítulo declara cómo se relaciona con otras asignaturas del plan de estudios (§K.1) y con la materia de aplicación concurrente principal (§K.2).

**Continuidad dentro del curso:** el capítulo declara explícitamente qué conceptos relacionados se retomarán después dentro de la **misma asignatura** (§E.5).

**Actividad de aprendizaje vinculada:** el capítulo declara qué parte de la actividad oficial del temario puede avanzar el alumno con este capítulo (§K.3), tanto las actividades que se trabajan directamente como aquellas a las que solo aporta insumos.

**Referenciación interna autocontenida:** todo ID de actividad oficial (`AC-NN` / `AI-NN`) que aparezca en el capítulo debe poder ser comprendido y localizado **dentro del propio capítulo**.

**No compite con 03d.** Lo complementa.

### Principio rector v2.4 — integrar visuales sin reinterpretar

03.E puede decidir **cómo integrar editorialmente** un recurso ya autorizado dentro del capítulo: ubicación entre párrafos, numeración de figura, redacción del pie, llamada desde la prosa, tamaño relativo, secuencia de lectura y explicación pedagógica que no añada semántica disciplinar nueva.

03.E **no puede cambiar** por iniciativa propia:

- ID NVD;
- objetivo perceptivo;
- problema cognitivo;
- mensaje cognitivo central;
- prioridad;
- procedencia;
- función primaria o secundaria;
- familia representacional;
- especificación representacional;
- tratamiento externo;
- unidades visuales estimadas;
- modo de agrupación;
- destino autorizado;
- criterio de satisfacción;
- identidad del recurso externo validado;
- contenido semántico de un RGE aprobado;
- contrato RGE, whitelist, blacklist o huella auditada.

Si integrar el recurso exige modificar alguno de esos elementos, 03.E **no corrige el contrato**: registra el conflicto y devuelve la incidencia a la skill propietaria.

**Regla de destino:** un recurso visual solo puede aparecer en el capítulo cuando 03.C-1 declare `Capítulo: sí` para esa NVD. La existencia del recurso no autoriza por sí misma su uso en 03.E.


### Principio rector: prosa continua, no presentación disfrazada

El capítulo debe leerse como un texto argumentado, no como una secuencia de slides.

Regla de oro: **si el capítulo tiene más subtítulos que párrafos por sección, está mal.** Proporción objetivo: 1 subtítulo cada 4–6 párrafos.

### Modo de composición

- **Operativo:** la sesión de origen es pendiente o próxima.
- **Retrospectivo:** la sesión de origen ya fue impartida. No altera la estructura: solo agrega una nota en la introducción y declara el modo en la primera hoja.

---

## Cuándo activar esta skill

Actívala cuando el usuario:

- Tenga ya generados el **Brief v2.7 o v2.8**, la **Ficha Teórica v1.11 o v1.12**, la **Ficha Normativa v1.4** y el perfil de estilo aplicable.
- Disponga de la **Ficha de Estrategia Visual 03.C-1 v1.2** de esa misma sesión.
- Para cada NVD con destino `Capítulo: sí`, exista un estado downstream verificable:
  - recurso externo resuelto por 03.C-3;
  - recurso generativo producido desde un RGE con `PASS` de 03.C-2B;
  - recurso híbrido con sus componentes autorizados y trazables;
  - o NVD V3/V4 pendiente aceptada explícitamente como no crítica por 03.C-1.
- Pida "capítulo del libro", "documento de estudio", "material de lectura para el alumno", o similar.
- Quiera armar el libro de estudio de la materia juntando varios capítulos.
- Quiera generar material de estudio para una sesión ya impartida (modo retrospectivo).

No la actives como emisión **completa** si:

- falta el Brief o la Ficha Teórica;
- falta 03.C-1;
- existe una NVD V1/V2 con destino `Capítulo: sí` que esté `PRESCRITA`, `EN_EJECUCIÓN` o `BLOQUEADA`;
- un recurso generativo no puede demostrar `PASS` y trazabilidad al contrato auditado;
- un recurso externo fue sustituido respecto del seleccionado por 03.C-3 sin nueva validación;
- la integración requeriría cambiar una decisión propiedad de 03.C-1, 03.C-2A/2B o 03.C-3.

En esos casos, el capítulo se emite como `incompleto por bloqueo visual contractual` solo si el usuario requiere un artefacto parcial; de lo contrario se detiene la emisión y se devuelve el conflicto upstream.

---

## Qué NO es este documento

| No es | Porque |
|---|---|
| La presentación en texto | La presentación es visual, secuencial y para proyectar |
| La guía docente | Esa es para el profesor, no para el alumno |
| Un resumen de la clase | Un resumen no profundiza |
| Un anexo de la presentación | Es un documento independiente y autocontenido |
| Una presentación con párrafos | Es prosa continua, no secuencia de slides |
| Un catálogo de imágenes | Las imágenes complementan, no sustituyen el texto |
| Un documento de sesión | Es un capítulo de un libro, no un registro de clase |
| Un catálogo de materias | La articulación se limita a 4 conexiones |
| Un glosario de códigos del pipeline | El capítulo no expone `C1`, `U2`, `AC-01` sin expandir |
| Texto genérico de IA | Debe sonar al docente que imparte la asignatura |

**Sí es:** capítulo técnico, argumentado, autocontenido, en la voz del docente, con articulación curricular explícita, continuidad declarada, actividad vinculada y **lenguaje natural para el alumno**.

---

## Estructura final: 14 bloques

```
0.  Pre-bloques de política editorial
    0.1–0.9   Perfil de estilo del docente
    0.10      Regla de audiencia (nuevo v2.4)
    0.11      Diccionario de expansión local (nuevo v2.4)
    0.12      Traducción de estados internos a prosa (nuevo v2.4)
A.  Primera hoja (identificación bibliográfica + actividades mencionadas)
B.  Tabla de contenido navegable
C.  Introducción y motivación
D.  Objetivos de aprendizaje
E.  Desarrollo temático por concepto (5 niveles + E.5 continuidad)
F.  Ejemplos trabajados (solo Núcleo)
G.  Casos de aplicación (condicional, solo Núcleo)
H.  Ejercicios de autoevaluación (solo Núcleo)
I.  Glosario (Núcleo y Panorama)
J.  Fuentes y referencias
K.  Articulación, continuidad y actividad de aprendizaje vinculada
    K.1 Antecedentes y relaciones disciplinares
    K.2 Materia de aplicación concurrente
    K.3 Actividad de aprendizaje vinculada
        K.3.1 Actividades que se trabajan directamente
        K.3.2 Otras actividades a las que el capítulo aporta
L.  Notas del docente (opcional)
M.  Advertencias y lagunas
Anexo Z.  Diccionario local y trazabilidad (interno, no dirigido al alumno)
```

---

## 0. Perfil de estilo del docente (pre-bloque)

Antes de redactar el capítulo, 03e asegura que existe el **perfil de estilo del docente**. Este perfil es un archivo persistente que se extrae una sola vez y se reutiliza en todos los capítulos de todas las asignaturas del docente.

### 0.1 Ubicación del archivo

```
/perfil_estilo_[docente].md
```

Ejemplo: `/perfil_estilo_christian-ramon-chi.md`

### 0.2 Verificación al iniciar

1. ¿Existe el archivo `perfil_estilo_[docente].md`?
2. ¿El archivo tiene todos los campos del §0.4?

**Si existe y está completo:** léelo y aplícalo durante la redacción.

**Si existe pero está incompleto:** pide al docente los datos faltantes.

**Si no existe:** ejecuta el procedimiento de extracción (§0.3) y créalo.

### 0.3 Procedimiento de extracción (primera vez)

Solicita al docente **3–5 textos representativos** de su prosa habitual:

- Al menos uno **técnico** (apuntes, reporte, artículo, memo).
- Al menos uno **narrativo** (correo, ensayo, mensaje).
- Al menos uno **didáctico** (explicación a alumnos, guía, material de clase).

**Si el docente no puede compartir textos**, hazle las siguientes 6 preguntas:

1. **Tono general:** ¿formal, académico, cercano, coloquial, mixto?
2. **Longitud de frases:** ¿cortas y directas, o largas y argumentadas?
3. **Humor:** ¿usas humor? ¿En qué dosis? ¿En qué contextos?
4. **Persona gramatical:** ¿primera persona ("como vimos"), impersonal ("se observa"), segunda persona ("observarás")?
5. **Muletillas y conectores:** ¿qué expresiones reconoces como tuyas?
6. **Cierres:** ¿cómo terminas normalmente un texto?

### 0.4 Estructura del perfil

```markdown
# Perfil de estilo — [Nombre del docente]

**Docente:** [nombre completo]
**Extraído:** [YYYY-MM-DD]
**Versión:** v1.0
**Basado en:** [N textos representativos / 6 respuestas a preguntas]

---

## 1. Tono
- **General:** [formal / académico / cercano / coloquial / mixto]
- **Técnico:** [tono específico]
- **Didáctico:** [tono específico]
- **Narrativo:** [tono específico]

## 2. Nivel de formalidad
- [Alto / Medio / Bajo]
- **Modulaciones:** [si varía según contexto]

## 3. Ritmo
- [Pausado / Dinámico / Variable]

## 4. Longitud de frases
- **Predominante:** [cortas / medias / largas / mixtas]

## 5. Vocabulario
- **Registro:** [técnico / accesible / mixto]
- **Palabras recurrentes:** [lista de 5–15]
- **Evita:** [palabras o expresiones que no usaría]

## 6. Muletillas y conectores
- [Lista de 5–15]

## 7. Puntuación
- **Uso de comas:** [frecuente / moderado / escaso]
- **Uso de punto y coma:** [sí / no / ocasional]
- **Uso de dos puntos:** [frecuente / moderado]
- **Uso de guiones largos:** [sí / no / ocasional]

## 8. Estructura de argumentación
- **Tipo:** [deductiva / inductiva / en capas / por contraste]
- **Cómo organiza ideas:** [de lo general a lo particular / etc.]

## 9. Humor
- **Presencia:** [sí / no / ocasional]
- **Tipo:** [irónico / seco / pedagógico / anecdótico]
- **Dosis:** [alta / media / baja]
- **Contextos:** [en qué tipo de textos aparece]

## 10. Metáforas y analogías
- **Presencia:** [sí / no / ocasional]
- **Tipo:** [cotidianas / técnicas / visuales / estructurales]

## 11. Cierres
- **Tipo:** [síntesis / pregunta abierta / remisión / dato / conclusión breve]
- **Longitud:** [corta / media / larga]

## 12. Ejemplos de su prosa

### Ejemplo 1 — Texto técnico
> [Fragmento de 3–5 líneas]

### Ejemplo 2 — Texto didáctico
> [Fragmento de 3–5 líneas]

### Ejemplo 3 — Texto narrativo
> [Fragmento de 3–5 líneas]

## 13. Notas adicionales
[Observaciones]
```

### 0.5 Aplicación durante la redacción

- Imita la voz del docente, no solo el tema.
- Mantén su nivel de formalidad.
- Usa sus expresiones recurrentes si encajan.
- Respeta su longitud de frases.
- Aplica su forma de argumentar.
- Respeta sus cierres.
- Evita clichés de IA.
- **Contexto:** el capítulo es didáctico-técnico. Se aplica el tono correspondiente.

### 0.6 Resolución de conflictos

| Tipo de conflicto | Quién gana |
|---|---|
| Estilístico (tono, ritmo, vocabulario, conectores) | La voz del docente |
| Estructural (niveles, extensión, proporciones) | La regla pedagógica |
| De citación (fuentes, referencias) | La regla pedagógica |
| De rigor (afirmaciones sin respaldo) | La regla pedagógica |
| De formato (bloques obligatorios, sintaxis) | La regla pedagógica |
| De tratamiento por nivel | La regla pedagógica |
| **De lenguaje y audiencia (§0.10–§0.12)** | **La regla pedagógica** |

**Regla general:** la voz personal nunca sacrifica rigor, citación, estructura, tratamiento por nivel, ni la política de audiencia.

### 0.7 Verificación de estilo

Al terminar el capítulo:

- ¿El texto suena al docente?
- ¿Mantiene su nivel de formalidad?
- ¿Usa sus conectores y muletillas recurrentes?
- ¿Respeta su longitud de frases?
- ¿Aplica su forma de argumentar?
- ¿Evita clichés de IA?
- ¿Los cierres siguen su patrón habitual?
- ¿No sacrificó rigor, citación, estructura ni niveles?

### 0.8 Versionado del perfil

Por defecto: se sobrescribe. Si el docente pide versionado, se conservan versiones anteriores como `perfil_estilo_[docente]_v1.md`, etc.

### 0.9 Cuándo actualizar el perfil

- Nuevos textos representativos.
- Cambio de estilo explícito.
- Después de 5–10 capítulos generados.

**Regla:** no se actualiza automáticamente.

---

### 0.10 Regla de audiencia (nuevo v2.4)

**Principio.** El capítulo producido por 03.E está dirigido al **alumno**. Los códigos internos del pipeline son metadatos entre skills, no lenguaje pedagógico.

**Definición de "código interno".**

- IDs de competencia: `C1`, `C2`, `C3`, ...
- IDs de unidad: `U1`, `U2`, ...
- IDs de subtema en formato compacto: `1.4`, `2.7`, ... cuando se usan como referencias cruzadas (no cuando aparecen como numeración del temario en una sección propia).
- IDs de actividad oficial: `AC-01`, `AI-02`, `AI-04`, ...
- IDs de necesidades y recursos visuales: `NVD-XX`, `ID_EXT`, `RGE-XX-YY`, ...
- Estados de eslabón: `introduce`, `desarrolla`, `aplica`, `evalúa`.
- Notación compacta del Brief: `C1=introduce`, `C2=desarrolla`, etc.

**Regla de expansión.**

1. **Primera mención de un código en el capítulo:** nombre legible completo + código entre paréntesis.
   - Ejemplo: `La competencia "Valorar escenarios naturales y urbanos considerando relaciones ambientales, socioculturales y económicas" (C2) se aborda en este capítulo…`
2. **Menciones posteriores:** nombre legible sin código.
   - Ejemplo: `Esta competencia se verifica inicialmente mediante…`
3. **Prohibición explícita:**
   - Incorrecto: `C2=evalúa`
   - Incorrecto: `Se evalúa C2.`
   - Incorrecto: `En U2 se aplica AI-04.`
   - Correcto: `En la Unidad 2 — Escenario natural se aplica el Proyecto final de levantamiento topográfico (AI-04).`

**Excepción única.** La sección **Anexo Z — Diccionario local y trazabilidad** al final del capítulo. En ella los códigos pueden aparecer sin expansión, siempre que estén precedidos por el diccionario local (§0.11) y esté claramente marcada como material interno, no como lectura del alumno.

**Prohibición adicional.** Ningún estado de eslabón aparece como código en la prosa. Se traducen según §0.12.

**Alcance.** La regla aplica a todos los bloques del capítulo (A–M) y a todos los elementos del capítulo, incluidos títulos, pies de figura, encabezados de tabla y notas al margen.

**Primera mención por documento.** La primera mención de un código se expande una sola vez en el capítulo. Las menciones posteriores dentro del mismo capítulo van sin código. Si un mismo código aparece en secciones lejanas (por ejemplo, en la introducción y en K.3), la expansión va en la primera mención y se puede recordar brevemente en la segunda si aporta claridad.

---

### 0.11 Diccionario de expansión local (nuevo v2.4)

**Propósito.** Antes de redactar el capítulo, 03.E construye una **tabla interna** con la equivalencia entre cada código que el Brief o las fichas mencionan y su nombre legible.

**Fuentes del diccionario.**

| Tipo de código | Fuente |
|---|---|
| Competencias (`C1`, `C2`, ...) | Brief bloque B (campo legible si existe) o Doc Maestro §21 |
| Unidades (`U1`, `U2`, ...) | Doc Maestro §7.b |
| Actividades oficiales (`AC-NN`, `AI-NN`) | Brief bloque G o Doc Maestro §7.c |
| Recursos visuales (`NVD-XX`, `ID_EXT`, `RGE-XX-YY`) | 03.C-1 + handoff downstream resuelto |
| Subtemas (`1.4`, `2.7`, ...) | Doc Maestro §7.b |
| Eslabones | §0.12 de esta skill (no requieren diccionario, se traducen) |

**Estructura de la tabla interna.**

| Código | Tipo | Nombre legible | Fuente |
|---|---|---|---|
| C1 | Competencia | Distinguir escenarios naturales y urbanos | Brief bloque B |
| U2 | Unidad | Unidad 2 — Escenario natural | Doc Maestro §7.b |
| AC-01 | Actividad oficial | Plenaria/debate y reporte o conclusiones | Brief bloque G |
| AI-04 | Actividad oficial | Proyecto final de levantamiento topográfico | Brief bloque G |
| NVD-02 | Recurso visual | Matriz de ética ambiental | 03.C-1 + recurso downstream resuelto |

**Regla del diccionario huérfano.**

Si un código aparece en el Brief o en las fichas y **no puede resolverse** contra el diccionario:

1. **No inventar el nombre.** No se asigna un nombre aproximado ni se omite el código.
2. **Detener la producción del capítulo.**
3. **Reportar el código huérfano** al usuario con la siguiente información:
   - Código no resuelto.
   - Sección del Brief o ficha donde aparece.
   - Fuentes consultadas.
   - Acción sugerida: revisar Brief o Doc Maestro para completar el diccionario.

**Regla del diccionario local.** El diccionario no se exporta a otras skills. Vive solo dentro de 03.E durante la producción del capítulo. Puede incluirse como Anexo Z del capítulo para trazabilidad interna, pero no reemplaza al diccionario canónico (que corresponde a skills upstream si existe).

**Regla de consumo del Brief v2.8.** Si el Brief es v2.8 o superior, el campo `Eslabones de competencia cubiertos` se usa para alimentar el diccionario y para verificar qué eslabones cubre el capítulo. Si el Brief es v2.7 o anterior, el campo no existe y el diccionario se construye sin eslabones.

---

### 0.12 Traducción de estados internos a prosa (nuevo v2.4)

**Propósito.** Los estados `introduce`, `desarrolla`, `aplica`, `evalúa` son **estados de progresión curricular**, no lenguaje pedagógico. Nunca aparecen como tales en la prosa del capítulo.

**Tabla de traducción contextual.**

| Estado interno | Traducciones posibles en prosa |
|---|---|
| `introduce` | "Este capítulo presenta por primera vez…" · "se toma contacto con…" · "se introduce la capacidad de…" · "aquí aparece por primera vez el concepto de…" |
| `desarrolla` | "Aquí se trabaja operativamente…" · "se practica…" · "se profundiza en…" · "el capítulo desarrolla el procedimiento de…" |
| `aplica` | "Se utiliza en un contexto nuevo…" · "se integra con…" · "se aplica a…" · "el alumno aplica este concepto a…" |
| `evalúa` | "Se verifica el logro mediante…" · "se recoge evidencia de…" · "esta actividad permite comprobar inicialmente…" · "el capítulo proporciona evidencia de…" |

**Regla de ajuste contextual.** La traducción no es literal. Se elige la fórmula que mejor encaje en el párrafo, manteniendo la semántica del eslabón.

**Regla de mención única.** Si un eslabón de la misma competencia aparece varias veces, se traduce una vez en la sección donde se aborda, y en las demás se hace referencia natural sin repetir la fórmula.

**Ejemplo aplicado.**

- Brief dice: `C2=evalúa`.
- En el capítulo se redacta: `Al cierre del capítulo, la actividad de autoevaluación permite comprobar inicialmente la capacidad de valorar escenarios naturales y urbanos considerando relaciones ambientales, socioculturales y económicas (C2).`

**Prohibición.** Ningún párrafo del capítulo usa las palabras `introduce`, `desarrolla`, `aplica` o `evalúa` como código. Si se usan en prosa, es porque son palabras corrientes del español ("este capítulo introduce al lector en…"), no porque reproduzcan el estado interno.

**Alcance.** La regla aplica a todos los bloques del capítulo, incluidos los encabezados de sección y las tablas. La única excepción es el Anexo Z.

---

## A. Primera hoja (siempre)

**Regla crítica:** toda la información identificadora de la sesión de origen vive **solo en esta primera hoja**. El cuerpo del texto no vuelve a mencionar la sesión.

```markdown
# Capítulo [N] — [Nombre del capítulo]

**Colección:** [Nombre del libro de estudio de la asignatura]

**Capítulo:** [N]
**Nombre del capítulo:** [nombre del tema en formato libro]
**Sesión de origen:** [N] *(trazabilidad interna)*
**Unidad del programa:** [Unidad X — Nombre de la unidad]
**Subtemas oficiales cubiertos:** [X.Y, X.Z]
**Pesos por subtema aplicados:** [X.Y=alto, X.Z=medio, ...]
**Alcance conceptual del subtema:** [literal / literal con extensión propedéutica /
amplio / panorámico]
**Modo de composición:** [operativo / retrospectivo]
**Motivo del modo retrospectivo:** [solo si aplica]
**Imágenes incluidas:** [lista de ID NVD + ID recurso o "sin imágenes integradas"]
**Estado de integración visual:** [completo / con omisiones no críticas autorizadas / incompleto por bloqueo visual contractual]
**Audiencia del documento:** alumno *(declaración obligatoria, v2.4)*
**Estado del capítulo:** [completo / incompleto por diccionario huérfano / incompleto
por ficha faltante / incompleto por bloqueo visual contractual]

**Distribución por nivel:**
- Núcleo: [N conceptos]
- Panorama: [N conceptos]
- Propedéutico: [N conceptos]
- Contexto: [N conceptos]
- Reservado: [N conceptos]
  - Continuidad explícita: [N]
  - Aplicación posterior: [N]
  - Fuera del curso: [N]

**Articulación curricular principal:** [lista de 2–4 asignaturas]

**Materia de aplicación concurrente principal:** [asignatura + cómo se aplica /
no aplica]

**Continuidad principal:** [secuencia de momentos donde se retoma el contenido]

**Actividades oficiales mencionadas en este capítulo:**
- Se trabajan directamente: [lista de IDs con nombre, o "ninguna"]
- Reciben aportes de este capítulo: [lista de IDs con nombre, o "ninguna"]

**Capítulos previos en la colección:** [nombres]
**Capítulos posteriores en la colección:** [nombres]

**Nivel de profundidad:** [introductorio / aplicado / técnico-profesional]
**Extensión:** [N] páginas
**Tiempo de lectura estimado:** [XX–XX min]
**Formato base:** Markdown (exportable a PDF)

**Perfil de estilo aplicado:** [docente + versión del perfil]

**Versiones de los insumos:**
- Doc Maestro: [v1.5 / v1.6]
- Brief: [v2.7 / v2.8]
- Ficha Teórica: [v1.11 / v1.12]
- Ficha Normativa: v1.4
- Orquestador Visual 03.C-1: v1.2
- 03.C-3: [v0.1 BORRADOR / no aplica / versión posterior compatible]
- 03.C-2A: [v1.2 / no aplica]
- 03.C-2B: [v1.0 / no aplica]
- Evidencia generativa: [PASS + ID RGE + huella si aplica / no aplica]
- Documento: v2.4

**Fecha de generación:** [YYYY-MM-DD]
```

**Reglas de la primera hoja:**

- **El campo `Actividades oficiales mencionadas en este capítulo`** declara dos listas: las actividades que se trabajan directamente con el capítulo y las que reciben aportes.
- **Si no hay ninguna actividad oficial mencionada**, ambas listas se declaran como `ninguna`.
- **El campo `Materia de aplicación concurrente principal`** es obligatorio. Se hereda del Brief bloque F. Si no hay, se declara `no aplica`.
- **El campo `Continuidad principal`** es obligatorio si hay conceptos Reservado con continuidad explícita o aplicación posterior.
- **El campo `Articulación curricular principal`** lista 2–4 asignaturas.
- **Los capítulos previos y posteriores se listan por nombre**, no por número de sesión.
- **El campo `Sesión de origen`** es de trazabilidad interna.
- **Los campos de versión de los insumos son obligatorios.**
- **El campo `Audiencia del documento: alumno`** es obligatorio desde v2.3.
- **El campo `Estado del capítulo`** es obligatorio desde v2.3.
- **El campo `Estado de integración visual`** es obligatorio desde v2.4.
- **Las versiones visuales declaradas deben corresponder a los recursos realmente integrados.**

---

## B. Tabla de contenido navegable

```markdown
## Tabla de contenido

1. [Introducción y motivación](#1-introducción-y-motivación)
2. [Objetivos de aprendizaje](#2-objetivos-de-aprendizaje)
3. [Desarrollo temático](#3-desarrollo-temático)
   - [3.1 Concepto Núcleo 1](#31-concepto-núcleo-1)
   - [3.2 Concepto Núcleo 2](#32-concepto-núcleo-2)
   - [3.3 Conceptos panorámicos](#33-conceptos-panorámicos)
   - [3.4 Conceptos propedéuticos](#34-conceptos-propedéuticos)
   - [3.5 Contexto y continuidad dentro del curso](#35-contexto-y-continuidad-dentro-del-curso)
4. [Ejemplos trabajados](#4-ejemplos-trabajados)
5. [Casos de aplicación](#5-casos-de-aplicación)
6. [Ejercicios de autoevaluación](#6-ejercicios-de-autoevaluación)
7. [Glosario](#7-glosario)
8. [Fuentes y referencias](#8-fuentes-y-referencias)
9. [Articulación, continuidad y actividad de aprendizaje vinculada](#9-articulación-continuidad-y-actividad-de-aprendizaje-vinculada)
   - [9.1 Antecedentes y relaciones disciplinares](#91-antecedentes-y-relaciones-disciplinares)
   - [9.2 Materia de aplicación concurrente](#92-materia-de-aplicación-concurrente)
   - [9.3 Actividad de aprendizaje vinculada](#93-actividad-de-aprendizaje-vinculada)
     - [9.3.1 Actividades que se trabajan directamente con este capítulo](#931-actividades-que-se-trabajan-directamente-con-este-capítulo)
     - [9.3.2 Otras actividades oficiales a las que este capítulo aporta](#932-otras-actividades-oficiales-a-las-que-este-capítulo-aporta)
10. [Notas del docente](#10-notas-del-docente)
11. [Advertencias y lagunas](#11-advertencias-y-lagunas)
12. [Anexo Z — Diccionario local y trazabilidad](#anexo-z--diccionario-local-y-trazabilidad)
```

**Regla:** los enlaces deben funcionar en Markdown nativo y en la exportación a PDF.

---

## C. Introducción y motivación

Párrafo breve (150–250 palabras) que:

- Contextualiza el tema del capítulo en el conjunto de la materia.
- Explica por qué importa el tema (aplicación profesional en Ing-Arq Mérida).
- **Referencia otros capítulos por nombre, no por sesión.**
- Anticipa lo que el alumno aprenderá.
- **Menciona la estructura del capítulo según los niveles.**

**Tono:** según el perfil de estilo del docente (§0). Cercano pero técnico. No infantilizar. No paternalista.

**Regla de audiencia (§0.10):** si la introducción menciona competencias, unidades o actividades oficiales, se expanden según §0.10. No se escriben códigos sin expansión.

**Cómo referenciar capítulos previos y posteriores:**

**Correcto:**
> "En el capítulo «Sistemas de representación topográfica» ya se revisaron las bases del dibujo técnico. Este capítulo incorpora la relación métrica que permite interpretar esas representaciones."

**Incorrecto:**
> "En la sesión anterior se revisaron los sistemas de representación topográfica..."

**En modo retrospectivo**, agregar al inicio de la introducción un párrafo breve:

> Este capítulo documenta una clase ya impartida. Se genera para estudio independiente y consulta posterior. El contenido refleja los temas tratados y está organizado para que puedas profundizar a tu propio ritmo.

El párrafo se integra en prosa, sin etiquetas.

---

## D. Objetivos de aprendizaje

Lista de 2–4 objetivos observables, heredados del Brief y refinados para lectura.

**Formato:** verbo observable + objeto + condición.

**Regla de niveles:** los objetivos se centran en los conceptos Núcleo. Los Panorama pueden mencionarse como "reconocer" o "identificar", no como "aplicar" o "resolver".

**Regla de audiencia:** los objetivos se redactan sin códigos. Si mencionan competencias del programa, se expanden según §0.10.

---

## E. Desarrollo temático por concepto

### Regla fundamental: desarrollo diferenciado por 5 niveles

El capítulo **no desarrolla todos los conceptos con la misma profundidad**. Cada concepto tiene un **nivel** asignado en la Ficha Teórica, y su desarrollo se calibra según ese nivel:

| Nivel | Desarrollo | Extensión | Ejemplos | Aplicación | Ejercicios |
|---|---|---|---|---|---|
| **Núcleo** | Prosa completa | 4–6 pág (alto); 2–4 (medio); 1–2 (bajo) | Sí | Sí | Sí |
| **Panorama** | Presentación conceptual | 3–6 párrafos agrupados | Breve | No | No |
| **Propedéutico** | Definición + ejemplo breve + remisión | 2–4 párrafos | Breve | No | No |
| **Contexto** | Mención de 1–2 líneas | 1–2 líneas | No | No | No |
| **Reservado** | Remisión por nombre | 1 frase | No | No | No |

### Regla de ponderación por peso (para Núcleo)

| Peso heredado | Extensión |
|---|---|
| Alto | 4–6 páginas |
| Medio | 2–4 páginas |
| Bajo | 1–2 páginas (raro) |

**Regla de consistencia:** si un Núcleo tiene peso bajo, hay inconsistencia con el Doc Maestro. Reportar al usuario antes de continuar.

### Estructura de la sección E

```markdown
## 3. Desarrollo temático

### 3.1 [Concepto Núcleo 1 — peso alto]
### 3.2 [Concepto Núcleo 2 — peso alto/medio]
### 3.3 Conceptos panorámicos
### 3.4 Conceptos propedéuticos
### 3.5 Contexto y continuidad dentro del curso
```

### Estructura interna del concepto Núcleo: prosa continua

```markdown
### N. [Nombre del concepto Núcleo]

[Párrafo 1: presentación del concepto y su relevancia.]

[Párrafo 2: definición técnica, con cita de fuente.]

[Párrafo 3: explicación del funcionamiento o lógica interna.]

[Párrafo 4: aplicación al contexto (Mérida, Ing-Arq).]

[Párrafo 5: errores frecuentes integrados en el flujo.]

[Párrafo 6 (opcional): cierre en prosa.]
```

**Reglas duras:**

- **Máximo 2 subdivisiones internas por concepto Núcleo.**
- **Párrafos de mínimo 4 líneas.**
- **Máximo 2 listas por concepto.**
- **Fórmulas integradas en prosa.**
- **Errores frecuentes en prosa.**
- **Prohibidas las etiquetas de conclusión.**
- **Regla de audiencia (§0.10):** el concepto se redacta sin códigos internos. Si se menciona un ID, se expande en primera mención.

### Estructura interna del concepto Panorama

Los Panorama se agrupan en una sola subsección. Cada uno recibe 3–6 párrafos, sin aplicación:

```markdown
### N. Conceptos panorámicos

#### N.1 [Concepto Panorama 1]
[3–6 párrafos que presentan: definición, relación con los Núcleo, y mención de
que su desarrollo técnico corresponde a un capítulo posterior.]

#### N.2 [Concepto Panorama 2]
[3–6 párrafos]
```

**Regla:** los Panorama no llevan ejemplos trabajados, ni aplicación práctica, ni ejercicios.

### Estructura interna del concepto Propedéutico

Los Propedéutico se agrupan en su propia subsección. Cada uno recibe 2–4 párrafos:

```markdown
### 3.4 Conceptos propedéuticos

#### 3.4.1 [Concepto Propedéutico 1]

[Párrafo 1: definición breve.]

[Párrafo 2: por qué se introduce aquí (competencia posterior documentada).]

[Párrafo 3 (opcional): ejemplo breve.]

[Párrafo 4: remisión explícita al momento donde se retoma.]
```

**Reglas del Propedéutico:**

- No lleva aplicación práctica.
- No lleva ejercicios.
- No lleva fuentes de contraste.
- **Sí lleva remisión explícita** al momento donde se retoma.
- Extensión: 2–4 párrafos.
- La remisión es obligatoria.
- La remisión se redacta en lenguaje natural (nombre del capítulo o del tema), no como código.

**Ejemplo:**

```markdown
#### 3.4.1 Resolución de una medición

La resolución de una medición es la magnitud más pequeña que un instrumento o
procedimiento puede distinguir. No se trata de la precisión, sino del límite mínimo
que el sistema puede diferenciar. Por ejemplo, una regla graduada en milímetros
tiene una resolución de 1 mm.

Este concepto se introduce aquí porque los instrumentos topográficos que se estudian
en capítulos posteriores tienen resoluciones específicas que determinan qué se puede
y qué no se puede medir con ellos.

Este concepto se retomará al estudiar los instrumentos topográficos, donde adquirirá
sentido operativo al comparar equipos con distintas capacidades.
```

### Estructura interna de las menciones de Contexto

Las menciones de Contexto se integran **dentro de los párrafos de Núcleo o Panorama** como frases de 1–2 líneas. No tienen subsección propia.

Ejemplo:
> "Los planos topográficos se complementan con sistemas de referencia global como UTM, que permiten georreferenciar la información a escala territorial."

### Estructura interna de la subsección E.5

La subsección E.5 declara la continuidad con las 3 categorías de Reservado:

```markdown
### 3.5 Contexto y continuidad dentro del curso

[Párrafo introductorio: 2–3 líneas que declaran qué conceptos relacionados no se
desarrollan en este capítulo y por qué.]

#### Continuidad explícita

[Conceptos Reservado con categoría "Continuidad explícita". Para cada uno: nombre
del concepto + capítulo donde se retoma.]

#### Aplicación posterior

[Conceptos Reservado con categoría "Aplicación posterior". Para cada uno: nombre
del concepto + momento donde se retoma.]

#### Fuera del curso

[Conceptos Reservado con categoría "Fuera del curso". Para cada uno: nombre del
concepto + declaración explícita de que no hay desarrollo previsto.]
```

**Reglas de E.5:**

- Siempre presente. Aunque no haya conceptos Reservado, se declara "sin continuidad documentada".
- Las 3 categorías aparecen en este orden: Continuidad explícita → Aplicación posterior → Fuera del curso. Si alguna categoría está vacía, se omite.
- Cada concepto Reservado aparece en la categoría correspondiente.
- **La redacción es declarativa, no de exclusión.** Se dice "se retomará en X", no "no se ve aquí".
- Prohibido el falso cierre.
- **Regla de audiencia:** la continuidad se redacta con nombres de capítulo o de tema, no con códigos de sesión.

### Transición natural dentro del desarrollo temático

Cada concepto Reservado (de cualquier categoría) recibe una **transición natural** dentro del párrafo donde se menciona por primera vez.

**Formato:** al final del párrafo donde el concepto se menciona, agregar una frase breve que remita al destino:

```markdown
[Párrafo que menciona el concepto Reservado...] Este concepto se retomará en el
capítulo «[nombre]».
```

**Regla:** la transición es breve (1 frase). No desarrolla el concepto.

**Excepción:** si el concepto Reservado solo aparece en E.5, no requiere transición adicional.

### Regla de proporcionalidad general

| Nivel | Proporción de extensión |
|---|---|
| Núcleo | 60–70% |
| Panorama | 15–20% |
| Propedéutico | 10–15% |
| Contexto | 5–10% |
| Reservado | 0% (solo E.5 + transiciones naturales) |

**Regla de verificación:** antes de redactar, verifica:

1. Los Núcleo ocupan entre 60–70%.
2. Los Panorama ocupan entre 15–20%.
3. Los Propedéutico ocupan entre 10–15%.
4. Los Contexto ocupan entre 5–10%.
5. Los Reservado no consumen extensión.
6. El concepto Núcleo de peso alto tiene más extensión que cualquier Panorama individual.

### Inclusión de imágenes y recursos visuales

El capítulo puede incluir únicamente recursos provenientes del **subsistema visual contractual 03.C** y cuyo `destino` en 03.C-1 autorice `Capítulo: sí`.

#### Compuerta visual de entrada para 03.E

Antes de insertar cualquier figura, clasifica cada NVD destinada al capítulo:

| Estado de integración | Condición | Acción de 03.E |
|---|---|---|
| `ADMISIBLE_EXTERNO` | 03.C-3 entregó recurso externo resuelto, trazable y utilizable | Integrar |
| `ADMISIBLE_GENERATIVO` | Existe `PASS` 03.C-2B + recurso producido por 03Cbis trazable al RGE aprobado | Integrar |
| `ADMISIBLE_HÍBRIDO` | Componentes externo y generativo están resueltos conforme al contrato | Integrar respetando funciones y agrupación |
| `OMISIBLE_NO_CRÍTICO` | V3/V4 pendiente y aceptación explícita de 03.C-1 | Omitir y registrar |
| `BLOQUEO_VISUAL` | V1/V2 no satisfecha, destino no autorizado, recurso sin trazabilidad o contrato contradictorio | No integrar; capítulo no puede declararse completo |

Esta compuerta **no reaudita semánticamente** el RGE ni rediseña la NVD. Solo verifica admisibilidad downstream.

#### Criterios de inclusión editorial

Un recurso admisible se integra si cumple los tres criterios editoriales:

1. **Destino autorizado:** 03.C-1 declara `Capítulo: sí`.
2. **Relación con el desarrollo:** el recurso se vincula con un concepto que efectivamente se desarrolla en el capítulo.
3. **Aporte real:** mejora comprensión, comparación, reconocimiento, secuencia o lectura técnica; no es decoración.

La función didáctica y el criterio de satisfacción **se heredan de 03.C-1**; 03.E no los redefine.

#### Cómo insertar el recurso

| Procedencia | Sintaxis / tratamiento |
|---|---|
| EXTERNO resuelto | `![Descripción](URL_o_ruta_validada)` |
| GENERATIVO resuelto | `![Descripción](ruta_o_referencia_del_recurso_generado)` |
| HÍBRIDO resuelto | Insertar los componentes según `modo de agrupación` y función diferenciada prescritos por 03.C-1 |
| OMISIBLE_NO_CRÍTICO | No insertar figura; registrar la omisión en el control interno |
| BLOQUEO_VISUAL | No insertar sustituto; declarar bloqueo |

**Prohibido en v2.4:**

- `URL pendiente de verificar`;
- `pendiente de generación`;
- prompts o instrucciones de generación dentro del capítulo;
- búsqueda improvisada de sustitutos;
- uso de un recurso externo distinto del validado por 03.C-3;
- uso de un recurso generativo con `RETURN` o sin `PASS` trazable;
- alterar un recurso generativo de forma que cambie su semántica aprobada;
- transformar `EXTERNO_PURO` en `EXTERNO_CON_ANOTACIÓN` por decisión de 03.E.

#### Pie de figura

Toda figura integrada lleva pie en cursiva:

`*Figura N. [Nombre descriptivo legible].*`

El cuerpo dirigido al alumno **no necesita exponer el ID técnico**. El vínculo `Figura N ↔ NVD ↔ recurso` se conserva en la tabla interna de trazabilidad visual y en el Anexo Z.

Si por razones editoriales se decide mostrar el ID, debe aparecer después del nombre descriptivo y nunca sustituirlo.

#### Fuente, licencia y atribución

Para recursos EXTERNO o componente externo de HÍBRIDO:

- conservar literalmente la fuente y localizador autorizados por 03.C-3;
- conservar autoría y licencia/condiciones de uso;
- incluir atribución visible cuando la licencia o el contrato lo exijan;
- no convertir una referencia persistente interna en una cita bibliográfica inventada.

Para recursos GENERATIVO:

- conservar internamente ID RGE y referencia al `PASS`;
- si existe `HUELLA_RGE_AUDITADO`, registrarla en la trazabilidad interna, no en la prosa del alumno;
- no presentar la huella ni el estado `PASS` como contenido pedagógico.

#### Máximos de imágenes por concepto

Los máximos editoriales se mantienen:

- Concepto Núcleo peso alto: máximo 4 imágenes.
- Concepto Núcleo peso medio: máximo 2 imágenes.
- Concepto Núcleo peso bajo: máximo 1 imagen.
- Concepto Panorama: máximo 1 imagen si aporta comprensión.

**Reglas adicionales:**

- los máximos editoriales no autorizan omitir una NVD V1/V2 si su criterio de satisfacción exige presencia en el capítulo;
- si el contrato visual exige más unidades de las que permite este máximo, se registra `CONFLICTO_DE_DENSIDAD_VISUAL` y se devuelve a 03.C-1; 03.E no altera el contrato ni excede silenciosamente su diseño editorial;
- una NVD V3/V4 puede omitirse solo con aceptación explícita como no crítica;
- si no existen NVD destinadas a capítulo, el capítulo se genera con texto puro y declara `sin imágenes integradas`.

### Regla de citación en el contenido

**Toda afirmación sustentable lleva cita al pie.**

Formato:
- `[ref: 3, p. 45]`
- `[ref: 5, §2.3]`
- `[ref: 7]`

**No inventar fuentes.** Las fuentes académicas proceden de la Ficha Teórica y Ficha Normativa; la fuente/autoría/licencia de recursos visuales externos procede de 03.C-3.

**Regla de audiencia:** los números de referencia bibliográfica (`[ref: 3]`) no se expanden porque el lector puede consultar la lista de fuentes al final del capítulo. Son códigos internos de citación, no códigos de trazabilidad curricular.

### Uso de fórmulas

Fórmulas en Markdown nativo o LaTeX, integradas en prosa.

**Correcto:**

```markdown
La relación fundamental se expresa como $D_{terreno} = D_{plano} \times N$, donde
$D_{plano}$ es la distancia medida sobre el papel, $N$ es el denominador de la
escala, y $D_{terreno}$ es la distancia real.
```

**Incorrecto:**

```markdown
La relación fundamental es:

$$
D_{terreno} = D_{plano} \times N
$$
```

### Aplicación del perfil de estilo

Durante la redacción de todo el bloque E:
- Aplica la voz del docente según §0.5.
- En caso de conflicto, resuelve según §0.6.
- En los conceptos Núcleo, mantén el tono técnico del docente.
- En los Panorama, el docente puede desplegar más su voz personal.
- **La política de audiencia (§0.10–§0.12) prevalece sobre el estilo.**

---

## F. Ejemplos trabajados (narrativos, solo para Núcleo)

Mínimo 2, idealmente 3 ejemplos resueltos **en prosa narrativa**.

### Distribución de ejemplos según nivel y peso

- Solo conceptos Núcleo llevan ejemplos.
- Al menos un ejemplo debe estar asociado al Núcleo de peso alto.
- Si hay dos o más Núcleo de peso alto: idealmente 3 ejemplos.

### Estructura de cada ejemplo

```markdown
### Ejemplo N — [Título breve]

[Prosa de 6–10 líneas: caso, datos, desarrollo, resultado, interpretación.]
```

**Regla de estilo:** el ejemplo se redacta en la voz del docente, siguiendo el perfil (§0).

**Regla de audiencia:** los ejemplos no mencionan códigos internos. Si mencionan actividades o competencias, se expanden según §0.10.

---

## G. Casos de aplicación (condicional, solo para Núcleo)

**Activación:** solo cuando el tema tenga aplicación regional directa a Mérida o Yucatán, y solo para conceptos Núcleo.

### Estructura de cada caso

```markdown
### Caso N — [Nombre del proyecto o situación]

[Prosa de 5–8 líneas.]
```

**Regla:** si el tema no tiene aplicación regional directa, se omite el bloque.

---

## H. Ejercicios de autoevaluación (solo para Núcleo)

**Activación:** siempre, salvo que el tema sea puramente histórico.

### Distribución de ejercicios según nivel

- Solo conceptos Núcleo llevan ejercicios.
- Al menos un ejercicio debe abordar el Núcleo de peso alto.
- Los Panorama no llevan ejercicios.

### Estructura

**3–5 ejercicios** para que el alumno verifique su comprensión.

Tipos:
- Preguntas de comprensión (2–3).
- Problema de aplicación (1–2).
- Caso breve (1).

### Sección de ejercicios

```markdown
## Ejercicios de autoevaluación

### Ejercicio 1 — [Tipo]
[Enunciado en 2–4 líneas]
```

### Sección de respuestas

Al final del capítulo, separadas de los enunciados.

**Regla:** el alumno debe poder autocorregirse.

**Regla de audiencia:** los enunciados no mencionan códigos. Si mencionan actividades oficiales, se expanden según §0.10.

---

## I. Glosario (términos de Núcleo y Panorama)

**Siempre presente.** Lista alfabética de **5–15 términos clave**.

**Regla de niveles:** el glosario incluye términos de Núcleo y Panorama. Los términos de Contexto y Reservado no se incluyen.

**Regla:** solo términos que aparecen en el capítulo. No inflar.

**Regla de estilo:** las definiciones se redactan en la voz del docente.

**Regla de audiencia:** el glosario no incluye códigos internos del pipeline. Solo términos del tema.

---

## J. Fuentes y referencias (con ponderación diferenciada)

**Siempre presente.** Lista completa de fuentes utilizadas, organizada por categoría.

```markdown
## Fuentes y referencias

### Bibliografía académica (categoría A)
1. ...

### Fuentes web confiables (categoría B)
3. ...

### Fuentes científicas, oficiales, normativas o institucionales (categoría C)
4. ...
```

**Cómo se cuenta cada concepto:**

| Nivel | Ponderación |
|---|---|
| Núcleo | 1.0 |
| Panorama | 0.5 |
| Propedéutico | 0.5 |
| Contexto | 0.5 |
| Reservado | 0.0 |

**Sección adicional si hay imágenes:**

```markdown
### Recursos visuales utilizados

| ID | Descripción | Fuente | Licencia | Estado |
|---|---|---|---|---|
```

**Regla de audiencia:** en la tabla de recursos visuales, la columna "ID" puede conservar el código (`H11`) porque la tabla es una referencia interna de trazabilidad, no prosa. La columna "Descripción" lleva el nombre legible.

---

## K. Articulación, continuidad y actividad de aprendizaje vinculada

Este bloque declara cómo se relaciona el capítulo con:
1. Otras asignaturas del plan de estudios (K.1).
2. La materia de aplicación concurrente principal (K.2).
3. Las actividades oficiales del temario (K.3).

### K.0 Reglas generales del bloque K

#### K.0.1 Fuentes de alimentación

| Subsección | Fuentes |
|---|---|
| **K.1** | Ficha Teórica bloque L + Brief bloque F + Doc Maestro (sección de articulación) |
| **K.2** | Brief bloque F + Ficha Teórica bloque L |
| **K.3** | Doc Maestro §7.c + Brief bloque G |

#### K.0.2 Niveles permitidos por subsección

| Nivel | K.1 | K.2 |
|---|---|---|
| Núcleo | Sí | Sí |
| Panorama | Sí | No |
| Contexto | Sí (mención breve) | No |
| Reservado | No | No |

**Razón:** la articulación curricular es una propiedad del capítulo. K.2 es una propiedad de los conceptos Núcleo con aplicación proyectual explícita.

#### K.0.3 Límites

| Subsección | Máximo |
|---|---|
| K.1 | 4 conexiones |
| K.2 | 1 materia de aplicación concurrente |
| K.3.1 | 3 actividades trabajadas directamente |
| K.3.2 | 3 actividades a las que el capítulo aporta |

#### K.0.4 Taxonomía de relaciones

- **Antecedente:** materia previa que aporta conocimiento base.
- **Aplicación concurrente:** materia de la misma etapa formativa donde el alumno aplica directamente lo aprendido.
- **Consecuente:** materia posterior que depende de este contenido.
- **Contexto disciplinar:** materia que ayuda a situar el conocimiento sin dependencia directa.

#### K.0.5 Trazabilidad por relación

Cada conexión responde:

1. **Asignatura:** ¿con qué materia se relaciona?
2. **Tipo de relación:** ¿antecedente, aplicación concurrente, consecuente o contexto disciplinar?
3. **Concepto vinculado:** ¿qué conocimiento específico se conecta?
4. **Aplicación:** ¿cómo se manifiesta esa relación?

Si alguno no está documentado, se declara `no declarado`.

#### K.0.6 Distinción conexión conceptual ≠ actividad

Una conexión curricular puede ser conceptual sin requerir una actividad. Las conexiones conceptuales se declaran en K.1. Las actividades de aplicación solo se desarrollan en K.2 si el Brief o la Ficha Teórica las declaran.

#### K.0.7 Regla antiinvención

Si la unidad o el producto de la asignatura vinculada no está declarado en los insumos, se mantiene exactamente como `unidad no declarada`. No se infiere.

#### K.0.8 Lenguaje neutral

- Se usa **"materia"**, **"asignatura"** o el **nombre oficial**.
- Se usa **"aplicación"** en lugar de "proyectual".
- Se usa **"concurrente"** para indicar que ocurre en la misma etapa formativa.
- **Solo se usa "taller" si es el nombre oficial de la asignatura.**

#### K.0.9 Referenciación interna de IDs de actividad oficial

Reglas para que todo ID (`AC-NN` / `AI-NN`) mencionado en el capítulo sea comprensible y localizable dentro del propio capítulo.

**Regla 1 — Primera mención autocontenida.**

La primera vez que aparece un ID, se escribe con su **nombre completo**:

> **AI-04 — Proyecto final: diseño y propuesta de un levantamiento topográfico**

Después de esa primera definición, ya puede usarse solo `AI-04`.

**Regla 2 — Menciones posteriores remiten a una sección del capítulo.**

Cuando un ID vuelve a aparecer, incluye una **referencia interna legible**:

> AI-04 recibe en este capítulo criterios de representación. **Véase "Actividades que se trabajan directamente con este capítulo" o "Otras actividades oficiales a las que este capítulo aporta" para la descripción completa de AI-04.**

**Regla 3 — ID mencionado ⇒ ID definido en K.3.**

Si un ID aparece en cualquier parte del capítulo, debe estar declarado en K.3.1 o K.3.2. Si no está, es un error bloqueante.

**Regla 4 — Prohibición de metalenguaje.**

El capítulo nunca menciona:
- Nombres de bloques internos (`K.3`, `E.5`, `bloque F`, etc.).
- Estados de actividad (`aporta`, `desarrolla`, `consolida`, etc.).
- Versiones de skills (`v2.3`, `v1.11`, etc.).
- Reglas de activación (`si el estado es X, entonces...`).
- Nombres de skills del pipeline (`03.E`, `03.D`, etc.).

**Ejemplo correcto:**

> **AI-04 — Proyecto final de levantamiento topográfico** también recibe aportaciones de este capítulo. En esta etapa se incorporan criterios para seleccionar y justificar la representación del terreno. **Véase "Otras actividades oficiales a las que este capítulo aporta" para la descripción de AI-04.**

#### K.0.10 Regla de audiencia aplicada al bloque K (nuevo v2.4)

**Regla 1 — IDs de competencia.** Si el capítulo menciona competencias declaradas (`C1`, `C2`, ...), la primera mención lleva nombre legible + código entre paréntesis. Las menciones posteriores llevan solo el nombre legible.

**Regla 2 — IDs de unidad.** El capítulo no usa `U1`, `U2` como referencia. Se usa el nombre completo de la unidad: "Unidad 2 — Escenario natural".

**Regla 3 — IDs de subtema.** El capítulo no usa `1.4`, `2.7` como referencia cruzada. Se usa el nombre del tema: "unidades de medida".

**Regla 4 — IDs visuales.** En prosa, se usa el nombre descriptivo del recurso. En tablas internas pueden conservarse ID NVD, ID externo e ID RGE en columnas separadas.

**Regla 5 — Estados internos.** Los estados `introduce`, `desarrolla`, `aplica`, `evalúa` no aparecen como código. Se traducen según §0.12.

**Regla 6 — Excepción.** El Anexo Z puede llevar códigos sin expansión, precedidos por el diccionario local.

### K.1 Antecedentes y relaciones disciplinares

```markdown
### K.1 Antecedentes y relaciones disciplinares

[Prosa breve: 1–2 párrafos que contextualizan el capítulo en el plan de estudios.]

| Asignatura | Tipo de relación | Concepto vinculado | Aplicación |
|---|---|---|---|
| [Asignatura 1] | [Antecedente / Aplicación concurrente / Consecuente / Contexto disciplinar] | [concepto] | [cómo se manifiesta] |
```

**Reglas:**

- Máximo 4 conexiones.
- Cada conexión debe tener trazabilidad documental.
- Si no hay trazabilidad: "sin articulación documentada".
- No se incluyen conexiones de tipo "Taller" en K.1 (esas van en K.2).
- **Regla de audiencia:** las asignaturas se mencionan por su nombre oficial, sin códigos de skill.

### K.2 Materia de aplicación concurrente

```markdown
### K.2 Materia de aplicación concurrente

[Prosa breve: 2–3 líneas.]

| Materia | Tipo de relación | Concepto vinculado | Cómo se aplica |
|---|---|---|---|
| [Asignatura] | Aplicación concurrente | [concepto] | [cómo se manifiesta] |

**Evidencia esperada en esa materia:** [descripción o "no aplica"]

**Pregunta para el alumno:** [pregunta]
```

**Reglas:**

- Solo una materia.
- Debe estar también declarada en K.1.
- El tipo de relación es siempre `Aplicación concurrente`.
- La materia se declara con su nombre oficial (con clave si está disponible).
- No se inventa la relación.
- Si no hay materia de aplicación concurrente, se omite la subsección.

### K.3 Actividad de aprendizaje vinculada

```markdown
### K.3 Actividad de aprendizaje vinculada

[Prosa breve: 2–3 líneas.]

#### K.3.1 Actividades que se trabajan directamente con este capítulo

[Si no hay ninguna: "Ninguna actividad oficial se trabaja directamente con este
capítulo."]

| ID | Actividad oficial | Estado en este capítulo | Producto parcial que puede avanzar |
|---|---|---|---|
| [AC-03] | [nombre] | [inicia / desarrolla / consolida / entrega / retroalimenta / cierra] | [descripción] |

**Qué parte del producto puede desarrollar el alumno con este capítulo:**
[Descripción específica.]

**Qué parte del producto requiere otras fuentes o sesiones:**
[Descripción.]

**Pregunta para el alumno:** [pregunta]

#### K.3.2 Otras actividades oficiales a las que este capítulo aporta

[Si no hay ninguna: "Este capítulo no aporta insumos a otras actividades oficiales."]

| ID | Actividad oficial | Qué aporta este capítulo |
|---|---|---|
| [AI-04] | [nombre] | [descripción del insumo] |

**Pregunta para el alumno:** [pregunta]
```

**Reglas de llenado:**

- K.3.1 máximo 3 actividades.
- K.3.2 máximo 3 actividades.
- Solo se declaran actividades oficiales del temario (§7.c del Doc Maestro).
- El estado declarado en K.3.1 debe coincidir con el Brief (bloque G).
- Las actividades con estado `aporta` van exclusivamente a K.3.2.
- Las actividades con estado `inicia`/`desarrolla`/`consolida`/`entrega`/`retroalimenta`/`cierra` van exclusivamente a K.3.1.
- Una actividad no puede aparecer en ambas subsecciones.
- El producto parcial debe ser específico.
- No se inventan actividades ni estados.
- Todo ID mencionado en el cuerpo del capítulo debe estar declarado en K.3.1 o K.3.2.
- K.3 se omite solo si el Brief declara `sin actividad oficial en esta sesión`.
- **Regla de audiencia:** en la tabla, la columna "ID" conserva el código porque es una tabla de referencia interna; la columna "Actividad oficial" lleva el nombre completo. En la prosa introductoria de K.3, las actividades se mencionan con nombre completo + código entre paréntesis la primera vez.

### K.4 Verificación del bloque K

- ¿El bloque K tiene K.1, K.2 (si aplica) y K.3 (si aplica)?
- ¿K.1 tiene máximo 4 conexiones?
- ¿K.2 tiene máximo 1 materia?
- ¿K.3.1 y K.3.2 tienen máximo 3 actividades cada una?
- ¿Ninguna actividad aparece en las dos subsecciones?
- ¿Cada conexión de K.1 tiene los 4 datos de trazabilidad?
- ¿K.2 declara la materia con su nombre oficial?
- ¿K.3 solo declara actividades oficiales del temario?
- ¿El estado de K.3.1 coincide con el Brief?
- ¿Las actividades de K.3.2 tienen estado `aporta`?
- ¿La primera hoja declara las dos listas de actividades mencionadas?
- ¿Todo ID mencionado en el cuerpo está declarado en K.3.1 o K.3.2?
- ¿La primera mención de cada ID incluye su nombre completo?
- ¿Las menciones posteriores remiten a la sección del propio capítulo?
- ¿El capítulo evita metalenguaje?
- ¿No se inventaron actividades ni conexiones?
- **¿Se respetó la regla de audiencia (§0.10) en la prosa introductoria de K.3?**

---

## L. Notas del docente (opcional)

**Activación:** solo si el docente las solicita.

**Regla de audiencia:** este bloque, si existe, puede llevar códigos internos porque está dirigido al docente, no al alumno. Sin embargo, si el bloque se incluye en el mismo archivo que lee el alumno, se aplica la regla de audiencia general. En caso de duda, se aplica la regla de audiencia.

---

## M. Advertencias y lagunas

**Siempre presente.**

```markdown
## Advertencias y lagunas

### Lagunas declaradas
[Prosa.]

### Advertencias
[Prosa.]
```

**Nota sobre niveles:**

> Este capítulo desarrolla [N] conceptos Núcleo en profundidad, presenta [N]
> conceptos Panorama, introduce [N] conceptos Propedéutico, y menciona [N] conceptos
> de Contexto. Los conceptos reservados son: [N] con continuidad explícita, [N] con
> aplicación posterior, [N] fuera del curso.

**Nota sobre actividades oficiales:**

> Este capítulo se relaciona con [N] actividades oficiales. Se trabajan directamente
> con el capítulo: [lista de IDs con nombre]. Reciben aportes del capítulo: [lista
> de IDs con nombre]. Si no hay actividades oficiales relacionadas, la nota se omite.

**Nota sobre materia de aplicación concurrente:**

> Este capítulo se aplica directamente en [materia + clave]. La evidencia esperada
> es [descripción]. Si no hay materia de aplicación concurrente, la nota se omite.

**En modo retrospectivo:** nota de retrospectiva.

**Nota sobre imágenes pendientes:** IDs correspondientes, con nombre descriptivo.

**Nota de audiencia (v2.4):** el capítulo está dirigido al alumno; los códigos internos del pipeline se han expandido en primera mención o traducido a prosa. El Anexo Z contiene el diccionario local y la trazabilidad para uso interno.

---

## Anexo Z — Diccionario local y trazabilidad (nuevo v2.4)

**Propósito.** Este anexo es la **única excepción** a la regla de audiencia. Está claramente marcado como material interno, no dirigido al alumno. Se coloca al final del capítulo, después del bloque M.

**Contenido.**

1. **Diccionario local de códigos.**
2. **Eslabones cubiertos por el capítulo.**
3. **Trazabilidad de la primera mención de cada código.**

**Estructura.**

```markdown
## Anexo Z — Diccionario local y trazabilidad

> Material interno. No forma parte de la lectura del alumno.

### Diccionario de códigos

| Código | Tipo | Nombre legible | Fuente |
|---|---|---|---|
| C1 | Competencia | Distinguir escenarios naturales y urbanos | Brief bloque B |
| C2 | Competencia | Valorar escenarios naturales y urbanos considerando relaciones ambientales, socioculturales y económicas | Brief bloque B |
| U1 | Unidad | Unidad 1 — Introducción a la topografía | Doc Maestro §7.b |
| AC-01 | Actividad oficial | Plenaria/debate y reporte o conclusiones | Brief bloque G |
| AI-04 | Actividad oficial | Proyecto final de levantamiento topográfico | Brief bloque G |
| NVD-02 | Recurso visual | Matriz de ética ambiental | 03.C-1 + recurso downstream resuelto |

### Eslabones cubiertos por este capítulo

- C1 = introduce
- C2 = desarrolla; evalúa (evidencia inicial)
- C3 = introduce

### Trazabilidad de la primera mención

| Código | Sección de primera mención |
|---|---|
| C1 | §C — Introducción |
| C2 | §C — Introducción |
| AI-04 | §K.3.2 |
| H11 | §3.2 |
```

**Reglas del Anexo Z:**

- Es obligatorio desde v2.3 si el Brief tiene al menos un campo con códigos internos (`Eslabones de competencia cubiertos`, actividades oficiales, recursos visuales).
- Es la única sección del capítulo donde los códigos aparecen sin expansión.
- Está claramente delimitado por la nota "Material interno".
- No reemplaza al diccionario canónico de skills upstream.
- No se exporta a otras skills.

---

## Reglas de operación de la skill 03e

### Reglas generales

1. **Lenguaje calibrado al nivel del alumno.**
2. **Extensión calibrada por nivel y peso.**
3. **No repite la presentación.**
4. **Autocontenido.**
5. **Citas en el contenido siempre que sea posible.**
6. **No inventa fuentes.**
7. **Ejemplos trabajados siempre** (mínimo 2, solo Núcleo).
8. **Autoevaluación siempre** (solo Núcleo).
9. **Glosario siempre** (solo Núcleo y Panorama).
10. **Fuentes y referencias siempre** (con ponderación diferenciada).
11. **Casos de contexto Mérida condicionales** (solo Núcleo).
12. **Conexión con taller condicional** (solo Núcleo).
13. **Notas del docente opcionales.**
14. **Fórmulas en Markdown o LaTeX, integradas en prosa.**
15. **Tabla de contenido navegable al inicio.**
16. **Formato base Markdown**, exportable a PDF.
17. **Lagunas declaradas siempre.**
18. **No invade territorio de 03d.**
19. **No incluye la guía docente.**
20. **Imágenes integradas en prosa.**

### Reglas anti-presentación

21. **Prohibida la subdivisión excesiva.** Máximo 2 subdivisiones internas por concepto Núcleo.
22. **Párrafos de mínimo 4 líneas.**
23. **Máximo 2 listas por concepto.**
24. **Fórmulas integradas en prosa.**
25. **Errores frecuentes en prosa.**
26. **Prohibidas las etiquetas de conclusión.**
27. **Regla anti-slide:** proporción 1 subtítulo cada 4–6 párrafos.
28. **Ejemplos narrativos, no fichas.**
29. **Regla de extensión real:** Núcleo peso alto = 4–6 páginas de prosa continua.

### Reglas de ponderación

30. **Los pesos por subtema vienen del Brief.**
31. **Prohibido `N/D`.**
32. **Prohibida la inversión de proporciones.**

### Reglas del modo de composición

33. **El modo se hereda del Brief.**
34. **El modo retrospectivo no altera la estructura del capítulo.**
35. **El modo retrospectivo no exime del cumplimiento de los pesos ni de los niveles.**

### Reglas de inclusión de imágenes

36. **Todo recurso visual debe superar la compuerta contractual de 03.E.**
37. **Solo se integran recursos con `Capítulo: sí` en el destino de 03.C-1.**
38. **Toda imagen lleva pie de figura con nombre descriptivo legible; la trazabilidad técnica vive en tabla interna/Anexo Z.**
39. **Máximo editorial de imágenes por concepto:** 4 Núcleo alto, 2 Núcleo medio, 1 Núcleo bajo, 1 Panorama, salvo conflicto contractual que debe escalarse.
40. **No se inventan, buscan, sustituyen ni generan imágenes desde 03.E.**
40.a. **Un EXTERNO no puede reemplazarse por otro recurso sin nueva validación de 03.C-3.**
40.b. **Un GENERATIVO con `RETURN` o sin PASS no puede integrarse.**
40.c. **03.E no puede modificar semántica, whitelist, blacklist, relaciones o causalidad de un RGE aprobado.**
40.d. **Una NVD V1/V2 destinada a capítulo y no satisfecha impide declarar el capítulo como completo.**
40.e. **Una NVD V3/V4 pendiente solo puede omitirse con aceptación explícita upstream como no crítica.**
40.f. **Si el problema exige cambiar objetivo, función, procedencia, familia, tratamiento, agrupación, destino o criterio de satisfacción, escalar a 03.C-1.**
40.g. **Si el problema pertenece al diseño generativo, devolver a 03.C-2A y exigir nueva auditoría 03.C-2B.**
40.h. **Si el problema pertenece a selección, derechos, atribución o identidad de un recurso externo, devolver a 03.C-3.**

### Reglas de formato de capítulo

41. **El capítulo es un capítulo de libro, no un documento de sesión.**
42. **Las referencias a otros capítulos se hacen por nombre.**
43. **La información identificadora vive solo en la primera hoja.**
44. **El nombre del archivo sigue la convención `capitulo_N_[slug].md`.**

### Reglas de niveles

45. **Los niveles vienen de la Ficha Teórica, bloque B.**
46. **El capítulo desarrolla cada concepto según su nivel.**
47. **La proporción de extensión por nivel respeta: Núcleo 60–70%, Panorama 15–20%, Propedéutico 10–15%, Contexto 5–10%, Reservado 0%.**
48. **Los ejemplos trabajados solo aplican a conceptos Núcleo.**
49. **Los casos de aplicación solo aplican a conceptos Núcleo.**
50. **Los ejercicios de autoevaluación solo aplican a conceptos Núcleo.**
51. **La conexión con taller (K.2) solo aplica a conceptos Núcleo.**
52. **El glosario incluye términos de Núcleo y Panorama.**
53. **La sección E organiza los conceptos en 5 subsecciones internas.**
54. **Los conceptos Panorama, Propedéutico, Contexto y Reservado no llevan pie de figura propio.**

### Reglas del perfil de estilo

55. **El capítulo se redacta imitando el estilo del docente.**
56. **El perfil se extrae una sola vez y se reutiliza.**
57. **Si no existe el perfil y el docente no puede compartir textos, se le hacen las 6 preguntas concretas.**
58. **La voz personal gana en forma; las reglas pedagógicas ganan en estructura.**
59. **La voz personal nunca sacrifica rigor, citación, estructura, niveles ni política de audiencia.**
60. **Al terminar el capítulo se verifica la consistencia de estilo.**

### Reglas de articulación curricular

61. **El bloque K se divide en K.1, K.2 y K.3.** No se mezclan.
62. **K.1 se alimenta de Ficha Teórica bloque L + Brief bloque F + Doc Maestro.**
63. **K.2 se alimenta de Brief bloque F + Ficha Teórica bloque L.**
64. **K.3 se alimenta de Doc Maestro §7.c + Brief bloque G.**
65. **03e no descubre relaciones nuevas.**
66. **K.1 máximo 4 conexiones. K.2 máximo 1 materia. K.3 máximo 3+3 actividades.**
67. **Cada conexión de K.1 declara: asignatura, tipo, concepto, aplicación.**
68. **K.1 permite Núcleo, Panorama y Contexto. K.2 y K.3 solo Núcleo.**
69. **La articulación puede ser conceptual sin requerir actividad.**
70. **Regla antiinvención:** unidades no declaradas se mantienen como `no declarada`.

### Reglas del nivel Propedéutico

71. **El capítulo tiene subsección E.4 "Conceptos propedéuticos" si hay al menos un Propedéutico.**
72. **Cada Propedéutico lleva 2–4 párrafos** con definición, razón de introducción y remisión.
73. **Los Propedéutico no llevan aplicación práctica.**
74. **Los Propedéutico no llevan ejercicios.**
75. **Los Propedéutico no llevan fuentes de contraste.**
76. **La remisión explícita es obligatoria.**
77. **Los Propedéutico no cuentan para la proporción Núcleo.**

### Reglas de continuidad dentro del curso

78. **La subsección E.5 se llama "Contexto y continuidad dentro del curso"** con 3 categorías.
79. **Siempre está presente.**
80. **Cada concepto Reservado aparece en su categoría.**
81. **La redacción es declarativa, no de exclusión.**
82. **Prohibido el falso cierre.**
83. **Cada concepto Reservado recibe transición natural** en el párrafo donde se menciona.
84. **Excepción:** si solo aparece en E.5, no requiere transición adicional.
85. **La primera hoja declara el campo `Continuidad principal`.**

### Reglas de actividad de aprendizaje vinculada

86. **K.3 declara las actividades oficiales del temario relacionadas con el capítulo.**
87. **K.3 se activa si el Brief declara al menos una actividad oficial vinculada, sin importar su estado.** Solo se omite si el Brief declara `sin actividad oficial en esta sesión`.
88. **K.3 se divide en K.3.1 y K.3.2.**
89. **K.3.1 máximo 3 actividades; K.3.2 máximo 3.**
90. **Las actividades con estado activo van a K.3.1.**
91. **Las actividades con estado `aporta` van a K.3.2.**
92. **Ninguna actividad aparece en ambas subsecciones.**
93. **Solo se declaran actividades oficiales del temario.**
94. **El estado de K.3.1 coincide con el Brief.**
95. **El producto parcial (K.3.1) y el aporte (K.3.2) son específicos.**

### Reglas de materia de aplicación concurrente

96. **El bloque K.2 se llama "Materia de aplicación concurrente".**
97. **K.2 se activa solo si el Brief (bloque F) declara la materia.**
98. **K.2 tiene máximo 1 materia.**
99. **La materia de K.2 debe estar también en K.1.**
100. **El tipo de relación en K.2 es siempre `Aplicación concurrente`.**
101. **K.2 declara la materia con su nombre oficial.**
102. **K.2 incluye la evidencia esperada.**
103. **K.2 incluye una pregunta para el alumno.**
104. **Si no hay materia, K.2 se omite y la primera hoja declara `no aplica`.**
105. **El lenguaje es neutral.**

### Reglas de referenciación interna de IDs

106. **Primera mención autocontenida:** ID + nombre completo.
107. **Menciones posteriores:** remiten a la sección del propio capítulo.
108. **ID mencionado ⇒ ID definido en K.3.1 o K.3.2.**
109. **Prohibición de metalenguaje.**
110. **Traducción pedagógica.**
111. **La primera hoja declara las dos listas de actividades mencionadas.**
112. **Si no hay actividad oficial, ambas listas se declaran como `ninguna`.**
113. **Si un ID se menciona pero no se trabaja ni recibe aportes claros, no debe mencionarse.**
114. **El checklist verifica que todo ID mencionado tenga definición completa dentro del propio capítulo.**
115. **El bloque M incluye nota que declara las actividades trabajadas y receptoras de aportes.**

### Reglas de audiencia (nuevas v2.4)

116. **El capítulo está dirigido al alumno.** Esto se declara en el bloque A, campo `Audiencia del documento`.
117. **Ningún código interno del pipeline aparece en la prosa del capítulo sin expansión.**
118. **Los códigos incluidos son:** `C1`, `U2`, `AC-01`, `AI-04`, `H11`, `I1`, `B1`, y cualquier otro que el pipeline use.
119. **La primera mención de un código lleva nombre legible completo + código entre paréntesis.**
120. **Las menciones posteriores del mismo código llevan solo el nombre legible.**
121. **Los estados `introduce`, `desarrolla`, `aplica`, `evalúa` no aparecen como código en la prosa.**
122. **La única excepción son los anexos de trazabilidad (Anexo Z), precedidos por el diccionario local.**
123. **La regla aplica a todos los bloques del capítulo, incluidos títulos, pies de figura, encabezados de tabla y notas al margen.**
124. **La primera mención por documento:** la expansión va una sola vez; las menciones posteriores van sin código.
125. **En tablas de referencia interna** (K.3, recursos visuales), la columna `ID` puede conservar el código; la columna `Nombre` lleva el nombre legible.
126. **En las notas del docente (bloque L)** se puede conservar código si el bloque se mantiene fuera del archivo dirigido al alumno; si va dentro, se aplica la regla general.

### Reglas del diccionario de expansión local (nuevas v2.4)

127. **Antes de redactar, 03.E construye el diccionario local con la tabla código → nombre legible.**
128. **El diccionario se construye a partir del Brief y del Doc Maestro (§7.b, §7.c, §8, §9, §21 si existe).**
129. **Si un código aparece en el Brief y no puede resolverse, se detiene la producción y se reporta el código huérfano.**
130. **No se inventan nombres legibles para códigos huérfanos.**
131. **El diccionario local no se exporta a otras skills; vive solo dentro de 03.E.**
132. **El diccionario puede incluirse como Anexo Z del capítulo para trazabilidad interna.**
133. **El diccionario local no reemplaza al diccionario canónico de skills upstream si existe.**
134. **Si el Brief es v2.8 o superior, el campo `Eslabones de competencia cubiertos` se usa para alimentar el diccionario.**

### Reglas de traducción de estados (nuevas v2.4)

135. **Los estados `introduce`, `desarrolla`, `aplica`, `evalúa` se traducen a prosa según la tabla de §0.12.**
136. **La traducción se ajusta al contexto del párrafo.**
137. **Si un mismo eslabón aparece varias veces, se traduce una vez y se hace referencia natural las siguientes.**
138. **Ningún párrafo del capítulo reproduce el estado interno como código.**
139. **Las palabras "introduce", "desarrolla", "aplica" o "evalúa" pueden aparecer en prosa solo como palabras corrientes del español, nunca como código.**
140. **El Anexo Z puede llevar eslabones como código, porque es material interno.**

### Reglas de emisión (nuevas v2.4)

141. **Si el diccionario tiene códigos huérfanos, el capítulo no se emite como completo.** Se emite como `incompleto por diccionario huérfano`, se declara al usuario y se espera resolución.
142. **Si el capítulo contiene códigos internos sin expandir en la prosa, se corrige antes de emitir.**
143. **El capítulo se emite con estado declarado en el bloque A:** `completo`, `incompleto por diccionario huérfano`, `incompleto por ficha faltante`.

---

## Contrato de salida

```markdown
# Capítulo [N] — [Nombre del capítulo]

## 0. Pre-bloques aplicados (referencia interna)
   0.1–0.9  Perfil de estilo del docente
   0.10     Regla de audiencia
   0.11     Diccionario de expansión local
   0.12     Traducción de estados internos a prosa

## A. Primera hoja (con audiencia, distribución por nivel, continuidad, materia
      concurrente y actividades oficiales mencionadas)
## B. Tabla de contenido navegable
## C. Introducción y motivación
## D. Objetivos de aprendizaje
## E. Desarrollo temático
   ### E.1 [Concepto Núcleo 1]
   ### E.2 [Concepto Núcleo 2]
   ### E.3 Conceptos panorámicos
   ### E.4 Conceptos propedéuticos
   ### E.5 Contexto y continuidad dentro del curso
## F. Ejemplos trabajados
## G. Casos de aplicación
## H. Ejercicios de autoevaluación
## I. Glosario
## J. Fuentes y referencias
## K. Articulación, continuidad y actividad de aprendizaje vinculada
   ### K.1 Antecedentes y relaciones disciplinares
   ### K.2 Materia de aplicación concurrente (condicional)
   ### K.3 Actividad de aprendizaje vinculada (condicional)
       #### K.3.1 Actividades que se trabajan directamente
       #### K.3.2 Otras actividades a las que el capítulo aporta
## L. Notas del docente (opcional)
## M. Advertencias y lagunas
## Anexo Z. Diccionario local y trazabilidad (interno, v2.4)
```

**Archivo:** `capitulo_N_[slug].md`

**Archivo alternativo si hay códigos huérfanos:** `capitulo_N_[slug]_incompleto.md`

---

## Cómo se relaciona con las otras skills

| Skill | Relación con 03e |
|---|---|
| 01 | Aporta Doc Maestro v1.5 o v1.6 (con §7.c, §8, §9) |
| 02 | Aporta Brief v2.7 o v2.8 (con articulación estructurada y actividades vinculadas) |
| 03a | Aporta conceptos con nivel (5), categoría de reserva (3) y bloque L |
| 03b | Aporta normativa |
| 03c | Aporta imágenes |
| 03d | Paralela |
| 05 | Consume los capítulos para compilar el libro |

---

## Checklist interno antes de entregar

### Verificaciones de legibilidad editorial (nuevas v2.4)

- ¿El capítulo declara `Audiencia del documento: alumno` en el bloque A?
- ¿El capítulo declara `Estado del capítulo` en el bloque A?
- ¿Se construyó el diccionario local antes de redactar?
- ¿El diccionario local cubre todos los códigos mencionados en el Brief y las fichas?
- ¿Hay algún código huérfano? Si sí, ¿se detuvo la producción y se reportó?
- ¿Ningún código interno aparece en la prosa sin expansión?
- ¿La primera mención de cada código lleva nombre legible + código entre paréntesis?
- ¿Las menciones posteriores llevan solo el nombre legible?
- ¿Los estados `introduce`, `desarrolla`, `aplica`, `evalúa` están traducidos a prosa?
- ¿Ningún párrafo reproduce el estado interno como código?
- ¿La única excepción son los anexos de trazabilidad (Anexo Z)?
- ¿El Anexo Z incluye el diccionario local?
- ¿El Anexo Z está claramente marcado como material interno?
- ¿En tablas de referencia interna (K.3, recursos visuales) se conserva código solo en la columna `ID` y nombre en la columna correspondiente?

### Verificaciones de referenciación interna de IDs

- ¿La primera mención de cada ID incluye su nombre completo?
- ¿Las menciones posteriores remiten a la sección del propio capítulo?
- ¿Todo ID mencionado en el cuerpo está declarado en K.3.1 o K.3.2?
- ¿Ningún ID se menciona "de pasada" sin definición?
- ¿El capítulo evita nombres de bloques internos, estados, versiones y reglas de activación?
- ¿Las consecuencias pedagógicas están traducidas a lenguaje del capítulo?

### Verificaciones de actividad de aprendizaje vinculada

- ¿La primera hoja declara las dos listas de actividades oficiales mencionadas?
- ¿K.3 se activa si hay al menos una actividad oficial vinculada, sin importar su estado?
- ¿K.3 se divide en K.3.1 y K.3.2?
- ¿K.3.1 tiene máximo 3 actividades?
- ¿K.3.2 tiene máximo 3 actividades?
- ¿Ninguna actividad aparece en ambas subsecciones?
- ¿Las actividades con estado activo están en K.3.1?
- ¿Las actividades con estado `aporta` están en K.3.2?
- ¿Solo se declaran actividades oficiales del temario?
- ¿El estado de K.3.1 coincide con el Brief?
- ¿El producto parcial (K.3.1) y el aporte (K.3.2) son específicos?
- ¿K.3 incluye las preguntas que conectan con las actividades oficiales?
- ¿No se inventaron actividades ni estados?
- ¿El bloque M incluye la nota sobre actividades oficiales?

### Verificaciones de materia de aplicación concurrente

- ¿El bloque K.2 se llama "Materia de aplicación concurrente"?
- ¿K.2 se activa solo si el Brief declara la materia?
- ¿K.2 tiene máximo 1 materia?
- ¿La materia de K.2 está también en K.1?
- ¿El tipo de relación en K.2 es `Aplicación concurrente`?
- ¿K.2 declara la materia con su nombre oficial?
- ¿K.2 incluye la evidencia esperada?
- ¿K.2 incluye la pregunta para el alumno?
- ¿Si no hay materia, K.2 se omite y la primera hoja declara `no aplica`?
- ¿El lenguaje es neutral?

### Verificaciones de continuidad

- ¿Existe la subsección E.5 "Contexto y continuidad dentro del curso"?
- ¿E.5 tiene las 3 categorías?
- ¿Cada concepto Reservado aparece en su categoría?
- ¿La redacción es declarativa, no de exclusión?
- ¿Cada concepto Reservado recibe transición natural?
- ¿La primera hoja declara `Continuidad principal`?
- ¿No hay falso cierre temático?

### Verificaciones del nivel Propedéutico

- ¿Existe la subsección E.4 si hay conceptos Propedéutico?
- ¿Cada Propedéutico tiene 2–4 párrafos?
- ¿Cada Propedéutico tiene remisión explícita?
- ¿Los Propedéutico no llevan aplicación, ejercicios ni fuentes de contraste?
- ¿Los Propedéutico no cuentan para la proporción Núcleo?

### Verificaciones de articulación curricular

- ¿La primera hoja declara `Articulación curricular principal`?
- ¿El bloque K tiene K.1 con máximo 4 conexiones?
- ¿K.1 tiene prosa breve + tabla de trazabilidad?
- ¿Cada conexión de K.1 tiene los 4 datos?
- ¿Cada conexión tiene trazabilidad documental?
- ¿K.2 se activa solo si hay aplicación explícita?
- ¿K.2 tiene máximo 1 materia?
- ¿K.2 declara `unidad no declarada` si no está en los insumos?
- ¿No se inventaron relaciones curriculares?
- ¿El campo `Articulación curricular principal` coincide con K.1 + K.2?

### Verificaciones del perfil de estilo

- ¿Existe el archivo `perfil_estilo_[docente].md`?
- ¿El perfil tiene todos los campos del §0.4?
- ¿Se aplicó el perfil durante la redacción?
- ¿Se resolvieron los conflictos según §0.6 (incluida la política de audiencia)?
- ¿Se verificó la consistencia de estilo según §0.7?
- ¿El capítulo suena al docente?
- ¿La primera hoja declara el perfil de estilo aplicado?

### Verificaciones de formato de capítulo

- ¿El capítulo tiene la primera hoja con toda la información identificadora?
- ¿El cuerpo del capítulo NO menciona la palabra "sesión"?
- ¿Las referencias a otros capítulos se hacen por nombre?
- ¿El nombre del archivo sigue la convención `capitulo_N_[slug].md`?

### Verificaciones de niveles

- ¿La Ficha Teórica es v1.11 o superior?
- ¿El capítulo declara `Distribución por nivel`?
- ¿Los conceptos Núcleo tienen desarrollo completo?
- ¿Los conceptos Panorama tienen presentación conceptual agrupada?
- ¿Los conceptos Contexto tienen mención de 1–2 líneas?
- ¿Los conceptos Reservado solo tienen remisión?
- ¿La proporción de extensión por nivel respeta las proporciones?
- ¿Los ejemplos, casos, ejercicios y conexión con taller son solo de Núcleo?
- ¿El glosario incluye términos de Núcleo y Panorama?
- ¿La sección M declara la estructura de niveles?

### Verificaciones de ponderación

- ¿El Brief es v2.7 o superior?
- ¿El capítulo declara `Pesos por subtema aplicados`?
- ¿Ningún Núcleo tiene menos extensión que uno medio o bajo?

### Verificaciones del modo de composición

- ¿El capítulo declara `Modo de composición`?
- Si retrospectivo: ¿el motivo está declarado?
- Si operativo: ¿la introducción NO incluye el párrafo retrospectivo?

### Verificaciones de integración visual

- ¿El campo `Imágenes incluidas` está declarado?
- ¿El campo `Estado de integración visual` está declarado?
- ¿Cada recurso corresponde a una NVD con `Capítulo: sí`?
- ¿Cada EXTERNO es exactamente el recurso validado por 03.C-3?
- ¿Cada GENERATIVO tiene `PASS` trazable y producción asociada?
- ¿Cada HÍBRIDO conserva la función y agrupación prescritas?
- ¿Ninguna NVD V1/V2 destinada al capítulo quedó sin satisfacer?
- ¿Toda V3/V4 omitida cuenta con aceptación explícita como no crítica?
- ¿Cada figura tiene pie con nombre legible?
- ¿Fuente, licencia y atribución se preservan cuando aplica?
- ¿La tabla interna registra NVD, recurso, procedencia y estado?
- ¿No existen placeholders de URL o generación pendiente?
- ¿Se respetan los máximos editoriales o se escaló cualquier conflicto de densidad?

### Verificaciones anti-presentación

- ¿El capítulo tiene más párrafos que subtítulos por sección?
- ¿La proporción subtítulos/párrafos es 1:4 a 1:6?
- ¿Los párrafos tienen mínimo 4 líneas?
- ¿Hay máximo 2 listas por concepto?
- ¿Las fórmulas están integradas en prosa?
- ¿Los ejemplos son narrativos?
- ¿Los conceptos Núcleo tienen máximo 2 subdivisiones internas?

### Verificaciones de contenido

- ¿Cada afirmación sustentable lleva cita?
- ¿Las citas coinciden con las referencias?
- ¿Hay mínimo 2 ejemplos?
- ¿Hay entre 3 y 5 ejercicios con respuestas?
- ¿El glosario tiene entre 5 y 15 términos?
- ¿Las lagunas están declaradas?
- ¿Los casos de contexto Mérida se activan solo si aplican?
- ¿La conexión con taller se activa solo si el Brief la declara?
- ¿Las notas del docente se incluyen solo si se pidieron?

---

## Archivos que produce la skill 03e

| Archivo | Contenido | Frecuencia |
|---|---|---|
| `capitulo_N_[slug].md` | Capítulo completo del libro | Por tema |
| `capitulo_N_[slug]_incompleto.md` | Capítulo incompleto por diccionario huérfano, ficha faltante o bloqueo visual contractual | Bajo demanda |
| `capitulo_N_[slug].pdf` | Versión PDF para distribuir (opcional) | Bajo demanda |
| `libro_[asignatura].md` | Compilación de todos los capítulos (opcional) | Al final del curso |
| `perfil_estilo_[docente].md` | Perfil de estilo del docente | Una vez por docente |

---

## Criterio final de calidad

La skill 03e cumple si:

### Criterios de legibilidad editorial (nuevos v2.4)

- **declara audiencia `alumno` en el bloque A**;
- **construye el diccionario local antes de redactar**;
- **el diccionario local cubre todos los códigos del Brief**;
- **ningún código huérfano bloquea la emisión sin ser reportado**;
- **ningún código interno aparece sin expandir en la prosa**;
- **la primera mención de cada código lleva nombre legible + código entre paréntesis**;
- **las menciones posteriores llevan solo el nombre legible**;
- **los estados internos están traducidos a prosa**;
- **ninguna reproducción de `C1=introduce` ni equivalente aparece en el capítulo**;
- **el Anexo Z es la única excepción y está precedido por el diccionario local**;
- **en tablas de referencia interna el código se conserva solo en la columna `ID`**;
- **el estado del capítulo está declarado (`completo` / `incompleto`)**.

### Criterios de referenciación interna de IDs

- **la primera mención de cada ID incluye su nombre completo**;
- **las menciones posteriores remiten a la sección del propio capítulo**;
- **todo ID mencionado está declarado en K.3.1 o K.3.2**;
- **ningún ID se menciona "de pasada" sin definición**;
- **el capítulo evita nombres de bloques internos, estados, versiones y reglas de activación**;
- **las consecuencias pedagógicas están traducidas a lenguaje del capítulo**.

### Criterios de actividad de aprendizaje vinculada

- **la primera hoja declara las dos listas de actividades mencionadas**;
- **K.3 se activa si hay al menos una actividad oficial vinculada**;
- **K.3 se divide en K.3.1 y K.3.2**;
- **K.3.1 máximo 3; K.3.2 máximo 3**;
- **ninguna actividad aparece en ambas**;
- **actividades activas en K.3.1; `aporta` en K.3.2**;
- **solo actividades oficiales del temario**;
- **el estado de K.3.1 coincide con el Brief**;
- **producto parcial y aporte son específicos**;
- **K.3 incluye las preguntas conectoras**;
- **no se inventaron actividades ni estados**;
- **si no hay actividad oficial, ambas listas se declaran como `ninguna`**.

### Criterios de materia de aplicación concurrente

- **K.2 se llama "Materia de aplicación concurrente"**;
- **K.2 se activa solo si el Brief declara materia**;
- **máximo 1 materia**;
- **la materia está también en K.1**;
- **tipo de relación es `Aplicación concurrente`**;
- **nombre oficial + evidencia esperada + pregunta**;
- **si no hay materia, K.2 se omite**;
- **lenguaje neutral**.

### Criterios de continuidad dentro del curso

- **existe E.5 con las 3 categorías**;
- **cada Reservado en su categoría**;
- **redacción declarativa**;
- **transición natural por cada Reservado**;
- **la primera hoja declara `Continuidad principal`**;
- **no hay falso cierre**.

### Criterios del nivel Propedéutico

- **existe E.4 si hay Propedéutico**;
- **2–4 párrafos cada uno**;
- **remisión explícita obligatoria**;
- **sin aplicación, ejercicios ni contraste**;
- **no cuentan para proporción Núcleo**.

### Criterios de articulación curricular

- **la primera hoja declara `Articulación curricular principal`**;
- **K.1 máximo 4 conexiones**;
- **K.1 prosa + tabla con los 4 datos**;
- **trazabilidad documental**;
- **K.2 solo si hay aplicación explícita**;
- **unidades/productos no declarados literalmente como `no declarado`**;
- **no se inventaron relaciones**.

### Criterios de estilo

- **existe el archivo `perfil_estilo_[docente].md`**;
- **el capítulo imita la voz del docente**;
- **respeta su nivel de formalidad, conectores, longitud de frases**;
- **no hay clichés de IA**;
- **la voz personal no sacrificó rigor, estructura ni política de audiencia**;
- **la primera hoja declara el perfil aplicado**.

### Criterios de formato de capítulo

- **primera hoja completa**;
- **el cuerpo no menciona "sesión"**;
- **referencias a otros capítulos por nombre**;
- **nombre del archivo `capitulo_N_[slug].md`**.

### Criterios de niveles

- **niveles de la Ficha Teórica**;
- **proporción de extensión respetada**;
- **Núcleo con desarrollo completo**;
- **Panorama con presentación conceptual agrupada**;
- **Contexto con mención**;
- **Reservado con remisión**;
- **ejemplos, casos, ejercicios, conexión con taller solo Núcleo**;
- **glosario con Núcleo y Panorama**;
- **sección M declara estructura**.

### Criterios generales

- **pesos por subtema del Brief reflejados**;
- **no aparece `N/D`**;
- **`Modo de composición` declarado**;
- **cada recurso visual supera la compuerta contractual y tiene destino `Capítulo: sí`**;
- **cada imagen tiene pie de figura con nombre descriptivo legible**;
- **la trazabilidad interna conserva ID NVD y recurso downstream**;
- **los recursos externos preservan fuente, licencia y atribución**;
- **los recursos generativos conservan evidencia interna de PASS sin exponer metalenguaje al alumno**;
- **el alumno puede estudiar sin clase**;
- **el capítulo se lee como texto argumentado**;
- **párrafos ≥ 4 líneas; máximo 2 subdivisiones internas por Núcleo**;
- **fórmulas integradas en prosa**;
- **ejemplos narrativos**;
- **citas coinciden con referencias**;
- **autoevaluación con respuestas separadas**;
- **glosario con términos clave**;
- **fuentes organizadas por categoría**;
- **tabla de contenido navegable**;
- **formato Markdown compatible con PDF**;
- **lagunas declaradas**;
- **lenguaje del nivel del Brief**;
- **proporción subtítulos/párrafos 1:4 a 1:6**;
- **capítulo autocontenido**;
- **el capítulo sale con lenguaje natural para el alumno, sin códigos internos del pipeline visibles**.

---

## Changelog de consolidación v2.3 → v2.4

**Propósito:** alinear 03.E con la arquitectura visual vigente y convertirla en consumidor editorial downstream de recursos visuales resueltos, sin reabrir decisiones de 03.C.

### Contenido normativo preservado de v2.3

Se preservan sin cambio de propósito:

- capítulo autónomo para alumno;
- estructura A–M + Anexo Z;
- desarrollo por cinco niveles;
- ponderación por subtema;
- modo operativo/retrospectivo;
- perfil de estilo del docente;
- política de audiencia;
- diccionario local;
- traducción de estados internos;
- articulación curricular K.1–K.3;
- actividad oficial vinculada;
- reglas anti-presentación;
- citación académica;
- autoevaluación, glosario y lagunas.

### Contenido nuevo en v2.4

1. **Interfaz visual nueva:** se elimina `Ficha Visual v1.8` como entrada contractual vigente.
2. **03.C-1 v1.2** se vuelve fuente canónica de NVD, destino, función, procedencia, tratamiento y criterio de satisfacción.
3. **03.C-3** alimenta recursos externos, preservando identidad, fuente, autoría, derechos, licencia, atribución y localizador.
4. **Rama generativa:** solo se integran recursos producidos desde RGE con `PASS` de 03.C-2B y trazabilidad a 03Cbis.
5. **Compuerta visual para capítulo:** `ADMISIBLE_EXTERNO`, `ADMISIBLE_GENERATIVO`, `ADMISIBLE_HÍBRIDO`, `OMISIBLE_NO_CRÍTICO`, `BLOQUEO_VISUAL`.
6. **Control de destino:** la NVD debe declarar `Capítulo: sí`.
7. **Principio de integración editorial sin reinterpretación.**
8. **El capítulo completo no admite placeholders de URL o generación pendiente.**
9. **NVD V1/V2 no satisfecha impide declarar el capítulo como completo.**
10. **V3/V4 pendiente** solo puede omitirse con aceptación upstream explícita como no crítica.
11. **Pies de figura orientados al alumno:** nombre legible; IDs técnicos trasladados a trazabilidad interna.
12. **Tabla de recursos visuales ampliada** con Figura, NVD, ID recurso, procedencia, fuente/localizador, licencia/atribución, PASS/huella y estado de integración.
13. **Preservación de atribución/licencia** para recursos externos.
14. **Preservación de identidad de RGE/PASS** para generativos sin exponer metalenguaje al alumno.
15. **Protocolo de retorno por propiedad contractual:** estrategia → 03.C-1; generativo → 03.C-2A + nueva 03.C-2B; externo → 03.C-3.
16. **Conflicto de densidad visual:** 03.E no altera silenciosamente ni el contrato ni sus máximos editoriales; escala a 03.C-1.

### Compatibilidad v2.4

- Brief: **v2.7 o v2.8**.
- Ficha Teórica: **v1.11 o v1.12**.
- Ficha Normativa: **v1.4**.
- Doc Maestro: **v1.5 o v1.6**.
- Perfil de estilo: vigente.
- 03.C-1: **v1.2 obligatorio**.
- 03.C-2A: **v1.2** cuando exista componente generativo.
- 03.C-2B: **v1.0** cuando exista componente generativo.
- 03.C-3: **v0.1 BORRADOR** como interfaz provisional mientras no exista versión estable posterior compatible.
- 03Cbis: se exige producción trazable al RGE aprobado; v2.4 no presume compatibilidad de una salida que no pueda demostrar `RGE → PASS → producción`.

**Regla de migración:** una `Ficha Visual v1.8` legado no satisface por sí sola el contrato visual de 03.E v2.4.

---

## Changelog de consolidación v2.2 → v2.3

**Propósito:** garantizar que el capítulo dirigido al alumno salga con lenguaje natural, sin códigos internos del pipeline visibles, sin modificar el resto del flujo.

**Contenido normativo preservado de v2.2 (sin cambios):**

- Posición en el flujo.
- Propósito.
- Cuándo activar.
- Qué NO es el documento.
- Estructura de 14 bloques.
- §0.1–§0.9 (perfil de estilo).
- Bloques A, B, C, D, E (con subsecciones internas), F, G, H, I, J, K (con K.0.1–K.0.9, K.1, K.2, K.3, K.4), L, M.
- Reglas 1–115.
- Checklist existente.
- Criterios finales existentes.
- Contrato de salida.
- Relación con otras skills.
- Archivos producidos.

**Contenido nuevo en v2.3:**

- **§0.10 Regla de audiencia**: prohíbe códigos internos sin expansión en el capítulo dirigido al alumno.
- **§0.11 Diccionario de expansión local**: procedimiento para construir la tabla código → nombre legible; regla del diccionario huérfano; consumo de Brief v2.8.
- **§0.12 Traducción de estados internos a prosa**: tabla de conversión contextual para `introduce`, `desarrolla`, `aplica`, `evalúa`.
- **§K.0.10 Regla de audiencia aplicada al bloque K**.
- **Nuevo bloque Anexo Z — Diccionario local y trazabilidad** (excepción única a la política de audiencia).
- **Bloque A ampliado**: campos `Audiencia del documento: alumno` y `Estado del capítulo`.
- **Reglas 116–143**: audiencia, diccionario, traducción de estados, emisión.
- **Verificaciones nuevas en checklist**: legibilidad editorial.
- **Criterios nuevos en criterio final**: legibilidad editorial.
- **Ejemplos en §0.10, §0.11, §0.12**: para cada política.
- **Reglas de emisión**: estado declarado (`completo` / `incompleto`).
- **Archivo alternativo**: `capitulo_N_[slug]_incompleto.md`.
- **Changelog v2.2 → v2.3** (este bloque).

**Cambios de empaquetado:**

- Se añadieron §0.10, §0.11, §0.12 sin renumerar §0.1–§0.9.
- Se añadió §K.0.10 sin renumerar K.0.1–K.0.9.
- Se añadió el bloque Anexo Z al final del capítulo sin renumerar los bloques A–M.
- Se añadieron reglas 116–143 sin renumerar 1–115.
- Se amplió el checklist con un bloque nuevo.
- Se amplió el criterio final con un bloque nuevo.
- Se actualizó el resumen de capacidades por versión.

**Actualizaciones de compatibilidad:**

- Brief consumidor: **v2.7 o v2.8** (v2.8 preferido por el campo `Eslabones de competencia cubiertos`).
- Ficha Teórica consumidora: **v1.11 o v1.12** (v1.12 preferida por el campo `Suficiencia para eslabón`).
- Ficha Normativa consumidora: v1.4.
- Ficha Visual consumidora: v1.8.
- Doc Maestro consumidor: v1.5 o v1.6.
- **No requiere cambios upstream.** La política de audiencia vive solo en 03.E.

---

## Changelog de consolidación v2.1 → v2.2 (conservado)

**Propósito:** convertir la skill en autocontenida y actualizar referencias a las skills ya consolidadas.

**Verificación de autocontención:**

- Se auditó v2.1 contra las versiones históricas v1.0–v2.0.
- v2.1 usaba referencias `[Sin cambios respecto a v2.0]` en varias secciones.
- Se expandieron literalmente todas las referencias a versiones anteriores.

**Cambios aplicados en v2.2:**

1. **Título:** v2.1 → v2.2.
2. **Referencias al Brief:** v2.6 → **v2.7**.
3. **Referencias a la Ficha Teórica:** v1.7 → **v1.11**.
4. **Referencias a la Ficha Normativa:** v1.3 → **v1.4**.
5. **Referencias a la Ficha Visual:** v1.7 → **v1.8**.
6. **Referencias al Doc Maestro:** v1.4 → **v1.5**.
7. **Nota de compatibilidad:** actualizada.
8. **Contenido íntegro expandido.**
9. **Resumen de capacidades por versión.**
10. **Changelog de consolidación.**

---

**Guía de uso del flujo completo:** consulta `guia_uso_flujo_skills_v4.0.md`.