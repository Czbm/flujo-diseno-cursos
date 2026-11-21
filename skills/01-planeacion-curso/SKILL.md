---
name: 01-planeacion-curso
description: Genera el Documento Maestro del Curso a partir de un temario oficial, calendario y encuadre docente: ponderacion, actividades oficiales, trazabilidad de competencias y calendario completo.
stage_id: "01"
version: "1.6"
status: stable
---

# Skill: Planeación General del Curso (Documento Maestro) — v1.6

## Propósito

Esta skill toma el **temario oficial** de una asignatura, los **datos de calendario** del periodo y las **decisiones de encuadre** del docente, y produce el **Documento Maestro del Curso**: la fuente única de verdad que integra fundamento curricular, competencias, articulación, ponderación temática por unidad y por subtema, **actividades oficiales de aprendizaje con IDs estables**, **matriz de trazabilidad de competencias**, metodología adaptativa, calendario completo, **matriz actividad × sesión**, **matriz de continuidad conceptual**, planeación por sesión (versión resumida), sistema de evaluación, evidencia integradora, normas de trabajo e indicadores de logro.

Es la **primera skill del flujo**. No depende de ninguna otra: ella misma realiza la ponderación de temas, la distribución de sesiones y la **identificación de actividades oficiales**. Un segundo paso (skill de Briefs por Sesión) expandirá después cada sesión del calendario en un brief de generación didáctica.

Aplica a cualquier asignatura, nivel, institución, modalidad y disciplina. No asume estructura pedagógica, tipo de evidencia ni organización de recursos específica: cada rasgo particular se incluye solo si el usuario confirma que aplica.

**Versión autocontenida.** Esta versión no depende de versiones anteriores. Todo el contenido vigente está expandido literalmente.

### Principios rectores

**Principio 1 — peso pedagógico ≠ estado operativo ≠ actividad oficial**

Tres entidades independientes que conviven en el documento:

1. **Peso pedagógico** (alto / medio / bajo): atributo del temario. Existe siempre, sin importar si la sesión ya se impartió o no. Vive en tabla 7.b.
2. **Estado operativo** (impartida / próxima / pendiente): atributo de la sesión en el calendario. Vive en el calendario (§10 del documento). No modifica el peso.
3. **Actividad oficial** (AC-NN / AI-NN): entidad del temario. Vive en §7.c y se distribuye por sesiones en §8.

**Ninguna sustituye a las otras.** Cada una tiene su lugar y su función.

**Regla dura:** una sesión impartida conserva su peso pedagógico completo en la tabla 7.b. Su estado operativo se declara en el calendario. Ambos campos viven en lugares distintos y nunca se sustituyen entre sí.

Esta separación es lo que permite generar material de estudio, composición de referencia o documentación histórica para sesiones ya impartidas sin inventar pesos ni romper la trazabilidad.

**Principio 2 — toda competencia declarada debe tener trazabilidad completa o decisión explícita**

Una competencia declarada en el fin de aprendizaje o en el perfil de egreso **no basta con estar nombrada**. Debe tener cadena operativa completa:

- **Se introduce**: sesión donde aparece por primera vez.
- **Se desarrolla**: sesión donde se trabaja operativamente.
- **Se aplica**: sesión donde se usa en un contexto nuevo o integrado.
- **Se evalúa**: evidencia donde se verifica el logro.

Si falta al menos un eslabón, la competencia es **huérfana** y **bloquea la emisión del documento** hasta que se resuelva (cubrir, reclasificar o retirar).

Esta es la diferencia entre un curso **coherente** (cada sección concuerda con las demás) y un curso **responsable** (el fin declarado tiene medios operativos planificados para alcanzarse).

---

## Cuándo activar esta skill

Actívala cuando el usuario:

- Quiera planear un curso que **aún no inicia** (cero sesiones impartidas) y necesite el documento maestro completo.
- Quiera **replantear** un curso ya en marcha y producir una versión actualizada del documento maestro.
- Pida una "planeación general", un "documento maestro de curso", o mencione necesitar competencias, articulación curricular, metodología, ponderación, calendario y sistema de evaluación en un solo documento.
- Tenga un temario oficial pero **todavía no tenga un calendario ponderado por sesión** (esta skill lo generará).
- Quiera **reconstruir retrospectivamente** el documento maestro de un curso ya terminado, para documentación o generación de material de estudio.

No la actives si solo se quiere expandir un calendario ya existente en briefs de generación didáctica: eso corresponde a la skill de Briefs por Sesión, que va después.

---

## Fase 1 — Recolección de contexto obligatoria

No generes el documento sin confirmar los datos de la sección 1.7 (mínimos obligatorios). Si el usuario ya los proporcionó en la conversación o en archivos del proyecto, decláralos como "confirmados" y pregunta solo lo que falte. Agrupa todas las preguntas en un solo bloque.

### 1.1 Datos de la asignatura

- Nombre de la materia y clave oficial (si aplica).
- Carrera, nivel o grado, cuatrimestre/semestre, periodo académico.
- Institución y docente (si aplica al documento).
- Número de alumnos del grupo.
- Fin de aprendizaje u objetivo oficial del curso (textual, tal como lo define el programa).
- Perfil general del grupo si es relevante (primer ingreso, conocimientos previos esperados).
- Materias que anteceden o preceden a esta asignatura (para la sección de articulación curricular).
- Unidades y subtemas completos del temario oficial.
- Criterios de evaluación oficiales y su ponderación porcentual. Si el programa no los define, pregúntalo directamente en vez de asumir un esquema estándar.

### 1.2 Datos de calendario

- Día(s) de la semana en que se imparte la clase.
- **Duración exacta de cada sesión.** Si la duración varía según el día de la semana (por ejemplo, lunes 60 min y miércoles 120 min), pídelo explícitamente: no asumas duración uniforme.
- Fecha de la primera sesión del curso.
- Fecha de cierre del cuatrimestre/semestre, o número total de sesiones otorgadas por la institución.
- Fechas no disponibles dentro del rango del curso: días festivos, suspensiones, periodos de examen, eventos institucionales.
- **Si el curso incluye horas de práctica profesional, vinculación, servicio social, residencia o trabajo de campo externo al aula**, y cómo se distribuyen en el calendario.
- Si la institución exige sesión de encuadre inicial y/o sesión de cierre/presentación final obligatorias, para reservarlas explícitamente.
- **Si la institución exige un formato oficial de planeación** (plantilla, plataforma, campos obligatorios). Si existe, pide el archivo o la descripción de sus campos.
- **Estado del curso:** sin iniciar, en marcha, o ya terminado.
  - Si es **sin iniciar**, todas las sesiones son `pendientes`.
  - Si es **en marcha**, algunas sesiones son `impartidas` y otras `próximas` o `pendientes`.
  - Si es **ya terminado**, todas las sesiones son `impartidas`.
  - **En todos los casos, el peso pedagógico se asigna a todos los subtemas.** El estado operativo no lo modifica.

### 1.3 Preguntas de encuadre (determinan qué secciones aplican)

Pregunta explícitamente, en un solo bloque:

1. **Modalidad y formato de trabajo:** ¿teórico, práctico o mixto? ¿Presencial, virtual o híbrido? ¿Requiere equipo, software, laboratorio, taller, trabajo de campo o recurso físico especial, o se desarrolla con exposición y materiales de lectura?
2. **Evidencia integradora:** ¿existe un producto final que articule todo el curso (proyecto, portafolio, examen integrador, ensayo final, caso práctico), o la evaluación se compone de evidencias independientes?
3. **Tipos de evidencia de evaluación:** ¿qué formatos usa el docente o exige la institución (exámenes, reportes, exposiciones, prácticas, participación, tareas, otro)?
4. **Articulación curricular:** ¿qué materias anteceden o preceden a este curso, y qué conocimientos previos espera el docente que el grupo ya tenga?
5. **Normas de trabajo del grupo:** ¿existe un reglamento institucional de asistencia, puntualidad o convivencia que deba incorporarse, o normas propias del docente?
6. **Recursos de apoyo:** ¿el docente quiere incluir bibliografía, sitios web, videos u otras referencias como parte del documento?
7. **Práctica profesional o vinculación:** ¿el curso incluye horas fuera del aula (práctica, servicio, residencia, campo)? Si sí, ¿cómo se ponderan y cómo se supervisan?
8. **Formato institucional:** ¿existe una plantilla oficial que el docente deba entregar? Si sí, ¿quieres que el documento maestro incluya al final una sección que mapee cada campo del formato oficial al contenido producido aquí?
9. **Propósito del documento maestro:** ¿es para planeación futura, para documentación histórica, o para ambos? Si es para documentación histórica o ambos, se declarará explícitamente en el encabezado de metadatos.
10. **Actividades oficiales del temario.** ¿El temario oficial declara actividades de aprendizaje explícitas? Si sí, ¿cuáles son y cómo se distribuyen entre conducción académica e independientes? ¿Qué producto o evidencia produce cada una? ¿Con qué criterio de evaluación se vinculan?

**Nota crítica sobre la pregunta 10:** las actividades oficiales del temario **no son lo mismo** que las actividades didácticas que el docente crea para enseñar. Ambas conviven, pero solo las del temario son **actividades oficiales**. Las actividades didácticas auxiliares se declaran en el Brief (skill 02) y en la composición (03.D).

**Si el temario no declara actividades explícitas:** la skill lo registra como `sin actividades oficiales declaradas` y omite las secciones §7.c, §8 y §9. El resto del flujo opera con normalidad.

No des por hecho ninguna respuesta a partir de materias trabajadas previamente con el mismo usuario; cada curso se construye desde sus propias respuestas.

### 1.4 Análisis interno de ponderación temática (paso obligatorio, trazable)

Antes de proponer la ponderación de la Fase 2, realiza un diagnóstico interno del temario. **Este análisis deja rastro en el documento final** (sección 5, apartado "Diagnóstico del temario"; y sección 7, tablas 7.a y 7.b), no se descarta. Incluye:

- **Temas críticos:** unidades con mayor número de subtemas, mayor peso en la evaluación, o que sean prerrequisito para temas posteriores.
- **Tipología de contenido:** clasifica cada unidad como predominantemente teórica (conceptos, principios), práctica (habilidades, aplicación, taller, laboratorio), analítica (resolución de problemas, casos) o actitudinal (ética, reflexión).
- **Carga cognitiva:** detecta si el temario avanza de lo simple a lo complejo, o si requiere práctica constante desde el inicio.
- **Peso interno por subtema:** clasifica cada subtema como alto / medio / bajo según los criterios de la Fase 2.2. **Este análisis se realiza para todos los subtemas del temario, sin importar el estado operativo de las sesiones.** Alimenta la tabla 7.b del documento final y es el insumo directo que hereda el Brief v2.7.

### 1.5 Extracción del fin y de las competencias declaradas (NUEVA en v1.6)

**Propósito:** antes de estructurar el curso, extraer explícitamente el fin de aprendizaje y las competencias que el curso se compromete a formar. Este listado será la base de la matriz de trazabilidad (§2.6 y §21 del documento final).

#### 1.5.1 Extracción del fin de aprendizaje

Del temario oficial, extraer **textualmente** el fin de aprendizaje de la asignatura. Es una declaración sintética de qué debe saber hacer el alumno al terminar.

Ejemplo: *"Al finalizar el curso, el alumno reconocerá y describirá los sistemas de representación topográfica y realizará levantamientos topográficos."*

#### 1.5.2 Descomposición del fin en competencias operativas

Descomponer el fin en **competencias operativas**: cada verbo de acción observable del fin se convierte en una competencia.

Ejemplo del fin anterior:
- **C1** — Reconocer sistemas de representación topográfica.
- **C2** — Describir sistemas de representación topográfica.
- **C3** — Realizar levantamientos topográficos.

Cada competencia debe formularse como **desempeño observable**: se puede verificar si el alumno lo logra o no.

#### 1.5.3 Extracción de competencias del perfil de egreso

Si el usuario proporciona un perfil de egreso o competencias declaradas por el programa, extraer las que **competen a esta asignatura**. Criterio de selección:

- La competencia es **pertinente** al campo disciplinar del curso.
- El curso es **responsable** de al menos un eslabón de su desarrollo.
- La competencia puede **evaluarse** con al menos una evidencia en este curso.

**Si el perfil de egreso no está disponible o es ambiguo**, declararlo explícitamente como limitación. En ese caso, el documento podrá emitirse como **versión condicionada** (ver Regla 33), verificando solo contra el fin de aprendizaje.

#### 1.5.4 Consolidación del listado de competencias

Fusionar las competencias derivadas del fin con las extraídas del perfil, eliminando duplicados. Producir el **listado oficial de competencias del curso**:

| ID | Competencia | Origen | Verbo observable |
|---|---|---|---|
| C1 | ... | Fin / Perfil | ... |
| C2 | ... | ... | ... |

#### 1.5.5 Declaración del criterio de operatividad

Antes de continuar, declarar qué significa **"aplicar"** en esta disciplina. Este criterio guía la verificación de la Fase 2.6.

Ejemplos por tipo de disciplina:
- **Disciplinas procedimentales** (medicina, ingeniería, derecho procesal): "aplicar" significa ejecutar un procedimiento sobre un caso real o simulado.
- **Disciplinas interpretativas** (historia, filosofía, crítica literaria): "aplicar" significa construir una interpretación fundamentada con evidencia.
- **Disciplinas creativas** (diseño, artes): "aplicar" significa producir una obra o propuesta con criterios explícitos.
- **Disciplinas híbridas** (arquitectura, comunicación, educación): puede combinar dos o más de los anteriores. Se declaran los criterios pertinentes.

**En disciplinas híbridas**, se permite declarar **más de un criterio**. La matriz de trazabilidad verificará cada competencia contra el criterio que le corresponda (ver Regla 34).

### 1.6 Trazabilidad del origen del dato (NUEVA en v1.6)

Todo dato usado en el documento debe etiquetarse según su origen:

- **Declarado**: aparece explícitamente en el temario, perfil, datos operativos o respuestas del usuario.
- **Asumido**: no aparece, pero se adopta por convención o decisión del diseñador. Debe justificarse.
- **Inferido**: se deriva del análisis del temario o del perfil.

Los datos asumidos e inferidos se declaran en el anexo del documento final (nueva sección §24).

### 1.7 Datos mínimos obligatorios (bloquean el avance)

La skill **no avanza a Fase 2** si falta cualquiera de estos datos. Si el usuario no los tiene, la skill se detiene y los solicita:

1. Nombre de la asignatura.
2. Fin de aprendizaje u objetivo oficial del curso.
3. Temario completo con unidades y subtemas. Se considera **incompleto** si falta alguna unidad o si una unidad no tiene subtemas listados.
4. Criterios de evaluación oficiales con ponderación porcentual (o confirmación explícita de que el programa no los define).
5. Día(s) de la semana y duración de cada sesión.
6. Fecha de primera sesión.
7. Fecha de cierre del periodo o número total de sesiones otorgadas.

**Nota v1.6:** si el usuario **no proporciona perfil de egreso**, este no es un dato mínimo obligatorio. El documento se emitirá como **versión condicionada** (ver Regla 33).

---

## Fase 2 — Ponderación y construcción de actividades y trazabilidad

### 2.0 Validación cruzada del calendario (paso previo obligatorio)

Antes de ponderar, verifica la consistencia del calendario. Si algo no cuadra, detente y pregunta al usuario:

- Confirma que la fecha de primera sesión caiga en uno de los días de la semana declarados. Si no coincide, avisa.
- Calcula cuántas sesiones hay entre la fecha de inicio y la fecha de cierre, descontando festivos, suspensiones y periodos de examen declarados.
- Compara ese número con el número de sesiones que el usuario declaró. Si no coincide, muestra ambos números y pide confirmación antes de continuar.
- Si la duración de sesión varía por día, calcula el total de minutos del curso, no solo el número de sesiones, y usa los minutos como unidad de ponderación en lugar de las sesiones cuando la desigualdad sea significativa (≥ 25% de diferencia).
- **Determina el estado operativo de cada sesión** a partir del estado del curso declarado en Fase 1.2: `impartida`, `próxima` o `pendiente`. Este estado se registrará en el calendario, no en la tabla 7.b.

Muestra el resultado de esta validación al usuario en una tabla breve antes de pasar a la ponderación.

### 2.1 Ponderación por unidad

Con el temario y el calendario confirmados, sigue este procedimiento y **muestra el razonamiento numérico al usuario antes de la propuesta final**:

1. **Cuenta los subtemas oficiales de cada unidad** y calcula qué porcentaje representa cada unidad del total de subtemas del curso.
2. **Calcula el total de sesiones disponibles en todo el curso**, restando explícitamente la(s) sesión(es) reservada(s) para encuadre inicial y cierre/presentación final, ya que no llevan contenido temático nuevo. Si hay horas de práctica externa, réstalas también y trátalas como bloque propio.
3. **Calcula la distribución proporcional ideal** de las sesiones temáticas por unidad, usando el porcentaje de subtemas como base (sesiones ideales = subtemas de la unidad / subtemas totales × sesiones temáticas disponibles).
4. **Ajusta la distribución ideal con criterios cualitativos**, en este orden de prioridad:
   - Peso de la unidad en la evaluación final o el proyecto integrador.
   - Complejidad técnica o dificultad conceptual relativa.
   - Dependencia curricular (temas prerrequisito no deben comprimirse; deben ubicarse antes de los temas dependientes).
   - Aplicabilidad profesional directa para la carrera del estudiante.
5. **Verifica la secuencia lógica de las unidades**: al no existir un orden ya impartido que respetar, confirma que el orden siga la progresión natural del proceso o disciplina (de lo general a lo particular, o de la preparación a la ejecución), y ajústalo si el temario oficial lo permite y el usuario lo autoriza.
6. Si el curso **ya está en marcha o terminado**, respeta las sesiones ya impartidas tal como ocurrieron y pondera solo las restantes. Las sesiones impartidas **conservan su peso pedagógico** tal como se les asignó o tal como correspondería asignarles según el temario.
7. Nunca alteres los pesos oficiales de evaluación (%) del programa; solo decide en qué sesión conviene recabar cada evidencia.

Presenta esta fase como una **tabla clara** antes de pasar al documento final, para que el usuario pueda objetar la ponderación o el orden.

**Tabla 7.a — Ponderación por unidad:**

| Unidad | Subtemas | % del contenido | Sesiones ideales (proporcional) | Sesiones ajustadas | Justificación del ajuste |
|---|---|---|---|---|---|

### 2.2 Asignación de pesos por subtema (obligatorio)

Una vez distribuida la carga por unidad, asigna un **peso interno** a cada subtema dentro de su unidad. Este peso gobierna la distribución de minutos en la skill 03d y la extensión en la skill 03e, y **es de cumplimiento obligatorio**: ningún subtema puede quedar sin ponderar.

**Principio crítico:** el peso es un atributo del temario, no del estado operativo. Una sesión ya impartida conserva el peso de sus subtemas. La tabla 7.b lista **todos** los subtemas del curso con su peso, sin importar si la sesión está impartida, próxima o pendiente.

**Escala de pesos:**

| Peso | Significado |
|---|---|
| **Alto** | El subtema es central para el objetivo de la unidad o de la sesión. Su concepto se evalúa directamente en una evidencia. Es prerrequisito de subtemas posteriores o de otras unidades. |
| **Medio** | El subtema aporta contexto necesario pero no es central. Apoya la comprensión del subtema alto sin ser prerrequisito estricto. |
| **Bajo** | El subtema es contextual, de repaso o de aplicación secundaria. Puede comprimirse sin afectar la comprensión del tema central. |

**Criterios de asignación (en orden de prioridad):**

1. **Relación con evidencia:** si el subtema se evalúa directamente en una evidencia del curso (examen, proyecto, reporte, etc.), mínimo debe ser medio. Si es el núcleo de la evidencia, es alto.
2. **Dependencia curricular:** si el subtema es prerrequisito de otros subtemas de la misma unidad o de unidades posteriores, mínimo debe ser medio. Si es prerrequisito crítico, es alto.
3. **Complejidad conceptual:** subtemas con mayor dificultad técnica o conceptual tienden a peso alto.
4. **Aplicabilidad profesional:** subtemas con aplicación directa al ejercicio profesional del egresado tienden a peso alto.
5. **Contexto o repaso:** subtemas que solo introducen contexto, repasan contenido previo o sirven de puente son peso bajo.

**Reglas duras:**

- **Toda unidad debe tener al menos un subtema de peso alto.** Si una unidad no tiene ninguno, hay un error en la asignación.
- **Los subtemas de peso bajo no pueden superar el 50% de los subtemas de la unidad.** Si los superan, la unidad no está bien ponderada.
- **Si una unidad tiene 2 subtemas o menos, todos se consideran de peso alto.** No tiene sentido ponderar internamente unidades con pocos subtemas.
- **Si una unidad tiene más de 10 subtemas**, se recomienda agruparlos en bloques internos antes de asignar pesos.
- **Los pesos se asignan a todos los subtemas del temario, sin excepción por estado operativo.** Una sesión ya impartida conserva los pesos de sus subtemas.
- **Prohibido usar `ya cubierto`, `no aplica`, `sin ponderar` o cualquier forma de peso vacío en la tabla 7.b.** El peso siempre es `alto`, `medio` o `bajo`. La única excepción son las sesiones sin subtemas temáticos propios (encuadre inicial, cierre/presentación final, práctica externa), que no se listan en la tabla 7.b.

**Presentación al usuario:**

Muestra la asignación de pesos en una tabla clara **antes de continuar a Fase 3**, para que el usuario pueda objetar. Si el usuario no objeta, se incorpora al documento final.

**Tabla 7.b — Ponderación por subtema:**

| Unidad | Subtema | Nombre | Peso interno | Justificación breve |
|---|---|---|---|---|
| U1 | 1.1 | [nombre] | Alto / Medio / Bajo | [1 línea] |
| U1 | 1.2 | [nombre] | ... | ... |
| U2 | 2.1 | [nombre] | ... | ... |
| ... | ... | ... | ... | ... |

**Regla de trazabilidad:** la tabla 7.b del documento final debe coincidir exactamente con la asignación presentada al usuario. No se modifica después sin autorización explícita.

**Nota sobre estado operativo:** la tabla 7.b **no incluye columna de estado**. El estado operativo (`impartida / próxima / pendiente`) se declara en el calendario general (sección 10 del documento).

### 2.3 Construcción de la tabla de actividades oficiales

**Activación:** solo si la pregunta 10 de Fase 1.3 reportó actividades oficiales declaradas en el temario.

#### Procedimiento

1. **Extraer literalmente del temario** todas las actividades de aprendizaje declaradas, tanto bajo conducción académica como independientes.
2. **Asignar un ID estable** a cada una:
   - `AC-NN` para actividades bajo conducción académica.
   - `AI-NN` para actividades independientes.
   - El número es secuencial, empezando en 01.
3. **Registrar los campos obligatorios** por actividad:
   - ID
   - Nombre de la actividad (literal del temario)
   - Régimen (conducción académica / independiente)
   - Tema(s) curricular(es) vinculado(s)
   - Producto o evidencia que produce
   - Criterio de evaluación asociado (si el temario lo declara)
   - Periodicidad (única / recurrente / progresiva)
4. **Vincular con el sistema de evaluación.** Cada actividad debe apuntar a un criterio de evaluación oficial. Si una actividad no tiene criterio vinculado, se declara `sin criterio vinculado` y se reporta.

#### Reglas duras

- **No inventar actividades.** Solo las que el temario declara.
- **No renombrar actividades.** El nombre debe ser literal o una paráfrasis fiel.
- **No omitir actividades.** Si el temario las declara, se registran todas.
- **No confundir con actividades didácticas auxiliares.** Estas se crean después, en el Brief y en 03.D.
- **Los IDs no cambian después de asignados.**
- **Los IDs no se reutilizan** si una actividad se elimina.

#### Presentación al usuario

Antes de continuar, presenta la tabla al usuario para confirmación.

### 2.4 Construcción de la matriz actividad × sesión

**Activación:** solo si §2.3 produjo al menos una actividad oficial.

#### Los 8 estados

| Estado | Significado |
|---|---|
| **`aporta`** | La sesión genera insumos que alimentarán la actividad, pero el alumno aún no la trabaja formalmente. |
| **`inicia`** | La sesión abre formalmente la actividad (consigna, primeros avances). |
| **`desarrolla`** | La sesión trabaja algún componente sustantivo del producto. |
| **`consolida`** | La sesión revisa, integra o refina lo producido. No avanza contenido nuevo pero cierra coherencia. |
| **`entrega`** | La sesión es fecha oficial de entrega (parcial o final). |
| **`retroalimenta`** | La sesión da feedback formal sobre lo entregado. |
| **`cierra`** | La sesión marca el cierre formal de la actividad. |
| **`no aplica`** | La actividad no toca esta sesión. |

#### Reglas de llenado

- **Múltiples estados por celda:** permitidos, separados por `+`. Ej: `inicia + entrega + cierra`.
- **Actividades recurrentes:** se marcan con `desarrolla` en todas las sesiones aplicables. No requieren estado especial.
- **Actividades progresivas:** se marcan con `inicia` en la primera sesión, `aporta` o `desarrolla` en las intermedias, `consolida` antes del cierre, `entrega + retroalimenta + cierra` al final.
- **Verificación de cobertura:** cada actividad debe tener al menos un `inicia` (o `desarrolla` si es recurrente), un `entrega` y un `cierra` distribuidos en el calendario. Si falta alguno, se reporta.
- **Celdas vacías se llenan con `no aplica`** (o se dejan en blanco si el usuario prefiere).

### 2.5 Construcción de la matriz de continuidad conceptual

**Activación:** siempre que haya conceptos en la tabla 7.b.

#### Propósito

Declarar explícitamente cuándo cada **concepto** se **introduce**, **desarrolla**, **aplica** y **evalúa** a lo largo del curso. Evita que un concepto quede huérfano.

**Nota v1.6:** esta matriz es de **conceptos**, no de competencias. No confundir con la matriz de trazabilidad de competencias (§2.6). Un concepto puede estar cubierto sin que la competencia que lo usa esté cubierta, y viceversa.

#### Estructura

| Concepto | Se introduce | Se desarrolla | Se aplica | Se evalúa | Observaciones |
|---|---|---|---|---|---|
| [concepto 1] | Sesión X | Sesiones X–Y | Sesión Z | Sesión W | — |
| [concepto 2] | ... | ... | ... | ... | ... |

#### Reglas de llenado

- **Se introduce:** sesión donde el concepto aparece por primera vez.
- **Se desarrolla:** sesiones donde se profundiza.
- **Se aplica:** sesiones donde se usa en ejercicios, casos o proyectos.
- **Se evalúa:** sesiones donde se recoge evidencia oficial.
- **Observaciones:** si el concepto tiene tratamiento especial (propedéutico, reservado con continuidad explícita, etc.), se declara aquí.

#### Verificación de cobertura

- Cada concepto del temario debe tener al menos un `se introduce` y un `se evalúa`.
- Si un concepto se introduce pero nunca se evalúa, se reporta.
- Si un concepto se evalúa sin haberse introducido, se reporta.

### 2.6 Construcción de la matriz de trazabilidad de competencias (NUEVA en v1.6)

**Activación:** siempre. Es la verificación estructural de la v1.6.

#### Propósito

Verificar que cada competencia declarada en §1.5 tenga cadena operativa completa. Es la diferencia entre un curso **coherente** y un curso **responsable**.

#### Estructura

| ID | Competencia | Introduce (S) | Desarrolla (S) | Aplica (S) | Evalúa (evidencia + S) | Estado |
|---|---|---|---|---|---|---|
| C1 | ... | S_N | S_N | S_N | Evidencia + S_N | Completa |
| C2 | ... | S_N | S_N | — | — | **Huérfana parcial** |
| C3 | ... | S_N | S_N | S_N | — | **Huérfana parcial** |

#### Criterios de completitud

Una competencia es **completa** si tiene los cuatro eslabones:

- **Introduce:** sesión donde el alumno toma contacto con la competencia.
- **Desarrolla:** sesión donde la competencia se trabaja operativamente (procedimiento, técnica, método, interpretación, producción).
- **Aplica:** sesión donde el alumno la usa en un contexto nuevo o integrado, según el criterio de operatividad declarado en §1.5.5.
- **Evalúa:** evidencia donde se verifica el logro.

Una competencia es **huérfana** si falta al menos uno de los cuatro.

#### Diagnóstico de competencias huérfanas

Para cada competencia huérfana, declarar:

- Qué eslabón falta.
- Por qué falta (error de planeación, restricción operativa, decisión pedagógica).
- Cuál es la decisión tomada (ver más abajo).

#### Resolución de competencias huérfanas

Tres opciones:

**Opción 1 — Cubrir**
Añadir sesión, actividad o evidencia donde falte el eslabón. Requiere volver a Fase 2.1–2.4 y reverificar.

**Opción 2 — Reclasificar**
Cambiar el estatus de la competencia:
- De **declarada** (debe tener los cuatro eslabones) a **contextual** (se menciona, no se evalúa).
- De **declarada** a **transversal** (se trabaja a lo largo del curso, no en una sesión específica).

La reclasificación debe justificarse. No es una vía para evitar la verificación; es una decisión pedagógica legítima cuando la competencia efectivamente no corresponde a este curso.

**Opción 3 — Retirar**
Proponer al programa retirar la competencia del perfil. Es una decisión institucional, no del diseñador. Si se elige esta opción, el Documento Maestro se emite declarando la propuesta pendiente de validación.

#### Registro de decisiones

Toda decisión sobre competencias huérfanas se registra en el documento final (§21), con:

- ID de la competencia.
- Eslabón faltante.
- Decisión tomada.
- Justificación.
- Si la decisión implica modificación del plan, qué se modificó.

#### Regla de bloqueo

El Documento Maestro **no se emite como versión completa** hasta que todas las competencias huérfanas tengan decisión tomada.

Si el usuario decide emitir sin resolver, el documento se declara explícitamente como **versión incompleta**, con la lista de competencias pendientes y la fecha prevista de resolución.

---

## Fase 3 — Síntesis y construcción del documento maestro

**Guía de extensión por sección:** este documento es de consulta, no de lectura lineal. Como referencia aproximada, las secciones 1–4 y 16–17 no deben exceder una página cada una; las secciones 5–7 y 10–11 una a dos páginas cada una; el calendario (§10) y la planeación por sesión (§11) crecen con el número de sesiones. Si una sección se desborda, probablemente está duplicando contenido de otra.

Construye solo las secciones que los insumos y las respuestas de la Fase 1 sostengan. Cada sección lleva indicada su condición de inclusión.

1. **Fundamento curricular** (siempre). Fin de aprendizaje textual del temario oficial y lógica de organización de las unidades, sin repetir el temario completo.

2. **Propósito general** (siempre). Una sola oración-síntesis de la capacidad final del curso, coherente con el fin de aprendizaje oficial.

3. **Competencias y resultados de aprendizaje** (siempre). Deriva de las unidades y subtemas las categorías que apliquen al tipo de conocimiento del curso (conocimientos, habilidades, actitudes, etc.). No fuerces siempre las mismas tres categorías si el contenido no las sostiene.

4. **Articulación curricular** (solo si el usuario identificó materias antecedentes o consecuentes). Tabla de conocimientos previos esperados y lista de asignaturas posteriores que aprovechan el curso. Si no las identifica todas, dilo explícitamente en vez de inventarlas.

5. **Metodología de trabajo** (siempre; adaptativa según el análisis de la Fase 1.4). No asumas un modelo fijo. Incluye:
   - **Diagnóstico del temario (trazabilidad de Fase 1.4):** párrafo breve que declare la tipología detectada por unidad (teórica / práctica / analítica / actitudinal) y la carga cognitiva observada. Esto permite verificar que el diseño metodológico se basó en el análisis y no en una plantilla.
   - **Justificación de la propuesta:** por qué esa metodología es la más eficiente y eficaz para este temario (ej. "Dado que la Unidad 2 concentra el 40% de la evaluación y es eminentemente práctica, se propone un enfoque de taller con brigadas rotativas").
   - **Estructura de sesión adaptada al peso temático:** define los momentos de la sesión (activación, explicación, práctica, cierre) y distribuye tiempos proporcionalmente al peso de los temas de cada tipo de sesión. Una sesión teórica no se estructura igual que una práctica. **Esta subsección describe el patrón general por tipo de sesión; no la ejecución particular de cada sesión (eso va en §11).**
   - **Priorización de actividades:** indica qué actividades son prioritarias para los temas con mayor peso (ej. estudio de caso sobre exposición magistral cuando el tema es analítico).
   - **Tabla de distribución de tiempo por tipo de sesión:** momentos de la sesión, tiempo/proporción aproximada, justificación de la variación respecto a la distribución estándar.
   - **Recursos didácticos sugeridos:** recursos que mejor se alineen con la tipología de cada unidad detectada en la Fase 1.4.

6. **Organización de recursos y espacios** (solo si el usuario confirmó que el curso requiere equipo, software, laboratorio, taller o trabajo de campo, o si hay horas de práctica profesional / vinculación / servicio). Disponibilidad, forma de organizar al grupo si se trabaja en equipos o rotaciones, roles a asignar, y —si aplica— convenios, supervisores externos y mecanismos de seguimiento de la práctica.

7. **Criterios de ponderación aplicados** (siempre). **Tres subsecciones obligatorias:**
   - **7.a — Ponderación por unidad:** unidad, subtemas, % del contenido, sesiones asignadas, ajustes cualitativos aplicados. Es la justificación numérica del calendario.
   - **7.b — Ponderación por subtema:** unidad, subtema, nombre, peso interno (alto / medio / bajo), justificación breve. **Esta tabla es de cumplimiento obligatorio y es la que hereda el Brief v2.7 y usan las skills 03d y 03e para distribuir minutos y extensión.** Ningún subtema puede quedar sin ponderar.
   - **7.c — Actividades oficiales de aprendizaje** (condicional, solo si el temario las declara):

     | ID | Actividad oficial | Régimen | Tema curricular | Producto / evidencia | Criterio de evaluación | Periodicidad |
     |---|---|---|---|---|---|---|
     | AC-01 | ... | Conducción académica | ... | ... | ... | Única / Recurrente / Progresiva |
     | AI-01 | ... | Independiente | ... | ... | ... | ... |

   **Regla de pesos en sesiones impartidas:** la tabla 7.b mantiene el peso pedagógico de **todos** los subtemas, incluidas las sesiones ya impartidas. El peso es un atributo del temario, no del estado operativo. El estado operativo (`impartida / próxima / pendiente`) se declara por separado en el calendario. **Prohibido** usar `ya cubierto`, `no aplica` o cualquier forma de peso vacío en la tabla 7.b.

   **Regla de IDs de actividad oficial:** los IDs (`AC-NN`, `AI-NN`) son estables y no cambian. Atraviesan todo el pipeline: Brief, 03.D, 03.E, 04. Cada actividad apunta a un criterio de evaluación oficial. Si el temario no declara actividades, §7.c se omite.

8. **Matriz actividad × sesión** (condicional, solo si §7.c tiene al menos una actividad). Estructura:

   | ID | Actividad | S1 | S2 | S3 | ... | Sn |
   |---|---|---|---|---|---|---|
   | AC-01 | ... | — | — | — | ... | desarrolla |
   | AI-01 | ... | — | aporta | inicia | ... | entrega+retroalimenta+cierra |

   **Reglas:**
   - Los 8 estados se usan según §2.4.
   - Múltiples estados por celda separados por `+`.
   - Actividades recurrentes: `desarrolla` en todas las sesiones aplicables.
   - Actividades progresivas: `inicia` → `desarrolla` → `consolida` → `entrega + retroalimenta + cierra`.
   - Celdas sin actividad: `—` o `no aplica`.
   - **Verificación de cobertura:** cada actividad tiene al menos un `inicia` (o `desarrolla` si es recurrente), un `entrega` y un `cierra`. Si falta, se reporta.

9. **Matriz de continuidad conceptual** (siempre que haya conceptos en tabla 7.b). Estructura:

   | Concepto | Se introduce | Se desarrolla | Se aplica | Se evalúa | Observaciones |
   |---|---|---|---|---|---|
   | ... | S[X] | S[X–Y] | S[Z] | S[W] | — |

   **Reglas:**
   - Cada concepto del temario debe aparecer.
   - `Se introduce`: sesión donde aparece por primera vez.
   - `Se desarrolla`: sesiones donde se profundiza.
   - `Se aplica`: sesiones donde se usa en ejercicios, casos o proyectos.
   - `Se evalúa`: sesiones donde se recoge evidencia oficial.
   - `Observaciones`: tratamiento especial (propedéutico, reservado con continuidad explícita, etc.).
   - **Verificación de cobertura:** cada concepto tiene al menos `se introduce` y `se evalúa`. Si falta, se reporta.

   **Nota v1.6:** esta matriz cubre **conceptos**. La matriz de competencias es la §21.

10. **Calendario general de sesiones** (siempre). Tabla con sesión, fecha, **duración**, unidad, tema, subtemas cubiertos, actividad central, evidencia o tarea, y **estado operativo** (`impartida`, `próxima`, `pendiente`).

    La columna "duración" es obligatoria cuando las sesiones varían; puede omitirse solo si todas las sesiones duran lo mismo.

    La columna **"estado"** es el único lugar del documento donde vive el estado operativo de cada sesión. **No se repite en la tabla 7.b.** Incluye explícitamente la sesión de encuadre inicial y la de cierre/presentación final, aunque no tengan subtemas propios.

    **Nota sobre el orden de columnas:** se recomienda que "estado" sea la última columna, para que las columnas temáticas (unidad, tema, subtemas) queden agrupadas.

11. **Planeación por sesión (versión resumida)** (siempre). Expande cada fila del calendario con **propósito de aprendizaje** y **evidencia esperada**. Esta sección es deliberadamente compacta: **describe la ejecución particular de cada sesión, no el patrón metodológico general (eso ya está en §5)**. El brief didáctico completo (conceptos visuales, recursos audiovisuales, ejes de guion) se genera después con la skill de Briefs por Sesión. Si la institución exige el detalle didáctico completo desde este documento, indícalo al usuario y ofrece expandir §11 como anexo sin alterar el resto. Señala advertencias de calendario solo si el usuario las mencionó.

12. **Evidencia integradora** (solo si el usuario confirmó que existe). Título, producto mínimo esperado, tabla de avances alineados a sesiones específicas del calendario, y una rúbrica o criterio de valoración interno que sume exactamente el porcentaje oficial asignado.

13. **Sistema de evaluación** (siempre). Tabla con cada evidencia oficial, su porcentaje, y la sesión o fecha de entrega correspondiente. Verifica que la suma sea 100% si el programa define porcentajes cerrados.

14. **Formatos de actividades recurrentes** (solo para los tipos de evidencia confirmados). Define un formato fijo y reutilizable para las evidencias que de hecho se usarán.

15. **Recursos recomendados** (solo si el usuario lo autorizó). Fuentes, lecturas, sitios o materiales, citando el origen.

16. **Normas de trabajo del grupo** (solo si el usuario proporcionó reglamento o normas propias). Lista numerada de disposiciones aplicables, sin inventar políticas no confirmadas.

17. **Seguimiento y ajuste del curso** (siempre, breve). Recomendaciones de diagnóstico inicial, refuerzo de temas críticos, y plan de contingencia ante imprevistos de calendario, adaptado a la modalidad confirmada. Si hay práctica externa, incluye mecanismo de coordinación con supervisores.

18. **Indicadores de logro** (siempre). Resultados observables y medibles al final del curso, derivados de las competencias de la sección 3. **Cada indicador debe seguir la plantilla: [verbo observable] + [objeto de aprendizaje] + [condición] + [criterio de logro], y debe mencionar al menos una evidencia concreta del curso.** Ejemplo correcto: "El estudiante *elabora* un reporte de práctica *a partir de datos recolectados en campo*, *cumpliendo con los criterios de la rúbrica de la sesión 12*". Ejemplo incorrecto: "El estudiante comprende los conceptos de la unidad 1".

19. **Referencias de planeación** (siempre). Documentos fuente usados: temario oficial, lineamientos institucionales, otros insumos declarados.

20. **Mapeo al formato institucional oficial** (solo si el usuario confirmó en Fase 1.2 que existe una plantilla institucional obligatoria). Tabla de dos columnas: campo del formato oficial → sección de este documento donde se satisface. Si algún campo del formato no tiene equivalente, dilo explícitamente en lugar de rellenarlo con contenido genérico.

21. **Matriz de trazabilidad de competencias** (NUEVA en v1.6, siempre presente). Estructura:

    | ID | Competencia | Introduce | Desarrolla | Aplica | Evalúa | Estado |
    |---|---|---|---|---|---|---|
    | C1 | ... | S_N | S_N | S_N | Evidencia + S_N | Completa |
    | C2 | ... | S_N | S_N | — | — | Huérfana parcial |
    | C3 | ... | S_N | S_N | S_N | — | Huérfana parcial |

    **Reglas:**
    - Cada competencia extraída en §1.5 debe aparecer.
    - Los cuatro eslabones se llenan según §2.6.
    - El **estado** puede ser: `Completa`, `Huérfana parcial`, `Huérfana total`.
    - **Registro de decisiones:** debajo de la tabla, se declara cada decisión tomada sobre competencias huérfanas: ID, eslabón faltante, decisión (cubrir / reclasificar / retirar), justificación.
    - **Regla de bloqueo:** si quedan competencias huérfanas sin decisión tomada, el documento se emite como **versión incompleta** y se declara explícitamente.
    - **Nota:** si el perfil de egreso no estaba disponible y el documento se emite como versión condicionada (Regla 33), esta sección declara esa limitación.

22. **Control de consistencia** (NUEVA en v1.6, siempre presente). Tabla con:

    | Control | Resultado |
    |---|---|
    | Cobertura del fin de aprendizaje | Completa / Parcial / Pendiente |
    | Cobertura del perfil de egreso (si aplica) | Completa / Parcial / No aplica |
    | Competencias huérfanas resueltas | N/N |
    | Ponderación total | 100% / X% |
    | Actividades oficiales con criterio vinculado | N/N |
    | Matriz actividad × sesión completa | Sí / No |
    | Matriz de continuidad conceptual completa | Sí / No |
    | Matriz de trazabilidad de competencias completa | Sí / No |
    | Estado del documento | Completo / Condicionado / Incompleto |

23. **Anexos** (NUEVA en v1.6, siempre presente):

    - **Datos asumidos e inferidos:** listado de todo dato que no es declarado, con su justificación.
    - **Decisiones pedagógicas registradas:** listado de decisiones tomadas durante el diseño que afectan la estructura (reclasificaciones, retiros, adaptaciones por restricciones).
    - **Restricciones operativas:** condiciones institucionales, de recursos o de calendario que limitan el diseño.
    - **Propuestas pendientes de validación institucional:** si alguna decisión requiere aprobación externa (por ejemplo, retirar una competencia del perfil).

Si algún insumo no aporta información suficiente para una sección condicional, **omite la sección por completo**. No la sustituyas con contenido genérico, supuesto o trasplantado de otra disciplina.

---

## Fase 4 — Documento de salida

- Entrega el resultado como un **único archivo Markdown** (usa `create_file`), con encabezado inicial de metadatos: asignatura, clave, programa/carrera, nivel, periodo, institución, docente, modalidad, número de sesiones, rango real de calendario, y **propósito del documento** (planeación futura / documentación histórica / ambos).
- Si el curso ya está en marcha o terminado, incluye **nota de actualización** al inicio indicando:
  - que el documento se construyó respetando las sesiones impartidas;
  - que los pesos pedagógicos se asignaron a todos los subtemas sin importar el estado operativo;
  - qué fechas deben confirmarse todavía con la autoridad académica.
- Numera las secciones de forma consecutiva usando solo las que apliquen. Si se omiten varias, renumera para que el documento quede limpio, o mantén la numeración con "no aplica" — pregunta al usuario cuál prefiere si es la primera vez que usa la skill.
- Usa **tablas** cuando compares datos con múltiples atributos (ponderación, calendario, evaluación, articulación, avances de evidencia integradora, trazabilidad).
- No dupliques contenido: si un dato ya está en el calendario general, no lo repitas íntegro en la planeación por sesión; amplíalo con propósito y evidencia.
- Asegúrate de que la sección 5 (Metodología) incluya el diagnóstico del temario y la tabla de distribución de tiempos adaptada al peso de los temas, con su justificación. No presentes metodología genérica sin sustento.
- **Asegúrate de que la sección 7 incluya las tres subsecciones:** 7.a (ponderación por unidad), 7.b (ponderación por subtema) y 7.c (actividades oficiales, condicional). La tabla 7.b es **de cumplimiento obligatorio**, debe listar **todos** los subtemas del curso (sin excepción por estado operativo) y es la que hereda el Brief v2.7. No puede haber subtemas sin ponderar.
- **Asegúrate de que las secciones 8 y 9 (matrices) estén presentes** si el temario declara actividades oficiales. Si no las declara, se omiten.
- **Asegúrate de que las secciones 21, 22 y 23 (trazabilidad, control, anexos) estén presentes siempre** (nuevas en v1.6).
- **No mezcles peso pedagógico y estado operativo.** El peso vive en la tabla 7.b; el estado vive en el calendario. No agregues columna de estado a la tabla 7.b ni columna de peso al calendario.
- **No confundas la matriz de continuidad conceptual (§9) con la matriz de trazabilidad de competencias (§21).** La primera es de conceptos; la segunda de competencias.
- Si existe formato institucional oficial, incluye la sección 20 de mapeo y advierte al usuario que el documento maestro no sustituye la entrega en la plantilla oficial, sino que la alimenta.
- **Declara el estado del documento** (Completo / Condicionado / Incompleto) en el control de consistencia (§22) y en el encabezado de metadatos.

---

## Reglas de consistencia

### Reglas generales

1. **Nunca alteres los porcentajes oficiales de evaluación del temario;** solo distribúyelos en fechas y secciones.
2. **No inventes asignaturas antecedentes o consecuentes, recursos físicos, tipos de evidencia, modelos pedagógicos ni fuentes bibliográficas** que el usuario no haya confirmado.
3. **No apliques por defecto ninguna estructura de sesión, esquema de evaluación o formato de reglamento usado en una asignatura anterior del mismo usuario;** cada curso se construye desde sus propias respuestas de la Fase 1.
4. **Priorización basada en peso:** la metodología debe ser explícita en cómo las actividades de mayor impacto reciben más tiempo y recursos que las de temas secundarios. No distribuyas el tiempo equitativamente si el peso es desigual.
5. **Adaptabilidad de la estructura:** si el análisis revela que un curso es 80% práctico, la metodología debe reflejar esa naturaleza, priorizando la práctica sobre la exposición.
6. **Reserva siempre** la sesión de encuadre inicial y la de cierre/presentación final, aunque no tengan subtemas oficiales.
7. **Valida siempre el calendario** antes de ponderar. Si los números no cuadran, detente y pregunta; no ajustes silenciosamente.
8. **No avances a Fase 2** si falta cualquiera de los datos mínimos obligatorios de la sección 1.7.
9. Si el temario oficial cambia de fuente (otro archivo, otra materia), repite la Fase 1 completa; no reutilices ponderaciones de otra materia.
10. Si tras generar este documento el usuario quiere expandir las sesiones en briefs didácticos, no reescribas este documento: usa la skill de Briefs por Sesión, que consume este mismo archivo.

### Reglas de peso pedagógico y estado operativo

11. **Pesos por subtema obligatorios:** todo subtema debe tener un peso interno declarado (alto / medio / bajo). No se permite dejar subtemas sin ponderar. Esta tabla (7.b) es la que hereda el Brief v2.7 y usan las skills 03d y 03e para distribuir minutos y extensión.
12. **Separación peso / estado:** el peso pedagógico (alto / medio / bajo) y el estado operativo (impartida / próxima / pendiente) son dos informaciones distintas que viven en lugares distintos:
    - El peso vive en la tabla 7.b.
    - El estado vive en el calendario general.
    - No se sustituyen entre sí. No se mezclan.
    - Una sesión impartida conserva su peso pedagógico completo.
13. **Prohibición de pesos vacíos:** prohibido usar `ya cubierto`, `no aplica`, `sin ponderar` o cualquier forma de peso vacío en la tabla 7.b. La única excepción son las sesiones sin subtemas temáticos propios (encuadre, cierre, práctica externa), que no se listan en la tabla 7.b.
14. **Regla de unidad con un solo subtema:** si una unidad tiene 2 subtemas o menos, todos se consideran peso alto por defecto. No se pondera internamente una unidad con pocos subtemas.
15. **Regla de mayoría:** en cualquier unidad, los subtemas de peso bajo no pueden superar el 50% del total de subtemas de la unidad.
16. **Toda unidad debe tener al menos un subtema de peso alto.** Si no lo tiene, hay un error de asignación que debe corregirse antes de continuar.
17. **Curso ya terminado:** cuando el curso está terminado, todas las sesiones son `impartidas`. La tabla 7.b mantiene los pesos pedagógicos completos. El documento maestro se genera con el mismo rigor que para un curso futuro, pero el campo "propósito del documento" se declara como `documentación histórica`.

### Reglas de actividades oficiales

18. **No inventes actividades oficiales.** Solo las que el temario declara.
19. **No renombres actividades oficiales.** El nombre debe ser fiel al temario.
20. **No confundas actividad oficial con actividad didáctica auxiliar.** Solo las del temario son oficiales.
21. **Los IDs de actividad oficial son estables.** No cambian, no se reutilizan.
22. **Los IDs de actividad atraviesan todo el pipeline.** Brief, 03.D, 03.E, 04 los consumen.
23. **Toda actividad oficial debe apuntar a un criterio de evaluación oficial.**
24. **La matriz actividad × sesión usa los 8 estados.** Múltiples estados por celda separados por `+`. Recurrentes con `desarrolla`.
25. **La matriz de continuidad conceptual cubre todos los conceptos del temario.**
26. **Verificación de cobertura en ambas matrices.** Si falta cobertura, se reporta.

### Reglas de trazabilidad de competencias (NUEVAS en v1.6)

27. **Competencia huérfana:** una competencia declarada es huérfana si le falta al menos uno de los cuatro eslabones (introduce, desarrolla, aplica, evalúa). El diagnóstico se realiza en Fase 2.6 y se reporta en §21 del documento.

28. **Regla de bloqueo:** el Documento Maestro **no se emite como versión completa** si existen competencias huérfanas sin decisión tomada. Las opciones son: cubrir, reclasificar o retirar. Si el usuario decide emitir sin resolver, el documento se marca como **versión incompleta** con lista de pendientes y fecha prevista de resolución.

29. **Opciones de resolución:** las tres opciones son cubrir (rediseñar Fase 2), reclasificar (cambiar estatus de la competencia) o retirar (decisión institucional). Toda decisión debe registrarse en §21 con ID, eslabón faltante, decisión y justificación.

30. **Registro obligatorio de decisiones:** cada decisión sobre competencia huérfana debe quedar registrada en el documento final. No basta con resolverla internamente durante el diseño; debe declararse.

31. **Criterio de operatividad:** antes de verificar trazabilidad, declarar qué significa "aplicar" en la disciplina del curso. En disciplinas híbridas, se permiten múltiples criterios. La matriz verifica cada competencia contra el criterio correspondiente.

32. **No confundir conceptos con competencias:** la matriz de continuidad conceptual (§9) cubre conceptos del temario. La matriz de trazabilidad de competencias (§21) cubre competencias declaradas. Una competencia puede estar cubierta aunque sus conceptos no estén todos listados; un concepto puede estar cubierto aunque la competencia que lo usa esté huérfana. No se sustituyen entre sí.

33. **Versión condicionada:** si el perfil de egreso no está disponible o es ambiguo, el documento puede emitirse como **versión condicionada**, declarando explícitamente que la verificación de trazabilidad se hizo solo contra el fin de aprendizaje. La limitación se registra en §21 y §22.

34. **Múltiples criterios de operatividad:** en disciplinas híbridas (que mezclan procedimiento, interpretación y producción), se permite declarar más de un criterio. La matriz de trazabilidad verifica cada competencia contra el criterio que le corresponda según su verbo observable.

35. **Escala por duración del curso:** en cursos de menos de 8 sesiones (módulos cortos, seminarios intensivos, cursos de verano), la exigencia de los cuatro eslabones puede reducirse a tres (introduce → aplica → evalúa), declarando explícitamente la reducción en §21. En cursos de 8 sesiones o más, se exigen los cuatro eslabones.

---

## Checklist interno antes de entregar

### Verificaciones generales

- ¿Se validó el calendario antes de ponderar?
- ¿Se respetaron las sesiones ya impartidas tal como ocurrieron?
- ¿La suma de porcentajes de evaluación es 100%?
- ¿Se reservó la sesión de encuadre inicial y la de cierre/presentación final?
- ¿Se generó el documento como único archivo Markdown con encabezado de metadatos?
- ¿La nota de actualización está presente si el curso ya está en marcha o terminado?
- ¿Las secciones usadas están numeradas de forma consecutiva?
- ¿La sección 5 incluye el diagnóstico del temario y la tabla de distribución de tiempos?
- ¿La sección 7 incluye las tablas 7.a y 7.b (y 7.c si aplica)?
- ¿La sección 10 (calendario) incluye columna de estado operativo y de duración (cuando las sesiones varían)?
- ¿Los indicadores de logro siguen la plantilla [verbo] + [objeto] + [condición] + [criterio] y mencionan evidencia concreta?
- ¿Se incluyó la sección 20 (mapeo institucional) si el usuario confirmó que existe plantilla oficial?
- ¿No se inventaron asignaturas, recursos, tipos de evidencia, modelos pedagógicos ni fuentes?
- ¿No se duplicó contenido entre secciones?

### Verificaciones de peso pedagógico

- ¿Todos los subtemas del temario tienen peso interno declarado (alto / medio / bajo)?
- ¿Algún subtema quedó sin ponderar?
- ¿Se usó `ya cubierto`, `no aplica`, `sin ponderar` o cualquier forma de peso vacío?
- ¿Toda unidad tiene al menos un subtema de peso alto?
- ¿Los subtemas de peso bajo superan el 50% en alguna unidad?
- ¿Las unidades con 2 subtemas o menos tienen todos sus subtemas como peso alto?
- ¿La tabla 7.b lista todos los subtemas del curso, incluidas las sesiones impartidas?
- ¿La tabla 7.b NO tiene columna de estado operativo?
- ¿El estado operativo se declara solo en el calendario?

### Verificaciones de actividades oficiales

- ¿Se extrajeron todas las actividades oficiales del temario?
- ¿Cada actividad tiene ID estable (`AC-NN` o `AI-NN`)?
- ¿Cada actividad tiene régimen (conducción / independiente)?
- ¿Cada actividad apunta a un criterio de evaluación?
- ¿Ninguna actividad fue inventada?
- ¿Ninguna actividad fue renombrada sin justificación?
- ¿La tabla §7.c está completa?

### Verificaciones de la matriz actividad × sesión

- ¿Cada actividad aparece en la matriz?
- ¿Se usan los 8 estados correctamente?
- ¿Las actividades recurrentes tienen `desarrolla` en todas las sesiones aplicables?
- ¿Cada actividad tiene al menos un `inicia`, un `entrega` y un `cierra`?
- ¿Se reportaron coberturas incompletas?

### Verificaciones de la matriz de continuidad conceptual

- ¿Cada concepto del temario aparece?
- ¿Cada concepto tiene al menos `se introduce` y `se evalúa`?
- ¿Se reportaron conceptos sin cobertura?
- ¿Se declararon tratamientos especiales (propedéutico, reservado, etc.)?

### Verificaciones de la matriz de trazabilidad de competencias (NUEVAS en v1.6)

- ¿Se extrajeron todas las competencias declaradas (fin + perfil)?
- ¿Cada competencia tiene los cuatro eslabones (introduce, desarrolla, aplica, evalúa)?
- ¿Las huérfanas están identificadas con el eslabón faltante declarado?
- ¿Las huérfanas tienen decisión tomada (cubrir, reclasificar, retirar)?
- ¿Las decisiones están registradas en §21 con justificación?
- ¿El criterio de operatividad de la disciplina está declarado antes de verificar?
- ¿En disciplinas híbridas se declararon múltiples criterios si aplica?
- ¿En cursos de menos de 8 sesiones se declaró la reducción de eslabones si aplica?
- ¿La matriz de competencias no se confunde con la matriz de conceptos?
- ¿El documento declara su estado (Completo / Condicionado / Incompleto) en §22?

### Verificaciones de trazabilidad del origen del dato (NUEVAS en v1.6)

- ¿Todo dato asumido o inferido está declarado en §23 (anexos)?
- ¿Las decisiones pedagógicas están registradas?
- ¿Las restricciones operativas están declaradas?
- ¿Las propuestas pendientes de validación institucional están registradas?

---

## Criterio final de calidad

La skill 01 cumple si:

### Criterios generales

- el Documento Maestro integra fundamento curricular, competencias, articulación, ponderación, metodología, calendario, evaluación, evidencia integradora y trazabilidad de competencias;
- las secciones condicionales se incluyen solo si los insumos las sostienen;
- no se inventó contenido genérico ni trasplantado de otra disciplina;
- el calendario fue validado antes de ponderar;
- las sesiones impartidas se respetaron tal como ocurrieron;
- la suma de porcentajes de evaluación es 100% (si el programa los define);
- la sesión de encuadre inicial y la de cierre/presentación final están reservadas;
- los indicadores de logro siguen la plantilla y mencionan evidencia concreta;
- el documento se entrega como único archivo Markdown con encabezado de metadatos;
- el documento declara su estado (Completo / Condicionado / Incompleto).

### Criterios de peso pedagógico

- **todos los subtemas del temario tienen peso interno declarado (alto / medio / bajo)**;
- **ningún subtema quedó sin ponderar**;
- **no se usó `ya cubierto`, `no aplica`, `sin ponderar` ni peso vacío**;
- **toda unidad tiene al menos un subtema de peso alto**;
- **los subtemas de peso bajo no superan el 50% en ninguna unidad**;
- **las unidades con 2 subtemas o menos tienen todos sus subtemas como peso alto**;
- **la tabla 7.b lista todos los subtemas del curso, incluidas las sesiones impartidas**;
- **la tabla 7.b NO tiene columna de estado operativo**;
- **el estado operativo se declara solo en el calendario**;
- **el peso pedagógico y el estado operativo no se sustituyen entre sí**.

### Criterios de actividades oficiales

- **las actividades oficiales están extraídas del temario sin inventar**;
- **cada actividad tiene ID estable (`AC-NN` o `AI-NN`)**;
- **cada actividad apunta a un criterio de evaluación oficial**;
- **la matriz actividad × sesión usa los 8 estados**;
- **cada actividad tiene cobertura completa (inicia → entrega → cierra)**;
- **la matriz de continuidad conceptual cubre todos los conceptos**;
- **cada concepto tiene cobertura completa (se introduce → se evalúa)**;
- **los IDs de actividad atraviesan el pipeline**;
- **no hay confusión entre actividad oficial y actividad didáctica auxiliar**.

### Criterios de trazabilidad de competencias (NUEVOS en v1.6)

- **todas las competencias declaradas (fin + perfil) están extraídas y listadas**;
- **cada competencia tiene los cuatro eslabones (introduce, desarrolla, aplica, evalúa) o decisión explícita**;
- **las competencias huérfanas están identificadas con el eslabón faltante declarado**;
- **toda competencia huérfana tiene decisión tomada: cubrir, reclasificar o retirar**;
- **las decisiones están registradas en §21 con justificación**;
- **el criterio de operatividad de la disciplina está declarado**;
- **en disciplinas híbridas se declararon múltiples criterios si aplica**;
- **en cursos de menos de 8 sesiones se declaró la reducción de eslabones si aplica**;
- **la matriz de competencias (§21) no se confunde con la matriz de conceptos (§9)**;
- **el documento declara su estado (Completo / Condicionado / Incompleto)**;
- **si el documento es incompleto, se declaran las competencias pendientes y fecha prevista**.

### Criterios de trazabilidad del origen del dato (NUEVOS en v1.6)

- **todo dato asumido o inferido está declarado en §23**;
- **las decisiones pedagógicas están registradas**;
- **las restricciones operativas están declaradas**;
- **las propuestas pendientes de validación institucional están registradas**.

### Criterios de trazabilidad interna

- la tabla 7.b del documento final coincide exactamente con la asignación presentada al usuario;
- la matriz actividad × sesión coincide con §7.c;
- la matriz de continuidad conceptual coincide con la tabla 7.b;
- la matriz de trazabilidad de competencias coincide con §1.5;
- el documento declara sus versiones de insumo.

---

## Changelog de consolidación v1.5 → v1.6

**Propósito:** incorporar la capa de trazabilidad de competencias como principio estructural de la planeación general. Cerrar la brecha entre "curso coherente" y "curso responsable" (fin declarado con medios operativos verificados).

**Contenido normativo preservado del v1.5 (sin cambios):**

- Propósito general (ahora extendido con la capa de trazabilidad).
- Principio 1 (peso ≠ estado ≠ actividad).
- Cuándo activar.
- Fase 1: §1.1 Datos de asignatura, §1.2 Datos de calendario, §1.3 Preguntas de encuadre, §1.4 Análisis interno de ponderación temática, §1.5 (ahora §1.7) Datos mínimos obligatorios.
- Fase 2: §2.0 Validación cruzada, §2.1 Ponderación por unidad, §2.2 Ponderación por subtema, §2.3 Actividades oficiales, §2.4 Matriz actividad × sesión, §2.5 Matriz de continuidad conceptual.
- Fase 3: secciones 1–20 del documento.
- Fase 4.
- Reglas generales 1–10.
- Reglas de peso/estado 11–17.
- Reglas de actividades oficiales 18–26.
- Checklist existente.
- Criterios finales existentes.
- Changelog anterior.

**Contenido nuevo en v1.6:**

- **Principio 2** (trazabilidad de competencias).
- **§1.5** Extracción del fin y de las competencias declaradas (con subsecciones 1.5.1 a 1.5.5).
- **§1.6** Trazabilidad del origen del dato.
- **§1.7** Datos mínimos obligatorios (antes §1.5).
- **§2.6** Construcción de la matriz de trazabilidad de competencias.
- **§21** Matriz de trazabilidad de competencias (documento final).
- **§22** Control de consistencia (documento final).
- **§23** Anexos (documento final).
- **Reglas 27–35** (trazabilidad de competencias).
- **Verificaciones nuevas** en el checklist (trazabilidad de competencias y origen del dato).
- **Criterios nuevos** en el criterio final (trazabilidad de competencias y origen del dato).

**Cambios de empaquetado:**

- Se renumeró §1.5 (datos mínimos) a §1.7 para hacer espacio a §1.5 (extracción de competencias) y §1.6 (trazabilidad del dato).
- Se renumeraron las verificaciones del checklist en cuatro bloques: generales, peso, actividades, continuidad conceptual, trazabilidad de competencias, origen del dato.
- Se renumeraron los criterios finales en cuatro bloques análogos.
- Se añadieron al documento final tres secciones nuevas (§21, §22, §23) sin renumerar las existentes.
- El changelog anterior (v1.4 → v1.5) se conserva íntegro al final de este changelog.

**Compatibilidad con skills del flujo:**

- Brief consumidor: **v2.7** (autocontenido). El Brief puede consumir la matriz de trazabilidad de competencias de §21 para declarar en cada brief qué eslabón cubre.
- Ficha Teórica consumidora: **v1.10** (implícito).
- Ficha Normativa consumidora: **v1.3** (implícito).
- Ficha Visual consumidora: **v1.7** (implícito).
- 03.D consumidor: **v1.8** (implícito).
- 03.E consumidor: **v2.2** (implícito).
- 04 Auditor: **v3.9** (implícito). El Auditor puede consumir el control de consistencia de §22 como insumo para su Fase 0 (verificación de fin).

**Nota sobre el flujo completo:** las skills 02, 03.A y 04.A pueden adoptar progresivamente el mismo principio de trazabilidad, cerrando el pipeline completo. La v1.6 de la skill 01 produce el insumo para que esas adopciones sean posibles.

---

## Changelog de consolidación v1.4 → v1.5 (conservado)

**Propósito:** convertir la skill en autocontenida. Todas las referencias `[Sin cambios respecto a v1.3]` y `[Las X de v1.3]` fueron expandidas literalmente.

**Contenido normativo preservado sin cambios:**

- Propósito completo.
- Principio rector peso ≠ estado ≠ actividad.
- Cuándo activar (5 disparadores).
- Fase 1 completa.
- Fase 2 completa.
- Fase 3 con las 20 secciones del documento.
- Fase 4 con el contrato de salida.
- Reglas de consistencia.
- Checklist interno.
- Criterio final de calidad.

**Cambios de empaquetado (no normativos):**

- Se eliminó la dependencia histórica v1.5 → v1.4 → v1.3.
- Se normalizó la numeración de reglas a un rango continuo 1–26.
- Se expandieron las secciones 1.1 a 2.5 sin referencias cruzadas.
- Se expandió el contrato completo de las 20 secciones del documento.

---

**Guía de uso del flujo completo:** consulta `guia_uso_flujo_skills.md`.