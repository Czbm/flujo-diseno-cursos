---
name: 03d-composicion-dual
description: Compone el paquete sincronico de sesion (presentacion proyectable para alumno + guia docente) integrando fichas y paquete visual resuelto.
stage_id: "03.D"
version: "2.1"
status: stable
---

# Skill: Composición Dual NUMA — Presentación + Guía Docente (03d) — v2.1

> **Visor y proyector recomendado:** las presentaciones Markdown y guías docentes generadas por esta skill están diseñadas para abrirse y proyectarse de forma nativa en [**NUMA Deck Presentations**](https://github.com/Czbm/numa-deck-presentations), con soporte para modo dual, KaTeX, SVG/imágenes y control remoto móvil (*Android-Link*).

## Propósito

Esta skill es **paralela a 03e (Capítulo de Libro Autónomo)**. Ambas consumen los mismos insumos académicos base y los recursos visuales resueltos del subsistema 03.C, pero producen productos distintos:

- **03d** produce material sincrónico: presentación proyectable + guía docente.
- **03e** produce material asincrónico: capítulo autocontenido del libro de la materia.

Pueden ejecutarse en paralelo sin dependencia mutua.

Esta skill consume **tres insumos académicos base** y **un conjunto visual contractual resuelto**:

1. **Brief de la Sesión N** (skill 02 v2.7 o v2.8) — 35–36 campos con contrato fijo, incluidos `Pesos por subtema`, `Modo de composición`, `Alcance conceptual del subtema`, `Competencias posteriores que activan el propedéutico`, `Articulación prioritaria` + `Materia de aplicación concurrente principal` (bloque F), `Actividades oficiales vinculadas` y, en v2.8, `Eslabones de competencia cubiertos`.
2. **Ficha Teórica** (03a v1.11 o v1.12) — conceptos clasificados por **5 niveles** (Núcleo / Panorama / Propedéutico / Contexto / Reservado), **3 categorías de reserva**, fundamento de exclusión y articulación curricular.
3. **Ficha Normativa** (03b v1.4).
4. **Conjunto visual contractual resuelto**, compuesto según aplique por:
   - **Ficha de Estrategia Visual de 03.C-1 v1.2**, que conserva el contrato NVD, el destino autorizado, la prioridad, la función, la procedencia, el tratamiento externo y el criterio de satisfacción;
   - **salidas de 03.C-3** para NVD `EXTERNO` o componente externo de `HÍBRIDO`, con `RECURSO_EXTERNO_RESUELTO`, fuente, localizador, derechos, atribución y referencia persistente;
   - **salidas generativas producidas por 03Cbis** únicamente cuando el RGE correspondiente haya recibido `PASS` de 03.C-2B v1.0 y pueda trazarse al contrato auditado;
   - **ensamble de componentes híbridos**, conservando la función diferenciada prescrita por 03.C-1.

El **conjunto visual contractual resuelto no constituye una nueva skill ni un nuevo nivel de decisión**. Es la agregación de los contratos y recursos ya autorizados que 03.D necesita para integrar visuales sin reinterpretar la estrategia.

Su función es convertir esos insumos en **dos archivos listos para NUMA Deck modo dual**:

- `presentacion_sesion_N.md` — audiencia: alumno.
- `guia_docente_sesion_N.md` — audiencia: docente.

**03.D no investiga, no busca recursos, no diseña RGE, no audita semánticamente RGE y no genera imágenes.** Su trabajo es **componer, decidir el reforzamiento inicial, calcular, integrar recursos autorizados, verificar legibilidad y auditar su propia composición**.

La única decisión pedagógica nueva que le pertenece por completo es el **bloque de reforzamiento inicial** en modo operativo. Las decisiones visuales pertenecen al subsistema 03.C y son vinculantes downstream.

### Principio rector v2.1 — integrar sin reinterpretar

03.D puede decidir **cómo explotar didácticamente** un recurso ya autorizado dentro de una presentación o guía: ubicación, tamaño relativo, secuencia de aparición, relación con el texto, momento de uso y nota docente.

03.D **no puede cambiar** por iniciativa propia:

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
- modo de agrupación visual;
- destino autorizado;
- criterio de satisfacción;
- identidad del recurso externo validado;
- semántica de un RGE aprobado;
- contrato RGE, whitelist, blacklist o huella auditada.

Si la composición exige cambiar alguno de esos elementos, 03.D **no corrige el contrato**: registra el conflicto y lo devuelve a la skill propietaria.

**Nota de compatibilidad:** esta skill requiere Brief **v2.7 o v2.8**, Ficha Teórica **v1.11 o v1.12**, Ficha Normativa **v1.4**, Doc Maestro **v1.5 o v1.6** y 03.C-1 **v1.2**. Para recursos externos consume la salida vigente de 03.C-3; mientras 03.C-3 permanezca en `BORRADOR v0.1`, su uso debe declararse como interfaz provisional. Para recursos generativos exige evidencia de `PASS` de 03.C-2B v1.0 y trazabilidad hacia la producción de 03Cbis. No se asume compatibilidad de una salida generativa que no pueda demostrar esa cadena.

**Versión autocontenida.** Esta versión no depende de versiones anteriores. Todo el contenido vigente está expandido literalmente.

### Resumen de capacidades por versión

- **v1.0:** composición básica con checkpoints y presupuesto.
- **v1.1:** pesos por subtema heredados del Brief.
- **v1.2:** modo de composición (operativo / retrospectivo).
- **v1.3:** recursos de elaboración propia pendientes con placeholder.
- **v1.4:** 5 variantes de placeholder + Anexo C con ID.
- **v1.5:** distribución diferenciada por nivel (Núcleo / Panorama / Contexto / Reservado).
- **v1.6:** nivel Propedéutico + categorías de reserva.
- **v1.7:** actividades oficiales vinculadas + slide oficial + slide auxiliar.
- **v1.8:** articulación curricular (Brief v2.6) + slide de aplicación concurrente.
- **v1.9:** consolidación autocontenida + referencias a Brief v2.7, Ficha Teórica v1.11, Ficha Normativa v1.4, estrategia visual 03.C-1 v1.8, Doc Maestro v1.5.
- **v2.0:** política de audiencia por producto (§0.10) + diccionario de expansión local (§0.11) + traducción de estados internos a prosa (§0.12) + Anexo F de trazabilidad interna (§3.5) + reglas 56–75 + checklist y criterios de legibilidad editorial. La presentación al alumno sale con lenguaje natural; la guía docente conserva códigos con expansión ligera.
- **v2.1:** sustituye la dependencia de `estrategia visual 03.C-1 v1.8` por el subsistema visual contractual `03.C-1 → [03.C-3 | 03.C-2A → 03.C-2B → 03Cbis]`; añade compuerta visual de entrada, regla de no reinterpretación, control de destino, identidad y estado por NVD, trazabilidad visual en Anexo C, retorno a la skill propietaria y elimina la generación de instrucciones de recursos propios desde 03.D.

---

## Cuándo activar esta skill

Actívala cuando el usuario:

- Tenga ya generados el Brief v2.7 o v2.8, la Ficha Teórica v1.11 o v1.12 y la Ficha Normativa v1.4 de una sesión concreta.
- Disponga de la **Ficha de Estrategia Visual 03.C-1 v1.2** de esa misma sesión.
- Para cada NVD destinada a `Presentación` o `Guía docente`, exista un estado downstream verificable:
  - recurso externo resuelto por 03.C-3;
  - recurso generativo producido desde un RGE con `PASS` de 03.C-2B;
  - recurso híbrido con sus componentes autorizados y trazables;
  - o NVD V3/V4 pendiente aceptada explícitamente como no crítica por 03.C-1.
- Pida "armar la presentación y la guía docente de la sesión N".
- Quiera regenerar una presentación o guía existente sin cambiar contratos upstream.
- Quiera generar material de referencia para una sesión ya impartida (modo retrospectivo).

No la actives como composición **completa** si:

- falta cualquiera de los tres insumos académicos base;
- falta 03.C-1;
- existe una NVD V1/V2 destinada a presentación o guía que esté `PRESCRITA`, `EN_EJECUCIÓN` o `BLOQUEADA`;
- un recurso generativo no puede demostrar `PASS` y trazabilidad al contrato auditado;
- un recurso externo fue sustituido respecto del seleccionado por 03.C-3 sin nueva validación;
- la composición requeriría cambiar una decisión propiedad de 03.C-1, 03.C-2A/2B o 03.C-3.

En esos casos, emite diagnóstico de bloqueo y remite al propietario contractual correspondiente.

---

## Estructura del flujo

```text
Brief v2.7/v2.8 ────────────┐
Ficha Teórica v1.11/v1.12 ──┤
Ficha Normativa v1.4 ────────┤
                              │
03.C-1 v1.2 ─────────────────┤
   │                          │
   ├─ EXTERNO → 03.C-3 ───────┤
   │                          │
   ├─ GENERATIVO              │
   │    03.C-2A               │
   │       ↓                  │
   │    03.C-2B PASS          │
   │       ↓                  │
   │    03Cbis ───────────────┤
   │                          │
   └─ HÍBRIDO → ambas ramas ──┤
                              ▼
                         03.D v2.1
                              │
                 ┌────────────┴────────────┐
                 ▼                         ▼
       presentacion_sesion_N.md   guia_docente_sesion_N.md
```

03.D es **consumidor e integrador** del subsistema visual. No crea una segunda estrategia visual.

---

## Fase 1 — Verificación de insumos

### 1.1 Verificación obligatoria

Confirma que están disponibles:

- **Brief v2.7 o v2.8** con los 35–36 campos completos.
- **Ficha Teórica v1.11 o v1.12** con niveles, reservas, fuentes, articulación y, si es v1.12, suficiencia por eslabón.
- **Ficha Normativa v1.4**.
- **Ficha de Estrategia Visual 03.C-1 v1.2** con bloques A–L y contratos NVD completos.
- Para cada NVD con destino `Presentación` o `Guía docente`, la evidencia downstream que corresponda:
  - **EXTERNO:** ficha 03.C-3 con handoff `RECURSO_EXTERNO_RESUELTO`, identidad del recurso, fuente/localizador, derechos/atribución y referencia persistente;
  - **GENERATIVO:** RGE trazable a 03.C-2A, veredicto `PASS` de 03.C-2B asociado al contrato auditado y recurso producido por 03Cbis;
  - **HÍBRIDO:** componente externo resuelto + componente generativo aprobado/producido, manteniendo la función diferenciada declarada por 03.C-1.

03.D **no acepta como equivalente** una antigua estrategia visual 03.C-1 v1.8 para satisfacer este contrato v2.1. Si únicamente existe ese insumo legado, se declara `INTERFAZ_VISUAL_LEGADA` y se remite a regenerar la estrategia mediante 03.C-1.

### 1.2 Verificación de coherencia entre insumos

Comprueba que todos los insumos son de la **misma sesión** y del **mismo Documento Maestro**.

Verifica además:

1. Todo ID NVD usado en downstream existe literalmente en 03.C-1.
2. La `procedencia` de cada NVD coincide con la rama que la resolvió.
3. El `destino` incluye `Presentación` y/o `Guía docente` antes de usar el recurso en ese producto.
4. La `función primaria`, prioridad, tratamiento externo, agrupación y criterio de satisfacción no fueron modificados downstream.
5. Para EXTERNO, el recurso usado es exactamente el seleccionado/validado por 03.C-3.
6. Para GENERATIVO, el recurso puede rastrearse al RGE con `PASS`; si existe huella disponible, se registra sin reinterpretarla.
7. Para HÍBRIDO, la composición conserva ambas funciones diferenciadas y no fusiona componentes si 03.C-1 prescribe una secuencia o separación.
8. NVD V1/V2 destinadas al producto están `SATISFECHAS`. Una V1/V2 `BLOQUEADA` bloquea la composición completa.
9. NVD V3/V4 no satisfechas solo pueden omitirse si 03.C-1 las acepta explícitamente como no críticas para el cierre.

### 1.2.bis Compuerta visual de entrada

Clasifica cada NVD destinada a 03.D:

| Estado de integración | Condición | Acción de 03.D |
|---|---|---|
| `ADMISIBLE_EXTERNO` | 03.C-3 entregó `RECURSO_EXTERNO_RESUELTO` | Integrar |
| `ADMISIBLE_GENERATIVO` | `PASS` 03.C-2B + recurso producido trazable | Integrar |
| `ADMISIBLE_HÍBRIDO` | Componentes externo y generativo resueltos conforme al contrato | Integrar respetando funciones |
| `OMISIBLE_NO_CRÍTICO` | V3/V4 pendiente y aceptación explícita de 03.C-1 | Omitir y registrar |
| `BLOQUEO_VISUAL` | V1/V2 no satisfecha, recurso sin trazabilidad, destino no autorizado o contrato contradictorio | No integrar; devolver upstream |

La compuerta no certifica semántica ni calidad documental. Solo verifica **admisibilidad contractual downstream**.

### 1.3 Verificación de datos operativos mínimos

Del Brief, extrae:

- Duración, hora real de inicio, número de alumnos, modalidad.
- Tipo de sesión, nivel de profundidad.
- **Pesos por subtema.**
- **Alcance conceptual del subtema.**
- **Competencias posteriores que activan el propedéutico** (si aplica).
- **Modo de composición.**
- **Prerrequisitos detectados.**
- **Articulación prioritaria** (bloque F).
- **Materia de aplicación concurrente principal** (bloque F).
- **Actividades oficiales vinculadas** (IDs, estados, productos parciales).
- **Actividad oficial principal de la sesión** (si hay 2+ activas).
- **Actividad didáctica auxiliar.**
- **Producto parcial esperado.**
- **Actividad recurrente** (si aplica).
- **Continuidad conceptual posterior.**
- **Eslabones de competencia cubiertos** (si el Brief es v2.8).

De la Ficha Teórica, extrae:

- Lista de conceptos con su nivel (5 niveles).
- Categoría de reserva para cada Reservado.
- Fundamento de exclusión para cada Fuera del curso.
- Peso heredado por concepto (solo Núcleo y Panorama).
- Corriente teórica dominante.
- Bloque L (articulación curricular).
- Mini-fichas de refuerzo.
- Suficiencia para eslabón (si la Ficha Teórica es v1.12).

Si falta alguno, detente.

### 1.4 Detección del modo de composición

- `operativo` → flujo normal con checkpoints.
- `retrospectivo` → reglas especiales (§1.5).

### 1.5 Reglas del modo retrospectivo

Cuando el modo es `retrospectivo`:

1. **No se generan checkpoints operativos.** La sesión ya ocurrió; el semáforo no aplica. Se sustituyen por referencias de sección o marcas de tiempo estimadas solo si aportan valor didáctico.

2. **La vista de conducción paralela se sustituye por un análisis retrospectivo.** Formato:

   | Hora estimada | Bloque | Subtema | Nivel | Actividad oficial | Peso | Min estimados | Tema |
   |---|---|---|---|---|---|---|---|

   Sin columnas de acción docente ni checkpoint.

3. **El presupuesto de tiempo es estimado, no vinculante.**

4. **El refuerzo inicial no se activa.** El bloque H del Brief se marca como `no aplica`.

5. **El boleto de salida y la tarea se mantienen** solo si aportan como material de estudio o referencia. Se declaran como "referencia histórica" en nota.

6. **El encabezado de los archivos declara el modo.**

7. **Los IDs NUMA se generan igual.**

8. **La auditoría 60/20/20 se mantiene** si la sesión tuvo fuentes declaradas.

**Regla adicional:** en modo retrospectivo, el motivo declarado en el Brief (bloque I, campo `Motivo del modo retrospectivo`) se incluye en el encabezado de ambos archivos.

---

## §0.10 Regla de audiencia por producto

**Principio.** La skill produce dos productos con audiencias distintas. La política de lenguaje se aplica **por producto**, no globalmente.

| Producto | Audiencia | Política de lenguaje |
|---|---|---|
| `presentacion_sesion_N.md` | Alumno | Estricta: sin códigos internos sin expansión en prosa |
| `guia_docente_sesion_N.md` | Docente | Flexible: códigos permitidos con expansión ligera en primera mención |

### §0.10.1 Definición de "código interno"

- IDs de competencia: `C1`, `C2`, ...
- IDs de unidad: `U1`, `U2`, ...
- IDs de subtema en formato compacto: `1.4`, `2.7`, ... cuando se usan como referencias cruzadas.
- IDs de actividad oficial: `AC-01`, `AI-02`, `AI-04`, ...
- IDs de recursos visuales: `H1`, `I1`, `B1`, `H11`, ...
- Estados de eslabón: `introduce`, `desarrolla`, `aplica`, `evalúa`.
- Estados de actividad: `aporta`, `inicia`, `desarrolla`, `consolida`, `entrega`, `retroalimenta`, `cierra`.
- Notación compacta del Brief: `C1=introduce`, `C2=desarrolla`, etc.

### §0.10.2 Política para la presentación al alumno

1. **Primera mención de un código en la presentación:** nombre legible completo + código entre paréntesis.
   - Correcto: `Proyecto final de levantamiento topográfico (AI-04)`.
   - Incorrecto: `AI-04`.
2. **Menciones posteriores:** solo nombre legible, sin código.
3. **Estados de actividad:** se traducen a lenguaje natural según §0.12. No aparecen como código.
4. **Excepción única:** el **Anexo F — Trazabilidad interna** (§3.5) al final de la presentación, claramente marcado como material interno, precedido por el diccionario local.
5. **Tablas de referencia interna:** en la **Agenda ponderada** y en los **Anexos A, B y E**, la columna "Actividad oficial" puede conservar el ID si el ID va acompañado del nombre legible. En la **prosa introductoria** de cualquier sección, se expande en primera mención.

### §0.10.3 Política para la guía docente

1. **Códigos permitidos** porque el lector es el docente.
2. **Expansión ligera en primera mención:** la primera vez que aparece un código en la guía, se acompaña del nombre legible.
   - Ejemplo: `AI-04 (Proyecto final de levantamiento topográfico)`.
3. **Menciones posteriores:** se puede usar solo el código.
4. **No se aplica la prohibición estricta** de la presentación.


### §0.10.4 Alcance

La política aplica a todos los elementos de cada producto: títulos, cuerpo, pies de figura, encabezados de tabla, notas al margen, agendas y anexos.

---

## §0.11 Diccionario de expansión local

**Propósito.** Antes de redactar la presentación, 03.D construye una **tabla interna** con la equivalencia entre cada código que el Brief, las fichas o los insumos mencionan y su nombre legible.

**Fuentes del diccionario:**

| Tipo de código | Fuente |
|---|---|
| Competencias | Brief bloque B (campo legible si existe) o Doc Maestro §21 |
| Unidades | Doc Maestro §7.b |
| Actividades oficiales | Brief bloque G o Doc Maestro §7.c |
| Recursos visuales | 03.C-1 (ID NVD y nombre de necesidad) + handoff downstream resuelto |
| Subtemas | Doc Maestro §7.b |
| Estados de eslabón | §0.12 (no requieren diccionario, se traducen) |
| Estados de actividad | §0.12 (no requieren diccionario, se traducen) |

**Estructura:**

| Código | Tipo | Nombre legible | Fuente |
|---|---|---|---|
| C1 | Competencia | Distinguir escenarios naturales y urbanos | Brief bloque B |
| U2 | Unidad | Unidad 2 — Escenario natural | Doc Maestro §7.b |
| AC-01 | Actividad oficial | Plenaria/debate y reporte o conclusiones | Brief bloque G |
| AI-04 | Actividad oficial | Proyecto final de levantamiento topográfico | Brief bloque G |
| NVD-02 | Recurso visual | Matriz de ética ambiental | 03.C-1 + recurso downstream resuelto |

**Regla del diccionario huérfano.**

Si un código aparece en los insumos y no puede resolverse:

1. **No inventar el nombre.**
2. **Detener la producción de la presentación.**
3. **Reportar el código huérfano** al usuario con la siguiente información:
   - Código no resuelto.
   - Sección del Brief, ficha o Doc Maestro donde aparece.
   - Fuentes consultadas.
   - Acción sugerida: revisar insumos para completar el diccionario.
4. **No emitir la presentación como completa.** Se emite como `incompleto por diccionario huérfano`.

**Regla del diccionario local.** Vive solo dentro de 03.D. Se incluye como Anexo F de la presentación. No reemplaza al diccionario canónico de skills upstream.

**Consumo de Brief v2.8.** Si el Brief es v2.8 o superior, el campo `Eslabones de competencia cubiertos` se usa para alimentar el diccionario y verificar qué eslabones cubre la sesión.

**Consumo de Ficha Teórica v1.12.** Si la Ficha Teórica es v1.12, el campo `Suficiencia para eslabón` de bloque B alimenta la verificación de cobertura de eslabones en la sesión.

---

## §0.12 Traducción de estados internos a prosa

**Propósito.** Los estados `introduce`, `desarrolla`, `aplica`, `evalúa` (eslabones) y `aporta`, `inicia`, `desarrolla`, `consolida`, `entrega`, `retroalimenta`, `cierra` (actividades) son **estados internos**. Nunca aparecen como código en la prosa de la presentación al alumno.

### §0.12.1 Tabla de traducción de eslabones

| Estado interno | Traducciones posibles en prosa |
|---|---|
| `introduce` | "Esta sesión presenta por primera vez…" · "se toma contacto con…" · "se introduce la capacidad de…" |
| `desarrolla` | "Aquí se trabaja operativamente…" · "se practica…" · "se profundiza en…" |
| `aplica` | "Se utiliza en un contexto nuevo…" · "se integra con…" · "se aplica a…" |
| `evalúa` | "Se verifica el logro mediante…" · "se recoge evidencia de…" · "esta actividad permite comprobar inicialmente…" |

### §0.12.2 Tabla de traducción de estados de actividad

| Estado interno | Traducciones posibles en prosa |
|---|---|
| `aporta` | "esta sesión aporta insumos para…" · "proporciona criterios para…" |
| `inicia` | "hoy se abre la actividad…" · "se da inicio a…" · "primeros avances de…" |
| `desarrolla` | "hoy se trabaja el componente…" · "avance sustantivo de…" |
| `consolida` | "se revisa e integra lo producido…" · "cierre de coherencia de…" |
| `entrega` | "hoy es fecha de entrega de…" · "se recibe…" |
| `retroalimenta` | "se da retroalimentación formal sobre…" |
| `cierra` | "hoy se cierra formalmente…" · "conclusión de…" |
| Combinaciones (`entrega+retroalimenta+cierra`) | "se entrega, retroalimenta y cierra…" |

**Regla de ajuste contextual.** La traducción no es literal. Se elige la fórmula que mejor encaje en el párrafo.

**Regla de mención única.** Si un estado aparece varias veces, se traduce una vez en la sección donde se aborda; las demás van con referencia natural.

**Prohibición.** Ningún párrafo de la presentación al alumno reproduce los estados internos como código. En la guía docente, los estados pueden aparecer en tablas de conducción.

---

## Fase 2 — Decisiones operativas

### 2.1 Decisión de reforzamiento inicial (decisión propia de 03d)

**Aplicable solo en modo operativo.** En modo retrospectivo, el refuerzo no se activa.

El Brief (bloque H) sugiere un tipo de refuerzo y una duración. **03d decide si se activa y con qué alcance.**

#### Criterios de decisión

| Situación | Acción |
|---|---|
| Brief sugiere "ninguno" | No se activa reforzamiento. |
| Brief sugiere "repaso breve" | Se activa 3–7 min. Sin consumir tiempo útil de subtemas nuevos. |
| Brief sugiere "re-enseñanza focalizada" | Se activa 8–15 min. Consume tiempo útil. |
| Brief sugiere "nivelación de prerrequisito" | Se activa 10–20 min. Reduce proporcionalmente los minutos de los subtemas nuevos. |
| Brief sugiere "por peso o dependencia" | Se activa 5–15 min. Consume tiempo útil. |
| Brief indica "no aplica" | No se activa. |

#### Reglas de decisión

1. **Nunca actives reforzamiento si el Brief no lo sugiere.**
2. **El reforzamiento no desplaza al subtema de peso alto.** Si al restar el refuerzo el subtema principal queda con menos de 15 min, la skill **no ajusta por iniciativa propia**: reporta al usuario y pide indicación.
3. **Si el refuerzo dura > 8 min, tiene su propio slide y su propio checkpoint.**
4. **Fuente del contenido de refuerzo:**
   - Sesión anterior → reutiliza el Brief anterior o la mini-ficha K de la Ficha Teórica.
   - Prerrequisito de unidad previa → usa la mini-ficha K de la Ficha Teórica ya generada (03a produce hasta 3 proactivamente).
   - Por peso o dependencia → reutiliza material de la Ficha Teórica o la Ficha Normativa ya producida.
   - **Nunca inventes contenido de refuerzo.**

#### Si falta mini-ficha fuente

Si el Brief sugiere refuerzo (bloque H) pero la Ficha Teórica no incluye mini-ficha del prerrequisito correspondiente, 03d **no improvisa ni desactiva en silencio**. Reporta al usuario y ofrece tres opciones:

1. **Regenerar 03a** con solicitud explícita de mini-ficha.
2. **Activar refuerzo con contenido derivado del Brief anterior** (si está disponible).
3. **Desactivar el refuerzo** y continuar sin él, declarando la razón en la guía docente.

03d no decide por sí sola. Espera indicación del usuario.

#### Documentación obligatoria del refuerzo

- Slide de apertura en la presentación (título, unidad y subtema de origen, razón breve, idea clave, pregunta rápida).
- Checkpoint propio si dura > 8 min.
- Notas docentes completas (Intención, Tú dices, Pregunta, Respuesta esperada, Señal de transición, Mensaje clave, Error frecuente, No profundizar todavía).
- Renglón propio en la vista de conducción paralela.

### 2.2 Presupuesto de tiempo por subtema

Procedimiento con **distribución diferenciada por nivel** e **incorporación de actividades oficiales**.

**Fuentes de datos:**

- **Pesos por subtema** del Brief.
- **Niveles por concepto** de la Ficha Teórica.
- **Actividades oficiales vinculadas** del Brief (IDs, estados, productos parciales).
- **Actividad didáctica auxiliar** del Brief.

#### Regla fundamental

El tiempo útil se distribuye entre **cinco capas de conceptos** y **dos tipos de actividad**:

**Capas de conceptos:**
1. Núcleo
2. Panorama
3. Propedéutico
4. Contexto
5. Reservado (0%, solo transición)

**Tipos de actividad:**
1. **Actividad oficial** (del temario, con ID). Consume tiempo propio.
2. **Actividad didáctica auxiliar** (creada para enseñar). Consume tiempo propio.

#### Paso 0 — Restar reforzamiento y reservar tiempo para actividades

**Solo en modo operativo.**

```
Duración total de la clase
  − Tiempo de apertura (portada + agenda): 3–5 min
  − Bloque de reforzamiento inicial (según §2.1)
  − Tiempo reservado para actividades oficiales: [según Brief]
  − Tiempo reservado para actividad didáctica auxiliar: [según Brief]
  − Tiempo de cierre y evaluación: 8–12 min
  − Holgura operativa: 5–10% del total
  = Tiempo útil para conceptos (5 capas)
```

**Cómo calcular el tiempo de actividades oficiales:**

| Estado de la actividad en la sesión | Tiempo reservado |
|---|---|
| `aporta` | 0 min (no consume tiempo propio; el concepto asociado sí) |
| `inicia` | 5–10 min (consigna + primeros avances) |
| `desarrolla` | 10–20 min (trabajo sustantivo) |
| `consolida` | 5–10 min (revisión e integración) |
| `entrega` | 0–5 min (recibir entregas; el trabajo es fuera de clase) |
| `retroalimenta` | 5–10 min (feedback formal) |
| `cierra` | 0–3 min (registro) |
| Combinaciones (`entrega + retroalimenta + cierra`) | Sumar los tiempos |

**Cómo calcular el tiempo de actividad didáctica auxiliar:**

| Tipo | Tiempo |
|---|---|
| Ejercicio en clase | 10–20 min |
| Estudio de caso | 15–25 min |
| Discusión guiada | 10–15 min |
| Práctica de laboratorio | 20–40 min |

#### Paso 1 — Distribuir minutos por nivel

**Capa 1 — Núcleo (destino: 50–60% del tiempo útil):**

| Peso heredado | Minutos |
|---|---|
| Alto | 40–50% del tiempo útil |
| Medio | 25–35% |
| Bajo | 10–20% |

**Capa 2 — Panorama (destino: 12–18%):**

| Tipo | Minutos por concepto |
|---|---|
| Panorama técnico | 2–3 min por concepto (máximo) |
| Panorama conceptual | 1–2 min por concepto |

**Capa 3 — Propedéutico (destino: 8–12%):**

| Tipo | Minutos por concepto |
|---|---|
| Propedéutico con ejemplo | 2–3 min por concepto |
| Propedéutico conceptual | 1–2 min por concepto |

**Regla:** el tiempo de Propedéutico se agrupa en **un solo bloque** al final del desarrollo temático, no se intercala entre Núcleos.

**Capa 4 — Contexto (destino: 5–10%):**

| Tipo | Minutos por concepto |
|---|---|
| Contexto con mención propia | 1 min |
| Contexto absorbido en otro bloque | 0 min |

**Capa 5 — Reservado (0%):**

- No recibe minutos propios.
- Se menciona como **transición** al final del bloque correspondiente (30 seg a 1 min máximo).
- Se declara como remisión por nombre al capítulo o momento donde se retoma.

#### Regla de verificación

Antes de redactar, verifica:

1. Los Núcleo ocupan 50–60% del tiempo útil.
2. Los Panorama ocupan 12–18%.
3. Los Propedéutico ocupan 8–12%.
4. Los Contexto ocupan 5–10%.
5. Los Reservado no consumen tiempo útil.
6. **Las actividades oficiales consumen el tiempo reservado en el Paso 0.**
7. **La actividad didáctica auxiliar consume el tiempo reservado en el Paso 0.**
8. El Núcleo de peso alto tiene más minutos que cualquier Panorama o Propedéutico individual.
9. **Si hay una actividad oficial principal, recibe al menos 15 min.**

Si alguna falla, ajusta.

#### Regla especial: sesión sin actividades oficiales

Si el Brief declara `sin actividad oficial en esta sesión`, se omite la reserva de tiempo para actividades oficiales y la proporción de conceptos vuelve a Núcleo 60–70%.

#### Regla especial: muchas Panorama o Propedéutico

Si una sesión tiene más de 6 conceptos Panorama, se agrupan en un solo bloque panorámico.

Si tiene más de 4 Propedéutico, se agrupan en un solo bloque propedéutico con submención de cada uno (1–2 líneas por concepto).

#### Regla especial: alcance `literal con extensión propedéutica`

Si el Brief declara este alcance:
- Los Núcleo siguen siendo los del temario literal.
- Los Propedéutico reciben tiempo específico (8–12%).
- No hay Panorama (el alcance no es amplio).

#### Paso 2 — Traducir minutos a slides

| Tipo de slide | Minutos | Aplica a |
|---|---|---|
| Slide de teoría Núcleo | 8–12 min | Núcleo |
| Slide de aplicación Núcleo | 10–15 min | Núcleo con aplicación |
| Slide panorámico | 2–3 min | Panorama agrupados |
| Slide propedéutico | 2–3 min | Propedéutico agrupados |
| **Slide de actividad oficial** | **5–20 min** | **Actividad oficial** |
| **Slide de actividad didáctica auxiliar** | **10–25 min** | **Actividad auxiliar** |
| Mención de contexto | 0–1 min | Contexto |
| Transición a capítulo siguiente | 0.5–1 min | Reservado |

#### Paso 3 — Tabla obligatoria de presupuesto

| Subtema / Bloque | Nivel | Categoría reserva | Actividad oficial | Peso | Min | % útil | Slides |
|---|---|---|---|---|---|---|---|
| **Reforzamiento inicial** | Reforz. | — | — | — | [min] | [%] | [n] |
| [Concepto Núcleo 1] | Núcleo | — | — | Alto | [min] | [%] | [n] |
| [Concepto Núcleo 2] | Núcleo | — | — | Medio | [min] | [%] | [n] |
| [Concepto Panorama 1] | Panorama | — | — | Medio | [min] | [%] | [n] |
| [Concepto Propedéutico 1] | Propedéutico | — | — | — | [min] | [%] | [n] |
| [Concepto Contexto] | Contexto | — | — | — | [min] | [%] | [n] |
| **[Actividad oficial AI-01]** | — | — | **AI-01** | — | [min] | [%] | [n] |
| **[Actividad auxiliar]** | — | — | — | — | [min] | [%] | [n] |
| [Transición a capítulo] | Reservado | Continuidad explícita | — | — | [min] | [%] | [n] |
| **Total** | — | — | — | — | [min] | 100% | [n] |

**En modo retrospectivo**, la fila de reforzamiento se declara `no aplica` y los minutos son estimados.

### 2.3 Cálculo de checkpoints en hora real

**Aplicable solo en modo operativo.**

#### Procedimiento

1. Tomar hora real de inicio.
2. Acumular duraciones en orden (apertura → reforzamiento → conceptos por nivel → actividades → cierre).
3. Calcular hora exacta de cada checkpoint.
4. Calcular margen dinámico `M` y `2M` por checkpoint.

#### Cálculo del margen `M`

| Peso del bloque | Fórmula base |
|---|---|
| Bajo | `M = max(2, redondear(15% × duración))` |
| Medio | `M = max(3, redondear(20% × duración))` |
| Alto | `M = max(4, redondear(25% × duración))` |
| Panorama agrupado | `M = 2 min` |
| Propedéutico agrupado | `M = 2 min` |
| Actividad difícil de interrumpir | Tratar como alto, +1 min |
| Bloque < 6 min | `M = 1–2 min` |
| Clase total de 45–60 min | `M` ≤ 5–6 min salvo justificación |

Ajustes de realidad obligatorios:

- **Recuperabilidad:** +1 min si el bloque siguiente puede comprimirse.
- **Criticidad:** +1 min si el bloque contiene idea indispensable.
- **Dependencia:** no ampliar si el bloque siguiente depende del actual.
- **Cierre protegido:** ningún margen compromete síntesis, boleto ni tarea.

#### Simbología obligatoria

- 🔵 **(<M)** XTD → adelantado; extender, profundizar.
- 🟢 **(±M)** OK → en margen; continuar.
- 🟡 **(>M)** RES → retrasado; resumir, acortar interacción.
- 🔴 **(>2M)** SKP → retraso fuerte; saltar contenido secundario.

#### Regla de discreción visual

- **Presentación del alumno:** solo simbología compacta.
- **Guía del docente:** traducción operativa específica por checkpoint.

#### Regla para checkpoints en bloques Panorama y Propedéutico

Los bloques Panorama y Propedéutico agrupados **no requieren checkpoint propio** si duran menos de 5 min. Se controlan mediante el checkpoint del bloque siguiente.

#### Regla para checkpoints en actividades oficiales

Las actividades oficiales que duran más de 10 min **tienen su propio checkpoint**.

### 2.4 Auditoría 60/20/20 final

03d **cruza** la Ficha Teórica (categorías A + C) y la Ficha Normativa (categoría B + normas) para verificar la mezcla final:

| Categoría | Origen | Objetivo |
|---|---|---|
| Bibliografía académica (A) | Ficha Teórica, bloque C | ~60% ponderado |
| Web confiable (B) | Ficha Teórica bloque D + Ficha Normativa | ~20% |
| Científica / oficial / institucional (C) | Ficha Teórica C.bis + Ficha Normativa | ~20% |

**Cómo se cuenta cada concepto:**

| Nivel | Ponderación |
|---|---|
| Núcleo | 1.0 |
| Panorama | 0.5 |
| Propedéutico | 0.5 |
| Contexto | 0.5 |
| Reservado | 0.0 |

#### Regla de interpretación

- Las normas técnicas, reglamentos, normativa patrimonial, datos oficiales y documentos institucionales se cuentan **todos** en categoría C.
- Si una sesión es predominantemente normativa, la categoría C puede superar el 20% objetivo. En ese caso **no se reajustan** las fichas: se reporta la mezcla real y se justifica.
- Si la categoría A cae por debajo del 40% en una sesión predominantemente normativa, se declara advertencia visible en el Anexo D.

#### Regla de flexibilización por naturaleza de la sesión

Cuando el Brief declare un `Tipo de sesión` predominantemente normativo, técnico-reglamentario o de cálculo con NTC, la mezcla 60/20/20 se flexibiliza:

- El objetivo del 60% para bibliografía académica **no se exige**.
- La categoría C puede dominar la mezcla.
- Se reporta la mezcla real en el Anexo D con la justificación.
- Se emite advertencia visible solo si la **categoría A cae por debajo del 20%**.

Si la mezcla final se desvía ≥ 15 puntos del objetivo, **declara advertencia visible** en la auditoría.

**Regla:** los recursos visuales no entran en el cálculo 60/20/20. Se controlan aparte en el Anexo C.

**Regla:** las actividades oficiales no entran en el cálculo 60/20/20, que solo cuenta conceptos.

---

## Fase 3 — Composición de los archivos

### 3.1 Preparación de IDs NUMA

Antes de redactar, se asignan los IDs internos:

- `numa-slide-id` — único dentro de cada archivo.
- `numa-sync-id` — compartido entre slide alumno y slide docente correspondientes.

Formato:

- `alumno-[clave-breve]-[sufijo]`
- `profesor-[clave-breve]-[sufijo]`
- `sync-[clave-breve]-[sufijo]`

Reglas:

- Minúsculas, sin espacios.
- No depender del número de slide.
- No reutilizar IDs.
- Si se agrega slide entre otros, IDs nuevos solo para el nuevo.
- Si solo se corrige texto, no cambiar IDs.
- En modo retrospectivo, los IDs se generan igual.

**Nota:** los IDs NUMA (`alumno-...`, `sync-...`) son distintos de:
- IDs de necesidades visuales (`NVD-XX`) de 03.C-1 y, cuando aplique, IDs downstream (`ID_EXT`, `RGE-XX-YY`).
- IDs de actividad oficial (`AC-NN`, `AI-NN`) del Brief.

Tres sistemas independientes.

### 3.2 Enlaces internos

Formato:

```markdown
[texto visible](slide-id:[numa-slide-id-destino])
```

No usar `slide:N` ni numeración manual.

### 3.3 Estructura del archivo `presentacion_sesion_N.md`

Cada slide inicia con sus metadatos NUMA invisibles:

```markdown
<!-- numa-slide-id: alumno-[clave]-[sufijo] -->
<!-- numa-sync-id: sync-[clave]-[sufijo] -->
```

**Encabezado de metadatos obligatorio:**

```
- Presentación versión: v2.1
- Brief versión: [v2.7 / v2.8]
- Ficha Teórica versión: [v1.11 / v1.12]
- Ficha Normativa versión: v1.4
- Orquestador Visual versión: v1.2
- 03.C-3 versión/estado: [v0.1 BORRADOR / no aplica / versión posterior compatible]
- 03.C-2A versión: [v1.2 / no aplica]
- 03.C-2B versión: [v1.0 / no aplica]
- Evidencia generativa: [PASS + ID RGE + huella si aplica / no aplica]
- Doc Maestro versión: [v1.5 / v1.6]
- Modo de composición: [operativo / retrospectivo]
- Motivo del modo retrospectivo: [solo si aplica]
- Estado de integración visual: [completo / bloqueado / con omisiones no críticas autorizadas]
- Pesos por subtema aplicados: [lista]
- Distribución por nivel: [N Núcleo, N Panorama, N Propedéutico, N Contexto, N Reservado]
- Actividades oficiales vinculadas: [lista de IDs]
- Audiencia del producto: alumno
- Estado de la presentación: [completo / incompleto por diccionario huérfano]
- Fecha de composición: YYYY-MM-DD
```

**En modo retrospectivo:**

> **Modo retrospectivo:** [nota estándar + motivo].

Secciones en orden:

1. **Portada informativa** — asignatura, sesión, título, grupo, duración, hora, modalidad, docente, unidad, subtemas.
2. **Agenda ponderada** — bloque, **nivel**, **actividad oficial asociada**, peso, duración, hora de cierre.
3. **Reforzamiento inicial** (condicional, solo modo operativo).
4. **Pregunta detonadora.**
5. **Slides de teoría — Núcleo** (2–3 ideas por slide, con aplicación).
6. **Slides de teoría — Panorama** (agrupados; sin aplicación).
7. **Slides propedéuticos** (agrupados; definición + ejemplo + remisión).
8. **Slides de aplicación Núcleo.**
9. **Slide de actividad oficial**: presenta la actividad oficial del temario con consigna clara.
10. **Slide de actividad didáctica auxiliar**: presenta la actividad creada para enseñar el tema.
11. **Situación profesional o error frecuente.**
12. **Slide de aplicación concurrente** (condicional, si Brief bloque F declara materia de aplicación concurrente principal).
13. **Transición a capítulos posteriores** (Reservado con continuidad explícita).
14. **Síntesis.**
15. **Boleto de salida.**
16. **Tarea.**
17. **Fuentes.**
18. **Anexo A** — distribución del tiempo (hora, bloque, **nivel**, **actividad oficial**, contenido, modalidad, semáforo).
19. **Anexo B** — mapa de trazabilidad curricular (bloque, unidad, subtema, **nivel**, **actividad oficial**, evidencia, peso heredado).
20. **Anexo C** — integración y trazabilidad visual.
21. **Anexo D** — auditoría 60/20/20 final.
22. **Anexo E** — **actividades oficiales de la sesión**.
23. **Anexo F** — **Trazabilidad interna** (nuevo v2.0, ver §3.5).

#### Reglas de estructura de slides según tipo

**Slides Núcleo:**
- Desarrollo completo con teoría, ejemplo y aplicación si aplica.
- 2–3 ideas por slide.
- Referencias al pie.
- Apoyo visual si aplica.

**Slides Panorama:**
- Agrupados por familia conceptual.
- 1–2 ideas por slide.
- Sin aplicación práctica.
- Con mención explícita de que el desarrollo técnico corresponde a un capítulo posterior.

**Slides Propedéutico:**
- Agrupados en un solo bloque.
- 1–2 ideas por slide.
- Sin aplicación práctica.
- Sin ejercicios.
- Con remisión explícita al momento donde se retoma.

**Slide de actividad oficial:**
- Presenta la actividad oficial del temario con consigna clara.
- Incluye:
  - Nombre completo de la actividad (literal del temario) + ID entre paréntesis en primera mención.
  - Estado traducido a prosa (no como código).
  - Producto parcial esperado (si aplica).
  - Tiempo asignado.
  - Qué se entrega hoy y qué no.
- **Regla de audiencia:** el nombre completo precede al ID. No aparece el ID solo.

**Slide de actividad didáctica auxiliar:**
- Presenta la actividad creada para enseñar el tema.
- Incluye:
  - Nombre de la actividad.
  - Instrucción clara.
  - Tiempo asignado.
  - Producto esperado.
  - Modalidad (individual / equipo / grupal).

**Slide de aplicación concurrente:**
- Presenta la **Materia de aplicación concurrente principal** declarada en el Brief (bloque F).
- Incluye:
  - Nombre de la asignatura (nombre oficial).
  - Unidad o etapa donde aplica (si está declarada).
  - Concepto vinculado.
  - Cómo se aplica el concepto de esta sesión en esa materia.
  - Evidencia esperada (si aplica).
- **Condicional:** se incluye solo si el Brief declara una materia de aplicación concurrente principal (no `no aplica`).
- **Lenguaje neutral:** se usa "materia", "asignatura" o el nombre oficial. Solo se usa "taller" si es el nombre oficial de la asignatura.

**Transición a Reservado:**
- Un slide final de transición que menciona los conceptos Reservado **con continuidad explícita** por nombre y remite al capítulo siguiente.
- Los Reservado con categoría "Aplicación posterior" se mencionan con remisión al momento (práctica, instrumentos, etc.).
- Los Reservado con categoría "Fuera del curso" se mencionan solo si aportan contexto; si no, se omiten de la presentación.

### 3.3.bis Integración de recursos visuales resueltos

03.D integra únicamente recursos que hayan superado la compuerta §1.2.bis.

#### Marcador de integración en Markdown

Mientras el archivo siga siendo Markdown y no contenga el recurso embebido físicamente, se utiliza un marcador textual **de integración**, no un placeholder de producción pendiente.

| Procedencia | Formato de integración |
|---|---|
| **EXTERNO resuelto** | `(integrar aquí NVD-XX / ID_EXT — fuente: [localizador] — archivo/URL: [referencia persistente])` |
| **GENERATIVO resuelto** | `(integrar aquí NVD-XX / RGE-XX-YY — archivo generado: [ruta o referencia])` |
| **HÍBRIDO resuelto** | `(integrar aquí NVD-XX — componentes: [ID_EXT] + [RGE] — modo: [agrupación prescrita])` |
| **OMISIBLE_NO_CRÍTICO** | No insertar marcador en la presentación; registrar únicamente en Anexo C y guía docente. |

**Prohibido en v2.1:**

- `URL pendiente de verificar`;
- `pendiente de generación`;
- instrucciones de prompt;
- sustitución de un recurso por búsqueda improvisada;
- generación de un recurso desde 03.D;
- uso de un recurso con `RETURN`;
- uso de un recurso generativo sin PASS trazable;
- uso de un recurso externo distinto del validado por 03.C-3.

#### Reglas de explotación didáctica

03.D puede decidir:

- en qué slide autorizado aparece el recurso;
- tamaño relativo y posición;
- si se muestra completo o mediante zoom/recorte **solo cuando esa explotación esté permitida por el contrato**;
- secuencia de aparición;
- relación entre texto oral/proyectado y recurso;
- tiempo de observación;
- preguntas docentes de lectura visual que no añadan semántica disciplinar nueva.

03.D no puede convertir un `EXTERNO_PURO` en recurso anotado por iniciativa propia. Si 03.C-1 prescribe `EXTERNO_CON_ANOTACIÓN`, la anotación debe respetar exactamente la descripción contractual y no introducir contenido nuevo.

#### Anexo C — Registro de integración visual

El antiguo “apoyo visual sugerido” pasa a ser un registro contractual de integración:

| Slide | ID NVD | ID recurso | Procedencia | Función | Destino autorizado | Tratamiento | Archivo/URL | Fuente / atribución | Estado upstream | Estado integración |
|---|---|---|---|---|---|---|---|---|---|---|

Valores de `Estado integración`:

- `INTEGRADO`;
- `OMITIDO_NO_CRÍTICO_AUTORIZADO`;
- `BLOQUEADO_NO_INTEGRADO`.

Para recursos externos, conservar fuente, derechos y atribución heredados de 03.C-3.

Para recursos generativos, registrar ID RGE y referencia al `PASS`; si se dispone de `HUELLA_RGE_AUDITADO`, registrarla en la guía o Anexo C interno sin exponerla como contenido pedagógico.

#### En la guía docente

Cada recurso integrado lleva una nota operativa mínima:

- ID NVD;
- función didáctica;
- qué debe observar el alumno;
- pauta de explotación;
- procedencia;
- referencia del recurso;
- restricciones de uso;
- atribución, si aplica;
- advertencia de no sustitución cuando el contrato la exija.

03.D **no produce** `instrucciones_recursos_propios_sesion_N.md`. La especificación y producción de recursos generativos pertenece a 03.C-2A → 03.C-2B → 03Cbis.

### 3.4 Estructura del archivo `guia_docente_sesion_N.md`

Cada slide docente con equivalente en la presentación inicia con:

```markdown
<!-- numa-slide-id: profesor-[clave]-[sufijo] -->
<!-- numa-sync-id: sync-[clave]-[sufijo] -->
```

**Encabezado de metadatos obligatorio:**

```
- Guía versión: v2.1
- Brief versión: [v2.7 / v2.8]
- Ficha Teórica versión: [v1.11 / v1.12]
- Ficha Normativa versión: v1.4
- Orquestador Visual versión: v1.2
- 03.C-3 versión/estado: [v0.1 BORRADOR / no aplica / versión posterior compatible]
- 03.C-2A versión: [v1.2 / no aplica]
- 03.C-2B versión: [v1.0 / no aplica]
- Evidencia generativa: [PASS + ID RGE + huella si aplica / no aplica]
- Doc Maestro versión: [v1.5 / v1.6]
- Modo de composición: [operativo / retrospectivo]
- Motivo del modo retrospectivo: [solo si aplica]
- Estado de integración visual: [completo / bloqueado / con omisiones no críticas autorizadas]
- Distribución por nivel: [N Núcleo, N Panorama, N Propedéutico, N Contexto, N Reservado]
- Actividades oficiales vinculadas: [lista de IDs]
- Audiencia del producto: docente
- Fecha de composición: YYYY-MM-DD
```

Secciones:

1. **Encabezado** — modo presentador, docente, grupo, propósito real, hilo conductor, unidad, subtemas.

2. **Ficha de actividades oficiales.** Antes de la vista de conducción:

```markdown
## Actividades oficiales de la sesión

### [ID] — [Nombre de la actividad]

- **Tipo:** [conducción académica / independiente]
- **Estado en esta sesión:** [aporta / inicia / desarrolla / consolida / entrega / retroalimenta / cierra]
- **Producto parcial esperado:** [descripción o "no aplica"]
- **Qué se trabaja hoy:** [descripción]
- **Qué no se entrega todavía:** [descripción o "no aplica"]
- **Qué debe conservar el alumno:** [descripción]
- **Cuándo continúa:** [sesión o "cierra hoy"]
- **Cuándo se entrega:** [sesión o "ya entregado"]
```

**Regla de audiencia:** en la guía docente el estado puede aparecer como código porque el lector es el profesor.

Si la sesión no tiene actividades oficiales, se declara "Sin actividades oficiales en esta sesión".

3. **Incidencias y restricciones visuales** heredadas de 03.C-1 / 03.C-3 / rama generativa. No incluyen instrucciones de generación nuevas.

4. **Vista de conducción** — dos variantes.

   **Modo operativo:**

   | Hora real | Slide | Subtema | Nivel | Actividad oficial | Peso | Min | Acción docente breve | Checkpoint |
   |---|---|---|---|---|---|---|---|---|

   **Modo retrospectivo:**

   | Hora estimada | Bloque | Subtema | Nivel | Actividad oficial | Peso | Min estimados | Tema |
   |---|---|---|---|---|---|---|---|

5. **Notas por slide.**

   **Notas específicas por tipo:**

   - **Núcleo:** notas completas.
   - **Panorama:** notas breves.
   - **Propedéutico:** notas breves + remisión.
   - **Contexto:** sin nota propia.
   - **Reservado:** nota de transición.
   - **Actividad oficial:** nota con intención, consigna que se da al alumno, qué observar, qué no calificar todavía, señal de transición.
   - **Actividad didáctica auxiliar:** nota con intención, instrucción, respuesta esperada, errores frecuentes, cómo vincular con la actividad oficial.
   - **Aplicación concurrente:** nota con intención, materia de aplicación concurrente principal, cómo se conecta el concepto con esa materia, pregunta para el alumno.

   **En slides con placeholder:** agregar la advertencia correspondiente.

### 3.5 Anexo F — Trazabilidad interna de la presentación (nuevo v2.0)

**Ubicación:** al final de la presentación al alumno, después del Anexo E.

**Propósito.** Es la **única excepción** a la regla de audiencia en la presentación. Está claramente marcado como material interno, no dirigido al alumno.

**Estructura:**

```markdown
## Anexo F — Trazabilidad interna

> Material interno. No forma parte de la proyección al alumno.

### Diccionario de códigos

| Código | Tipo | Nombre legible | Fuente |
|---|---|---|---|
| C1 | Competencia | ... | Brief bloque B |
| AI-04 | Actividad oficial | ... | Brief bloque G |
| H11 | Recurso visual | ... | Brief bloque E |

### Eslabones de competencia cubiertos por esta sesión

- C1 = introduce
- C2 = desarrolla

### Estados de actividad oficial

- AI-01 = inicia+desarrolla
- AI-04 = aporta
```

**Reglas del Anexo F:**

- Obligatorio desde v2.0 si la presentación menciona al menos un código interno.
- Única sección de la presentación donde los códigos pueden aparecer sin expansión en prosa.
- Claramente delimitado por la nota "Material interno".
- No reemplaza al diccionario canónico de skills upstream.

---

## Fase 4 — Auditoría final

### Trazabilidad con insumos

- ¿El contenido coincide con el Brief?
- ¿Los pesos por subtema coinciden **literalmente** con los del Brief?
- ¿El `Modo de composición` coincide con el del Brief?
- ¿Los **niveles** de los conceptos coinciden con la Ficha Teórica?
- ¿Las **categorías de reserva** coinciden?
- ¿Los **fundamentos de exclusión** de los Fuera del curso están declarados?
- ¿El `Alcance conceptual` del Brief se refleja en la distribución por nivel?
- ¿Los **Propedéutico** tienen remisión explícita al momento donde se retoman?
- ¿La **articulación curricular** de la presentación coincide con el Brief bloque F y con la Ficha Teórica bloque L?
- ¿El **slide de aplicación concurrente** usa lenguaje neutral?
- ¿Los IDs de actividad oficial coinciden con los de §7.c del Doc Maestro?
- ¿El estado de la actividad coincide con §8?
- ¿La distinción actividad oficial / auxiliar es clara?
- ¿El producto parcial esperado coincide con el Brief?
- ¿La normativa coincide con la Ficha Normativa sin inventar claves?
- ¿Cada recurso visual proviene de una NVD de 03.C-1 y de un handoff downstream admisible, sin sustitución ni URL inventada?
- ¿El refuerzo inicial está justificado y sustentado?

### Coherencia interna

- **Modo operativo:**
  - ¿Los checkpoints usan hora real?
  - ¿Cada checkpoint está en slide propio?
  - ¿La simbología es compacta?
  - ¿Los márgenes M y 2M son dinámicos?
- **Modo retrospectivo:**
  - ¿Se declara el modo y el motivo?
  - ¿No hay checkpoints operativos?
  - ¿La vista es un análisis retrospectivo?
- **Distribución por nivel y actividades:**
  - ¿Los Núcleo ocupan 50–60%?
  - ¿Los Panorama ocupan 12–18%?
  - ¿Los Propedéutico ocupan 8–12%?
  - ¿Los Contexto ocupan 5–10%?
  - ¿Los Reservado no consumen tiempo útil?
  - ¿Las actividades oficiales consumen el tiempo reservado?
  - ¿La actividad auxiliar consume el tiempo reservado?
  - ¿La actividad oficial principal recibe al menos 15 min?
  - ¿Cada slide declara su nivel?
  - ¿Los Núcleo tienen estructura de slide completo?
  - ¿Los Panorama no tienen aplicación práctica?
  - ¿Los Contexto no tienen slide propio?
  - ¿Los Propedéutico tienen remisión explícita?
- **Recursos visuales:**
  - ¿Cada recurso usado corresponde a una NVD con destino autorizado para el producto?
  - ¿Cada EXTERNO es exactamente el recurso validado por 03.C-3?
  - ¿Cada GENERATIVO tiene `PASS` trazable y producción asociada?
  - ¿Cada HÍBRIDO conserva la función y agrupación prescritas?
  - ¿Ninguna V1/V2 destinada al producto quedó sin satisfacer?
  - ¿El Anexo C registra NVD, recurso, procedencia, referencia y estado de integración?
  - ¿La guía docente conserva las restricciones y la atribución cuando aplica?
  - ¿No existen placeholders de búsqueda o generación pendiente?
- **Aplicación concurrente:**
  - ¿El slide usa lenguaje neutral (sin "taller" salvo nombre oficial)?
  - ¿Se activa solo si el Brief declara la materia?

### Legibilidad editorial (nuevo v2.0)

- ¿La presentación declara `Audiencia del producto: alumno` en el encabezado?
- ¿La guía docente declara `Audiencia del producto: docente` en el encabezado?
- ¿Se construyó el diccionario local antes de redactar la presentación?
- ¿El diccionario local cubre todos los códigos mencionados en los insumos?
- ¿Hay algún código huérfano? Si sí, ¿se detuvo la producción y se reportó?
- ¿Ningún código interno aparece en la presentación sin expansión en prosa?
- ¿La primera mención de cada código lleva nombre legible + código entre paréntesis?
- ¿Las menciones posteriores llevan solo el nombre legible?
- ¿Los estados de eslabón y de actividad están traducidos a prosa?
- ¿Ningún párrafo de la presentación reproduce el estado interno como código?
- ¿El Anexo F incluye el diccionario local?
- ¿El Anexo F está claramente marcado como material interno?
- ¿En tablas de referencia interna (Agenda, Anexo A/B/E) el código va acompañado del nombre?
- ¿La guía docente expande los códigos en primera mención?
- ¿El estado de la presentación está declarado (`completo` / `incompleto`)?

### Formato NUMA

- ¿Cada slide tiene `numa-slide-id` único?
- ¿Los slides correspondientes comparten `numa-sync-id`?
- ¿Los enlaces internos usan `slide-id:`?
- ¿Los metadatos aparecen como comentarios HTML invisibles?

### Mezcla documental

- ¿El Anexo D reporta la auditoría 60/20/20 con ponderación diferenciada?
- ¿Los recursos visuales y las actividades oficiales quedaron fuera?
- ¿Hay advertencia visible si desviación ≥ 15 puntos?

### Cierre

- ¿Se entregan los dos archivos separados?
- ¿El reforzamiento inicial tiene slide, checkpoint y notas?
- ¿La vista de conducción incluye nivel, peso y minutos?
- ¿La tarea prepara el siguiente capítulo?

Si alguna verificación falla, no ajustes los insumos: repórtalo al usuario.

---

## Fase 5 — Entrega

- **Archivos Markdown**:
  - `presentacion_sesion_N.md`
  - `guia_docente_sesion_N.md`
- Entregar ambos archivos por separado.
- No mezclar.
- No numerar slides manualmente.
- No usar enlaces por número fijo.

### Encabezado de metadatos obligatorio

- Presentación versión: v2.1
- Guía versión: v2.1
- Brief versión: [v2.7 / v2.8]
- Ficha Teórica versión: [v1.11 / v1.12]
- Ficha Normativa versión: v1.4
- Orquestador Visual versión: v1.2
- 03.C-3 versión/estado: [v0.1 BORRADOR / no aplica / versión posterior compatible]
- 03.C-2A versión: [v1.2 / no aplica]
- 03.C-2B versión: [v1.0 / no aplica]
- Evidencia generativa: [PASS + ID RGE + huella si aplica / no aplica]
- Doc Maestro versión: [v1.5 / v1.6]
- **Modo de composición:** [operativo / retrospectivo]
- **Motivo del modo retrospectivo:** [si aplica]
- **Recursos de elaboración propia pendientes:** [N]
- **Distribución por nivel:** [N Núcleo, N Panorama, N Propedéutico, N Contexto, N Reservado]
- **Actividades oficiales vinculadas:** [lista de IDs]
- **Audiencia del producto:** [alumno / docente]
- **Estado de la presentación:** [completo / incompleto por diccionario huérfano]
- Pesos por subtema aplicados: [lista]
- Fecha de composición: YYYY-MM-DD

---

## Reglas de consistencia

### Reglas generales

1. **No investigues, no busques, no clasifiques.**
2. **Los pesos por subtema vienen del Brief (bloque B).**
3. **La única decisión propia es el refuerzo inicial (solo modo operativo).**
4. **Nunca inventes fuentes, URLs, licencias, claves de norma, citas ni páginas.**
5. **Respeta licencia Flexible por defecto.**
6. **Respeta referencia exacta.**
7. **Los márgenes M y 2M son dinámicos.**
8. **Ningún checkpoint invade un slide de contenido.**
9. **La presentación no muestra instrucciones operativas largas.**
10. **La guía no repite la bibliografía completa.**
11. **Si el refuerzo deja sin tiempo al subtema alto, reporta al usuario.**
12. **Si el Brief sugiere "ninguno" en refuerzo, no lo actives.**
13. **Si la mezcla 60/20/20 se desvía ≥ 15 puntos, emite advertencia visible.**
14. **Prohibido `N/D` en la ponderación.**
15. **No se recalcula el peso.**
16. **El modo retrospectivo no bloquea.**
17. **El modo retrospectivo se declara explícitamente.**
18. **Cada recurso visual usado debe superar la compuerta de admisibilidad §1.2.bis.**
19. **El ID NVD se hereda literalmente de 03.C-1; los IDs downstream (`ID_EXT`, `RGE`) se conservan sin renombrar.**
20. **03.D no busca, diseña, audita semánticamente ni genera recursos visuales.**
20.a. **Un recurso solo puede usarse en un producto cuyo `destino` esté autorizado por 03.C-1.**
20.b. **Un EXTERNO no puede sustituirse por otro recurso sin nueva validación de 03.C-3.**
20.c. **Un GENERATIVO con `RETURN` o sin PASS no puede integrarse.**
20.d. **La composición no puede modificar la semántica, whitelist, blacklist, relaciones o causalidad de un RGE aprobado.**
20.e. **Una V1/V2 no satisfecha bloquea la composición completa del producto al que está destinada.**
20.f. **Una V3/V4 pendiente solo puede omitirse con aceptación explícita upstream como no crítica.**
20.g. **Si la corrección exige cambiar objetivo, función, procedencia, familia, tratamiento, agrupación o criterio de satisfacción, escalar a 03.C-1.**
20.h. **Si el problema pertenece al diseño generativo, devolver a 03.C-2A y exigir nueva auditoría 03.C-2B.**
20.i. **Si el problema pertenece a selección, derechos o identidad de un recurso externo, devolver a 03.C-3.**

### Reglas de niveles

21. **Los niveles vienen de la Ficha Teórica, bloque B.**
22. **La distribución de minutos respeta la proporción por nivel:**
    - Núcleo: 50–60% del tiempo útil.
    - Panorama: 12–18%.
    - Propedéutico: 8–12%.
    - Contexto: 5–10%.
    - Reservado: 0% (solo transición).
23. **Cada slide declara su nivel.**
24. **Los Panorama no tienen aplicación práctica.**
25. **Los Contexto no tienen slide propio.**
26. **Los Reservado solo aparecen en el slide de transición final.**

### Reglas del nivel Propedéutico

27. **Los Propedéutico se agrupan en un solo bloque.**
28. **Los Propedéutico no tienen aplicación práctica.**
29. **Los Propedéutico no tienen ejercicios.**
30. **Cada Propedéutico tiene remisión explícita al momento donde se retoma.**
31. **El bloque Propedéutico ocupa entre 8–12% del tiempo útil.**
32. **Si hay más de 4 Propedéutico, se agrupan con submención.**

### Reglas de las categorías de reserva

33. **Cada Reservado hereda su categoría de la Ficha Teórica.**
34. **Los Reservado con "Continuidad explícita" se mencionan con remisión al capítulo siguiente.**
35. **Los Reservado con "Aplicación posterior" se mencionan con remisión al momento.**
36. **Los Reservado con "Fuera del curso" se mencionan solo si aportan contexto.**

### Reglas de actividades oficiales

37. **El Brief declara las actividades oficiales vinculadas con ID y estado.** 03d las hereda literalmente. No las inventa, no las renombra, no las modifica.
38. **La actividad oficial y la actividad didáctica auxiliar se distinguen explícitamente.**
39. **La actividad oficial tiene su propio slide** cuando el estado es `inicia`, `desarrolla`, `consolida` o combinaciones con `entrega`.
40. **La actividad auxiliar tiene su propio slide** cuando se realiza en clase.
41. **Cada actividad oficial activa recibe tiempo explícito en la agenda.**
42. **Si hay 2+ actividades oficiales activas, la principal recibe al menos 15 min.**
43. **El producto parcial esperado se declara en el slide y en la guía.**
44. **La guía docente incluye una ficha por actividad oficial** con los 7 campos.
45. **La vista de conducción paralela incluye columna `Actividad oficial`.**
46. **La continuidad conceptual posterior se declara en la transición final.**

### Reglas de articulación curricular

47. **El slide "Conexión con taller" se renombra a "Slide de aplicación concurrente".**
48. **El slide de aplicación concurrente usa lenguaje neutral.**
49. **El slide de aplicación concurrente se activa solo si el Brief (bloque F) declara una materia de aplicación concurrente principal (no `no aplica`).**
50. **El slide de aplicación concurrente hereda del Brief (bloque F) y de la Ficha Teórica (bloque L).** No se inventa, no se renombra, no se modifica.
51. **La articulación prioritaria de la Ficha Teórica (bloque L) no se duplica en el slide.** El slide solo presenta la materia de aplicación concurrente principal. La articulación prioritaria completa vive en el Anexo B.
52. **No se usa el término "taller" como categoría universal.**
53. **Si el Doc Maestro o el Brief no declaran articulación, el slide se omite y se declara `sin aplicación concurrente documentada`.**

### Reglas de fundamento de exclusión

54. **Los conceptos Fuera del curso tienen fundamento declarado** (Alcance curricular / Nivel / Especialidad).
55. **Los conceptos Fuera del curso no se desarrollan en la presentación.** Se declaran en el bloque M del capítulo de 03e.

### Reglas de audiencia (nuevas v2.0)

56. **La presentación al alumno sigue política estricta de audiencia:** ningún código interno sin expansión en prosa, salvo en el Anexo F.
57. **La guía docente sigue política flexible:** códigos permitidos con expansión ligera en primera mención.
58. **El archivo auxiliar de instrucciones no está sujeto a política de audiencia.**
59. **La primera mención de un código en la presentación lleva nombre legible + código entre paréntesis.**
60. **Las menciones posteriores del mismo código llevan solo el nombre legible.**
61. **Los estados de eslabón y de actividad no aparecen como código en la presentación.**
62. **Los estados internos se traducen a prosa según §0.12.**
63. **En tablas de referencia interna** (Agenda ponderada, Anexo A, Anexo B, Anexo E), la columna "Actividad oficial" puede conservar el ID si va acompañado del nombre legible.
64. **La política aplica a todos los elementos del producto:** títulos, cuerpo, pies de figura, encabezados de tabla, notas al margen.

### Reglas del diccionario de expansión local (nuevas v2.0)

65. **Antes de redactar la presentación, 03.D construye el diccionario local.**
66. **El diccionario se construye a partir del Brief, las fichas y el Doc Maestro.**
67. **Si un código aparece en los insumos y no puede resolverse, se detiene la producción y se reporta.**
68. **No se inventan nombres legibles para códigos huérfanos.**
69. **El diccionario se incluye como Anexo F de la presentación.**
70. **El diccionario no reemplaza al diccionario canónico de skills upstream.**

### Reglas de traducción de estados (nuevas v2.0)

71. **Los estados de eslabón y de actividad se traducen a prosa según §0.12.**
72. **La traducción se ajusta al contexto del párrafo.**
73. **En la guía docente, los estados pueden aparecer en tablas de conducción** (columnas `Nivel` y `Actividad oficial`).

### Reglas de emisión (nuevas v2.0)

74. **Si el diccionario tiene códigos huérfanos, la presentación no se emite como completa.** Se emite como `incompleto por diccionario huérfano`, se declara al usuario y se espera resolución.
75. **Si la presentación contiene códigos internos sin expandir en la prosa, se corrige antes de emitir.**

---

## Archivos que produce la skill 03d

| Archivo | Contenido | Condición |
|---|---|---|
| `presentacion_sesion_N.md` | Presentación para proyectar | Siempre que no exista bloqueo contractual |
| `guia_docente_sesion_N.md` | Guía del docente modo presentador | Siempre que no exista bloqueo contractual |

---

## Criterio final de calidad

La skill 03d cumple si:

### Criterios de legibilidad editorial (nuevos v2.0)

- **la presentación declara audiencia `alumno`**;
- **la guía docente declara audiencia `docente`**;
- **se construyó el diccionario local antes de redactar**;
- **el diccionario local cubre todos los códigos de los insumos**;
- **ningún código huérfano bloquea la emisión sin ser reportado**;
- **ningún código interno aparece en la presentación sin expandir en prosa**;
- **la primera mención de cada código en la presentación lleva nombre legible + código entre paréntesis**;
- **las menciones posteriores llevan solo el nombre legible**;
- **los estados internos están traducidos a prosa en la presentación**;
- **ninguna reproducción de `C1=introduce` ni equivalente aparece en la presentación**;
- **el Anexo F es la única excepción y está precedido por el diccionario local**;
- **en tablas de referencia interna el código va acompañado del nombre**;
- **la guía docente expande los códigos en primera mención**;
- **el estado de la presentación está declarado (`completo` / `incompleto`)**;
- **el archivo auxiliar no está sujeto a política de audiencia**.

### Criterios de articulación curricular

- **el slide se llama "Slide de aplicación concurrente"**;
- **el slide se activa solo si el Brief declara materia concurrente**;
- **el lenguaje es neutral (sin "taller" salvo nombre oficial)**;
- **el slide hereda del Brief (bloque F) y de la Ficha Teórica (bloque L)**;
- **no se inventan ni renombran relaciones**;
- **si no hay articulación, se declara `sin aplicación concurrente documentada`**.

### Criterios de actividades oficiales

- **los IDs de actividad oficial coinciden con §7.c del Doc Maestro**;
- **los estados coinciden con §8 del Doc Maestro**;
- **la actividad oficial y la auxiliar se distinguen explícitamente**;
- **cada actividad oficial activa tiene su propio slide**;
- **la actividad auxiliar tiene su propio slide**;
- **cada actividad oficial recibe tiempo explícito en la agenda**;
- **la actividad oficial principal recibe al menos 15 min**;
- **el producto parcial esperado se declara**;
- **la guía docente incluye la ficha por actividad oficial con 7 campos**;
- **la vista de conducción paralela incluye columna `Actividad oficial`**;
- **la continuidad conceptual posterior se declara en la transición final**.

### Criterios de distribución por nivel

- **los Núcleo ocupan 50–60% del tiempo útil**;
- **los Panorama ocupan 12–18%**;
- **los Propedéutico ocupan 8–12%**;
- **los Contexto ocupan 5–10%**;
- **los Reservado no consumen tiempo útil**;
- **cada slide declara su nivel**;
- **los Núcleo tienen estructura de slide completo**;
- **los Panorama no tienen aplicación práctica**;
- **los Contexto no tienen slide propio**;
- **los Propedéutico tienen remisión explícita**.

### Criterios del nivel Propedéutico

- **los Propedéutico están en un bloque propio**;
- **los Propedéutico no tienen aplicación práctica ni ejercicios**;
- **cada Propedéutico tiene remisión explícita**;
- **el bloque Propedéutico ocupa 8–12% del tiempo útil**.

### Criterios de las categorías de reserva

- **cada Reservado tiene su categoría heredada**;
- **los Reservado con Continuidad explícita se mencionan con remisión al capítulo**;
- **los Reservado con Aplicación posterior se mencionan con remisión al momento**;
- **los Reservado con Fuera del curso se mencionan solo si aportan contexto**.

### Criterios generales

- el alumno entiende qué aprende y para qué;
- el docente puede conducir sin leer un discurso;
- los pesos por subtema heredados del Brief están reflejados;
- no aparece `N/D` en ninguna ponderación;
- el `Modo de composición` está declarado;
- en modo retrospectivo, se aplican las reglas especiales;
- cada recurso visual usado supera la compuerta de admisibilidad visual;
- el Anexo C registra NVD, ID de recurso, procedencia, destino, estado y referencia;
- la guía docente conserva función, restricciones y atribución cuando aplica;
- la teoría viene de la Ficha Teórica sin inventar;
- la normativa viene de la Ficha Normativa sin inventar;
- los recursos visuales provienen del subsistema 03.C sin reinterpretación ni sustitución silenciosa;
- el refuerzo inicial está decidido y documentado;
- el formato NUMA está listo para modo dual;
- los IDs NUMA son estables;
- la mezcla 60/20/20 está auditada con ponderación diferenciada;
- la trazabilidad con Doc Maestro y Brief es verificable;
- se entregan los archivos separados sin mezcla.

---

## Ejemplo mínimo de aplicación (nuevo v2.0)

### En la presentación — slide de actividad oficial

**Antes (incorrecto, v1.9):**

> **AI-01** — estado: desarrolla. Producto parcial: sección de unidades del mapa conceptual.

**Después (correcto, v2.0):**

> **Mapa conceptual sobre escalas, unidades de medida e instrumentos (AI-01)**
> Hoy se trabaja la sección de unidades de medida del mapa conceptual.
> Lo que se entrega hoy: avance de la sección.
> Lo que continúa: consolidación en la siguiente sesión.

### En la presentación — síntesis

**Antes (incorrecto, v1.9):**

> C1=introduce; C2=desarrolla. Se refuerza U1. Se aplica en AI-04.

**Después (correcto, v2.0):**

> Esta sesión introduce la capacidad de distinguir escenarios naturales y urbanos (C1) y desarrolla operativamente la capacidad de valorar esos escenarios con criterios ambientales, socioculturales y económicos (C2). Se apoya en la Unidad 1 — Introducción a la topografía y aporta criterios al Proyecto final de levantamiento topográfico (AI-04).

### En el Anexo F — excepción

```markdown
## Anexo F — Trazabilidad interna

> Material interno. No forma parte de la proyección al alumno.

### Diccionario de códigos

| Código | Tipo | Nombre legible |
|---|---|---|
| C1 | Competencia | Distinguir escenarios naturales y urbanos |
| C2 | Competencia | Valorar escenarios con criterios ambientales, socioculturales y económicos |
| AI-01 | Actividad oficial | Mapa conceptual sobre escalas, unidades de medida e instrumentos |
| AI-04 | Actividad oficial | Proyecto final de levantamiento topográfico |

### Eslabones cubiertos
- C1 = introduce
- C2 = desarrolla

### Estados de actividad
- AI-01 = inicia+desarrolla
- AI-04 = aporta
```

### En la guía docente — expansión ligera permitida

**Correcto (guía docente):**

> La actividad AI-04 (Proyecto final de levantamiento topográfico) recibe criterios de esta sesión. En la siguiente sesión se trabajará el avance correspondiente.

El código AI-04 se usa solo porque la primera mención llevó el nombre legible entre paréntesis.

---

## Changelog de consolidación v1.9 → v2.0

**Propósito:** garantizar que la presentación al alumno salga con lenguaje natural, sin códigos internos del pipeline visibles, sin modificar el resto del flujo.

**Contenido normativo preservado de v1.9 (sin cambios):**

- Propósito.
- Cuándo activar.
- Estructura del flujo.
- Fase 1 completa (§1.1–§1.5).
- Fase 2 completa (§2.1–§2.4).
- Fase 3 §3.1–§3.4.
- Fase 4 auditoría (con verificaciones nuevas añadidas).
- Fase 5 entrega (con encabezados actualizados).
- Reglas 1–55.
- Criterios finales existentes.
- Archivos producidos.

**Contenido nuevo en v2.0:**

- **§0.10 Regla de audiencia por producto**: política diferenciada para presentación (estricta), guía docente (flexible) y archivo auxiliar (libre).
- **§0.11 Diccionario de expansión local**: procedimiento para construir la tabla código → nombre legible; regla del diccionario huérfano; consumo de Brief v2.8 y Ficha Teórica v1.12.
- **§0.12 Traducción de estados internos a prosa**: dos tablas de conversión contextual (eslabones y estados de actividad).
- **§3.5 Anexo F — Trazabilidad interna**: excepción única a la política de audiencia en la presentación.
- **Bloque de metadatos de la presentación** ampliado con `Audiencia del producto: alumno` y `Estado de la presentación`.
- **Bloque de metadatos de la guía** ampliado con `Audiencia del producto: docente`.
- **Reglas 56–75**: audiencia, diccionario, traducción de estados, emisión.
- **Verificaciones nuevas en checklist**: legibilidad editorial.
- **Criterios nuevos en criterio final**: legibilidad editorial.
- **Ejemplo mínimo de aplicación** (§ final): antes/después por tipo de producto.
- **Changelog v1.9 → v2.0**.

**Cambios de empaquetado:**

- Se añadieron §0.10, §0.11, §0.12 antes de Fase 2.
- Se añadió §3.5 al final de Fase 3.
- Se añadió Anexo F a la estructura de la presentación (sección 23).
- Se añadieron reglas 56–75 sin renumerar 1–55.
- Se amplió el checklist con un bloque nuevo (legibilidad editorial).
- Se amplió el criterio final con un bloque nuevo (legibilidad editorial).
- Se ampliaron los encabezados de metadatos de presentación y guía.

**Actualizaciones de compatibilidad:**

- Brief consumidor: **v2.7 o v2.8** (v2.8 preferido por el campo `Eslabones de competencia cubiertos`).
- Ficha Teórica consumidora: **v1.11 o v1.12** (v1.12 preferida por el campo `Suficiencia para eslabón`).
- Ficha Normativa consumidora: v1.4.
- estrategia visual 03.C-1 consumidora: v1.8.
- Doc Maestro consumidor: v1.5 o v1.6.
- **No requiere cambios upstream.** La política de audiencia vive solo en 03.D.

---

**Guía de uso del flujo completo:** consulta `guia_uso_flujo_skills.md`.

---

## Changelog de consolidación v2.0 → v2.1

**Propósito:** alinear 03.D con la arquitectura visual vigente y convertirla en consumidor downstream de contratos visuales resueltos, eliminando responsabilidades visuales que ya pertenecen a 03.C.

### Contenido normativo preservado de v2.0

Se preservan sin cambio de propósito:

- composición dual presentación + guía;
- modos operativo y retrospectivo;
- ponderación por subtema;
- distribución por 5 niveles;
- actividades oficiales y actividad auxiliar;
- articulación curricular;
- refuerzo inicial como única decisión pedagógica propia;
- cálculo de checkpoints;
- auditoría 60/20/20;
- IDs NUMA;
- política de audiencia;
- diccionario de expansión local;
- traducción de estados internos a prosa;
- Anexo F de trazabilidad interna.

### Contenido nuevo en v2.1

1. **Interfaz visual nueva:** se elimina `estrategia visual 03.C-1 v1.8` como entrada contractual vigente.
2. **Consumo de 03.C-1 v1.2** como fuente canónica de NVD, destino, función, procedencia y criterio de satisfacción.
3. **Consumo de 03.C-3** para recursos externos resueltos, preservando identidad, fuente, derechos y atribución.
4. **Consumo de rama generativa** únicamente con `PASS` de 03.C-2B y producción trazable.
5. **Compuerta visual de entrada (§1.2.bis)** con estados `ADMISIBLE_EXTERNO`, `ADMISIBLE_GENERATIVO`, `ADMISIBLE_HÍBRIDO`, `OMISIBLE_NO_CRÍTICO`, `BLOQUEO_VISUAL`.
6. **Principio de integración sin reinterpretación.**
7. **Control de destino:** un recurso solo puede aparecer en presentación/guía si 03.C-1 autorizó ese destino.
8. **Regla de no sustitución externa:** un recurso validado por 03.C-3 no se reemplaza downstream sin nueva validación.
9. **Regla de PASS generativo:** `RETURN` o ausencia de PASS bloquea integración.
10. **Anexo C reformulado** como registro de integración y trazabilidad visual.
11. **Marcadores de integración** sustituyen a placeholders de búsqueda/generación pendiente.
12. **Se elimina `instrucciones_recursos_propios_sesion_N.md`** de las salidas de 03.D.
13. **Protocolo de retorno por propiedad contractual:**
    - estrategia → 03.C-1;
    - diseño generativo → 03.C-2A + nueva 03.C-2B;
    - recurso externo → 03.C-3.
14. **NVD V1/V2 no satisfecha bloquea composición completa** del producto correspondiente.
15. **NVD V3/V4 pendiente** solo puede omitirse si upstream la acepta expresamente como no crítica.

### Compatibilidad v2.1

- Brief: **v2.7 o v2.8**.
- Ficha Teórica: **v1.11 o v1.12**.
- Ficha Normativa: **v1.4**.
- Doc Maestro: **v1.5 o v1.6**.
- 03.C-1: **v1.2 obligatorio**.
- 03.C-2A: **v1.2** cuando exista componente generativo.
- 03.C-2B: **v1.0** cuando exista componente generativo.
- 03.C-3: **v0.1 BORRADOR** como interfaz provisional mientras no exista versión estable posterior compatible.
- 03Cbis: se exige producción trazable al RGE aprobado; esta v2.1 no presume compatibilidad de una salida que no pueda demostrar la cadena `RGE → PASS → producción`.

**Regla de migración:** una `estrategia visual 03.C-1 v1.8` legado no satisface por sí sola el contrato visual de 03.D v2.1.

---

**Guía de uso del flujo completo:** consulta `guia_uso_flujo_skills_v4.0.md`.
