---
name: 05-compilador-libro
description: Compila los capitulos aprobados de 03.E en el libro unificado de la asignatura y genera el reporte editorial de compilacion.
stage_id: "05"
version: "1.1"
status: stable
---

# Skill: Compilador de Libro de Materia (05) — v1.1

## Posición en el flujo

Esta skill es un **post-procesador editorial**. No forma parte de la cadena de diseño y generación de una sesión, pero sí pertenece al ecosistema completo como etapa posterior a la producción de capítulos 03.E.

Su posición recomendada es:

```text
03.E v2.4
   ↓
04.A v2.5
   ↓
04.B v1.2   [si existen correcciones ejecutables]
   ↓
capítulo final
   ↓
[05] Compilador
   ↓
libro_[asignatura].md
```

La relación con 04.A/04.B es **condicional**:

- un capítulo puede compilarse si ya está editorialmente cerrado;
- si existe auditoría 04.A, 05 puede usar su resultado como evidencia adicional de estado;
- si 04.B ejecutó correcciones, 05 compila la versión corregida;
- 05 **no exige** ejecutar 04.B cuando no existen propuestas aplicables;
- 05 **no reaudita** trazabilidad, nivel, legibilidad ni fidelidad visual.

Su función es **post-procesar capítulos ya generados por 03.E v2.4+** y compilarlos en un libro de la materia. Opera sobre productos terminados o explícitamente compilables con advertencias, no sobre capítulos en construcción.

```text
03.E v2.4+ (por capítulo) ───► capitulo_1_[slug].md
                               capitulo_2_[slug].md
                               capitulo_3_[slug].md
                               ...
                                      │
                                      ▼
                             [05] Compilador
                                      │
                                      ▼
                             libro_[asignatura].md
```

**Cuándo se invoca:**
- Al final del curso, cuando todos los capítulos están generados.
- En cualquier momento intermedio, para compilar una versión parcial.
- Después de corregir un capítulo, para recompilar.
- Para verificar coherencia del conjunto sin modificar capítulos individuales.

**Cuándo NO se invoca:**
- Si los capítulos están en construcción.
- Si algún capítulo tiene estado `BLOQUEADO_PARA_COMPILACIÓN`.
- Si existe un bloqueo visual contractual crítico no resuelto en un capítulo.
- Si hay errores estructurales graves que deben resolverse antes.

---

## Propósito

Esta skill toma todos los `capitulo_N_[slug].md` de una asignatura y produce:

1. **`libro_[asignatura].md`** — el libro completo, con portada, índice general,
   prólogo, capítulos compilados, referencias consolidadas y apéndices.

2. **`reporte_compilacion_[asignatura].md`** — un reporte de verificación con:
   - Capítulos compilados (lista).
   - Capítulos faltantes (huecos en la numeración).
   - Referencias cruzadas verificadas.
   - Referencias rotas o huérfanas.
   - Inconsistencias detectadas.
   - Advertencias de compilación.

**No genera capítulos nuevos.** No investiga. No compone. Solo compila lo que existe
y reporta la coherencia del conjunto.

---

## Cuándo activar esta skill

Actívala cuando el usuario:

- Pida "compilar el libro de [asignatura]", "juntar los capítulos", "armar el libro
  de la materia".
- Quiera verificar la coherencia de referencias cruzadas entre capítulos.
- Quiera una versión parcial del libro (solo los capítulos disponibles).
- Quiera regenerar el libro tras corregir un capítulo.

No la actives si:
- No existe la carpeta de la asignatura.
- No hay al menos 2 capítulos generados.
- Los capítulos tienen errores estructurales graves sin resolver.
- Algún capítulo está marcado `BLOQUEADO_PARA_COMPILACIÓN`.
- Un capítulo declara bloqueo visual contractual crítico pendiente.

---

## Qué NO es esta skill

| No es | Porque |
|---|---|
| Generadora de capítulos | Eso es 03.E |
| Auditora de capítulos | Eso corresponde a 04.A; 05 no reaudita capítulos |
| Correctora de errores | Solo reporta; 04.B corrige cuando existe propuesta compatible |
| Fusionadora de contenido | Compila, no reescribe |

**Sí es:** el compilador que junta los capítulos, verifica la coherencia del conjunto
y produce el libro de la materia.

---

## Estructura del libro compilado

```
libro_[asignatura].md
├── Portada
├── Nota preliminar (opcional)
├── Índice general
├── Prólogo (opcional, breve)
├── Capítulo 1 — [nombre]
├── Capítulo 2 — [nombre]
├── Capítulo 3 — [nombre]
├── ...
├── Referencias consolidadas
├── Índice de capítulos por unidad del programa
├── Glosario consolidado (opcional)
└── Nota final de compilación
```

---

## Estructura de la skill: 7 fases

```
Fase 1 — Verificación de insumos
Fase 2 — Descubrimiento y ordenamiento de capítulos
Fase 3 — Verificación de coherencia estructural
Fase 4 — Verificación de referencias cruzadas
Fase 5 — Construcción de portada, índice y prólogo
Fase 6 — Compilación del libro
Fase 7 — Verificación final y reporte
```

---

## Fase 1 — Verificación de insumos

### 1.1 Carpeta de asignatura

Confirma que existe una carpeta con:

- Al menos 2 archivos `capitulo_N_[slug].md`.
- Nombres que sigan la convención `capitulo_[N]_[slug].md`.

Si la carpeta no existe → detente.

Si hay menos de 2 capítulos → reporta al usuario y pregunta si quiere generar un libro
parcial.

### 1.2 Datos de la asignatura

Del `documento_maestro_[asignatura].md` (o directamente del usuario), extrae:

- Nombre completo de la asignatura.
- Clave.
- Carrera.
- Cuatrimestre.
- Institución.
- Docente.
- Periodo.
- Nombre del libro (por defecto: "[Asignatura] — Libro de Estudio").

Si no existe el Doc Maestro, pregunta al usuario los datos mínimos.

### 1.2.bis Compatibilidad de capítulos

La versión recomendada de entrada es **03.E v2.4+**.

Se aceptan capítulos anteriores únicamente si:
- conservan una estructura equivalente;
- no contienen estados visuales pendientes incompatibles con el libro final;
- sus recursos y atribuciones pueden preservarse sin reinterpretación.

05 no convierte automáticamente un capítulo legado al contrato 03.E v2.4.

### 1.2.ter Estado de compilabilidad por capítulo

Antes de compilar, clasifica cada capítulo:

| Estado | Criterio |
|---|---|
| `APTO_PARA_COMPILAR` | Estructura completa, sin bloqueos críticos, recursos y referencias preservables |
| `COMPILABLE_CON_ADVERTENCIAS` | Tiene incidencias menores o no críticas, pero puede incluirse sin alterar contenido |
| `BLOQUEADO_PARA_COMPILACIÓN` | Tiene errores estructurales graves, bloqueo visual contractual crítico o evidencia insuficiente para preservar integridad |

05 no corrige el capítulo para cambiar de estado. Solo reporta el motivo.

### 1.3 Modo de compilación

Pregunta al usuario:

| Modo | Descripción |
|---|---|
| **Completo** | Compila todos los capítulos disponibles en orden numérico |
| **Parcial** | Compila solo los capítulos indicados (ej. capítulos 1–5) |
| **Rango por unidad** | Compila solo los capítulos de una unidad del programa |

Por defecto: **Completo**.

### 1.4 Modo de estilo de compilación

Pregunta al usuario:

| Modo | Descripción |
|---|---|
| **Estricto** | Detiene la compilación si encuentra referencias cruzadas rotas |
| **Flexible** | Compila con advertencias; el usuario decide después si corrige |

Por defecto: **Flexible**.

---

## Fase 2 — Descubrimiento y ordenamiento de capítulos

### 2.1 Descubrimiento

Lista todos los archivos que sigan la convención `capitulo_N_[slug].md` en la carpeta
de la asignatura.

### 2.2 Detección de huecos

Verifica que la numeración sea consecutiva:

- Si hay capítulos 1, 2, 4, 5 → hueco en el 3.
- Si hay capítulos 1, 2, 3, 5 → hueco en el 4.
- Reporta los huecos al usuario.

**Los huecos no bloquean la compilación** en modo Flexible. Se reportan y se compila
con los capítulos disponibles.

### 2.3 Detección de duplicados

Verifica que no haya dos capítulos con el mismo número:

- `capitulo_3_[slug].md` y `capitulo_3_[slug-v2].md` → duplicado.

Reporta los duplicados y pide al usuario que elija cuál usar.

### 2.4 Ordenamiento

Ordena los capítulos por número ascendente.

Si algún capítulo no tiene número claro en el nombre, se ordena al final y se reporta.

### 2.5 Resultado

Produce una lista ordenada de capítulos a compilar:

| # | Archivo | Capítulo | Slug |
|---|---|---|---|
| 1 | `capitulo_01_[slug].md` | 1 | [slug] |
| 2 | `capitulo_02_[slug].md` | 2 | [slug] |
| ... | ... | ... | ... |

---

## Fase 3 — Verificación de coherencia estructural

### 3.1 Verificación de bloques obligatorios

Por cada capítulo, verifica que tenga los bloques mínimos:

- **A. Primera hoja** con: Capítulo, Colección, Sesión de origen, Unidad, Subtemas,
  Pesos, Alcance, Modo, Distribución por nivel, Capítulos previos y posteriores.
- **B. Tabla de contenido.**
- **C. Introducción.**
- **D. Objetivos.**
- **E. Desarrollo temático** con subsecciones por nivel.
- **M. Advertencias y lagunas.**
- **Anexo Z**, si el capítulo lo incorpora como zona interna de trazabilidad; debe preservarse sin fusionarlo con contenido para alumno.

Si un capítulo no tiene alguno de estos bloques, se reporta como **capítulo
incompleto**.

### 3.2 Verificación de primera hoja

Verifica que la primera hoja de cada capítulo tenga:

- `Capítulo: [N]`
- `Colección: [nombre del libro]`
- `Sesión de origen: [N]`
- `Unidad del programa: [X — nombre]`
- `Subtemas oficiales cubiertos: [X.Y, X.Z]`
- `Pesos por subtema aplicados`
- `Alcance conceptual del subtema`
- `Modo de composición`
- `Distribución por nivel`
- `Capítulos previos en la colección`
- `Capítulos posteriores en la colección`
- `Estado del capítulo` o campo equivalente, si existe
- `Estado de integración visual` o campo equivalente, si existe

Si falta alguno, se reporta.

### 3.3 Verificación de menciones de "sesión"

Verifica que el **cuerpo** del capítulo (excluyendo la primera hoja) **no mencione la
palabra "sesión"**.

Si aparece, se reporta como **inconsistencia de formato**.

### 3.4 Verificación de nombres de capítulo

Verifica que la `Colección` sea consistente entre todos los capítulos (mismo nombre
del libro).

Si hay discrepancias, se reporta.

### 3.5 Resultado

Produce una tabla de coherencia estructural:

| Capítulo | Bloques OK | Primera hoja OK | Menciones "sesión" | Colección consistente |
|---|---|---|---|---|
| 1 | ✅ | ✅ | ✅ | ✅ |
| 2 | ⚠️ Falta M | ✅ | ✅ | ✅ |
| ... | ... | ... | ... | ... |


### 3.6 Verificación de integridad visual y assets

Por cada capítulo 03.E v2.4+, verificar:

- que las figuras referenciadas tengan ruta/archivo/localizador resoluble;
- que los pies de figura existan y se mantengan asociados a la figura correcta;
- que fuente, licencia y atribución externas se preserven cuando correspondan;
- que referencias internas a `NVD`, `ID_EXT`, `RGE` o PASS permanezcan únicamente en zonas internas donde sean legítimas;
- que el `Anexo Z` se preserve literalmente como zona interna;
- que no exista un marcador de recurso crítico pendiente incompatible con un capítulo completo;
- que cualquier recurso híbrido conserve sus componentes y relación documental.

05 no valida de nuevo la semántica del recurso. Solo verifica que la compilación pueda **preservar** lo que el capítulo ya declara.

### 3.7 Clasificación de compilabilidad

Después de verificar estructura y assets, asigna uno de los estados de §1.2.ter.

Reglas mínimas:

- falta estructural grave → `BLOQUEADO_PARA_COMPILACIÓN`;
- asset crítico faltante → `BLOQUEADO_PARA_COMPILACIÓN`;
- bloqueo visual contractual crítico declarado → `BLOQUEADO_PARA_COMPILACIÓN`;
- advertencia editorial menor → `COMPILABLE_CON_ADVERTENCIAS`;
- sin incidencias críticas → `APTO_PARA_COMPILAR`.

En modo Flexible, solo se permite continuar con `APTO_PARA_COMPILAR` y `COMPILABLE_CON_ADVERTENCIAS`.


---

## Fase 4 — Verificación de referencias cruzadas

Esta es la fase crítica de la compilación. Verifica que las referencias entre
capítulos sean coherentes.

### 4.1 Extracción de referencias

Por cada capítulo, extrae todas las referencias a otros capítulos. Las referencias
tienen la forma:

- "en el capítulo «[nombre]»"
- "el capítulo «[nombre]»"
- "se revisó en «[nombre]»"
- "se verá en «[nombre]»"
- Cualquier mención entre comillas angulares `«...»` que corresponda a un capítulo.

### 4.2 Verificación de existencia

Para cada referencia extraída, verifica que exista un capítulo con ese nombre en la
colección.

**Tipos de referencias:**

| Tipo | Verificación |
|---|---|
| **Referencia a capítulo previo** | Debe existir en la colección |
| **Referencia a capítulo posterior** | Debe existir en la colección |
| **Referencia a capítulo faltante** | Si el capítulo no existe, se reporta como referencia huérfana |

### 4.3 Verificación de simetría

Para cada capítulo N, verifica que:

- Los capítulos que declara como "previos" efectivamente existen y aparecen antes.
- Los capítulos que declara como "posteriores" efectivamente existen y aparecen
  después.
- La simetría es bidireccional: si el capítulo 5 dice "viene después del capítulo 3",
  el capítulo 3 debe decir "seguido por el capítulo 5".

### 4.4 Detección de referencias huérfanas

Una referencia huérfana es una mención a un capítulo que no existe en la colección.

Ejemplos:
- "El concepto se profundiza en el capítulo «Software topográfico»" → si no existe
  `capitulo_XX_software-topografico.md`, es huérfana.
- "Como se vio en el capítulo «Coordenadas geográficas»" → si no existe, es huérfana.

**Manejo:**
- En modo **Estricto**: detiene la compilación y reporta.
- En modo **Flexible**: reporta como advertencia y continúa.

### 4.5 Detección de referencias rotas por nombre

Una referencia rota es una mención a un capítulo cuyo nombre no coincide exactamente
con ninguno de la colección.

Ejemplos:
- "El capítulo «Sistemas de representación»" → si el capítulo se llama "Sistemas de
  representación topográfica", hay inconsistencia de nombre.
- "El capítulo «Ventilación cruzada»" → si el capítulo se llama "Estrategias de
  ventilación", hay inconsistencia.

**Manejo:** se reporta como inconsistencia de nomenclatura con sugerencia de
unificación.

### 4.6 Verificación de índice de capítulos

Verifica que el campo `Capítulos previos en la colección` y `Capítulos posteriores en
la colección` de cada primera hoja coincida con la realidad de la colección.

Ejemplo:
- Capítulo 5 declara previos: [1, 2, 3, 4].
- Verifica que efectivamente existan los capítulos 1, 2, 3, 4.
- Verifica que el capítulo 4 declare como posterior al capítulo 5.

### 4.7 Resultado

Produce una tabla de referencias cruzadas:

| Capítulo origen | Referencia | Capítulo destino | Estado |
|---|---|---|---|
| Cap. 2 | "capítulo «Escalas»" | Cap. 3 | ✅ Válida |
| Cap. 2 | "capítulo «Coordenadas UTM»" | No existe | ⚠️ Huérfana |
| Cap. 4 | "capítulo «Ventilación cruzada»" | Cap. 7 (nombre: "Estrategias de ventilación") | ⚠️ Nombre inconsistente |
| Cap. 5 | previos [1, 2, 3, 4] | Existen 1, 2, 3, 4 | ✅ Simétrica |

---

## Fase 5 — Construcción de portada, índice y prólogo

### 5.1 Portada del libro

Construye la portada:

```markdown
# [Nombre de la asignatura]

## Libro de Estudio

**Clave:** [LIAXXXX]
**Carrera:** [Licenciatura en Ingeniero-Arquitecto]
**Cuatrimestre:** [X]
**Institución:** [nombre]
**Docente:** [nombre]
**Periodo:** [YYYY-YYYY]
**Edición:** [v1.0 — fecha de compilación]

---

**Colección:** [nombre del libro, si aplica]

**Capítulos incluidos:** [N]
**Páginas totales estimadas:** [N]
**Fecha de compilación:** [YYYY-MM-DD]

---

*Este libro fue compilado a partir de los capítulos generados por el sistema de
diseño de curso. Los capítulos son autocontenidos y pueden leerse en orden o de
forma independiente.*
```

### 5.2 Nota preliminar (opcional)

Si el usuario la solicita, se agrega una nota preliminar breve (150–250 palabras) que
explique:

- El propósito del libro.
- Cómo se generó.
- Cómo se organiza.
- Cómo se recomienda leerlo.

### 5.3 Índice general

Construye el índice general con los capítulos compilados y sus secciones principales.

```markdown
## Índice general

**Capítulo 1 — [nombre]**
- 1.1 [sección]
- 1.2 [sección]
- ...

**Capítulo 2 — [nombre]**
- 2.1 [sección]
- 2.2 [sección]
- ...

...
```

Los enlaces internos deben funcionar en Markdown estándar.

### 5.4 Índice por unidad del programa (opcional)

Si el usuario lo solicita, se agrega un índice alternativo que agrupa los capítulos
por unidad del programa oficial.

```markdown
## Índice por unidad del programa

**Unidad 1 — [nombre]**
- Capítulo 1 — [nombre]
- Capítulo 2 — [nombre]
- Capítulo 3 — [nombre]

**Unidad 2 — [nombre]**
- Capítulo 4 — [nombre]
- ...
```

### 5.5 Prólogo (opcional)

Si el usuario lo solicita, se agrega un prólogo breve (300–500 palabras) que
contextualice el libro en la formación del Ingeniero-Arquitecto.

**Regla:** el prólogo no inventa contenido académico. Solo presenta el libro.

---

## Fase 6 — Compilación del libro

### 6.1 Estructura del libro compilado

```markdown
# [Nombre de la asignatura] — Libro de Estudio

[Portada]

[Nota preliminar (opcional)]

[Índice general]

[Índice por unidad (opcional)]

[Prólogo (opcional)]

---

# Capítulo 1 — [nombre]

[Contenido completo del capítulo 1]

---

# Capítulo 2 — [nombre]

[Contenido completo del capítulo 2]

---

...

---

# Referencias consolidadas

[Lista de fuentes de todos los capítulos, ordenadas alfabéticamente por autor]

---

# Índice de capítulos por unidad del programa

[Tabla resumen]

---

# Glosario consolidado (opcional)

[Términos de todos los capítulos, ordenados alfabéticamente con referencia al
capítulo donde aparecen]

---

# Nota final de compilación

**Total de capítulos:** [N]
**Capítulos faltantes:** [lista o "ninguno"]
**Referencias cruzadas verificadas:** [N]
**Referencias huérfanas:** [N]
**Fecha de compilación:** [YYYY-MM-DD]

*Este libro fue compilado automáticamente. Si detectas alguna inconsistencia,
repórtala al docente.*
```

### 6.2 Reglas de compilación

1. **Cada capítulo empieza en una nueva página.** En Markdown, se usa un salto de
   sección (`---`).

2. **El título de cada capítulo se eleva a nivel H1.** Si en el capítulo original
   está en H1, se mantiene. Si está en H2, se eleva.

3. **Los enlaces internos de cada capítulo se preservan.** Si un capítulo tiene un
   enlace a su propia sección, sigue funcionando.

4. **Las referencias cruzadas a otros capítulos se preservan tal cual.** No se
   convierten en enlaces automáticamente, salvo que el usuario lo solicite.

5. **Los pies de figura se preservan.** Cada capítulo mantiene su numeración de
   figuras y su asociación con el recurso visual correspondiente.

6. **Las citas bibliográficas se preservan.** Se recompilan en la sección de
   Referencias consolidadas.

7. **Los modos retrospectivos se preservan.** Un capítulo retrospectivo mantiene su
   nota de modo en su primera hoja.

8. **Los assets visuales se preservan.** No se renombran, sustituyen ni reubican de forma que rompa rutas o referencias.

9. **El Anexo Z se preserva íntegro.** No se consolida con otros anexos Z ni se mueve al final global del libro.

10. **Las atribuciones y licencias se preservan.** No se eliminan durante consolidación editorial.

11. **No se modifica la trazabilidad visual interna.** IDs NVD/RGE/PASS permanecen solo donde ya eran legítimos.

### 6.3 Consolidación de referencias

Extrae todas las fuentes citadas en todos los capítulos y consolídalas en una sola
sección al final del libro.

**Reglas:**

- Eliminar duplicados documentales reales.
- Ordenar alfabéticamente por autor o criterio bibliográfico dominante del corpus.
- **No renumerar las citas internas de cada capítulo.**
- La sección consolidada funciona como bibliografía global deduplicada, no como sistema nuevo de numeración.
- Si varios capítulos usan numeraciones locales distintas para la misma fuente, conservar las citas locales y reportar la duplicidad en el informe.
- No alterar DOI, URL, autoría, fecha, edición ni localizador por razones de uniformidad estética.

**Regla de seguridad:** 05 no reescribe sistemas de citación internos. Solo consolida una vista bibliográfica global.

### 6.4 Consolidación de glosario (opcional)

Si el usuario lo solicita, se construye un glosario consolidado:

```markdown
# Glosario consolidado

**A**
- **Altimetría:** [definición] — Cap. 2.
- **Área:** [definición] — Cap. 3.

**B**
- **Base:** [definición] — Cap. 5.
```

**Regla:** solo se incluyen términos que aparecen en el glosario de algún capítulo.

---

## Fase 7 — Verificación final y reporte

### 7.1 Verificación final

Antes de entregar, verifica:

- ¿El libro compilado tiene portada, índice y todos los capítulos?
- ¿Los capítulos están en orden ascendente?
- ¿Cada capítulo mantiene su primera hoja completa?
- ¿Cada capítulo tiene estado de compilabilidad válido?
- ¿No se incluyó ningún capítulo `BLOQUEADO_PARA_COMPILACIÓN`?
- ¿Las referencias cruzadas válidas siguen funcionando?
- ¿Las referencias huérfanas están reportadas?
- ¿La sección de referencias consolidadas incluye todas las fuentes?
- ¿Los assets visuales siguen resolviendo después de compilar?
- ¿Los pies de figura permanecen asociados a sus recursos?
- ¿Las atribuciones/licencias se preservaron?
- ¿Los Anexos Z permanecen íntegros por capítulo?
- ¿El glosario consolidado incluye todos los términos (si aplica)?
- ¿La nota final declara el total de capítulos y las advertencias?

### 7.2 Reporte de compilación

Produce el reporte:

```markdown
# Reporte de compilación — [Asignatura]

**Fecha:** [YYYY-MM-DD]
**Modo:** [completo / parcial / rango por unidad]
**Modo de estilo:** [estricto / flexible]

## Capítulos compilados

| # | Archivo | Capítulo | Título | Estado compilabilidad |
|---|---|---|---|---|
| 1 | capitulo_01_[slug].md | 1 | [título] | APTO_PARA_COMPILAR |
| 2 | capitulo_02_[slug].md | 2 | [título] | COMPILABLE_CON_ADVERTENCIAS |
| ... | ... | ... | ... |

**Total:** [N]

## Capítulos faltantes

| # | Capítulo esperado | Estado |
|---|---|---|
| 3 | capitulo_03_[slug].md | No encontrado |
| 7 | capitulo_07_[slug].md | No encontrado |

**Total faltantes:** [N]

## Coherencia estructural

| Capítulo | Bloques | Primera hoja | Menciones "sesión" | Colección |
|---|---|---|---|---|
| 1 | ✅ | ✅ | ✅ | ✅ |
| 2 | ⚠️ Falta M | ✅ | ✅ | ✅ |
| ... | ... | ... | ... | ... |


## Integridad visual y assets

| Capítulo | Assets | Pies | Atribución/licencia | Anexo Z | Estado |
|---|---|---|---|---|---|
| 1 | ✅ | ✅ | ✅ | ✅ | APTO |
| 2 | ⚠️ | ✅ | ✅ | ✅ | ADVERTENCIA |

## Referencias cruzadas

### Válidas

| Cap. origen | Referencia | Cap. destino |
|---|---|---|
| 2 | "capítulo «Escalas»" | 3 |
| ... | ... | ... |

**Total válidas:** [N]

### Huérfanas

| Cap. origen | Referencia | Estado |
|---|---|---|
| 2 | "capítulo «Coordenadas UTM»" | Capítulo no existe |
| ... | ... | ... |

**Total huérfanas:** [N]

### Rotas por nombre

| Cap. origen | Referencia | Cap. similar | Sugerencia |
|---|---|---|---|
| 4 | "capítulo «Ventilación cruzada»" | Cap. 7 "Estrategias de ventilación" | Unificar nombre |
| ... | ... | ... | ... |

**Total rotas por nombre:** [N]

## Inconsistencias adicionales

- [Lista de inconsistencias no clasificadas arriba]

## Advertencias

- [Lista de advertencias]

## Recomendaciones

1. [Correcciones sugeridas al usuario]
2. [...]

## Decisión

- ✅ **Libro compilado** — todos los capítulos incluidos están `APTO_PARA_COMPILAR`
- ⚠️ **Libro compilado con advertencias** — existe al menos un `COMPILABLE_CON_ADVERTENCIAS`
- ❌ **Compilación detenida** — existe al menos un capítulo `BLOQUEADO_PARA_COMPILACIÓN` dentro del conjunto solicitado

---

*Reporte generado automáticamente por la skill 05 — Compilador de Libro.*
```

### 7.3 Entrega

- **Archivo principal:** `libro_[asignatura].md`
- **Archivo de reporte:** `reporte_compilacion_[asignatura].md`
- **Opcional:** `libro_[asignatura].pdf` (si el usuario lo solicita)

---

## Reglas de operación de la skill 05

1. **No genera capítulos nuevos.** Solo compila lo que existe.
2. **No corrige errores en los capítulos.** Solo los reporta.
3. **No reescribe el contenido.** Solo junta y ordena.
4. **No inventa capítulos faltantes.** Reporta los huecos.
5. **No cambia la numeración de las figuras de cada capítulo.**
6. **No cambia la numeración de las citas de cada capítulo.** La consolidación
   mantiene la numeración original y agrega una numeración global.
7. **No elimina advertencias.** Las advertencias de cada capítulo se preservan.
8. **No modifica los modos retrospectivos.** Los capítulos retrospectivos mantienen
   su nota.
9. **No fusiona capítulos.** Cada capítulo es una unidad independiente.
10. **No omite capítulos silenciosamente.** Si un capítulo no existe, se reporta.
11. **No reaudita capítulos.** No sustituye 04.A.
12. **No implementa correcciones.** No sustituye 04.B.
13. **No revalida RGE ni recursos externos.** Confía en el estado heredado del capítulo.
14. **No modifica Anexo Z.**
15. **No elimina atribuciones, licencias ni fuentes visuales.**
16. **No recompone imágenes ni cambia rutas sin preservar resolubilidad.**
17. **No incluye silenciosamente capítulos bloqueados.**

---

## Contrato de salida

```markdown
# Libro de Estudio — [Asignatura]

## Portada
## Nota preliminar (opcional)
## Índice general
## Índice por unidad (opcional)
## Prólogo (opcional)

## Capítulo 1 — [nombre]
## Capítulo 2 — [nombre]
## Capítulo 3 — [nombre]
## ...

## Referencias consolidadas
## Índice de capítulos por unidad del programa
## Glosario consolidado (opcional)
## Nota final de compilación
```

**Archivos que produce:**

| Archivo | Contenido | Frecuencia |
|---|---|---|
| `libro_[asignatura].md` | Libro compilado | Bajo demanda |
| `reporte_compilacion_[asignatura].md` | Reporte de verificación | Bajo demanda |
| `libro_[asignatura].pdf` | Versión PDF para distribuir (opcional) | Bajo demanda |

---

## Checklist interno antes de entregar

### Verificaciones de compilación

- ¿La carpeta de asignatura existe?
- ¿Hay al menos 2 capítulos generados?
- ¿Los capítulos siguen la convención `capitulo_N_[slug].md`?
- ¿Se detectaron huecos en la numeración?
- ¿Se detectaron duplicados?
- ¿Los capítulos están ordenados por número ascendente?
- ¿Cada capítulo tiene los bloques mínimos (A, B, C, D, E, M)?
- ¿Cada capítulo tiene la primera hoja completa?
- ¿Cada capítulo tiene estado `APTO_PARA_COMPILAR` o `COMPILABLE_CON_ADVERTENCIAS`?
- ¿Se excluyeron/bloquearon correctamente los capítulos `BLOQUEADO_PARA_COMPILACIÓN`?
- ¿El cuerpo de cada capítulo NO menciona la palabra "sesión"?
- ¿La colección es consistente entre todos los capítulos?

### Verificaciones visuales y de assets

- ¿Cada figura mantiene su recurso asociado?
- ¿Todas las rutas o referencias visuales siguen siendo resolubles?
- ¿Se preservaron pies de figura?
- ¿Se preservaron fuente, licencia y atribución?
- ¿Cada Anexo Z permanece dentro de su capítulo y sin modificaciones?
- ¿No se movieron IDs internos visuales a zonas visibles para el alumno?
- ¿No se perdió ningún asset crítico durante la compilación?

### Verificaciones de referencias cruzadas

- ¿Se extrajeron todas las referencias a otros capítulos?
- ¿Todas las referencias apuntan a capítulos existentes?
- ¿Se detectaron referencias huérfanas?
- ¿Se detectaron referencias rotas por nombre?
- ¿Se verificó la simetría de "previos" y "posteriores"?
- ¿Se reportaron las referencias problemáticas?

### Verificaciones del libro compilado

- ¿La portada está completa?
- ¿El índice general incluye todos los capítulos?
- ¿El índice por unidad está presente (si aplica)?
- ¿El prólogo está presente (si aplica)?
- ¿Las referencias consolidadas incluyen todas las fuentes?
- ¿La consolidación bibliográfica evitó renumerar citas internas de los capítulos?
- ¿El glosario consolidado incluye todos los términos (si aplica)?
- ¿La nota final declara el total de capítulos y las advertencias?

### Verificaciones del reporte

- ¿El reporte incluye la lista de capítulos compilados?
- ¿El reporte incluye los capítulos faltantes?
- ¿El reporte incluye la coherencia estructural?
- ¿El reporte incluye las referencias cruzadas (válidas, huérfanas, rotas)?
- ¿El reporte incluye las recomendaciones?
- ¿El reporte declara la decisión final?

---

## Criterio final de calidad

La skill 05 cumple si:

- el libro compilado incluye portada, índice general, todos los capítulos disponibles
  en orden, referencias consolidadas y nota final;
- los capítulos se preservan sin modificaciones (salvo elevación a H1 del título);
- las referencias cruzadas válidas se identifican;
- las referencias huérfanas se reportan;
- las referencias rotas por nombre se reportan con sugerencia de unificación;
- los huecos en la numeración se reportan;
- los duplicados se detectan;
- la coherencia estructural de cada capítulo se verifica;
- cada capítulo tiene estado de compilabilidad explícito;
- ningún capítulo bloqueado se incluye silenciosamente;
- assets, pies de figura, atribuciones y licencias se preservan;
- los Anexos Z se preservan por capítulo;
- la bibliografía global se consolida sin reescribir la numeración interna;
- el reporte de compilación es completo y trazable;
- no se inventan capítulos faltantes;
- no se corrigen errores silenciosamente;
- no se fusionan capítulos;
- el libro puede leerse de forma continua o por capítulos independientes;
- el índice general funciona en Markdown y en PDF.


---

## Changelog de consolidación v1.0 → v1.1

**Propósito:** actualizar la skill 05 para el flujo vigente y para capítulos 03.E v2.4+, sin convertirla en auditora ni correctora.

### Cambios principales

1. Posición en flujo actualizada:
   `03.E → 04.A → 04.B (si aplica) → 05`.
2. Compatibilidad explícita con 03.E v2.4+.
3. Estados de compilabilidad:
   - `APTO_PARA_COMPILAR`
   - `COMPILABLE_CON_ADVERTENCIAS`
   - `BLOQUEADO_PARA_COMPILACIÓN`
4. Verificación de integridad visual y assets.
5. Preservación explícita de Anexo Z.
6. Preservación de fuente, licencia y atribución.
7. Prohibición de incluir capítulos con bloqueo visual contractual crítico.
8. Política bibliográfica corregida: consolidación global sin renumerar citas internas.
9. Reporte ampliado con estado de compilabilidad e integridad visual.
10. Reglas explícitas de no reauditar, no corregir y no revalidar contratos visuales.

### Frontera funcional

05:
- compila;
- ordena;
- verifica coherencia del conjunto;
- preserva.

05 no:
- audita académicamente;
- implementa mejoras;
- redefine visuales;
- corrige capítulos;
- selecciona recursos;
- revalida RGE.


---

**Esta skill es un post-procesador del ecosistema de diseño de curso.** Se puede invocar
cuando existan al menos dos capítulos 03.E compilables, ya sea al cierre del curso o en una compilación parcial.
