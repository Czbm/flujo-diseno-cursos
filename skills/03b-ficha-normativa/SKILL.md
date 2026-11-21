---
name: 03b-ficha-normativa
description: Desarrolla la Ficha Normativa de una sesion integrando marco normativo, contexto regional y restricciones tecnicas aplicables.
stage_id: "03.B"
version: "1.4"
status: stable
---

# Skill: Ficha Normativa (03b) — Versión cerrada v1.4

## Posición en el flujo

Esta skill alimenta a **03d (Composición Dual)** y a **03e (Capítulo de Libro
Autónomo)**. Su salida —la Ficha Normativa— es consumida directamente en la Fase 1 y
Fase 2 de 03d, y en la Fase 2 de 03e para:

- verificar tipo de proyecto, zona patrimonial y ámbito normativo;
- cruzar la mezcla documental 60/20/20 (categoría C);
- alimentar slides técnicos y de aplicación;
- reportar lagunas y advertencias al docente;
- aportar el contexto normativo regional que el capítulo de libro cita;
- priorizar normativa mexicana (NOM, NMX, reglamentos) sobre normativa
  internacional.

**Versión autocontenida.** Esta versión no depende de versiones anteriores. Todo el
contenido vigente está expandido literalmente.

---

## Propósito

Esta skill toma el **Brief v2.7** (skill 02) y produce la **Ficha Normativa** de la
sesión: el conjunto de normas técnicas, reglamentos, normativa patrimonial, contexto
regional, datos oficiales y fuentes institucionales aplicables al contenido.

No decide qué enseñar (eso viene del Brief). No busca recursos visuales (eso es 03c).
No compone la sesión (eso es 03d). Solo investiga y clasifica el cuerpo normativo.

**Prioridad normativa mexicana:** al buscar normativa, se prefieren las NOM, NMX,
reglamentos federales, estatales y municipales mexicanos. Solo se expande a normativa
internacional cuando no existe equivalente nacional (§1.7).

**Nota de compatibilidad:** esta skill requiere que el Brief sea **v2.7** (o superior)
y que el Doc Maestro sea **v1.5** (o superior). El Brief v2.7 incluye los campos
`Pesos por subtema`, `Modo de composición` y `Alcance conceptual del subtema`. Si el
Brief es v2.6 o anterior, se declara `no declarado` en el campo de modo y se marca la
ficha como incompleta para el handoff con 03d y 03e.

---

## Estructura final de la skill

```
A. Metadatos + categoría documental + modo de composición
B. Normas técnicas aplicables
C. Reglamentos locales y estatales
D. Normativa patrimonial (activación automática)
E. Contexto regional específico (activación condicional)
F. Datos oficiales verificables
G. Fuentes científicas e institucionales
H. Lagunas declaradas
I. Advertencias para composición
```

---

## 1.7 Regla de prioridad normativa

Al buscar normativa, reglamentos y documentos oficiales, la skill sigue este orden
de prioridad:

### 1.7.1 Prioridad normativa mexicana

1. **NOM — Normas Oficiales Mexicanas.** Obligatorias. Se buscan primero.
2. **NMX — Normas Mexicanas.** Voluntarias pero reconocidas. Se buscan después
   de NOM.
3. **Reglamentos federales, estatales y municipales mexicanos.**
4. **Documentos oficiales de instituciones mexicanas** (INAH, INEGI, SEDATU,
   CONAVI, SEDUMA Yucatán, Ayuntamiento de Mérida, etc.).
5. **Normativa internacional** (ISO, ASTM, ACI, AISC, IEEE, NEC, etc.) **solo
   cuando no exista equivalente mexicano.**

### 1.7.2 Reglas de búsqueda

- **Siempre buscar primero la NOM o NMX mexicana** para el concepto.
- **Si no existe NOM o NMX mexicana**, buscar reglamento federal, estatal o
  municipal aplicable.
- **Si tampoco existe**, buscar documento oficial de institución mexicana.
- **Si no existe ninguna fuente mexicana**, usar la norma internacional declarando
  la ausencia de equivalente nacional en el bloque I.

### 1.7.3 Qué cuenta como "normativa mexicana"

- Norma emitida por autoridad mexicana (DOF, SENER, SCT, SEDATU, SEDUMA, etc.).
- Norma emitida por organismo mexicano de normalización (ONNCCE, etc.).
- Reglamento federal, estatal o municipal mexicano.
- Documento oficial de institución mexicana reconocida.

Los criterios son **acumulativos, no excluyentes.**

### 1.7.4 Normas internacionales sin equivalente mexicano

Algunas normas internacionales son el estándar de facto en México porque no existe
NOM o NMX equivalente. Ejemplos:

- **AISC** (diseño de acero estructural).
- **ACI** (diseño de concreto reforzado).
- **ISO 5455** (escalas en dibujo técnico).
- **ASTM** (materiales y ensayos).
- **IEEE / NEC** (instalaciones eléctricas).

Estas normas se aceptan como fuente principal **declarando explícitamente que no
existe equivalente mexicano** en el bloque I. No se buscan alternativas forzadas.

### 1.7.5 Relación con el 60/20/20

La regla normativa **no modifica la proporción 60/20/20**. La normativa siempre
pertenece a la categoría C (científica, oficial, institucional o normativa). La
regla geográfica solo ordena dentro de la categoría C:

- Se prefieren NOM, NMX, reglamentos y documentos oficiales mexicanos.
- Las normas internacionales se aceptan solo cuando no existe equivalente mexicano.

---

# Ficha Normativa — Sesión [N]

## A. Metadatos

- Asignatura: [nombre]
- Sesión: [N]
- Subtemas cubiertos: [claves del Brief v2.7, bloque B]
- Contexto geográfico: [Mérida, Yucatán / otra localidad]
- Tipo de proyecto: [Vivienda unifamiliar / Comercial / Educativo / Patrimonial / Otro]
- Brief origen (versión y fecha): [v2.7, YYYY-MM-DD]
- Ficha de Contexto Regional de la asignatura (referencia): [ID o URL]
- **Categoría documental dominante:** [A / B / C / mixta]
- **Modo de composición:** [operativo / retrospectivo]
  - Heredado literal del Brief v2.7, bloque A. No se recalcula, no se inventa.
  - Si el Brief es v2.6 o anterior, se declara `no declarado` y se reporta.
- Ficha versión: v1.4
- Brief versión: v2.7
- Doc Maestro versión: v1.5
- Fecha de generación: YYYY-MM-DD

### Regla de clasificación documental

Las fuentes de la Ficha Normativa se clasifican de la siguiente forma para la
auditoría 60/20/20 que ejecuta 03d:

| Bloque de la Ficha | Categoría documental |
|---|---|
| B — Normas técnicas | **C** (oficial / normativa) |
| C — Reglamentos locales y estatales | **C** |
| D — Normativa patrimonial (INAH, etc.) | **C** |
| E — Contexto regional (si es dato oficial) | **C** |
| F — Datos oficiales verificables | **C** |
| G — Fuentes científicas e institucionales | **C** |

Salvo que una fuente dentro de estos bloques provenga de un medio web confiable que no
sea oficial (por ejemplo, un fabricante reconocido), en cuyo caso se clasifica como
**B**.

---

## B. Normas técnicas aplicables

| Clave | Nombre | Categoría normativa | Ámbito | Autoridad emisora | **Procedencia** | Vigencia | Última actualización | Obligatoriedad | Aplica a subtema | Referencia exacta | URL oficial |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NOM-020-ENER-2011 | Eficiencia energética en edificaciones | Eficiencia energética | Federal | SENER | **México** | Vigente | 2011 | Obligatoria | 3.2 | §5.2 [envolvente] | [URL] |
| ISO 5455:1979 | Escalas en dibujo técnico | Dibujo técnico | Internacional | ISO | **Internacional** | Vigente | 1979 | Recomendada | 1.2 | §3 [escalas] | [URL] |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

**Valores válidos:**
- Categoría normativa: accesibilidad / instalaciones / seguridad estructural / eficiencia energética / sustentabilidad / patrimonial / urbanística / protección civil / otra
- Ámbito: Federal / Estatal / Municipal / Internacional
- **Procedencia: México / Internacional**
- Vigencia: Vigente / En revisión / Derogada / En consulta pública
- Obligatoriedad: Obligatoria / Recomendada / Voluntaria
- Referencia exacta: solo clave. Nota breve entre corchetes **solo si la parte relevante es crítica**.

**Reglas de llenado:**

- **Si el ámbito es `Internacional`**, se declara en el bloque I la ausencia de
  equivalente mexicano.
- **Se buscó primero NOM o NMX mexicana** para cada concepto antes de pasar a
  normativa internacional.

---

## C. Reglamentos locales y estatales

| Documento | Categoría normativa | Ámbito | Autoridad | **Procedencia** | Vigencia | Tema | Aplica a subtema | Referencia exacta | URL oficial |
|---|---|---|---|---|---|---|---|---|---|
| Reglamento de Construcciones del Estado de Yucatán | Urbanística / uso de suelo | Estatal | Gobierno del Estado | **México** | Vigente | Alturas, retiros, cocheras | 3.2 | Art. 47 [retiros frontales] | [URL] |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

**Valores de `Procedencia`:** México / Internacional.

---

## D. Normativa patrimonial

> **Activación automática:** este bloque se despliega si el Brief contiene al menos una de estas palabras: centro histórico, INAH, zona arqueológica, patrimonio, monumento histórico, monumento artístico, colonial, virreinal, prehispánico, catalogado, protegido, maya (en contexto patrimonial). Si no, se omite por completo.

| Documento | Autoridad | **Procedencia** | Ámbito de aplicación | Restricción específica | Trámite requerido | Aplica a subtema | Referencia exacta | URL oficial |
|---|---|---|---|---|---|---|---|---|
| Ley Federal sobre Monumentos y Zonas Arqueológicos | INAH | **México** | Centro Histórico de Mérida | Intervención en fachadas, cambio de uso, alturas | Permiso INAH previo | 3.3 | Art. 27 [intervenciones] | [URL] |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

---

## E. Contexto regional específico

> **Activación condicional:** este bloque se despliega **solo si la sesión trata específicamente de clima, suelo o sismicidad**. En cualquier otro caso, sustituir todo el bloque por la línea:
>
> `Contexto regional: ver Ficha de Contexto Regional de la asignatura [ID o URL].`

| Campo | Valor |
|---|---|
| Clima | [cálido subhúmedo, temp. media, humedad, precipitación] |
| Vientos dominantes | [dirección, velocidad, zona de huracán] |
| Sismicidad | [zona NTC aplicable] |
| Suelo | [tipo, presencia de cenotes, nivel freático] |
| Temperatura del suelo | [valor a 1 m] |
| Patrimonio próximo | [zona INAH colindante, si aplica] |

---

## F. Datos oficiales verificables

| Dato | Organismo productor | **Procedencia** | Año | Aplica a subtema | URL oficial |
|---|---|---|---|---|---|
| Población de Mérida: [valor] | INEGI | **México** | 2020 | 1.2 | [URL] |
| ... | ... | ... | ... | ... | ... |

**Organismos típicos:** INEGI, CONAVI, SEDATU, SEDUMA Yucatán, Ayuntamiento de Mérida, CONAPO, CONAGUA.

**Valores de `Procedencia`:** México / Internacional.

---

## G. Fuentes científicas e institucionales (categoría C del 60/20/20)

| Autor / Institución | Título | Tipo | Año | **Procedencia** | **Idioma original** | Aplica a subtema | DOI o URL |
|---|---|---|---|---|---|---|---|
| [UADY / CINVESTAV / UNAM] | [título] | [Artículo revisado / Reporte técnico / Tesis doctoral] | [año] | **México** | **Español** | [subtema] | [DOI/URL] |
| ... | ... | ... | ... | ... | ... | ... | ... |

**Valores de `Procedencia`:** México / Latinoamérica / España / Otro.

**Valores de `Idioma original`:** Español / Inglés / Francés / Portugués / Otro.

**Regla:** se prefieren fuentes mexicanas o latinoamericanas en español. Si se usa
fuente extranjera habiendo nacional disponible, se declara en el bloque I.

---

## H. Lagunas declaradas

| Subtema sin fuente | Razón | Impacto para composición | Fuente alternativa (si existe) |
|---|---|---|---|
| 3.4 — [concepto] | No se encontró bibliografía académica verificable en acceso abierto | El compositor deberá decidir: omitir, cubrir con web confiable o reportar al docente | [Blog de despacho local / entrevista con maestro] |
| ... | ... | ... | ... |

**Regla:** toda laguna debe declararse.

**Categorías de laguna:**
- Sin fuente disponible.
- Fuente débil (sin autoría clara).
- En disputa sin consenso.
- Idioma no accesible.
- Fuente de pago.
- Fuente desactualizada.

---

## I. Advertencias para composición

| Tipo | Descripción |
|---|---|
| Norma en proceso de actualización | [clave, fecha estimada de publicación] |
| Conflicto federal vs. estatal | [NOM permite X, reglamento estatal restringe a Y] |
| Contenido que requiere contraste con teoría | [norma cita coeficientes que requieren comprensión de física térmica] |
| Norma que requiere permiso previo | [INAH exige permiso antes de intervención en fachada] |
| Dato oficial desactualizado | [último censo disponible 2020, proyección pendiente] |
| **Brief o Doc Maestro incompatible** | [si el Brief es v2.6 o el Doc Maestro es v1.4, se declara aquí; la ficha se genera pero queda marcada como incompleta] |
| **Norma internacional sin equivalente mexicano** | **"Para el concepto [X] no existe NOM, NMX, reglamento ni documento oficial mexicano. Se usó la norma [Y] porque es el estándar de facto en México para este tema. Se declara la ausencia de equivalente nacional."** |
| **Fuente extranjera con equivalente nacional disponible** | **"Para el concepto [X] existe la fuente mexicana [Y]. Se usó la fuente [W] por [razón]. La fuente mexicana se conserva como [secundaria / contraste]."** |

---

## Reglas de operación de la skill 03b

### Reglas generales

1. **Siempre** genera bloques A, H e I.
2. **Bloque B** se genera si el Brief menciona norma técnica, eficiencia, instalaciones, seguridad estructural o accesibilidad.
3. **Bloque C** se genera si el Brief menciona reglamento, zonificación, uso de suelo, retiros, alturas o licencia de construcción.
4. **Bloque D** se activa automáticamente si el Brief contiene al menos una palabra detonadora del catálogo.
5. **Bloque E** solo se despliega si la sesión trata de clima, suelo o sismicidad. En cualquier otro caso, sustituye por la línea de referencia.
6. **Bloque F** se genera si el guion requiere afirmaciones cuantitativas.
7. **Bloque G** se genera si hay aportación científica o institucional relevante.
8. **Nunca inventes claves de norma, artículos, URLs ni vigencias.** Si no puedes verificar, declara la laguna.
9. **No dupliques normas** entre bloques. Cada documento aparece una sola vez.
10. **La columna `Referencia exacta`** debe contener solo la clave. La nota breve entre corchetes es la excepción, no la regla.
11. **Categoría documental dominante** debe declararse siempre en el bloque A.
12. **Las fuentes se clasifican para el 60/20/20** según la regla del bloque A.
13. **Versiones obligatorias:** la ficha declara `Ficha versión`, `Brief versión` y
    `Doc Maestro versión` en el bloque A. Los valores esperados son v1.4, v2.7 y v1.5
    respectivamente. Si el Brief o el Doc Maestro son de versiones anteriores, se
    declara en el bloque I (`Brief o Doc Maestro incompatible`) y se marca la ficha
    como incompleta para el handoff con 03d y 03e.
14. **El modo de composición se hereda literal del Brief v2.7, bloque A.** No se
    reclasifica. Si el Brief es v2.6 o anterior, se declara `no declarado` y se reporta
    al usuario.

### Reglas de prioridad normativa

15. **Siempre buscar primero la NOM o NMX mexicana** para el concepto.
16. **Si no existe NOM o NMX mexicana**, buscar reglamento federal, estatal o
    municipal aplicable.
17. **Si tampoco existe**, buscar documento oficial de institución mexicana.
18. **Si no existe ninguna fuente mexicana**, usar la norma internacional
    declarando la ausencia de equivalente nacional en el bloque I.
19. **La regla normativa no modifica la proporción 60/20/20.** La normativa siempre
    pertenece a la categoría C.
20. **Toda norma tiene declarada su `Procedencia` (México / Internacional).**
21. **Toda fuente científica o institucional tiene declarada su `Procedencia` y su
    `Idioma original`.**

---

## Archivos que produce la skill 03b

| Archivo | Contenido | Frecuencia |
|---|---|---|
| `ficha_normativa_sesion_N.md` | Ficha completa de la sesión | Por sesión |
| `contexto_regional_[asignatura].md` | Contexto climático, suelo, sismicidad, patrimonio | Se crea una vez por asignatura |

---

## Checklist interno antes de entregar

### Verificaciones de prioridad normativa

- ¿Se buscó primero la NOM o NMX mexicana?
- ¿Si no existe NOM o NMX, se buscó reglamento federal, estatal o municipal?
- ¿Si no existe ninguna fuente mexicana, se declaró la ausencia de equivalente
  nacional en el bloque I?
- ¿Cada fuente normativa tiene declarada su procedencia (México / Internacional)?
- ¿Cada fuente científica o institucional tiene declarada su procedencia y su
  idioma original?
- ¿La proporción 60/20/20 se mantuvo intacta?

### Verificaciones generales

- ¿El bloque A tiene todos los metadatos, incluido el modo de composición y las
  versiones (Ficha v1.4, Brief v2.7, Doc Maestro v1.5)?
- ¿El bloque B tiene la columna `Procedencia`?
- ¿El bloque C tiene la columna `Procedencia`?
- ¿El bloque D tiene la columna `Procedencia`?
- ¿El bloque G tiene las columnas `Procedencia` e `Idioma original`?
- ¿El bloque H declara lagunas?
- ¿El bloque I incluye las advertencias sobre norma internacional sin equivalente
  y fuente extranjera con equivalente nacional?
- ¿No se inventaron claves de norma, artículos, URLs ni vigencias?

---

## Criterio final de calidad

La skill 03b cumple si:

### Criterios de prioridad normativa

- **se buscó primero la NOM o NMX mexicana**;
- **se agotaron las fuentes normativas mexicanas antes de pasar a las
  internacionales**;
- **si se usó norma internacional, se declaró la ausencia de equivalente
  nacional**;
- **cada fuente normativa está clasificada por procedencia**;
- **cada fuente científica o institucional tiene procedencia e idioma original**;
- **la proporción 60/20/20 se mantuvo intacta**.

### Criterios generales

- cada fuente tiene licencia verificable o advertencia explícita;
- los conceptos sin fuente están declarados como lagunas;
- las acciones pendientes del docente están listas para heredarse a 03d y 03e;
- **la ficha declara sus versiones (Ficha v1.4, Brief v2.7, Doc Maestro v1.5) y su
  modo de composición, y es consumible por 03d y 03e sin preguntas adicionales**;
- si el Brief o el Doc Maestro son incompatibles, se declara explícitamente;
- no se inventaron claves de norma, artículos, URLs ni vigencias.

---

## Changelog de consolidación v1.3 → v1.4

**Propósito:** actualizar referencias a skills consolidadas.

**Verificación de autocontención:**

- Se auditó v1.3.
- **No se encontraron referencias `[Igual que vX]` ni `[Sin cambios respecto a vX]`.**
- v1.3 ya estaba completamente autocontenida.

**Cambios aplicados en v1.4:**

1. **Título:** v1.3 → v1.4.
2. **Referencias al Brief:** v2.5 → **v2.7** (consolidado en la conversación previa).
3. **Referencias al Doc Maestro:** v1.4 → **v1.5** (consolidado en la conversación
   previa).
4. **Nota de compatibilidad:** actualizada a Brief v2.7 y Doc Maestro v1.5.
5. **Bloque A (metadatos):** ejemplo actualizado a v2.7 / v1.5.
6. **Reglas y checklist:** todas las referencias `Brief v2.5` → `Brief v2.7` y
   `Doc Maestro v1.4` → `Doc Maestro v1.5`.
7. **Changelog de consolidación** (este bloque).

**Contenido normativo preservado sin cambios:**

- §1.7 (prioridad normativa mexicana).
- Bloques A–I.
- Reglas de operación 1–21.
- Checklist interno.
- Criterio final de calidad.

**Compatibilidad downstream:**

- Brief consumidor: **v2.7**.
- Doc Maestro consumidor: **v1.5**.
- 03.D consumidor: v1.8.
- 03.E consumidor: v2.2.

---

**Guía de uso del flujo completo:** consulta `guia_uso_flujo_skills.md`.

