---
name: orquestador-curso
description: Meta-agente orquestador autonomo, idempotente y reanudable del flujo completo de diseno de cursos (etapas 01 a 05).
stage_id: "00"
version: "1.1"
status: stable
---

# SKILL: Orquestador Autónomo del Flujo Completo de Diseño de Curso
### Versión 1.1 — ejecución idempotente, reanudable y sin intervención del usuario

> **Rol:** meta-skill de orquestación.
>
> **No sustituye** ninguna skill disciplinar del flujo.
>
> **Función:** descubrir el estado real de un workspace de asignatura, reutilizar artefactos vigentes, regenerar únicamente lo necesario y ejecutar automáticamente el grafo completo de dependencias hasta alcanzar el máximo cierre posible.
>
> **Principio rector:** **inspeccionar → clasificar → reutilizar → ejecutar → verificar → reanudar**, nunca “regenerar todo por defecto”.

---

## 0. Objetivo

Esta skill permite que un agente ejecute de forma autónoma el ecosistema completo de diseño de curso sin requerir decisiones intermedias del usuario.

Debe poder comenzar en cualquiera de estos escenarios:

1. **workspace vacío** con insumos fuente;
2. **workspace parcialmente construido**;
3. **workspace con Documento Maestro ya existente**;
4. **workspace con Documento Maestro + Briefs existentes**;
5. **workspace con sesiones parcialmente desarrolladas**;
6. **workspace con productos 03.D / 03.E ya creados**;
7. **workspace previamente auditado por 04.A**;
8. **workspace con correcciones 04.B pendientes o ejecutadas**;
9. **workspace con capítulos listos para compilar mediante 05**;
10. **re-ejecución posterior a cambios upstream**.

La skill debe ser **idempotente**:

> Si se ejecuta dos veces sobre el mismo workspace sin cambios en insumos, skills ni artefactos, la segunda ejecución no debe volver a producir artefactos ya válidos.

---

# 1. Alcance y frontera

## 1.1 Qué hace

El orquestador:

- localiza las skills instaladas;
- valida sus versiones;
- localiza los insumos de la asignatura;
- inventaría artefactos ya existentes;
- determina qué artefactos son reutilizables;
- detecta qué artefactos quedaron obsoletos por cambios upstream;
- construye un grafo de dependencias;
- decide automáticamente qué skill debe ejecutarse a continuación;
- ejecuta ramas independientes en paralelo cuando el entorno lo permita;
- reanuda procesos incompletos;
- enruta RETURN / conflictos / propuestas upstream;
- aplica automáticamente 04.B cuando corresponda;
- reaudita cuando una corrección material lo exige;
- compila el libro con 05 cuando existen capítulos compilables;
- mantiene un estado persistente del flujo;
- produce un reporte final completo.

## 1.2 Qué NO hace

El orquestador no:

- redefine competencias;
- inventa contenido académico;
- sustituye decisiones de 01–05;
- reinterpreta contratos visuales;
- selecciona por sí mismo un recurso externo;
- diseña por sí mismo un RGE;
- certifica semánticamente un RGE;
- modifica PASS / RETURN;
- corrige directamente un documento cuando la propiedad pertenece a otra skill;
- oculta incompatibilidades;
- crea de nuevo un artefacto solo porque desconoce su procedencia;
- usa la fecha de modificación como único criterio de vigencia.

## 1.3 Autoridad normativa

En caso de conflicto:

1. la **skill propietaria del artefacto** tiene prioridad;
2. después, la versión vigente declarada en este manifiesto;
3. después, `guia_uso_flujo_skills_v4.2`;
4. esta meta-skill solo decide **orden, reutilización, invalidación y routing**.

Nunca modifica silenciosamente el contrato de una skill downstream.

---

# 2. Manifiesto de skills esperado

El agente debe descubrir estas skills por ID lógico, no únicamente por nombre exacto de archivo.

| ID lógico | Versión esperada | Nombre de referencia |
|---|---:|---|
| `01` | `v1.6` | `01.-SKILL-Planeacion-General-Curso-universal_v1.6` |
| `02` | `v2.8` | `02.-SKILL-Briefs-Sesion_v2.8` |
| `03.A` | `v1.12` | `03.A - SKILL_Ficha-teorica_v1.12` |
| `03.B` | `v1.4` | `03.B - SKILL_Ficha-normativa_v1.4` |
| `03.C-1` | `v1.2` | `03.C - 1. Skill - orquestador-visual - v1.2` |
| `03.C-2A` | `v1.3` | `03.C - 2A. Skill - disenador-generativo - v1.3` |
| `03.C-2B` | `v1.1` | `03.C - 2B. Skill - auditor-semantico_v1.1` |
| `03.C-2C` | `v0.1 BORRADOR` | `03.C - 2C. Skill - ejecutor-generativo_v0.1` |
| `03.C-3` | `v0.1 BORRADOR` | `03.C - 3. External-Resources_v0.1` |
| `03.D` | `v2.1` | `03.D - SKILL_guiones_numa_v2.1` |
| `03.E` | `v2.4` | `03.E - Skill_Capítulo-de-Libro-Autónomo_v2.4` |
| `04.A` | `v2.5` | `04.A - SKILL_Auditoría-de-Coherencia_v2.5` |
| `04.B` | `v1.2` | `04.B - SKILL_Implementación de Mejoras_v1.2` |
| `05` | `v1.1` | `05.- Skill  Compilador de Libro de Materia_v1.1` |
| `ESTILO` | `v2.0` | `perfil_estilo_CRC_v2.0` |
| `GUIA` | `v4.1` | `guia_uso_flujo_skills_v4.2` |

### 2.1 Regla de descubrimiento

Para cada ID:

1. buscar archivos cuyo nombre contenga el ID y versión esperada;
2. confirmar versión leyendo el encabezado del archivo;
3. si existen varios candidatos:
   - priorizar coincidencia exacta de versión;
   - priorizar archivo sin sufijos de copia como `(2)`, `(3)` cuando exista un nombre canónico;
   - si el contenido es idéntico por SHA-256, elegir uno y registrar duplicados;
   - si el contenido difiere, marcar `SKILL_DUPLICADA_AMBIGUA`.
4. nunca escoger una versión anterior si existe la versión esperada.

### 2.2 Skill faltante

Si falta una skill:

- marcar `SKILL_FALTANTE`;
- bloquear únicamente las ramas que dependan de ella;
- continuar todas las ramas independientes;
- no pedir intervención durante la ejecución.

### 2.3 Regla especial 03.C-2C v0.1

`03.C-2C` es requerida cuando exista una NVD `GENERATIVO` o `HÍBRIDO` cuya rama generativa haya obtenido `PASS` en 03.C-2B.

Si no se localiza 03.C-2C:

```text
GENERATIVO → BLOQUEADO_FALTA_03C2C
HÍBRIDO    → componente generativo bloqueado
EXTERNO    → puede continuar
NINGUNO    → puede continuar
```

El orquestador no absorbe la función de 03.C-2C ni llama directamente a un motor visual saltándose esa etapa.

Mientras 03.C-2C siga en `BORRADOR v0.1`:

- puede ejecutarse en modo autónomo;
- todo resultado debe conservar `ID_RGE`, `HUELLA_RGE_AUDITADO`, `PASS_REF` y `HASH_SHA256_ARCHIVO`;
- solo `RECURSO_GENERATIVO_RESUELTO` permite integración downstream;
- su uso debe quedar registrado como interfaz aún no congelada.

### 2.4 Regla especial 03.C-3 v0.1

Mientras 03.C-3 siga etiquetada como `BORRADOR v0.1`:

- puede ejecutarse en modo autónomo;
- todo resultado debe registrar `INTERFAZ_PROVISIONAL_03C3`;
- sus conflictos se enrutan normalmente a 03.C-1;
- su uso no autoriza declarar el ecosistema visual global como congelado.

---

# 3. Entradas del orquestador

## 3.1 Entradas mínimas

La ejecución requiere:

- **directorio raíz de skills**;
- **directorio raíz de la asignatura / workspace**.

Todo lo demás debe descubrirse automáticamente.

## 3.2 Insumos fuente potenciales

Buscar, entre otros:

- temario;
- programa oficial;
- calendario;
- encuadre;
- criterios de evaluación;
- datos institucionales;
- documento maestro existente;
- briefs existentes;
- perfil de estilo;
- archivos históricos de sesiones;
- recursos visuales existentes;
- capítulos existentes;
- informes 04.A;
- registros 04.B;
- libro previamente compilado.

## 3.3 No preguntar por datos ya presentes

Antes de solicitar, inferir o crear cualquier dato:

1. inspeccionar el workspace;
2. buscarlo en artefactos existentes;
3. buscarlo en el Documento Maestro;
4. buscarlo en Briefs;
5. buscarlo en metadatos de sesión;
6. solo si no existe y una skill lo requiere, aplicar la política de bloqueo de §14.

En modo autónomo **no se solicita al usuario**.

---

# 4. Estado persistente del flujo

El orquestador debe crear y mantener:

```text
/estado_flujo_autonomo.json
/reporte_flujo_autonomo.md
```

Opcionalmente:

```text
/historial_flujo_autonomo/
```

## 4.1 Propósito de `estado_flujo_autonomo.json`

El estado persistente permite:

- saber qué existe;
- saber qué fue producido por qué skill;
- recordar hashes;
- detectar cambios;
- evitar regeneración;
- reanudar después de una ejecución interrumpida.

## 4.2 Esquema mínimo

```json
{
  "schema": "flujo_autonomo_v1",
  "course_id": "...",
  "last_run": "...",
  "skills": {
    "01": {
      "version": "v1.6",
      "path": "...",
      "sha256": "...",
      "status": "OK"
    }
  },
  "sources": {
    "programa": {
      "path": "...",
      "sha256": "..."
    }
  },
  "artifacts": {
    "documento_maestro": {
      "path": "...",
      "producer": "01",
      "producer_version": "v1.6",
      "sha256": "...",
      "upstream_fingerprint": "...",
      "status": "VALIDO_REUTILIZABLE"
    }
  },
  "sessions": {
    "1": {
      "brief": "...",
      "03A": "...",
      "03B": "...",
      "03C1": "...",
      "03D": "...",
      "03E": "..."
    }
  },
  "blockers": [],
  "warnings": []
}
```

## 4.3 Hashes

Usar SHA-256 sobre bytes exactos para:

- skills;
- insumos fuente;
- artefactos;
- contratos donde la skill propietaria ya use SHA-256.

El hash del orquestador es de **trazabilidad**, no sustituye hashes contractuales de 03.C-2B.

---

# 5. Clasificación universal de artefactos

Todo artefacto descubierto debe recibir exactamente uno de estos estados:

| Estado | Significado |
|---|---|
| `AUSENTE` | No existe |
| `PRESENTE_SIN_VALIDAR` | Existe pero aún no se verificó |
| `VALIDO_REUTILIZABLE` | Puede consumirse sin regenerar |
| `OBSOLETO_UPSTREAM` | Un insumo o artefacto upstream cambió |
| `INCOMPATIBLE_VERSION` | Contrato/versiones no compatibles |
| `INCOMPLETO` | Existe, pero su propia skill lo declaró incompleto |
| `BLOQUEADO` | Existe una condición que impide continuar |
| `DUPLICADO_AMBIGUO` | Hay múltiples candidatos no equivalentes |
| `SUPERSEDED` | Existe pero fue sustituido por versión más reciente |
| `GENERADO_EN_ESTA_EJECUCION` | Creado o actualizado en el run actual |

## 5.1 Existencia no implica vigencia

Está prohibida esta regla:

```text
si archivo existe → reutilizar
```

La regla correcta es:

```text
si archivo existe
    → validar productor
    → validar versión
    → validar upstream
    → validar contrato mínimo
    → validar estado interno
    → reutilizar solo si todo es compatible
```

---

# 6. Fingerprint de upstream

## 6.1 Principio

Cada artefacto debe asociarse a un `upstream_fingerprint`.

El fingerprint se calcula a partir de:

- hashes de insumos directos;
- versiones de skills relevantes;
- IDs o hashes contractuales cuando existan.

## 6.2 Ejemplos

### Documento Maestro

```text
FP_MAESTRO =
SHA256(
  hash_temario
  + hash_calendario
  + hash_encuadre
  + hash_criterios_evaluacion
  + hash_skill_01
)
```

### Briefs

```text
FP_BRIEFS =
SHA256(
  hash_documento_maestro
  + hash_skill_02
)
```

### 03.A de sesión N

```text
FP_03A_N =
SHA256(
  hash_brief_N
  + hash_skill_03A
)
```

### 03.B de sesión N

```text
FP_03B_N =
SHA256(
  hash_brief_N
  + hash_skill_03B
)
```

### 03.C-1

```text
FP_C1_N =
SHA256(
  hash_brief_N
  + hash_03A_N
  + hash_03B_N
  + hash_skill_C1
)
```

### 03.D

Incluir:

- Brief;
- 03.A;
- 03.B;
- contrato 03.C-1;
- recursos visuales resueltos destinados a 03.D;
- skill 03.D.

### 03.E

Incluir:

- Brief;
- 03.A;
- 03.B;
- contrato 03.C-1;
- recursos visuales resueltos destinados a capítulo;
- perfil de estilo;
- skill 03.E.

## 6.3 Workspace legado sin estado previo

Si no existe `estado_flujo_autonomo.json`:

1. **no regenerar todo**;
2. inventariar artefactos;
3. inspeccionar sus metadatos;
4. reconstruir linaje cuando sea verificable;
5. marcar `VALIDO_REUTILIZABLE` si:
   - estructura compatible;
   - versión compatible;
   - no existe evidencia de upstream más reciente;
   - estado interno es apto;
6. si el linaje no puede probarse pero el contrato es completo:
   - marcar `VALIDO_REUTILIZABLE_CON_LINAJE_RECONSTRUIDO`;
   - registrar fingerprint desde ese momento;
7. solo regenerar si existe evidencia positiva de incompatibilidad.

**Regla:** la falta de un manifiesto previo no es razón suficiente para destruir trabajo válido.

---

# 7. Grafo de dependencias

## 7.1 Grafo principal

```text
FUENTES
  │
  ▼
 01
  │
  ▼
 02
  │
  ├──────────────┐
  ▼              ▼
03.A            03.B
  │              │
  └──────┬───────┘
         ▼
       03.C-1
         │
   ┌─────┼────────────┐
   │     │            │
EXTERNO GENERATIVO   HÍBRIDO
   │     │            │
 03.C-3 03.C-2A       ├── 03.C-3
   │     │            └── 03.C-2A
   │     ▼                 │
   │   03.C-2B             ▼
   │     │               03.C-2B
   │    PASS                │
   │     ▼                 PASS
   │   03.C-2C               ▼
   │                      03.C-2C
   │     │                  │
   │     ▼                  ▼
   │ RECURSO_           RECURSO_
   │ GENERATIVO_        GENERATIVO_
   │ RESUELTO           RESUELTO
   └──────────┬─────────────┘
              ▼
       VISUAL_RESUELTO
              │
        ┌─────┴─────┐
        ▼           ▼
      03.D         03.E
        │           │
        ▼           ▼
      04.A         04.A
        │           │
        ▼           ▼
      04.B*        04.B*
        │           │
        └─────┬─────┘
              ▼
          04.A cierre*
              │
              ▼
         capítulos finales
              │
              ▼
              05
```

`*` = solo cuando aplique.

## 7.2 Paralelización permitida

Puede ejecutarse en paralelo:

- 03.A y 03.B de la misma sesión;
- sesiones distintas si comparten un Documento Maestro/Briefs ya congelados;
- rama externa y generativa de una NVD HÍBRIDA;
- 03.D y 03.E cuando ambos tienen todos sus insumos resueltos;
- auditorías 04.A de productos distintos.

No paralelizar:

- 03.C-2B antes de cerrar RGE;
- 03.C-2C antes de PASS;
- 04.B antes de 04.A;
- 05 mientras los capítulos seleccionados sigan mutando.

---

# 8. Fase PRE-0 — Descubrimiento del workspace

Antes de ejecutar cualquier skill:

1. listar recursivamente archivos;
2. identificar skills;
3. identificar fuentes;
4. identificar artefactos derivados;
5. identificar sesiones;
6. identificar duplicados;
7. calcular hashes;
8. cargar estado previo si existe;
9. reconstruir el grafo real;
10. producir un plan interno de ejecución.

## 8.1 Catálogo de artefactos por patrón

Buscar semánticamente y por filename:

| Artefacto | Patrones típicos |
|---|---|
| Documento Maestro | `documento_maestro*`, `*maestro*curso*` |
| Briefs | `briefs_sesion*`, `brief_sesion*` |
| 03.A | `ficha_teorica*` |
| 03.B | `ficha_normativa*` |
| 03.C-1 | `ficha_estrategia_visual*`, `*orquestacion_visual*` |
| 03.C-2A | `ficha_diseno_generativo*` |
| paquete 2B | `paquete_rge_cerrados*` |
| 03.C-2B | `ficha_auditoria_semantica*` |
| 03.C-2C | `registro_produccion_generativa*`, `recurso_*` |
| 03.C-3 | `ficha_recursos_externos*` |
| 03.D | `presentacion_sesion*`, `guia_docente_sesion*` |
| 03.E | `capitulo_*` |
| 04.A | `informe_04A*`, `*auditoria*coherencia*` |
| 04.B | `registro_cambios_04B*`, documentos revisados |
| 05 | `libro_*`, `reporte_compilacion_*` |

No depender exclusivamente de estos nombres: leer encabezados cuando sea necesario.

---

# 9. Fase PRE-1 — Reutilización de Documento Maestro

## 9.1 Prioridad

Antes de ejecutar 01:

1. buscar Documento Maestro existente;
2. validar que corresponde a la asignatura;
3. validar compatibilidad con 01 v1.6;
4. verificar que contiene elementos estructurales requeridos por downstream, incluyendo §21/§22/§23 cuando aplique;
5. verificar estado interno;
6. comparar upstream conocido.

## 9.2 Resultado

### Si es reutilizable

```text
DOCUMENTO_MAESTRO = VALIDO_REUTILIZABLE
SKIP 01
```

### Si está obsoleto

```text
DOCUMENTO_MAESTRO = OBSOLETO_UPSTREAM
RUN 01
INVALIDAR 02 y downstream afectado
```

### Si falta

```text
RUN 01
```

### Si hay varios

- si idénticos → elegir canónico;
- si uno tiene versión mayor compatible → elegir ese;
- si divergen materialmente → `DUPLICADO_AMBIGUO`, bloquear 01/02 y continuar solo ramas cuya independencia pueda probarse.

## 9.3 Prohibición

Nunca crear un segundo Documento Maestro con otro nombre solo porque uno ya existente no coincide con el patrón esperado.

---

# 10. Fase PRE-2 — Reutilización de Briefs

Antes de ejecutar 02:

1. localizar colección de Briefs;
2. confirmar contrato v2.8 de 36 campos;
3. confirmar correspondencia con el Documento Maestro vigente;
4. verificar matriz de cobertura;
5. detectar sesiones faltantes;
6. detectar Briefs duplicados.

## 10.1 Política incremental

Si la colección es válida salvo sesiones nuevas o modificadas:

- regenerar solo briefs afectados **si 02 permite salida parcial segura**;
- si 02 exige regenerar el conjunto para preservar matriz global, regenerar el conjunto;
- nunca conservar una matriz global incoherente.

## 10.2 Resultado

```text
BRIEFS = VALIDO_REUTILIZABLE → SKIP 02
BRIEFS = OBSOLETO_UPSTREAM    → RUN 02
BRIEFS = AUSENTE              → RUN 02
```

---

# 11. Fase 1 — Planeación automática

Ejecutar 01 únicamente si §9 determinó que es necesario.

## 11.1 Inputs

Consumir automáticamente todos los insumos fuente disponibles.

No pedir confirmaciones.

## 11.2 Cierre

Solo considerar Documento Maestro válido si 01 lo declara completo según su propio contrato.

Si existe:

```text
COMPETENCIA_HUERFANA_SIN_DECISION
```

marcar flujo curricular como `BLOQUEADO_01`.

No inventar la decisión.

---

# 12. Fase 2 — Briefs automáticos

Ejecutar 02 únicamente si §10 lo exige.

## 12.1 Cierre

La colección debe preservar:

- 36 campos;
- cobertura de competencia;
- eslabones;
- matriz global consistente.

Si 02 reporta eslabón huérfano:

- no avanzar esa dependencia como completa;
- registrar bloqueo;
- continuar sesiones independientes solo si el contrato lo permite.

---

# 13. Fase 3 — Procesamiento por sesión

Para cada sesión con Brief válido:

```text
SESSION_STATE = READY_03
```

## 13.1 Ejecutar/reutilizar 03.A

- reutilizar si fingerprint coincide;
- ejecutar si ausente/obsoleto;
- si 03.A declara insuficiencia conceptual, no inventar.

## 13.2 Ejecutar/reutilizar 03.B

- reutilizar si fingerprint coincide;
- ejecutar si ausente/obsoleto;
- preservar prioridad normativa definida en 03.B.

## 13.3 Join

03.C-1 solo puede ejecutarse cuando 03.A y 03.B están en estado consumible.

---

# 14. Política de cero intervención

El usuario solicita ejecución sin intervención.

Por tanto:

## 14.1 No hacer preguntas durante el run

Está prohibido detenerse para preguntar:

- qué archivo usar cuando la elección puede resolverse por versión/hash;
- si debe reutilizar un Documento Maestro válido;
- si debe regenerar Briefs obsoletos;
- qué sesión ejecutar primero;
- si debe correr 04.B cuando 04.A produjo una corrección downstream de prioridad obligatoria;
- si debe reauditar después de una corrección material.

## 14.2 Ambigüedad no crítica

Resolver mediante:

1. contrato explícito;
2. versión;
3. hash;
4. precedencia del grafo;
5. política conservadora de menor modificación.

Registrar:

```text
DECISION_AUTONOMA
```

## 14.3 Bloqueo real

Si falta un dato que ninguna skill puede inferir legítimamente:

```text
BLOQUEO_NO_RESOLUBLE_AUTONOMAMENTE
```

Acciones:

1. no inventar;
2. bloquear la rama;
3. continuar las demás;
4. incluir el bloqueo en reporte final;
5. no preguntar durante la ejecución.

---

# 15. Fase 4 — Orquestación visual por sesión

## 15.1 Reutilizar 03.C-1

Si existe estrategia visual válida con fingerprint compatible:

```text
SKIP 03.C-1
```

Si 03.A/03.B o Brief cambió:

```text
INVALIDAR 03.C-1
```

## 15.2 Leer NVD

Para cada NVD:

```text
PROCEDENCIA =
EXTERNO
GENERATIVO
HÍBRIDO
NINGUNO
```

Enrutar automáticamente.

---

# 16. Rama EXTERNO

## 16.1 Ejecutar 03.C-3

Si no existe recurso externo resuelto válido:

```text
RUN 03.C-3
```

Si existe y:

- identidad coincide;
- contrato coincide;
- fuente/localizador siguen presentes;
- estado es resuelto;

reutilizar.

## 16.2 Conflicto upstream

Si 03.C-3 devuelve conflicto:

```text
RETURN → 03.C-1
```

03.C-1 puede modificar estrategia dentro de su propia autoridad.

Después:

- invalidar solo ramas afectadas;
- volver a ejecutar 03.C-3 si sigue siendo EXTERNO/HÍBRIDO.

## 16.3 Límite de ciclos

Máximo por NVD:

```text
MAX_CICLOS_C1_C3 = 3
```

Después:

```text
BLOQUEADO_CICLO_EXTERNO
```

---

# 17. Rama GENERATIVO

## 17.1 03.C-2A

Reutilizar un RGE solo si:

- corresponde a la misma NVD;
- Bloque E canónico está íntegro;
- inputs/versión no cambiaron;
- estado es apto para auditoría.

Si cambia el RGE después de PASS:

```text
INVALIDAR PASS
```

## 17.2 03.C-2B

Todo RGE nuevo o modificado debe pasar por 03.C-2B.

Resultado:

```text
PASS
RETURN
```

### RETURN

```text
RETURN → 03.C-2A
corregir contrato
regenerar vistas/paquete
RUN 03.C-2B desde cero
```

Máximo:

```text
MAX_CICLOS_2A_2B = 3
```

## 17.3 PASS

Solo `PASS` habilita producción.

Registrar:

- `ID_NVD`;
- `ID_RGE`;
- `HUELLA_RGE_AUDITADO`;
- `PASS_REF`;
- veredicto.

Interpretación obligatoria:

```text
PASS = AUTORIZACIÓN_DE_PRODUCCIÓN
```

`PASS` no significa que el recurso ya exista.

## 17.4 03.C-2C

Antes de ejecutar 03.C-2C verificar:

```text
ID_RGE_RECIBIDO = ID_RGE_AUDITADO
HASH_RGE_RECIBIDO = HUELLA_RGE_AUDITADO
VEREDICTO = PASS
```

Si no coincide:

```text
CONTRATO_DISTINTO_DEL_AUDITADO
```

y bloquear producción.

Si coincide:

```text
PASS → RUN 03.C-2C
```

03.C-2C debe producir desde el contrato exacto auditado.

Salida válida:

```text
RECURSO_GENERATIVO_RESUELTO
```

con al menos:

- `ID_NVD`;
- `ID_RGE`;
- `HUELLA_RGE_AUDITADO`;
- `PASS_REF`;
- archivo final;
- `HASH_SHA256_ARCHIVO`;
- formato;
- dimensiones;
- motor;
- intentos;
- estado.

## 17.5 Reutilización de producción

Reutilizar un recurso generativo existente solo si:

```text
ID_RGE coincide
HUELLA_RGE_AUDITADO coincide
HASH_SHA256_ARCHIVO coincide con el archivo real
archivo existe
estado = RECURSO_GENERATIVO_RESUELTO
```

Si el archivo falta o está corrupto pero el RGE/PASS no cambió:

```text
RUN 03.C-2C con el mismo PASS
```

No volver a 2A/2B.

Si cambia el RGE:

```text
INVALIDAR PASS
INVALIDAR 03.C-2C
RETURN → 03.C-2A → 03.C-2B → nuevo PASS → 03.C-2C
```

## 17.6 Fallos de 03.C-2C

### `FALLO_DE_EJECUCION`

Permitir reintento dentro del límite propio de 03.C-2C.

### `CONFLICTO_DE_CONTRATO`

```text
RETURN → 03.C-2A
→ nueva auditoría 03.C-2B
→ nuevo PASS
→ 03.C-2C
```

### `CONFLICTO_DE_ESTRATEGIA_VISUAL`

```text
RETURN → 03.C-1
```

### `BLOQUEADO_MOTOR`

Si no existe fallback contractual válido:

```text
RETURN → 03.C-2A
```

# 18. Rama HÍBRIDO

Ejecutar en paralelo cuando sea posible:

```text
componente externo   → 03.C-3
componente generativo → 03.C-2A → 03.C-2B → 03.C-2C
```

Cerrar HÍBRIDO solo cuando:

- componente externo = `RECURSO_EXTERNO_RESUELTO`;
- componente generativo = `RECURSO_GENERATIVO_RESUELTO`;
- identidad preservada;
- función diferenciada preservada;
- agrupación/secuencia contractual disponible.

Si una rama queda bloqueada:

```text
HÍBRIDO = BLOQUEADO_PARCIAL
```

---

# 19. Cierre visual de sesión

Construir internamente:

```text
VISUAL_PACKAGE_SESSION_N
```

No es una nueva skill ni un nuevo contrato.

Es un índice de handoffs ya válidos:

```text
NVD
→ procedencia
→ recurso(s)
→ destino(s)
→ estado
→ evidencia
```

## 19.1 NVD crítica

Si una NVD V1/V2 destinada a 03.D o 03.E no está satisfecha:

- bloquear únicamente el producto afectado;
- no fingir cierre.

## 19.2 V3/V4

Puede omitirse únicamente si upstream lo autoriza como no crítico.

---

# 20. Fase 5 — 03.D automática

Para cada sesión:

1. verificar Brief;
2. verificar 03.A;
3. verificar 03.B;
4. verificar 03.C-1;
5. verificar recursos destinados a Presentación/Guía;
6. reutilizar 03.D si fingerprint coincide;
7. ejecutar 03.D v2.1 si falta/obsoleto.

Outputs:

- `presentacion_sesion_N.md`;
- `guia_docente_sesion_N.md`.

No generar `instrucciones_recursos_propios_sesion_N.md`.

---

# 21. Fase 6 — 03.E automática

Para cada sesión:

1. verificar Brief;
2. verificar 03.A;
3. verificar 03.B;
4. verificar 03.C-1;
5. verificar recursos con destino `Capítulo`;
6. verificar perfil de estilo v2.0;
7. reutilizar capítulo si fingerprint coincide;
8. ejecutar 03.E v2.4 si falta/obsoleto.

## 21.1 Perfil de estilo

Si existe `perfil_estilo_CRC_v2.0`:

```text
REUTILIZAR
```

No regenerarlo por curso.

Si no existe y 03.E lo requiere:

```text
BLOQUEADO_FALTA_PERFIL_ESTILO
```

salvo que 03.E permita explícitamente derivarlo de otra fuente válida.

---

# 22. Fase 7 — Auditoría 04.A automática

Auditar automáticamente:

- productos 03.D terminados;
- capítulos 03.E terminados.

## 22.1 Reutilizar informe

Un informe 04.A puede reutilizarse si:

- documento auditado no cambió;
- 04.A sigue siendo v2.5;
- contexto contractual no cambió.

Si el documento cambió:

```text
INVALIDAR INFORME 04.A
```

## 22.2 Cuatro capas

Esperar resultados independientes de:

- trazabilidad;
- nivel;
- legibilidad;
- fidelidad visual cuando aplique.

## 22.3 Clasificar propuestas

Separar:

```text
DOWNSTREAM_EXECUTABLE
UPSTREAM_C1
UPSTREAM_C2A_2B
UPSTREAM_C3
REGENERATE_03CBIS
NO_ACTION
```

---

# 23. Fase 8 — 04.B automática

## 23.1 Política de aplicación

Sin intervención del usuario, seleccionar automáticamente:

- todas las propuestas `EJECUTABLE_DOWNSTREAM` de prioridad **alta**;
- todas las de prioridad **media** que sean necesarias para cerrar una brecha diagnosticada;
- propuestas de prioridad **baja** solo si:
  - son puramente editoriales;
  - no aumentan alcance académico;
  - no introducen colisión;
  - su implementación es determinista.

Registrar qué propuestas bajas no se implementaron.

## 23.2 Upstream

Si 04.A asigna propietario upstream:

### `03.C-1`

- invalidar estrategia afectada;
- ejecutar 03.C-1;
- reejecutar ramas afectadas;
- regenerar 03.D/03.E;
- volver a 04.A.

### `03.C-2A / 03.C-2B`

- invalidar RGE/PASS afectado;
- ejecutar 2A;
- auditar de nuevo con 2B;
- producir con 03.C-2C;
- reintegrar;
- volver a 04.A.

### `03.C-3`

- ejecutar nueva resolución externa;
- reintegrar;
- volver a 04.A.

### `03.C-2C`

- mantener `ID_RGE + HUELLA_RGE_AUDITADO + PASS_REF` exactos;
- regenerar producción sin modificar el contrato;
- verificar nuevo `HASH_SHA256_ARCHIVO`;
- reintegrar;
- volver a 04.A.

## 23.3 Máximo de bucles 04

Por documento:

```text
MAX_CICLOS_04 = 3
```

Si persiste la misma brecha:

```text
BLOQUEADO_CICLO_CALIDAD
```

No seguir indefinidamente.

---

# 24. Condición de cierre por producto

Un producto puede declararse `CERRADO` si:

- no tiene bloqueos contractuales;
- no tiene propuesta 04.A alta pendiente;
- no tiene corrección upstream requerida pendiente;
- las capas aplicables no presentan condición bloqueante.

Puede declararse:

```text
CERRADO_CON_ADVERTENCIAS
```

si solo permanecen:

- observaciones bajas;
- limitaciones documentadas no bloqueantes;
- 03.C-3 provisional sin conflicto concreto.

---

# 25. Fase 9 — Compilación automática con 05

## 25.1 Cuándo ejecutar

Ejecutar 05 si:

- existen al menos 2 capítulos;
- el usuario pidió flujo completo o la política del proyecto incluye libro;
- los capítulos seleccionados están:
  - `APTO_PARA_COMPILAR`, o
  - `COMPILABLE_CON_ADVERTENCIAS`.

## 25.2 No ejecutar

Si todos los capítulos están bloqueados o solo existe uno:

```text
05 = NO_APLICA_AUN
```

No es un error global.

## 25.3 Reutilización

Si existe `libro_[asignatura].md`:

- comparar hashes de capítulos incluidos;
- comparar 05 v1.1;
- comparar metadatos de compilación.

Si nada cambió:

```text
SKIP 05
```

Si cambió un capítulo:

```text
RUN 05
```

No recompilar por cambios irrelevantes en archivos que no entran al libro.

---

# 26. Invalidación mínima

Cuando cambia un artefacto, invalidar únicamente descendientes reales.

## 26.1 Tabla normativa

| Cambio | Invalidar |
|---|---|
| fuente curricular | 01 y todo downstream afectado |
| Documento Maestro | 02 y downstream |
| Brief N | 03.A/B/C y productos de sesión N |
| 03.A N | 03.C-1 si depende conceptualmente + D/E |
| 03.B N | 03.C-1 si depende normativamente + D/E |
| 03.C-1 NVD | ramas visuales de esa NVD + D/E destinos afectados |
| RGE | PASS + 03.C-2C + integraciones |
| recurso generativo producido | D/E que lo consumen + 04 posterior; si solo se corrompe el archivo, repetir 03.C-2C con mismo PASS |
| recurso externo | D/E que lo consumen |
| 03.D | 04.A/04.B de 03.D |
| 03.E | 04.A/04.B de capítulo + 05 |
| 04.B revisa capítulo | 04.A cierre + 05 |
| perfil estilo | 03.E afectados + 04 posteriores |
| skill cambia versión | todos sus outputs, salvo compatibilidad demostrable |

---

# 27. Política ante cambio de versión de una skill

Si una skill cambia:

```text
vX → vY
```

no invalidar ciegamente todo.

## 27.1 Procedimiento

1. comparar contrato de entrada/salida;
2. leer changelog;
3. clasificar:
   - `PATCH_NO_CONTRACTUAL`;
   - `CAMBIO_COMPATIBLE`;
   - `CAMBIO_CONTRACTUAL`;
4. si contractual:
   - invalidar outputs relevantes;
5. si compatible:
   - validar outputs existentes;
   - reutilizar si pasan el nuevo contrato.

## 27.2 Regla conservadora

Si no puede determinar compatibilidad:

```text
INCOMPATIBLE_VERSION
```

y regenerar desde esa skill, no desde 01 innecesariamente.

---

# 28. Manejo de duplicados y versiones históricas

## 28.1 Nunca borrar automáticamente

El orquestador no elimina archivos históricos salvo instrucción externa explícita.

## 28.2 Selección canónica

Para un mismo artefacto:

1. versión declarada vigente;
2. estado completo;
3. upstream compatible;
4. hash registrado;
5. fecha solo como último criterio auxiliar.

## 28.3 Archivos superseded

Marcar:

```text
SUPERSEDED
```

y excluir del grafo activo.

---

# 29. Política de nombres y carpetas

El orquestador debe preservar nombres existentes válidos.

Solo crear estructura nueva si no existe.

Estructura recomendada:

```text
/asignatura/
  estado_flujo_autonomo.json
  reporte_flujo_autonomo.md

  documento_maestro_[asignatura].md
  briefs_sesion_[asignatura].md
  perfil_estilo_CRC_v2.0.md

  /sesion_N/
    ficha_teorica_sesion_N.md
    ficha_normativa_sesion_N.md
    ficha_estrategia_visual_sesion_N.md

    ficha_diseno_generativo_sesion_N.md
    paquete_rge_cerrados_para_auditoria.md
    ficha_auditoria_semantica_sesion_N.md
    ficha_recursos_externos_sesion_N.md

    /recursos_externos/
    /recursos_generados/

    presentacion_sesion_N.md
    guia_docente_sesion_N.md
    capitulo_N_[slug].md

    informe_04A_[producto].md
    registro_cambios_04B_[producto].md

  libro_[asignatura].md
  reporte_compilacion_[asignatura].md
```

No mover archivos existentes solo por ajustarlos a esta estructura.

---

# 30. Motor de ejecución

## 30.1 Pseudocódigo principal

```text
LOAD skills
VALIDATE skill manifest

LOAD or CREATE estado_flujo_autonomo.json

DISCOVER workspace
HASH sources + artifacts
CLASSIFY artifacts

IF Documento Maestro != VALIDO_REUTILIZABLE:
    RUN 01

IF Briefs != VALIDO_REUTILIZABLE:
    RUN 02

FOR each valid session:
    ENSURE 03.A
    ENSURE 03.B
    ENSURE 03.C-1

    FOR each NVD:
        ROUTE provenance
        RESOLVE external/generative/hybrid
        IF 03.C-2B = PASS:
            ENSURE 03.C-2C
        HANDLE RETURN / production failure automatically

    IF visual gate allows 03.D:
        ENSURE 03.D

    IF visual gate allows 03.E:
        ENSURE 03.E

    FOR each produced product:
        ENSURE 04.A
        ROUTE proposals

        IF downstream:
            RUN 04.B
            RUN 04.A closure

        IF upstream:
            REGENERATE minimal dependency chain
            RUN 04.A again

IF >= 2 compilable chapters:
    ENSURE 05

WRITE state
WRITE report
RETURN summary
```

## 30.2 ENSURE

Definición:

```text
ENSURE artifact:
    if VALIDO_REUTILIZABLE:
        reuse
    elif AUSENTE:
        run producer
    elif OBSOLETO_UPSTREAM:
        run producer
    elif INCOMPATIBLE_VERSION:
        run producer
    elif INCOMPLETO:
        follow producer-specific routing
    elif BLOQUEADO:
        record and continue independent graph
```

---

# 31. Transacciones y escritura segura

Antes de reemplazar un artefacto existente:

1. generar nueva versión en temporal;
2. validar que el productor cerró correctamente;
3. calcular hash;
4. solo entonces promover a ruta canónica;
5. actualizar estado.

Si falla la ejecución:

- conservar el artefacto anterior;
- marcar intento fallido;
- no dejar un archivo parcialmente escrito como canónico.

---

# 32. Política de reanudación

Al iniciar una ejecución:

1. leer `estado_flujo_autonomo.json`;
2. comprobar que archivos registrados todavía existen;
3. recalcular hashes;
4. detectar diferencias;
5. reanudar desde el nodo mínimo necesario.

Ejemplo:

```text
01 válido
02 válido
03.A sesiones 1–8 válidas
03.B sesiones 1–8 válidas
03.C sesión 6 incompleta

→ reanudar en 03.C sesión 6
→ no volver a ejecutar 01, 02, 03.A ni 03.B
```

---

# 33. Política de fallos parciales

Un fallo de una sesión no bloquea automáticamente todo el curso.

Ejemplo:

```text
S1 CERRADA
S2 CERRADA
S3 BLOQUEADA_FALTA_03CBIS
S4 CERRADA
```

El agente:

- continúa S4 y siguientes;
- puede compilar capítulos cerrados si 05 lo permite;
- reporta hueco S3;
- no inventa contenido.

---

# 34. Priorización automática

Orden de prioridad:

1. bloqueos upstream compartidos;
2. Documento Maestro;
3. Briefs;
4. sesiones con productos próximos a cierre;
5. NVD V1;
6. NVD V2;
7. NVD V3;
8. NVD V4;
9. 04.A/04.B;
10. 05.

Dentro de igual prioridad:

- menor número de sesión primero;
- luego menor ID NVD/RGE;
- orden lexical como desempate.

Esto garantiza determinismo.

---

# 35. Reporte final obligatorio

Crear:

```text
reporte_flujo_autonomo.md
```

## 35.1 Formato

```markdown
# Reporte de ejecución autónoma

## 1. Resumen
- Asignatura
- Fecha
- Estado global
- Skills detectadas
- Skills faltantes

## 2. Artefactos reutilizados
| Artefacto | Productor | Motivo de reutilización | Hash |

## 3. Artefactos generados/regenerados
| Artefacto | Productor | Motivo | Upstream |

## 4. Artefactos obsoletos descartados del grafo activo
| Artefacto | Motivo |

## 5. Estado por sesión
| Sesión | Brief | 03.A | 03.B | 03.C | 03.D | 03.E | 04 |

## 6. Estado visual
| Sesión | NVD | Procedencia | Estado | Bloqueo |

## 7. Auditoría y correcciones
| Producto | 04.A | 04.B | Reauditoría | Estado |

## 8. Compilación
- Estado 05
- Capítulos incluidos
- Capítulos bloqueados
- Libro generado/reutilizado

## 9. Decisiones autónomas
| ID | Decisión | Regla aplicada |

## 10. Bloqueos
| ID | Rama | Causa | Propietario | Próximo nodo |

## 11. Advertencias
- interfaces provisionales
- skills faltantes
- linaje reconstruido

## 12. Estado final
COMPLETO / PARCIAL / BLOQUEADO
```

---

# 36. Estado global

Usar exactamente:

## `COMPLETO`

Todos los productos solicitables por los insumos disponibles cerraron sin bloqueos críticos.

## `COMPLETO_CON_ADVERTENCIAS`

Todo cerró, pero existen advertencias no bloqueantes.

## `PARCIAL`

Algunas sesiones/productos cerraron y otras ramas quedaron bloqueadas.

## `BLOQUEADO`

No puede producirse ningún producto principal por falta de un upstream común.

---

# 37. Criterios de reutilización específicos

## 37.1 Documento Maestro

Reutilizar si:

- corresponde a la asignatura;
- contrato compatible con 01 v1.6;
- §21/22/23 presentes cuando los downstream los requieren;
- fuentes conocidas no cambiaron;
- no está declarado incompleto.

## 37.2 Briefs

Reutilizar si:

- contrato 36 campos;
- Documento Maestro coincide;
- matriz global válida;
- no faltan sesiones esperadas sin explicación.

## 37.3 03.A / 03.B

Reutilizar si:

- Brief no cambió;
- versión compatible;
- estado consumible.

## 37.4 03.C-1

Reutilizar si:

- Brief/03.A/03.B no cambiaron;
- NVD completas;
- destinos y procedencias explícitos.

## 37.5 RGE + PASS

Reutilizar PASS solo si:

```text
ID_RGE igual
HUELLA_RGE_AUDITADO igual
contrato exacto igual
```

## 37.6 Recurso generativo producido

Reutilizar solo si:

```text
ID_RGE coincide
HUELLA_RGE_AUDITADO coincide
PASS_REF coincide
HASH_SHA256_ARCHIVO coincide
archivo existe
estado = RECURSO_GENERATIVO_RESUELTO
```

Si solo cambia o se corrompe el archivo y el contrato/PASS siguen idénticos, repetir 03.C-2C sin invalidar 03.C-2B.

## 37.7 Recurso externo

Reutilizar si:

- ID exacto;
- recurso accesible cuando aplique;
- fuente/localizador/derechos presentes;
- no existe evidencia de sustitución.

## 37.8 03.D / 03.E

Reutilizar si:

- todos sus upstream coinciden;
- producto no está bloqueado;
- 04.B posterior no produjo una versión revisada más nueva.

## 37.9 04.A

Reutilizar solo sobre el hash exacto del documento auditado.

## 37.10 04.B

Reutilizar solo si:

- informe 04.A origen es el mismo;
- documento base es el mismo;
- propuestas seleccionadas son las mismas.

## 37.11 Libro 05

Reutilizar si el conjunto y hash de capítulos incluidos no cambió.

---

# 38. Política de outputs revisados

Cuando 04.B produce una revisión:

- esa revisión se vuelve el artefacto canónico downstream;
- el original no se borra;
- marcar original como `SUPERSEDED_BY_04B`;
- 05 debe consumir la versión revisada.

---

# 39. No crear por duplicado

## Regla dura

Antes de generar **cualquier** archivo:

```text
SEARCH equivalent artifact
VALIDATE identity
VALIDATE version
VALIDATE upstream
```

Solo después:

```text
CREATE
```

### Ejemplos prohibidos

- crear `documento_maestro_v2.md` porque ya existe `documento_maestro.md`;
- crear nuevos Briefs sin revisar `briefs_sesion_asignatura.md`;
- producir un segundo capítulo porque el primero tiene nombre distinto;
- volver a auditar un documento sin comprobar si ya existe 04.A sobre el mismo hash;
- recompilar el libro si los capítulos no cambiaron.

---

# 40. Contrato de autonomía

El agente que use esta skill debe operar bajo:

```text
AUTONOMIA = ALTA
PREGUNTAS_INTERMEDIAS = 0
REUTILIZACION = PRIORITARIA
REGENERACION = MINIMA
REGISTRO_DE_DECISIONES = OBLIGATORIO
INVENTAR_DATOS = PROHIBIDO
CONTINUAR_RAMA_INDEPENDIENTE = OBLIGATORIO
```

Si el usuario da una instrucción específica posterior, esa instrucción puede cambiar esta política para esa ejecución.

---

# 41. Instrucción operativa final

1. Descubre skills y workspace.
2. Valida manifiesto de versiones.
3. Carga estado previo si existe.
4. Inventa artefactos y calcula hashes.
5. Reconstruye linaje.
6. Clasifica cada artefacto.
7. Reutiliza todo artefacto válido.
8. Ejecuta 01 solo si Documento Maestro falta o quedó obsoleto.
9. Ejecuta 02 solo si Briefs faltan o quedaron obsoletos.
10. Procesa cada sesión desde el primer nodo inválido.
11. Ejecuta 03.A y 03.B.
12. Ejecuta 03.C-1.
13. Resuelve cada NVD por procedencia.
14. No produzcas generativos sin PASS exacto de 03.C-2B.
15. Ejecuta 03.C-2C solo después de PASS y no sustituyas su función con generación directa.
16. Ejecuta 03.D / 03.E solo cuando sus compuertas visuales lo permitan.
17. Audita con 04.A.
18. Ejecuta 04.B solo para correcciones downstream.
19. Rutea automáticamente correcciones upstream.
20. Reaudita después de cambios materiales.
21. Cierra productos cuando no existan bloqueos.
22. Ejecuta 05 sobre capítulos compilables.
23. Actualiza estado persistente.
24. Entrega reporte de ejecución.
25. No preguntes al usuario durante el run.
26. No inventes para desbloquear.
27. No regeneres un artefacto válido.

---

# 42. Checklist del orquestador

## Preflight

- [ ] ¿Se localizaron las skills?
- [ ] ¿Se validaron versiones?
- [ ] ¿Se detectó 03.C-2C v0.1 y su estado provisional?
- [ ] ¿Se registró 03.C-3 como provisional?
- [ ] ¿Se localizó el perfil de estilo?
- [ ] ¿Se cargó estado previo?
- [ ] ¿Se calcularon hashes?

## Reutilización

- [ ] ¿Se buscó Documento Maestro antes de ejecutar 01?
- [ ] ¿Se buscaron Briefs antes de ejecutar 02?
- [ ] ¿Se buscaron artefactos por sesión?
- [ ] ¿Se validó upstream y no solo existencia?
- [ ] ¿Se evitó crear duplicados?

## Sesiones

- [ ] ¿03.A/03.B están vigentes?
- [ ] ¿03.C-1 está vigente?
- [ ] ¿cada NVD fue ruteada?
- [ ] ¿RETURN se manejó automáticamente?
- [ ] ¿PASS + ID_RGE + HUELLA_RGE_AUDITADO se verificaron antes de 03.C-2C?
- [ ] ¿solo `RECURSO_GENERATIVO_RESUELTO` avanzó downstream?
- [ ] ¿NVD V1/V2 bloqueantes impidieron cierre cuando correspondía?

## Productos

- [ ] ¿03.D reutilizado si era válido?
- [ ] ¿03.E reutilizado si era válido?
- [ ] ¿04.A corresponde al hash exacto?
- [ ] ¿04.B solo ejecutó downstream?
- [ ] ¿upstream se enroutó al propietario?
- [ ] ¿se evitó bucle infinito?

## Compilación

- [ ] ¿cada capítulo tiene estado compilable?
- [ ] ¿05 se omitió si nada cambió?
- [ ] ¿assets y Anexo Z se preservan?

## Estado

- [ ] ¿se actualizó `estado_flujo_autonomo.json`?
- [ ] ¿se produjo `reporte_flujo_autonomo.md`?
- [ ] ¿se declararon bloqueos?
- [ ] ¿se registraron decisiones autónomas?

---

# 43. Caso de ejemplo A — Documento Maestro y Briefs ya existen

Workspace:

```text
documento_maestro_topografia.md
briefs_sesion_topografia.md
/sesion_1/
  ficha_teorica_sesion_1.md
```

Ejecución:

```text
1. validar Documento Maestro → VALIDO_REUTILIZABLE → SKIP 01
2. validar Briefs → VALIDO_REUTILIZABLE → SKIP 02
3. sesión 1:
   03.A existe y coincide → SKIP
   03.B ausente → RUN 03.B
   03.C-1 ausente → RUN
   ...
```

Resultado:

**No se recrean Documento Maestro ni Briefs.**

---

# 44. Caso de ejemplo B — Cambió el Brief de sesión 6

Estado previo:

```text
01 válido
02 colección actualizada
S1–S5 cerradas
S6 productos antiguos
S7–S12 cerradas
```

El hash del Brief 6 cambia.

Invalidación:

```text
S6 03.A
S6 03.B
S6 03.C-1
ramas visuales S6
03.D S6
03.E S6
04 S6
05
```

No invalidar:

```text
01
02
S1–S5
S7–S12
```

---

# 45. Caso de ejemplo C — 03.C-2C faltante o bloqueada

03.C-1 prescribe:

```text
NVD-01 EXTERNO
NVD-02 GENERATIVO
NVD-03 NINGUNO
```

Ejecución:

```text
NVD-01 → 03.C-3 → RECURSO_EXTERNO_RESUELTO
NVD-02 → 03.C-2A → 03.C-2B PASS → 03.C-2C
NVD-03 → no requiere ejecución
```

Si 03.C-2C no está disponible:

```text
NVD-02 = BLOQUEADO_FALTA_03C2C
```

Si 03.C-2C existe pero el archivo falla técnicamente:

```text
03.C-2C → retry según su contrato
```

Si el archivo está corrupto en una re-ejecución pero `ID_RGE + HUELLA_RGE_AUDITADO + PASS_REF` siguen vigentes:

```text
repetir 03.C-2C
```

sin volver a 03.C-2A/03.C-2B.

Si NVD-02 es V1 destinada al capítulo:

```text
03.E = BLOQUEADO
```

Si presentación solo consume NVD-01:

```text
03.D puede cerrar
```

# 46. Caso de ejemplo D — 04.A devuelve corrección upstream

04.A detecta:

```text
recurso externo distinto del autorizado
propietario = 03.C-3
```

El orquestador:

```text
NO enviar como edición libre a 04.B
RUN 03.C-3
obtener recurso resuelto
RUN 03.E
RUN 04.A
```

Si después queda solo corrección de pie:

```text
04.B → EJECUTABLE_DOWNSTREAM
```

---

# 47. Criterio final de calidad

Esta skill cumple si:

- una re-ejecución sin cambios produce **cero regeneraciones innecesarias**;
- un Documento Maestro válido se reutiliza;
- Briefs válidos se reutilizan;
- un cambio local invalida únicamente descendientes reales;
- ningún generativo se produce sin PASS;
- ningún recurso externo se sustituye silenciosamente;
- 04.B nunca invade propiedad upstream;
- sesiones independientes continúan aunque otra se bloquee;
- el proceso puede reanudarse;
- toda decisión autónoma queda registrada;
- todo bloqueo real queda explícito;
- no se solicita intervención durante el run;
- el estado final refleja la realidad del workspace.

---

# 47.1 Changelog v1.0 → v1.1

1. Se actualiza la guía normativa de v4.1 a v4.2.
2. 03.C-2A pasa de v1.2 a v1.3.
3. 03.C-2B pasa de v1.0 a v1.1.
4. Se incorpora 03.C-2C v0.1 como ejecutor generativo.
5. Se elimina la antigua etapa 03Cbis del grafo activo.
6. `PASS` se interpreta como `AUTORIZACIÓN_DE_PRODUCCIÓN`.
7. Solo `RECURSO_GENERATIVO_RESUELTO` puede avanzar a 03.D/03.E.
8. Se incorpora gate de `ID_RGE + HUELLA_RGE_AUDITADO + PASS_REF`.
9. Se incorpora reutilización de producción por `HASH_SHA256_ARCHIVO`.
10. Corrupción o pérdida del archivo con contrato/PASS intactos regenera solo 03.C-2C.
11. Cambio del RGE invalida PASS y producción.
12. Se actualiza la rama HÍBRIDO.
13. Se actualizan routing 04.A/04.B e invalidación mínima.
14. Se reemplaza el caso de ejemplo de falta de 03Cbis por manejo de 03.C-2C.
15. Se mantiene 03.C-3 v0.1 como interfaz provisional.

---

# 48. Estado de esta skill

**v1.1 — PROPUESTA OPERATIVA ACTUALIZADA**

Esta meta-skill se alinea con el subsistema visual vigente:

```text
03.C-1
├─ EXTERNO → 03.C-3
├─ GENERATIVO → 03.C-2A → 03.C-2B → 03.C-2C
└─ HÍBRIDO → 03.C-3 + 03.C-2A → 03.C-2B → 03.C-2C
```

Versiones generativas esperadas:

- 03.C-2A v1.3;
- 03.C-2B v1.1;
- 03.C-2C v0.1 BORRADOR.

Advertencias arquitectónicas actuales:

1. `03.C-2C` sigue en `BORRADOR v0.1` y requiere prueba real;
2. `03.C-3` sigue en `BORRADOR v0.1`;
3. el orquestador debe conservar evidencia de estas interfaces provisionales.

La antigua 03.C-2C no forma parte del grafo vigente.

El orquestador considera cerrada una rama generativa únicamente cuando existe:

```text
RECURSO_GENERATIVO_RESUELTO
```

trazable a:

```text
ID_NVD
→ ID_RGE
→ HUELLA_RGE_AUDITADO
→ PASS
→ 03.C-2C
→ HASH_SHA256_ARCHIVO
```

La ausencia de 03.C-2C o 03.C-3 no invalida ramas independientes: bloquea únicamente las dependencias afectadas.

