---
name: 02-briefs-sesion
description: Expande cada sesion del Documento Maestro en un Brief contractual estructurado para alimentar 03.A, 03.B, 03.C, 03.D y 03.E.
stage_id: "02"
version: "2.8"
status: stable
---

# Skill: Briefs por Sesión para Generación Didáctica (v2.8)

## Propósito

Esta skill toma el **Documento Maestro de Curso** (producido por la skill 01 v1.5 o superior) y expande **cada sesión del calendario** en un **brief estructurado con contrato fijo**, consumible por las cinco sub-skills del flujo de generación didáctica:

- **03a — Ficha Teórica:** conceptos, corriente teórica, fuentes, articulación curricular, expansión conceptual controlada por alcance.
- **03b — Ficha Normativa:** tipo de proyecto, zona patrimonial, contexto regional.
- **03c — Ficha Visual:** conceptos a ilustrar, restricciones visuales.
- **03d — Composición Dual:** hora real, duración, prerrequisitos, refuerzo inicial, pesos por subtema, modo de composición, actividades oficiales vinculadas.
- **03e — Capítulo de Libro Autónomo:** nivel, tipo de sesión, prerrequisitos, articulación curricular, conceptos clave, pesos por subtema, modo de composición, actividad de aprendizaje vinculada.

Esta skill **no pondera temas, no reparte sesiones y no decide el calendario**. Su única función es:

1. **Enriquecer** cada sesión con los campos que las cinco sub-skills necesitan consumir.
2. **Verificar** que el conjunto de briefs cubra todos los eslabones de competencia declarados en el Documento Maestro (introduce → desarrolla → aplica → evalúa).

La verificación es una capa nueva respecto a v2.7. Cierra la brecha entre "briefs completos individualmente" y "conjunto de briefs responsable de las competencias declaradas".

Aplica a cualquier materia, nivel educativo, duración de sesión, modalidad, periodicidad y **disciplina**. El vocabulario es neutral: no presupone talleres, proyectos ni formas disciplinares específicas.

**Versión autocontenida.** Esta versión no depende de versiones anteriores. Todo el contenido vigente está expandido literalmente.

### Principio rector

**Briefs individualmente completos ≠ conjunto de briefs responsable.**

Un conjunto de briefs puede estar completo campo por campo y, a la vez, no cubrir un eslabón de alguna competencia declarada en el Documento Maestro. La v2.8 detecta esa carencia antes de emitir.

**Regla dura:** el conjunto de briefs no se emite como completo si existe al menos un eslabón de competencia declarada sin sesión asignada en el Documento Maestro. Se emite como **incompleto** con lista de eslabones huérfanos.

---

## Cuándo activar esta skill

Actívala cuando el usuario:

- Ya tenga un Documento Maestro de Curso generado (o en curso).
- Pida "briefs por sesión", "fichas de sesión para generar guiones", "preparar el material de cada clase", o similar.
- Quiera un documento intermedio entre la planeación general y el flujo de cinco sub-skills de generación didáctica.
- Quiera generar material de estudio o documentación para **sesiones ya impartidas** (modo retrospectivo).

No la actives si todavía no existe el Documento Maestro: primero corresponde la skill 01, que produce el calendario y la ponderación.

**Nota de compatibilidad:** esta skill requiere que el Doc Maestro sea **v1.5 o superior** (con tabla 7.b completa, sección de articulación curricular, §21 con la matriz de trazabilidad de competencias, y — si el temario declara actividades oficiales — §7.c, §8 y §9). Si el Doc Maestro es v1.4 o anterior, no tiene §21 y el Brief v2.8 no puede cumplir su capa de verificación. En ese caso, detente y remite a la skill 01 v1.5.

**Excepción:** si el temario oficial **no declara actividades explícitas**, el Doc Maestro se genera sin §7.c, §8 y §9. En ese caso, el Brief v2.8 funciona con normalidad para todo lo demás, y los campos de actividad oficial se marcan como `sin actividad oficial declarada`. La verificación de competencias (§21) sí sigue vigente.

---

## Estructura del flujo

```
Skill 01 ──► Documento Maestro v1.5 ──┐
        (con §7.c, §8, §9, §21)       │
                                       ▼
                                 Skill 02 (esta)
                                       │
                                       ▼
                    Briefs individuales + Matriz de cobertura
                                       │
              ┌────────────────────────┼────────────────────────┐
              ▼                        ▼                        ▼
          03a Teórica            03b Normativa            03c Visual
              │                        │                        │
              └────────────┬───────────┴────────────────────────┘
                           ▼
                   Brief + 3 fichas
                           │
                ┌──────────┴──────────┐
                ▼                     ▼
        03d Composición        03e Capítulo
        (sincrónico)           (asincrónico)
```

---

## Fase 1 — Verificación del insumo y encuadre global

### 1.1 Verificación del Documento Maestro (obligatorio)

Confirma que existe y está disponible:

- Calendario general de sesiones con fechas, duración y **estado operativo** (`impartida / próxima / pendiente`).
- Sección de metodología adaptativa.
- Sistema de evaluación.
- **Tabla 7.a — Ponderación por unidad.**
- **Tabla 7.b — Ponderación por subtema** (con pesos en todos los subtemas, sin excepción por estado operativo).
- **§7.c — Actividades oficiales de aprendizaje** (si el temario las declara).
- **§8 — Matriz actividad × sesión** (si aplica).
- **§9 — Matriz de continuidad conceptual** (siempre).
- **§21 — Matriz de trazabilidad de competencias** (siempre en v1.5+). Contiene la lista de competencias declaradas y los cuatro eslabones esperados (introduce → desarrolla → aplica → evalúa).
- **§22 — Control de consistencia** (v1.5+). Permite verificar el estado del Maestro antes de consumirlo.
- Competencias y resultados de aprendizaje.
- Diagnóstico del temario y tipología por unidad.
- **Sección de articulación curricular** (materias antecedentes, consecuentes, de aplicación concurrente).
- **Competencias posteriores del curso** (necesarias para determinar si aplica el alcance propedéutico).
- Modalidad del curso y número de alumnos.
- Contexto geográfico del curso.
- Propósito del documento maestro.

**Verificación crítica:**

- Si falta el Doc Maestro → detente y remite a la skill 01.
- Si el Doc Maestro es v1.4 o anterior → detente y remite a 01 v1.5 (falta §21).
- Si falta la tabla 7.b → detente.
- Si la tabla 7.b contiene pesos vacíos (`ya cubierto`, `no aplica`, `sin ponderar`) → detente. El Doc Maestro no siguió la regla de separación peso/estado.
- Si falta §21 (matriz de trazabilidad de competencias) → detente. Sin ella, no se puede verificar la cobertura de eslabones.
- Si §21 tiene competencias huérfanas sin decisión tomada → detente. El Maestro está incompleto; primero debe resolverse en skill 01.
- Si falta la sección de articulación curricular → se declara `no declarada` en el Brief y se reporta al usuario.
- Si falta la sección de competencias posteriores y el subtema parece literal → se declara `no declaradas` y no se aplicará alcance propedéutico.
- Si el temario no declara actividades oficiales → continúa con normalidad; §7.c, §8 y §9 estarán ausentes y los campos de actividad se marcarán como `sin actividad oficial declarada`.

### 1.2 Encuadre global del curso (una sola vez)

Pregunta en un solo bloque. **No asumas respuestas a partir de cursos previos.**

1. **Tipo de curso según área disciplinar.** ¿A cuál de las siguientes áreas pertenece esta asignatura? (Historia y teoría / Diseño arquitectónico / Representación / Construcción y materiales / Estructuras / Instalaciones / Sustentabilidad / Paisaje / Administración y legislación / Formación humana / Matemáticas y ciencias.)

2. **Corriente teórica dominante del curso.** ¿Una sola corriente a lo largo del curso, o varía por unidad? Si varía, ¿qué corriente corresponde a cada unidad?

3. **Materia de aplicación concurrente principal.** ¿Existe una asignatura donde el alumno aplique directamente lo aprendido en la misma etapa formativa? Si sí, ¿cuál y cómo se relaciona? Si no, se declara `no aplica`.

   **Nota:** el término es neutral. Puede ser un taller de diseño, una clínica jurídica, una práctica hospitalaria, un laboratorio de análisis, un seminario de caso, un estudio de mercado, o cualquier asignatura donde el alumno aplique lo aprendido en la misma etapa.

4. **Contexto geográfico del caso.** ¿Los proyectos y ejemplos se sitúan en Mérida, Yucatán, o en otra localidad? Si varía por sesión, se declarará por sesión.

5. **Datos operativos de la sesión.** ¿Todas las sesiones tienen la misma duración y hora de inicio, o varían por día? Si varían, se declararán por sesión.

6. **Restricciones de recursos.** ¿Hay restricciones para la generación de contenido (sin práctica física, sin laboratorio, sin acceso a cierto software, solo recursos digitales)?

7. **Nivel de profundidad esperado.** ¿Uniforme a lo largo del curso, o varía (introductorio → aplicado → técnico-profesional)?

8. **Alcance del encargo.** ¿Los briefs se generarán solo para sesiones pendientes y próximas, o también para sesiones ya impartidas? Si se generarán para sesiones impartidas, se declarará el motivo (documentación histórica, material de estudio para alumnos que no asistieron, reconstrucción para auditoría, etc.).

### 1.3 Verificación de la matriz de trazabilidad de competencias del Maestro (NUEVA en v2.8)

**Activación:** siempre.

**Propósito:** extraer del Documento Maestro (§21) la lista completa de competencias declaradas y los cuatro eslabones esperados por cada una, para poder verificar en Fase 4 que el conjunto de briefs los cubre.

#### Procedimiento

1. Leer **§21 — Matriz de trazabilidad de competencias** del Doc Maestro.
2. Extraer la lista de competencias declaradas (IDs `C1, C2, ...`).
3. Para cada competencia, extraer los cuatro eslabones esperados y la sesión o evidencia que el Maestro les asignó:
   - Introduce (sesión).
   - Desarrolla (sesión).
   - Aplica (sesión).
   - Evalúa (evidencia + sesión).
4. Verificar que **ningún eslabón esté sin sesión asignada** en el Maestro.
   - Si el Maestro dejó un eslabón sin sesión (porque la competencia fue reclasificada como contextual o transversal, o porque el Maestro se emitió como versión incompleta), se declara la limitación y se ajusta la verificación.
5. Producir la **tabla de referencia** que servirá para verificar la cobertura en Fase 4.

#### Estructura de la tabla de referencia

| ID | Competencia | Introduce (S) | Desarrolla (S) | Aplica (S) | Evalúa (S) | Estado en Maestro |
|---|---|---|---|---|---|---|
| C1 | ... | S_N | S_N | S_N | S_N | Completa |
| C2 | ... | S_N | S_N | S_N | S_N | Completa |
| C3 | ... | — | — | — | — | Reclasificada / Transversal / Pendiente |

#### Reglas duras

- **No inventar competencias.** Solo las de §21 del Maestro.
- **No modificar el estado de las competencias.** Si el Maestro las declaró completas, huérfanas, contextuales o transversales, ese estatus se respeta.
- **Si §21 no existe** → detente y remite a la skill 01 v1.5.
- **Si §21 tiene competencias huérfanas sin decisión** → detente. El Maestro debe resolverse antes de generar los briefs.
- **La tabla de referencia se conserva** y se usa en Fase 4 para verificar cobertura.

#### Presentación al usuario

Antes de continuar, presenta la tabla de referencia al usuario. Si el usuario objeta, se detiene la generación hasta resolver la objeción.

---

## Fase 2 — Encuadre operativo por sesión

### 2.1 Datos operativos por sesión

Por cada sesión del calendario:

- Duración real (minutos).
- Hora real de inicio.
- Modalidad de la sesión (presencial / virtual / híbrida).
- Número de alumnos del grupo.
- Estado operativo (`impartida / próxima / pendiente`) — heredado del calendario del Doc Maestro.

Si el Doc Maestro ya los declara, se heredan. Si no, se preguntan al usuario una sola vez, agrupados, sin abrir pregunta por sesión.

### 2.2 Detección de prerrequisitos por sesión

La skill 02 examina el temario oficial y el Doc Maestro para detectar, por cada sesión, los conceptos prerrequisito que la sesión asume:

- Conceptos de sesiones previas dentro de la misma unidad.
- Conceptos base de unidades previas.
- Conceptos que el Doc Maestro marcó como críticos o como dependencia curricular.

El resultado no decide el refuerzo inicial. Solo lo **sugiere** a 03d, que es quien tiene la última palabra.

### 2.3 Clasificación del tipo de sesión

Cada sesión se clasifica en uno o varios tipos, según la naturaleza del contenido:

| Tipo de sesión | Cuándo aplica | Campos específicos que activa |
|---|---|---|
| **Teórica / histórica** | Conceptos, corrientes, historiografía | Corriente teórica, contraste, citas |
| **Analítica** | Resolución de problemas, casos, crítica | Ejes de análisis, criterios, comparación |
| **Proyectual** | Diseño, metodología, partido | Conexión con aplicación concurrente, sitio, prefiguración |
| **Técnica / cálculo** | Estructuras, matemáticas, instalaciones | Fórmula, procedimiento, NTC |
| **Constructiva / material** | Sistemas, procesos, acabados | Detalle constructivo, fabricante, NTC |
| **Bioclimática / sustentable** | Clima, energía, agua, materiales | Clima, normativa energética, certificaciones |
| **Normativa / legislación** | Leyes, reglamentos, trámites | Norma aplicable, ámbito, vigencia |
| **Formación humana** | Desarrollo personal, ética, convivencia | Corriente psicológica o filosófica |
| **Taller / práctica** | Modelos, maquetas, dibujo | Insumos físicos, herramientas, espacio |

Si una sesión combina tipos, se declara cuál domina y cuáles son secundarios.

### 2.4 Herencia de pesos por subtema (obligatorio)

Por cada sesión del calendario, el Brief hereda **desde la tabla 7.b del Doc Maestro** el peso (alto / medio / bajo) de cada subtema cubierto en esa sesión.

**Procedimiento:**

1. Del Brief, tomar la lista de subtemas oficiales cubiertos (bloque B).
2. Del Doc Maestro, sección 7.b, tomar el peso interno de cada uno de esos subtemas.
3. Registrar en el bloque B del Brief la lista de pesos correspondiente.
4. Si un subtema de la sesión no aparece en la tabla 7.b, **no se inventa el peso**: se marca como `sin ponderar en Doc Maestro` y se reporta al usuario para que regenere el Doc Maestro.

**Reglas de herencia:**

- **No se recalcula el peso.** Se hereda tal cual del Doc Maestro.
- **No se inventa el peso** si falta.
- **No se modifica el peso** aunque el Brief detecte que la sesión tiene muchos subtemas y pocos minutos. Ese problema se resuelve en 03d.
- **Si la sesión cubre un solo subtema**, su peso es el que declare la tabla 7.b. No se marca como `N/D` bajo ninguna circunstancia.
- **El peso no depende del estado operativo.** Una sesión impartida conserva los pesos de sus subtemas.
- **Si el Doc Maestro es v1.4 o anterior** y no tiene la tabla 7.b, detente.

### 2.5 Modo de composición (obligatorio)

Cada brief declara un **modo de composición** derivado del estado operativo:

| Estado operativo | Modo de composición | Comportamiento en 03d y 03e |
|---|---|---|
| `pendiente` | **operativo** | Flujo normal. Checkpoints, vista paralela, presupuesto vinculante, refuerzo inicial activable. |
| `próxima` | **operativo** | Igual que pendiente. |
| `impartida` | **retrospectivo** | Sin checkpoints operativos, sin vista paralela. Presupuesto estimado, no vinculante. Refuerzo inicial no se activa. Material de referencia y estudio. |

**Reglas del modo de composición:**

- El modo se deriva automáticamente del estado operativo. No se pregunta al usuario.
- Si el estado es `impartida`, el modo es `retrospectivo` y se requiere declarar el **motivo** en el bloque I.
- Si el estado es `pendiente` o `próxima`, el modo es `operativo` y el motivo no aplica.
- El modo se declara en el bloque A del Brief, campo `Modo de composición`.
- El motivo se declara en el bloque I del Brief, campo `Motivo del modo retrospectivo`.

**Motivos válidos del modo retrospectivo:**

- Documentación histórica del curso.
- Generación de material de estudio para alumnos que no asistieron.
- Reconstrucción para auditoría institucional.
- Otro (especificar).

**Prohibición:** no se puede declarar modo retrospectivo sin motivo. Tampoco se puede declarar modo operativo para una sesión impartida.

### 2.6 Determinación del alcance conceptual del subtema

Por cada sesión, determina el **alcance conceptual** del subtema oficial. Este campo gobierna la expansión conceptual que hará 03.A.

#### Los cuatro valores posibles

| Valor | Cuándo aplica | Qué debe hacer 03.A |
|---|---|---|
| **`literal`** | El temario nombra técnicas específicas y autocontenidas. No hay competencia posterior que exija introducir conceptos ahora. | No expande. Los conceptos son los del temario. |
| **`literal con extensión propedéutica`** | El temario nombra técnicas específicas, **pero existe una competencia posterior documentada que requiere introducir algunos conceptos ahora** (sin desarrollarlos técnicamente). | Expande solo para agregar conceptos **Propedéutico**. Los Núcleo siguen siendo los del temario. |
| **`amplio`** | El temario nombra una categoría disciplinar amplia que agrupa múltiples subconceptos reconocidos por la disciplina. | Expande en 5 niveles (Núcleo / Panorama / Propedéutico / Contexto / Reservado). |
| **`panorámico`** | El temario nombra una categoría amplia y la sesión es introductoria. | Expande con énfasis en Panorama y Propedéutico. Núcleo reducido. |

#### Test de determinación

**Señales de alcance `literal`:**
- Nombra una técnica, procedimiento o producto específico.
- Se puede enseñar como unidad autocontenida.
- El temario enumera explícitamente los subconceptos.
- **No hay competencia posterior documentada** que dependa de conceptos no incluidos en el temario.

**Señales de alcance `literal con extensión propedéutica`:**
- Cumple todas las señales de `literal`.
- **Además**, existe al menos una competencia posterior documentada (en el Doc Maestro, el temario o el Brief) que requiere que el alumno comprenda conceptos que no están enumerados literalmente en el subtema actual.
- Los conceptos propedéuticos son **preparatorios**, no núcleo del tema.

**Señales de alcance `amplio`:**
- Usa términos como "sistemas de", "fundamentos de", "principios de", "métodos de", "tipos de".
- El temario no enumera los subconceptos.
- La disciplina reconoce múltiples subconceptos bajo esa denominación.

**Señales de alcance `panorámico`:**
- Cumple todas las señales de `amplio`.
- Además, la sesión está en cuatrimestres tempranos (1–3) o es introductoria.
- El Brief declara un nivel de profundidad `introductorio`.

#### Cómo se declara en el Brief

```
- **Alcance conceptual del subtema:** [literal / literal con extensión propedéutica / amplio / panorámico]
- **Nota de alcance:** [instrucción específica para 03.A, opcional]
- **Competencias posteriores que activan el propedéutico:** [solo si aplica; lista de competencias documentadas]
```

**Ejemplo de nota para alcance propedéutico:**

> "1.4 Unidades de medida" es literal, pero el Doc Maestro establece que el alumno debe reconocer las limitaciones de las tecnologías topográficas (competencia de sesiones 6 y 12). Por tanto, se introducen como Propedéutico los conceptos de resolución, precisión, exactitud, error de medición y cifras significativas, sin desarrollar cálculo formal de incertidumbre ni tolerancias metrológicas.

#### Verificación de consistencia

- Si el test da `literal` pero hay competencias posteriores documentadas, reconsiderar si debe ser `literal con extensión propedéutica`.
- Si el test da `literal con extensión propedéutica` pero no hay competencia posterior documentada, retroceder a `literal`.
- Si el test da `amplio` pero el nivel de profundidad es `técnico-profesional` y el cuatrimestre es avanzado (7–9), considerar reducir a `literal con extensión propedéutica` o `literal`.
- Si hay duda, marcar como `amplio` y agregar nota explicando la decisión.

#### Prohibiciones

- **No marcar todo como `literal`** por prudencia.
- **No marcar todo como `amplio`** por defecto.
- **No marcar `literal con extensión propedéutica` sin competencia posterior documentada.** El propedéutico no se inventa.
- **No inventar competencias posteriores.** Solo se declaran las que estén en el Doc Maestro, el temario o el Brief.
- **No contradecir el temario.** Si el temario enumera subconceptos específicos, el alcance es `literal` aunque la denominación parezca amplia.

### 2.7 Asignación de actividades oficiales por sesión

**Activación:** solo si el Doc Maestro tiene §7.c y §8.

#### Procedimiento

1. **Consultar la matriz §8 del Doc Maestro** para la sesión N.
2. **Identificar qué actividades oficiales tienen estado activo en esa sesión** (cualquier estado excepto `no aplica`).
3. **Para cada actividad oficial activa en la sesión, extraer:**
   - ID de actividad (`AC-NN` o `AI-NN`).
   - Nombre de la actividad (de §7.c).
   - Estado en esta sesión (de §8).
   - Producto parcial esperado (si el estado es `desarrolla` o `consolida`).
4. **Si la sesión no tiene actividades oficiales activas** (todas en `no aplica`), se declara `sin actividad oficial en esta sesión`.

#### Reglas duras

- **No inventar actividades oficiales.** Solo las de §7.c.
- **No renombrar actividades oficiales.** El nombre debe ser fiel al temario.
- **No modificar el estado de la actividad.** Viene de §8 del Doc Maestro.
- **Una sesión puede tener 0, 1 o varias actividades oficiales activas.**
- **Los IDs de actividad son estables y atraviesan el pipeline.**

### 2.8 Asignación de articulación curricular por sesión (obligatorio)

**Activación:** siempre.

#### Procedimiento

1. **Consultar la sección de articulación curricular del Doc Maestro v1.5.**
2. **Identificar qué materias del plan de estudios se relacionan con el contenido de esta sesión específica.**
3. **Clasificar cada relación por tipo:**
   - **Antecedente:** materia previa que aporta conocimiento base.
   - **Aplicación concurrente:** materia de la misma etapa formativa donde el alumno aplica directamente lo aprendido.
   - **Consecuente:** materia posterior que depende de este contenido.
   - **Contexto disciplinar:** materia que ayuda a situar el conocimiento sin dependencia directa.
4. **Declarar hasta 4 materias en `Articulación prioritaria`**, ordenadas por relevancia.
5. **Declarar 0 o 1 materia en `Materia de aplicación concurrente principal`**.
6. **Si ninguna materia se relaciona con la sesión**, declarar `sin articulación documentada`.

#### Reglas duras

- **No inventar relaciones.** Solo las declaradas en el Doc Maestro.
- **Máximo 4 materias en `Articulación prioritaria`.**
- **Máximo 1 materia en `Materia de aplicación concurrente principal`.**
- **La materia de aplicación concurrente principal debe estar también en `Articulación prioritaria`.**
- **Si el Doc Maestro no declara articulación, se declara `sin articulación documentada`.**
- **La relación debe ser específica al contenido de esta sesión**, no genérica al curso.

### 2.9 Determinación de eslabones de competencia cubiertos por sesión (NUEVA en v2.8)

**Activación:** siempre, si §1.3 produjo una tabla de referencia con al menos una competencia.

**Propósito:** para cada sesión, determinar qué competencias cubre y qué eslabón(es) de cada una activa. Esta información alimenta la verificación de cobertura en Fase 4.

#### Procedimiento

1. **Consultar la tabla de referencia** producida en §1.3.
2. **Para cada competencia declarada**, verificar si la sesión N está asignada a alguno de sus cuatro eslabones (según lo que declaró el Maestro en §21).
3. **Registrar en el Brief los eslabones cubiertos por esta sesión**, con el formato:
   ```
   Eslabones de competencia cubiertos: C1=introduce, C2=desarrolla, C3=evalúa
   ```
4. **Si la sesión no cubre ningún eslabón de ninguna competencia**, se declara `ninguno (sesión de fundamento operativo)`.

#### Ejemplo

Si en §21 del Maestro aparece:
- C1 — Introduce en S2, Desarrolla en S3, Aplica en S4, Evalúa en S4.
- C2 — Introduce en S2, Desarrolla en S5, Aplica en S6, Evalúa en S6.

Entonces:
- Sesión 2 cubre: `C1=introduce, C2=introduce`.
- Sesión 3 cubre: `C1=desarrolla`.
- Sesión 4 cubre: `C1=aplica, C1=evalúa`.
- Sesión 5 cubre: `C2=desarrolla`.
- Sesión 6 cubre: `C2=aplica, C2=evalúa`.

#### Reglas duras

- **No inventar cobertura.** Solo se declaran los eslabones que el Maestro asignó a esa sesión.
- **No modificar la asignación del Maestro.** Si el Maestro puso "C1 introduce en S2", el Brief de S2 lo declara. Si el Brief detecta un error del Maestro, se reporta como hallazgo adicional, pero no se corrige.
- **Una sesión puede cubrir 0, 1 o varios eslabones**, de una o varias competencias.
- **El formato es compacto**: `[ID]=[eslabón], [ID]=[eslabón], ...`.
- **Los cuatro eslabones válidos son**: `introduce`, `desarrolla`, `aplica`, `evalúa`.

#### Coherencia con §2.6

Si una sesión cubre un eslabón `aplica` de alguna competencia, el alcance conceptual de sus subtemas debería ser coherente (al menos `literal con extensión propedéutica` o superior). Si el alcance es `literal` puro y la sesión está aplicando una competencia, se reporta como posible inconsistencia del Maestro.

---

## Fase 3 — Generación de briefs por sesión

Por **cada sesión del calendario** —incluyendo encuadre inicial, cierre/presentación final y sesiones con práctica profesional o campo— se produce un Brief con el **contrato fijo v2.8** definido más abajo.

No se redacta el guion completo ni se describen imágenes específicas: el brief es el insumo, no el contenido final.

No se recalcula ni se reordena nada. Se hereda del Doc Maestro y se enriquece.

---

## Contrato fijo del Brief v2.8

Cada brief tiene **9 bloques** y un total de **36 campos** (uno más que v2.7).

El campo nuevo es `Eslabones de competencia cubiertos` en el bloque B.

```markdown
## Sesión N — [fecha] — [tema]

### A. Identificación
- Asignatura: [nombre]
- Clave: [LIAxxxx]
- Cuatrimestre: [X]
- Sesión N: [N]
- Fecha: [YYYY-MM-DD]
- Duración (min): [XX]
- Hora real de inicio: [HH:MM]
- Modalidad: [presencial / virtual / híbrida]
- Número de alumnos: [XX]
- Estado: [impartida / próxima / pendiente]
- Modo de composición: [operativo / retrospectivo]

### B. Contenido curricular
- Unidad: [X]
- Tema: [nombre del tema]
- Subtemas oficiales cubiertos: [X.Y, X.Z]
- Alcance conceptual del subtema: [literal / literal con extensión propedéutica / amplio / panorámico]
- Nota de alcance: [instrucción específica para 03.A, opcional]
- Competencias posteriores que activan el propedéutico: [solo si aplica]
- Pesos por subtema: [X.Y=alto, X.Z=medio, ...]
- Objetivo de aprendizaje: [verbo observable + objeto + condición]
- Nivel de profundidad: [introductorio / aplicado / técnico-profesional]
- Tipo de sesión: [según catálogo §2.3]
- Eslabones de competencia cubiertos: [C1=introduce, C2=desarrolla, ...] o [ninguno (sesión de fundamento operativo)]

### C. Marco conceptual
- Área disciplinar: [según catálogo §1.2]
- Corriente teórica dominante: [según catálogo, heredada del curso o declarada por sesión]
- Conceptos en debate (preliminar): [lista]
- Conceptos que requieren aplicación práctica: [lista]

### D. Contexto normativo y regional
- Tipo de proyecto: [vivienda / comercial / educativo / patrimonial / industrial / infraestructura / otro / no aplica]
- Zona patrimonial: [sí / no / no aplica]
- Trata clima / suelo / sismicidad: [sí / no]
- Contexto geográfico: [Mérida, Yucatán / otro / no aplica]
- Ámbito normativo probable: [federal / estatal / municipal / varios]

### E. Recursos visuales
- Conceptos clave a ilustrar: [lista con tipo de recurso esperado por concepto]
- Recurso audiovisual sugerido: [tipo por concepto]
- Restricciones visuales específicas: [si aplica]

### F. Articulación curricular y ejes de guion
- **Articulación prioritaria:** [lista de hasta 4 materias]
  - Formato: `[Asignatura] — [tipo: antecedente / aplicación concurrente / consecuente / contexto disciplinar] — [cómo se aplica]`
  - Si no aplica: `sin articulación documentada`
- **Materia de aplicación concurrente principal:** [asignatura + unidad + cómo se aplica / no aplica]
  - Solo una materia. Debe estar también en la articulación prioritaria.
- Preguntas que el guion debe resolver: [3–5]
- Conexión con tema anterior: [una línea]
- Conexión con tema siguiente: [una línea]

### G. Evaluación y actividades
- **Actividades oficiales vinculadas:** [lista de IDs con estado y producto parcial]
  - Formato: `[ID] — [nombre] — estado: [estado] — producto parcial: [descripción]`
  - Si no aplica: `sin actividad oficial en esta sesión`
- **Actividad oficial principal de la sesión:** [ID + nombre, o "ninguna"]
  - Solo si hay 2+ actividades oficiales activas.
- **Actividad didáctica auxiliar:** [descripción libre de la actividad creada para enseñar el tema]
- **Producto parcial esperado:** [descripción del avance que el alumno debe producir, si aplica]
- **Actividad recurrente:** [si aplica]
- **Actividad de cierre:** [descripción breve]
- **Evidencia esperada:** [producto concreto]
- **Peso en evaluación:** [%]
- **Continuidad conceptual posterior:** [lista de conceptos que esta sesión introduce y se retoman después, con destino]
  - Formato: `[concepto] → [sesión o capítulo donde se retoma]`

### H. Prerrequisitos y refuerzo
- Prerrequisitos detectados: [lista]
- Tipo de refuerzo sugerido: [repaso breve / re-enseñanza focalizada / nivelación / por peso o dependencia / ninguno]
  - En modo retrospectivo, se marca como `no aplica`.
- Duración estimada de refuerzo: [min]
  - En modo retrospectivo, se marca como `no aplica`.

### I. Trazabilidad
- Doc Maestro versión: [v1.5]
- Brief generado: [YYYY-MM-DD]
- Brief versión: [v2.8]
- Motivo del modo retrospectivo: [solo si Modo = retrospectivo]
  - Documentación histórica del curso
  - Generación de material de estudio para alumnos que no asistieron
  - Reconstrucción para auditoría institucional
  - Otro: [especificar]
- Observaciones: [si aplica]
```

---

## Fase 4 — Verificación de cobertura de eslabones (NUEVA en v2.8)

**Activación:** siempre, si §1.3 produjo una tabla de referencia con al menos una competencia.

**Propósito:** antes de emitir el conjunto de briefs, verificar que **todos los eslabones de todas las competencias declaradas en §21 del Maestro tengan al menos un brief asignado**.

### 4.1 Construcción de la matriz de cobertura

Cruzando la tabla de referencia (§1.3) con los eslabones declarados por cada brief (§2.9), construir la **matriz de cobertura de competencias**:

| ID | Competencia | Introduce | Desarrolla | Aplica | Evalúa | Estado |
|---|---|---|---|---|---|---|
| C1 | ... | S_N | S_N | S_N | S_N | Completa |
| C2 | ... | S_N | S_N | — | — | **Huérfana parcial** |
| C3 | ... | S_N | S_N | S_N | S_N | Completa |

**Reglas de llenado:**

- Cada celda se llena con la sesión o sesiones que cubren ese eslabón.
- Si la celda queda vacía → eslabón huérfano.
- El estado de la competencia se calcula:
  - **Completa**: los cuatro eslabones tienen al menos una sesión.
  - **Huérfana parcial**: falta al menos un eslabón.
  - **Huérfana total**: no tiene ningún eslabón cubierto.

### 4.2 Diagnóstico de eslabones huérfanos

Si hay eslabones huérfanos, reportar:

- Competencia afectada.
- Eslabón faltante.
- Verificación cruzada con §21 del Maestro:
  - Si el Maestro asignó ese eslabón a una sesión, pero el brief de esa sesión no lo declaró → error de generación (revisar §2.9).
  - Si el Maestro no asignó el eslabón a ninguna sesión → error del Maestro (reportar y remitir a skill 01).

### 4.3 Regla de bloqueo

El conjunto de briefs **no se emite como completo** si existe al menos un eslabón huérfano sin resolver.

Las opciones son:

- **Cubrir**: identificar la sesión donde debió declararse el eslabón y corregir §2.9. Solo aplica si el error es de generación de briefs.
- **Reportar**: si el error es del Maestro (no asignó el eslabón a ninguna sesión), se reporta y se remite a skill 01. El conjunto se emite como **incompleto**.
- **Aceptar**: si el Maestro declaró la competencia como contextual, transversal o pendiente, se acepta y se documenta.

### 4.4 Presentación al usuario

La matriz de cobertura se incluye en el documento de salida (Fase 5). Si hay eslabones huérfanos, se declaran al inicio del documento con una nota de estado.

---

## Fase 5 — Documento de salida

- Entrega un **único archivo Markdown** (`create_file`) con encabezado de metadatos: asignatura, clave, programa, nivel, periodo, modalidad, número de sesiones, referencia al Documento Maestro del que se deriva, versión de la skill, y **estado de cobertura de competencias** (`completo` / `incompleto`).
- Un bloque por sesión, en orden cronológico, con encabezados `## Sesión N — fecha — tema`.
- No repitas íntegro el contenido del Documento Maestro: hereda lo necesario y aporta los campos nuevos.
- Si el curso ya está en marcha, indica al inicio cuáles sesiones ya se impartieron y si se incluyen o no (según el alcance declarado en Fase 1.2, pregunta 8).
- **Incluye al final la matriz de cobertura de competencias** (§4.1) con el estado de cada competencia.
- Incluye al final una **tabla de control de cobertura** que verifique que cada brief tiene los 36 campos completos.
- Si el conjunto se emite como **incompleto**, se declaran al inicio:
  - Los eslabones huérfanos (si los hay).
  - Los errores del Maestro detectados (si los hay).
  - Las acciones pendientes para completar.

---

## Verificación final (checklist interno antes de entregar)

### Verificaciones generales

- ¿Cada brief tiene los 36 campos del contrato?
- ¿Cada brief hereda los pesos por subtema de la tabla 7.b del Doc Maestro?
- ¿Algún subtema quedó sin ponderar? Si sí, ¿se reportó?
- ¿Cada brief declara `Modo de composición` derivado del estado operativo?
- ¿Los briefs en modo retrospectivo declaran `Motivo del modo retrospectivo`?
- ¿Cada brief clasifica el tipo de sesión?
- ¿Cada brief declara `Zona patrimonial` y `Trata clima / suelo / sismicidad`?
- ¿Cada brief declara `Prerrequisitos detectados` y `Tipo de refuerzo sugerido` (o `no aplica` si modo retrospectivo)?
- ¿Cada brief declara `Corriente teórica dominante`?
- ¿La hora real y la duración coinciden con el Doc Maestro?
- ¿Los datos derivados (no heredados) están declarados como tales?
- ¿No se inventó ningún dato curricular, normativo, visual ni de ponderación?
- ¿El brief es consumible por 03a, 03b, 03c, 03d y 03e sin preguntas adicionales?
- ¿Cada brief declara el nivel de profundidad en nomenclatura (introductorio / aplicado / técnico-profesional)?
- ¿Cada brief tiene el campo `Tipo de sesión` con tipo dominante + secundario cuando aplica?
- ¿Cada brief declara `Eslabones de competencia cubiertos`?

### Verificaciones del alcance conceptual

- ¿Cada brief declara `Alcance conceptual del subtema`?
- ¿El alcance se determinó aplicando el test de §2.6?
- ¿Los briefs con alcance `amplio`, `panorámico` o `literal con extensión propedéutica` tienen `Nota de alcance`?
- ¿La `Nota de alcance` no inventa subconceptos?
- ¿No se marcó todo como `literal`?
- ¿No se marcó todo como `amplio`?
- ¿El alcance es coherente con el nivel académico del alumno?
- ¿El alcance es coherente con la articulación curricular del Doc Maestro?

### Verificaciones del propedéutico

- ¿Los briefs con alcance `literal con extensión propedéutica` declaran las competencias posteriores que activan el propedéutico?
- ¿Las competencias posteriores están documentadas en el Doc Maestro, el temario o el Brief?
- ¿No se marcó `literal con extensión propedéutica` sin competencia documentada?

### Verificaciones de actividades oficiales

- ¿Cada brief declara `Actividades oficiales vinculadas`?
- ¿Los IDs de actividad provienen de §7.c del Doc Maestro?
- ¿El estado de la actividad proviene de §8?
- ¿Se distingue claramente entre actividad oficial y actividad didáctica auxiliar?
- ¿Se declara la actividad oficial principal si hay 2+ activas?
- ¿Se declara el producto parcial esperado si la actividad es progresiva?
- ¿Se declara la continuidad conceptual posterior?
- ¿Se declara la actividad recurrente si aplica?
- ¿Ninguna actividad didáctica auxiliar sustituye a una oficial?

### Verificaciones de articulación curricular

- ¿Cada brief declara `Articulación prioritaria`?
- ¿La articulación prioritaria tiene máximo 4 materias?
- ¿Cada relación declara asignatura, tipo y cómo se aplica?
- ¿Se declara `Materia de aplicación concurrente principal` cuando aplica?
- ¿La materia de aplicación concurrente principal está también en la articulación prioritaria?
- ¿Si no hay articulación, se declara `sin articulación documentada`?
- ¿El lenguaje es neutral (sin "taller" salvo que sea nombre oficial de la asignatura)?

### Verificaciones de trazabilidad de competencias (NUEVAS en v2.8)

- ¿Se verificó que el Doc Maestro es v1.5 o superior y tiene §21?
- ¿Se extrajo la tabla de referencia de competencias (§1.3)?
- ¿Cada brief declara `Eslabones de competencia cubiertos`?
- ¿Los eslabones declarados coinciden con §21 del Maestro?
- ¿Se construyó la matriz de cobertura de competencias (§4.1)?
- ¿Ningún eslabón de competencia declarada quedó sin brief asignado?
- ¿Si hay eslabones huérfanos, se identificó si son error del Maestro o error de generación de briefs?
- ¿El conjunto de briefs se emite como `completo` o `incompleto`?
- ¿Si es `incompleto`, se declaran los eslabones huérfanos al inicio?
- ¿El campo `Doc Maestro versión` en bloque I declara `v1.5` o superior?
- ¿El campo `Brief versión` en bloque I declara `v2.8`?

---

## Archivos que produce la skill 02

| Archivo | Contenido | Frecuencia |
|---|---|---|
| `briefs_sesion_[asignatura].md` | Todos los briefs + matriz de cobertura en un solo archivo | Por curso |
| `briefs_sesion_N.md` | Brief individual | Bajo demanda |
| `briefs_sesion_retrospectivos_[asignatura].md` | Briefs de sesiones impartidas | Bajo demanda |

---

## Ejemplo mínimo de Brief v2.8 — Modo operativo

```markdown
## Sesión 4 — 2026-09-26 — Unidades de medida

### A. Identificación
- Asignatura: Topografía
- Clave: LIA0525
- Cuatrimestre: 5
- Sesión N: 4
- Fecha: 2026-09-26
- Duración (min): 90
- Hora real de inicio: 08:30
- Modalidad: presencial
- Número de alumnos: 10
- Estado: próxima
- Modo de composición: operativo

### B. Contenido curricular
- Unidad: 1
- Tema: Introducción a la topografía
- Subtemas oficiales cubiertos: 1.4
- Alcance conceptual del subtema: literal con extensión propedéutica
- Nota de alcance: "1.4 Unidades de medida" es literal (longitud, superficie, equivalencias, consistencia dimensional). Se introducen como Propedéutico los conceptos de resolución, precisión vs exactitud, error de medición y cifras significativas. Las unidades angulares quedan como Panorama por pertenecer a la misma familia conceptual del subtema.
- Competencias posteriores que activan el propedéutico: reconocer el alcance y las limitaciones de las tecnologías topográficas disponibles.
- Pesos por subtema: 1.4=medio
- Objetivo de aprendizaje: El alumno utiliza unidades de longitud y superficie y realiza conversiones coherentes, reconociendo la resolución y limitaciones básicas de una medición.
- Nivel de profundidad: introductorio
- Tipo de sesión: técnica / cálculo (dominante)
- Eslabones de competencia cubiertos: C2=desarrolla

### C. Marco conceptual
- Área disciplinar: Representación
- Corriente teórica dominante: no declarada
- Conceptos en debate: no aplica
- Conceptos que requieren aplicación práctica: conversión de unidades, consistencia dimensional

### D. Contexto normativo y regional
- Tipo de proyecto: no aplica
- Zona patrimonial: no aplica
- Trata clima / suelo / sismicidad: no
- Contexto geográfico: Mérida, Yucatán
- Ámbito normativo probable: federal (SI)

### E. Recursos visuales
- Conceptos clave a ilustrar: cadena de unidades de longitud; diferencia longitud-superficie; tabla de equivalencias; conversión paso a paso
- Recurso audiovisual sugerido: diagramas vectoriales, tabla visual
- Restricciones visuales específicas: no asumir instrumentos específicos

### F. Articulación curricular y ejes de guion
- Articulación prioritaria:
  - Matemáticas aplicadas a arquitectura — antecedente — operaciones con unidades y equivalencias
  - Dibujo de representación — aplicación concurrente — cotas, unidades y consistencia dimensional
  - Geometría / Geometría II — antecedente — longitud, superficie y relaciones dimensionales
  - Diseño Arquitectónico IV — consecuente — consistencia dimensional en documentación del sitio
- Materia de aplicación concurrente principal: Dibujo de representación — unidad no declarada — cotas, unidades y consistencia dimensional
- Preguntas que el guion debe resolver: ¿Qué unidad conviene según la magnitud?; ¿Cómo se convierten longitudes y superficies?; ¿Por qué m y m² no se convierten igual?; ¿Por qué no deben reportarse más cifras de las justificadas?
- Conexión con tema anterior: Escalas
- Conexión con tema siguiente: Formas del terreno

### G. Evaluación y actividades
- Actividades oficiales vinculadas:
  - AC-02 — Reportes de lo visto en clase y/o conclusiones — estado: desarrolla+entrega — producto parcial: reporte/conclusiones
  - AI-01 — Mapa conceptual sobre escalas, unidades de medida e instrumentos — estado: inicia+desarrolla — producto parcial: sección de unidades de medida
  - AI-04 — Proyecto final de levantamiento topográfico — estado: aporta — producto parcial: criterios de unidades y consistencia
- Actividad oficial principal de la sesión: AI-01
- Actividad didáctica auxiliar: ejercicios de conversión y detección de errores dimensionales
- Producto parcial esperado: sección de unidades de medida del mapa conceptual
- Actividad recurrente: AC-02 — Reporte de clase
- Actividad de cierre: explicar un error dimensional y una limitación básica de una medición
- Evidencia esperada: ejercicios de conversión + avance del mapa conceptual
- Peso en evaluación: AI-01 integra Mapa conceptual 10%; AC-02 integra Reportes 10%
- Continuidad conceptual posterior:
  - Resolución, precisión y error de medición → sesión 6 (Instrumentos)
  - Unidades angulares → sesión 12 (Mediciones angulares y polígonos)
  - Escala + unidades → sesión 9 (Representación gráfica del terreno)

### H. Prerrequisitos y refuerzo
- Prerrequisitos detectados: 1.3 Escalas; aritmética básica y equivalencias métricas
- Tipo de refuerzo sugerido: repaso breve
- Duración estimada de refuerzo: 5 min

### I. Trazabilidad
- Doc Maestro versión: v1.5 (2026-09-20)
- Brief generado: 2026-09-22
- Brief versión: v2.8
- Motivo del modo retrospectivo: no aplica
- Observaciones: alcance propedéutico activado por competencia posterior documentada. Eslabón C2=desarrolla heredado de §21 del Maestro.
```

---

## Reglas de consistencia

### Reglas generales

1. **No recalcules ponderaciones ni reordenes sesiones.** El calendario viene cerrado.
2. **No modifiques objetivo, evidencia ni peso de evaluación.** Solo refina la redacción del objetivo si es necesario para que el verbo sea observable.
3. **No inventes corriente teórica.** Si no está declarada en la Fase 1.2, márcala como "no declarada" para que 03a decida.
4. **No inventes tipo de proyecto.** Si no está claro, derívalo del tema pero declara la derivación.
5. **No inventes prerrequisitos.** Solo se declaran los que tengan base en el temario o el Doc Maestro.
6. **No inventes conceptos visuales, recursos ni fuentes.** Solo los que se sustenten en los subtemas oficiales.
7. **Clasifica siempre el tipo de sesión.** Si es mixto, declara cuál domina.
8. **Distingue dato heredado vs. dato derivado.** Todo dato derivado se declara como tal.
9. **Si el Doc Maestro cambia, regenera solo los briefs afectados.**
10. **Si falta el Documento Maestro o alguna sección crítica, no improvises.** Remite a la skill 01.
11. **El brief debe ser consumible** por 03a, 03b, 03c, 03d y 03e sin que ninguna tenga que preguntar al usuario datos adicionales.
12. **Si el curso ya está en marcha**, genera briefs solo para las sesiones pendientes, salvo que el usuario pida incluirlas (modo retrospectivo).
13. **Toda sesión con práctica profesional, vinculación, servicio o campo** debe declararlo explícitamente en los bloques B y D.
14. **Toda sesión debe declarar `Zona patrimonial` y `Trata clima / suelo / sismicidad`** aunque el valor sea "no aplica". Esos dos campos activan bloques automáticos en 03b.
15. **Pesos por subtema obligatorios.** El Brief no puede emitirse si algún subtema de la sesión no tiene peso heredado de la tabla 7.b.
16. **No se recalcula el peso.** Aunque la sesión tenga demasiados subtemas para el tiempo disponible, el peso se hereda tal cual. El ajuste ocurre en 03d.
17. **El modo de composición se deriva del estado operativo, no se pregunta al usuario.**
18. **El peso no depende del estado operativo.** Una sesión impartida conserva sus pesos. La separación peso/estado es la regla de la skill 01 v1.5.

### Reglas del alcance conceptual

19. **Todo brief debe declarar `Alcance conceptual del subtema`.** Valores válidos: `literal`, `literal con extensión propedéutica`, `amplio`, `panorámico`. Si no se puede determinar, se marca como `no declarado` y se reporta al usuario.
20. **El test de determinación de alcance se aplica siempre.** No se asigna por costumbre ni por defecto.
21. **Si el alcance es `amplio`, `panorámico` o `literal con extensión propedéutica`, se agrega `Nota de alcance`** con instrucción específica para 03.A.
22. **No se marca todo como `literal`** por prudencia. Eso reproduce el problema de estrechamiento.
23. **No se marca todo como `amplio`** por defecto. Eso sobrecarga sesiones que no lo necesitan.
24. **La `Nota de alcance` no inventa subconceptos.** Solo menciona los que la disciplina reconoce bajo esa denominación.

### Reglas del propedéutico

25. **El valor `literal con extensión propedéutica` solo se usa si existe al menos una competencia posterior documentada** en el Doc Maestro, el temario o el Brief.
26. **Las competencias posteriores que activan el propedéutico se declaran explícitamente** en el campo `Competencias posteriores que activan el propedéutico`.
27. **No se inventan competencias posteriores.** Si no están documentadas, el alcance se mantiene como `literal`.

### Reglas de actividades oficiales

28. **El Brief hereda los IDs de actividad oficial de §7.c del Doc Maestro v1.5.** No se inventan, no se renombran, no se modifican.
29. **El estado de la actividad viene de §8 del Doc Maestro.** No se recalcula.
30. **Una sesión puede tener 0, 1 o varias actividades oficiales activas.**
31. **Si una sesión tiene 2+ actividades oficiales activas, se declara cuál es la principal.**
32. **La actividad didáctica auxiliar se distingue explícitamente de la actividad oficial.** Nunca se confunden.
33. **El producto parcial esperado solo aplica si la actividad es progresiva.**
34. **La continuidad conceptual posterior viene de §9 del Doc Maestro.**
35. **La actividad recurrente se declara solo si el temario la declara como recurrente.**
36. **Si el temario no declara actividades oficiales, los campos de actividad se marcan como `sin actividad oficial declarada`.**
37. **Ninguna actividad didáctica auxiliar puede sustituir a una actividad oficial.**
38. **Los IDs de actividad atraviesan todo el pipeline** (03.D, 03.E, 04).

### Reglas de articulación curricular

39. **El Brief hereda la articulación curricular del Doc Maestro v1.5.** No la inventa, no la renombra, no la modifica.
40. **La `Articulación prioritaria` tiene máximo 4 materias.**
41. **La `Materia de aplicación concurrente principal` es 0 o 1 materia.**
42. **La materia de aplicación concurrente principal debe estar también en la articulación prioritaria.**
43. **Cada relación declara: asignatura, tipo, y cómo se aplica.**
44. **Si no hay articulación documentada, se declara `sin articulación documentada`.**
45. **El término `Materia de aplicación concurrente principal` es neutral.** Se usa para cualquier disciplina (taller, clínica, práctica, laboratorio, seminario).
46. **No se usa el término `taller` como categoría universal.** Se usa solo si la institución lo declara explícitamente como nombre de la asignatura.

### Reglas de trazabilidad de competencias (NUEVAS en v2.8)

47. **El Doc Maestro consumido debe ser v1.5 o superior.** Si es v1.4 o anterior, no tiene §21 y la verificación de cobertura no puede ejecutarse. Detente y remite a la skill 01 v1.5.

48. **Toda competencia declarada en §21 del Maestro se conserva íntegra en la tabla de referencia** (§1.3). No se inventan competencias, no se eliminan competencias, no se modifican estados.

49. **Cada brief declara `Eslabones de competencia cubiertos`** según lo que el Maestro haya asignado en §21. Si el Maestro asignó un eslabón a la sesión, el brief lo declara. Si no asignó ninguno, se declara `ninguno (sesión de fundamento operativo)`.

50. **El formato del campo es compacto y estricto:** `[ID]=[eslabón], [ID]=[eslabón], ...`. Los eslabones válidos son `introduce`, `desarrolla`, `aplica`, `evalúa`.

51. **Antes de emitir el conjunto, se construye la matriz de cobertura de competencias** (§4.1) cruzando la tabla de referencia con los eslabones declarados por cada brief.

52. **Regla de bloqueo:** el conjunto de briefs no se emite como completo si existe al menos un eslabón de competencia declarada sin brief asignado. Se emite como **incompleto** con lista de eslabones huérfanos.

53. **Diagnóstico diferenciado de eslabones huérfanos:**
    - Si el Maestro asignó el eslabón a una sesión, pero el brief de esa sesión no lo declaró → **error de generación de briefs**. Se corrige §2.9 y se regenera el brief.
    - Si el Maestro no asignó el eslabón a ninguna sesión → **error del Maestro**. Se reporta al usuario y se remite a skill 01.
    - Si el Maestro declaró la competencia como contextual, transversal o pendiente → se acepta y se documenta.

---

## Criterio final de calidad

La skill 02 cumple si:

### Criterios generales

- cada brief tiene los 36 campos del contrato;
- cada brief hereda los pesos por subtema de la tabla 7.b del Doc Maestro;
- cada brief declara `Modo de composición` derivado del estado operativo;
- los briefs retrospectivos declaran su motivo;
- cada brief declara `Alcance conceptual del subtema` aplicando el test de §2.6;
- los briefs con alcance `amplio`, `panorámico` o `literal con extensión propedéutica` tienen `Nota de alcance`;
- los briefs con alcance `literal con extensión propedéutica` declaran competencias posteriores documentadas;
- no se marcó `literal con extensión propedéutica` sin competencia documentada;
- ningún subtema queda sin ponderar;
- cada brief declara `Actividades oficiales vinculadas`;
- los IDs de actividad provienen de §7.c del Doc Maestro;
- el estado de la actividad proviene de §8;
- se distingue actividad oficial de actividad didáctica auxiliar;
- se declara la actividad oficial principal si hay 2+ activas;
- se declara el producto parcial esperado si aplica;
- se declara la continuidad conceptual posterior;
- se declara la actividad recurrente si aplica;
- ninguna actividad didáctica auxiliar sustituye a una oficial;
- cada brief declara `Articulación prioritaria`;
- la articulación prioritaria tiene máximo 4 materias;
- cada relación declara asignatura, tipo y cómo se aplica;
- se declara `Materia de aplicación concurrente principal` cuando aplica;
- la materia de aplicación concurrente principal está también en la articulación prioritaria;
- si no hay articulación, se declara `sin articulación documentada`;
- el lenguaje es neutral (sin "taller" salvo que sea nombre oficial);
- cada campo está justificado por un consumidor concreto;
- las cinco sub-skills pueden ejecutarse sin preguntar al usuario datos adicionales;
- no se inventó ningún dato curricular, normativo, conceptual, visual ni de ponderación;
- la trazabilidad con el Doc Maestro es verificable;
- el refuerzo inicial se sugiere sin decidirse;
- el modo retrospectivo no bloquea la generación;
- la `Nota de alcance` no inventa subconceptos fuera de la disciplina;
- no se marcó todo como `literal` ni todo como `amplio`.

### Criterios de trazabilidad de competencias (NUEVOS en v2.8)

- el Doc Maestro consumido es v1.5 o superior y contiene §21;
- se extrajo la tabla de referencia de competencias (§1.3);
- cada brief declara `Eslabones de competencia cubiertos`;
- los eslabones declarados coinciden con §21 del Maestro;
- se construyó la matriz de cobertura de competencias (§4.1);
- ningún eslabón de competencia declarada quedó sin brief asignado;
- si hay eslabones huérfanos, se diagnosticó si son error del Maestro o error de generación de briefs;
- el conjunto se emite como `completo` o `incompleto` según corresponda;
- si es `incompleto`, se declaran los eslabones huérfanos al inicio del documento;
- el campo `Doc Maestro versión` en bloque I declara `v1.5` o superior;
- el campo `Brief versión` en bloque I declara `v2.8`.

---

## Changelog de consolidación v2.7 → v2.8

**Propósito:** incorporar la capa de trazabilidad de competencias al conjunto de briefs. Cerrar la brecha entre "briefs individualmente completos" y "conjunto de briefs responsable de las competencias declaradas en el Maestro".

**Contenido normativo preservado del v2.7 (sin cambios):**

- Propósito general (extendido con la capa de verificación).
- Cuándo activar.
- Estructura del flujo (actualizada con §21).
- Fase 1: §1.1 Verificación del Doc Maestro, §1.2 Encuadre global.
- Fase 2: §2.1 Datos operativos, §2.2 Prerrequisitos, §2.3 Tipo de sesión, §2.4 Herencia de pesos, §2.5 Modo de composición, §2.6 Alcance conceptual, §2.7 Actividades oficiales, §2.8 Articulación curricular.
- Fase 3: Generación de briefs.
- Contrato de brief (bloques A–I).
- Reglas generales 1–18.
- Reglas de alcance conceptual 19–24.
- Reglas del propedéutico 25–27.
- Reglas de actividades oficiales 28–38.
- Reglas de articulación curricular 39–46.
- Checklist existente (ampliado).
- Criterios finales existentes (ampliados).
- Ejemplo mínimo (actualizado con el nuevo campo).
- Changelog anterior v2.6 → v2.7.

**Contenido nuevo en v2.8:**

- **Principio rector** (briefs individualmente completos ≠ conjunto responsable).
- **§1.3** Verificación de la matriz de trazabilidad de competencias del Maestro.
- **§2.9** Determinación de eslabones de competencia cubiertos por sesión.
- **Nuevo campo** en bloque B del contrato: `Eslabones de competencia cubiertos`.
- **Fase 4** Verificación de cobertura de eslabones (con matriz de cobertura).
- **Fase 5** Documento de salida (antes Fase 4).
- **Reglas 47–53** (trazabilidad de competencias).
- **Verificaciones nuevas** en el checklist (trazabilidad de competencias).
- **Criterios nuevos** en el criterio final (trazabilidad de competencias).
- **Matriz de cobertura de competencias** en el documento de salida.
- **Regla de bloqueo:** conjunto de briefs no se emite como completo si hay eslabones huérfanos.

**Cambios de empaquetado:**

- Se añadió Fase 4 (verificación de cobertura) y la antigua Fase 4 pasó a Fase 5.
- Se amplió el contrato de brief de 35 a 36 campos.
- Se ampliaron las verificaciones del checklist con un bloque nuevo.
- Se ampliaron los criterios finales con un bloque nuevo.

**Actualizaciones de compatibilidad:**

- Doc Maestro requerido: **v1.5** (antes v1.4). Cambio crítico: la v1.5 introduce §21 (matriz de trazabilidad de competencias), sin la cual la v2.8 no puede cumplir su verificación.
- Ficha Teórica consumidora: **v1.10** (implícito).
- Ficha Normativa consumidora: **v1.3** (implícito).
- Ficha Visual consumidora: **v1.7** (implícito).
- 03.D consumidor: **v1.8** (implícito).
- 03.E consumidor: **v2.2** (implícito).
- 04 Auditor: **v3.9** (implícito). El Auditor puede consumir la matriz de cobertura de competencias de v2.8 como insumo para su Fase 0.

---

## Changelog de consolidación v2.6 → v2.7 (conservado)

**Propósito:** convertir la skill en autocontenida. Todos los `[Igual que vX]` y `[Sin cambios respecto a vX]` fueron expandidos literalmente.

**Contenido normativo preservado sin cambios:**

- Contrato de 35 campos (bloques A–I).
- 46 reglas de consistencia (renumeradas de forma continua).
- Los 8 campos nuevos respecto a v2.0:
  1. Pesos por subtema (v2.1)
  2. Modo de composición (v2.2)
  3. Motivo del modo retrospectivo (v2.2)
  4. Alcance conceptual del subtema (v2.3, con 4 valores desde v2.4)
  5. Nota de alcance (v2.3)
  6. Competencias posteriores que activan el propedéutico (v2.4)
  7. Actividades oficiales vinculadas + Actividad principal + Actividad auxiliar + Producto parcial + Continuidad conceptual (v2.5)
  8. Articulación prioritaria + Materia de aplicación concurrente principal (v2.6)

**Cambio de empaquetado (no normativo):**

- Se eliminó la dependencia histórica v2.7 → v2.6 → v2.5 → v2.4.
- Se normalizó la numeración de reglas a un rango continuo 1–46.
- Se expandieron las secciones 2.1 a 2.8 sin referencias cruzadas.
- Se expandió el contrato completo de 35 campos con todos los bloques explícitos.

**Actualizaciones de compatibilidad:**

- Doc Maestro requerido: **v1.4** (antes v1.3 en v2.5).
- Ficha Teórica consumidora: **v1.10** (implícito).
- Ficha Normativa consumidora: **v1.3** (implícito).
- Ficha Visual consumidora: **v1.7** (implícito).
- 03.D consumidor: **v1.8** (implícito).
- 03.E consumidor: **v2.2** (implícito).
- 04 Auditor: **v3.9** (implícito).

---

**Guía de uso del flujo completo:** consulta `guia_uso_flujo_skills.md`.