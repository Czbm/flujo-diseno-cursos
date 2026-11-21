# Guía de uso — Flujo completo de skills para diseño de curso — v4.2

## 0. Alcance de esta guía

Esta guía describe el estado operativo del ecosistema de skills para transformar un temario oficial en un sistema didáctico trazable: planeación general, briefs por sesión, desarrollo teórico y normativo, estrategia visual, resolución de recursos visuales, composición sincrónica, capítulo autónomo, auditoría académica, implementación de mejoras y compilación del libro.

La v4.2 sustituye a la guía v4.1 como referencia de uso. Se actualiza contra los archivos vigentes revisados el 2026-10-11 y distingue explícitamente entre:

- **versiones cerradas o estables**;
- **versiones cerradas o estables**;
- **borradores todavía no congelados**;
- **interfaces provisionales explícitas**;
- **pendientes reales de cierre arquitectónico**.

> **Regla de lectura:** esta guía describe el flujo real que resulta de los contratos actuales. Cuando dos skills no coinciden todavía en su interfaz, la guía no presupone compatibilidad silenciosa: la brecha se declara.

---

## 1. Qué produce el ecosistema

El flujo puede producir, por asignatura:

- Documento Maestro del Curso.
- Briefs contractuales por sesión.
- Ficha Teórica por sesión.
- Ficha Normativa por sesión.
- Estrategia visual por NVD.
- Recursos visuales externos resueltos.
- Recursos generativos diseñados, auditados y producidos.
- Presentación proyectable para alumno.
- Guía docente.
- Capítulo autocontenido del libro de la materia.
- Informe de auditoría académica de trazabilidad, nivel y legibilidad.
- Documento revisado + registro de cambios después de implementar mejoras.
- Libro compilado de la asignatura + reporte de compilación.

El flujo admite tanto **modo operativo** para sesiones próximas o pendientes como **modo retrospectivo** para sesiones ya impartidas.

---

## 2. Versiones vigentes revisadas

| ID | Skill / archivo | Versión o estado revisado | Estado de uso |
|---|---|---:|---|
| **01** | Planeación General del Curso | **v1.6** | Vigente |
| **02** | Briefs por Sesión | **v2.8** | Vigente |
| **03.A** | Ficha Teórica | **v1.12** | Vigente |
| **03.B** | Ficha Normativa | **v1.4** | Vigente |
| **03.C-1** | Orquestador Visual | **v1.2** | Estable / contractual |
| **03.C-2A** | Diseñador de Recursos Generativos | **v1.3** | Vigente |
| **03.C-2B** | Auditor Semántico | **v1.1** | Vigente / cerrada |
| **03.C-2C** | Ejecutor de Recursos Generativos | **BORRADOR v0.1** | Interfaz operativa nueva; prueba real pendiente |
| **03.C-3** | External Resources | **BORRADOR v0.1** | Interfaz provisional; cierre pendiente |
| **03.D** | Composición Dual NUMA | **v2.1** | Vigente / alineada con 03.C |
| **03.E** | Capítulo de Libro Autónomo | **v2.4** | Vigente / alineada con 03.C |
| **04.A** | Auditoría de Coherencia | **v2.5** | Vigente / cuatro capas |
| **04.B** | Implementación de Mejoras | **v1.2** | Vigente / propiedad contractual visual |
| **05** | Compilador de Libro de Materia | **v1.1** | Vigente / post-proceso alineado |
| — | Perfil de estilo CRC | **v2.0** | Persistente |
| **06** | Exportador profesional | Pendiente | No existe skill cerrada |

### Cambio estructural respecto a la guía v4.0

Desde v4.0 se cerraron las interfaces downstream que estaban pendientes:

```text
03.D v2.1  → 03.D v2.1
03.E v2.4  → 03.E v2.4
04.A v2.5  → 04.A v2.5
04.B v1.2  → 04.B v1.2
05   v1.0  → 05   v1.1
```

La arquitectura visual downstream ya no depende contractualmente de `Ficha Visual v1.8`.

El control de calidad queda formalmente separado:

```text
04.A — diagnostica en cuatro capas
        1) trazabilidad de competencias
        2) coherencia de nivel
        3) legibilidad editorial
        4) fidelidad de integración visual

04.B — implementa solo correcciones que le pertenecen downstream
       y escala las correcciones cuya propiedad es upstream
```

La secuencia recomendada es:

```text
documento terminado
      ↓
    04.A
      ↓
informe + propuestas + propietario de corrección
      ↓
    04.B
      ↓
documento revisado / propuestas escaladas
      ↓
04.A opcional de verificación
```

## 3. Arquitectura general vigente

```text
ETAPA 1 — PLANEACIÓN Y RESPONSABILIDAD CURRICULAR

Temario + calendario + encuadre
        │
        ▼
[01] Documento Maestro v1.6
        │
        ▼
[02] Briefs por Sesión v2.8


ETAPA 2 — DESARROLLO DISCIPLINAR DE LA SESIÓN

Brief de sesión
    │
    ├────────► [03.A] Ficha Teórica v1.12
    │
    └────────► [03.B] Ficha Normativa v1.4
                      │
                      ▼
              [03.C-1] Orquestador Visual v1.2
                      │
           ┌──────────┼──────────┐
           │          │          │
        EXTERNO   GENERATIVO   HÍBRIDO
           │          │          │
           ▼          ▼          ├──────────────────┐
       [03.C-3]   [03.C-2A]      ▼                  ▼
           │          │       [03.C-3]          [03.C-2A]
           │          ▼                              │
           │      [03.C-2B]                         ▼
           │     PASS / RETURN                  [03.C-2B]
           │          │                              │
           │        PASS                           PASS
           │          ▼                              ▼
           │      [03.C-2C]                       [03.C-2C]
           │   ejecuta recurso                  ejecuta recurso
           │          │                              │
           └──────────┴──────────────┬───────────────┘
                                     ▼
                         paquete visual resuelto


ETAPA 3 — PRODUCTOS DIDÁCTICOS

Brief + 03.A + 03.B + 03.C-1 + recursos visuales resueltos
        │
        ├────────► [03.D] Presentación + Guía docente v2.1
        │
        └────────► [03.E] Capítulo Autónomo v2.4


ETAPA 4 — CONTROL DE CALIDAD ACADÉMICA, EDITORIAL Y VISUAL

Documento terminado de 03.D o 03.E
        │
        ▼
[04.A] Auditoría de Coherencia v2.5
        │
        ├─ trazabilidad
        ├─ nivel
        ├─ legibilidad
        └─ fidelidad visual
        │
        ▼
informe + propuestas + propietario de corrección
        │
        ▼
[04.B] Implementación de Mejoras v1.2
        │
        ├─ ejecuta si propietario = 03.D / 03.E
        └─ escala si propietario = 03.C-1 / 03.C-2A-2B / 03.C-3 / 03.C-2C
        │
        ▼
documento revisado
        │
        └────────► reauditoría 04.A si se requiere verificar cierre


ETAPA 5 — POST-PROCESO DEL LIBRO

capítulos 03.E v2.4+ terminados / corregidos
        │
        ▼
[05] Compilador v1.1
        │
        ├────────► libro_[asignatura].md
        └────────► reporte_compilacion_[asignatura].md
```


### Cierre de la rama generativa

La rama generativa vigente queda formalmente separada en tres responsabilidades:

```text
03.C-2A = diseña el RGE
03.C-2B = audita el contrato y emite PASS / RETURN
03.C-2C = ejecuta el contrato aprobado y produce el archivo
```

`PASS` significa **autorización de producción**, no recurso terminado.

Solo el estado:

```text
RECURSO_GENERATIVO_RESUELTO
```

emitido por 03.C-2C habilita el consumo del recurso por 03.D / 03.E.

Si el RGE cambia después de PASS:

```text
PASS_INVALIDADO
→ 03.C-2A
→ 03.C-2B desde cero
→ nuevo PASS
→ 03.C-2C
```

03.C-2C puede resolver microdecisiones técnicas de producción, pero no modificar semántica, relaciones, arquitectura, whitelist, blacklist, función, procedencia ni destino.

### Regla sobre 05

05 sigue siendo un **post-proceso**, no una skill de diseño ni de auditoría. Puede ejecutarse sobre capítulos cerrados directamente desde 03.E o después de 04.A/04.B. Su obligación es clasificar cada capítulo como:

- `APTO_PARA_COMPILAR`;
- `COMPILABLE_CON_ADVERTENCIAS`;
- `BLOQUEADO_PARA_COMPILACIÓN`.

Nunca corrige el capítulo para cambiar ese estado.

## 4. Cadena curricular central

### 4.1 01 — Documento Maestro v1.6

**Función:** crear la fuente única de verdad del curso.

La v1.6 incorpora como principio estructural la **trazabilidad de competencias**. Una competencia declarada debe tener cadena operativa:

```text
introduce → desarrolla → aplica → evalúa
```

Si falta un eslabón, la competencia queda huérfana y debe existir una decisión explícita: cubrir, reclasificar o retirar.

**Elementos críticos que ahora deben viajar downstream:**

- tabla 7.b de ponderación por subtema;
- actividades oficiales con IDs estables;
- matriz actividad × sesión;
- matriz de continuidad conceptual;
- matriz de trazabilidad de competencias §21;
- estado global del Documento Maestro: Completo / Condicionado / Incompleto;
- trazabilidad del origen del dato en §23.

**Salida contractual:** Documento Maestro v1.6.

### 4.2 02 — Briefs por Sesión v2.8

**Función:** convertir el Documento Maestro en briefs operativos por sesión y verificar que el conjunto de briefs sea responsable de las competencias declaradas.

Cambio clave de v2.8:

- contrato ampliado de **35 a 36 campos**;
- nuevo campo `Eslabones de competencia cubiertos`;
- matriz de cobertura de competencias;
- regla de bloqueo cuando queda un eslabón huérfano.

El brief individual ya no basta: el conjunto completo debe cubrir lo declarado en el Maestro.

**Upstream recomendado:** 01 v1.6.

**Downstream:** 03.A, 03.B, subsistema visual, 03.D y 03.E.

### 4.3 03.A — Ficha Teórica v1.12

**Función:** realizar la expansión conceptual controlada y clasificar cada concepto en:

- Núcleo;
- Panorama;
- Propedéutico;
- Contexto;
- Reservado.

La v1.12 incorpora **suficiencia conceptual por eslabón de competencia**. No basta con que la ficha esté completa: debe sostener los eslabones que el Brief declara.

Ejemplos de criterio:

- `introduce`: al menos un concepto relacionado;
- `desarrolla`: al menos un Núcleo desarrollado;
- `aplica`: Núcleo presente en bloque de aplicación;
- `evalúa`: Núcleo vinculado a la evidencia declarada.

Si no puede sostener el eslabón, reporta la brecha; no inventa conceptos ni modifica el Brief.

**Compatibilidad preferente:** Brief v2.8 + Doc Maestro v1.6.

### 4.4 03.B — Ficha Normativa v1.4

**Función:** construir el cuerpo normativo, reglamentario, institucional y regional que aplica al contenido.

Prioridad:

```text
NOM → NMX → reglamento mexicano → institución mexicana → normativa internacional
```

No decide qué enseñar y no resuelve recursos visuales.

**Compatibilidad:** acepta Brief v2.7 o superior; por tanto Brief v2.8 es compatible.

---

## 5. Subsistema visual

### 5.1 Regla arquitectónica principal

**03.C-1 es la única capa que decide la necesidad visual y su procedencia.**

Ningún downstream puede cambiar por iniciativa propia:

- procedencia;
- objetivo perceptivo;
- función didáctica;
- problema cognitivo;
- familia representacional;
- criterio de satisfacción.

### 5.2 03.C-1 — Orquestador Visual v1.2

**Pregunta que responde:**

> ¿Qué necesita verse para que el estudiante comprenda mejor, y qué estrategia visual debe resolverlo?

Produce NVD contractuales y clasifica cada una como:

- `EXTERNO`;
- `GENERATIVO`;
- `HÍBRIDO`;
- `NINGUNO`.

### 5.3 Rama generativa

```text
03.C-1
   ↓
03.C-2A v1.3 — diseña
   ↓
RGE_CERRADO_PARA_AUDITORÍA
   ↓
03.C-2B v1.1 — audita
   ├── RETURN → 03.C-2A
   └── PASS
         ↓
      03.C-2C — produce
```

#### 03.C-2A — Diseñador Generativo v1.2

- hereda el contrato de 03.C-1;
- define arquitectura visual, jerarquía, componentes y relaciones;
- fija whitelist y blacklist;
- construye el RGE ejecutable;
- usa el **Bloque E como fuente canónica interna**;
- cuando existe RGE cerrado, emite obligatoriamente el paquete de auditoría como espejo íntegro del Bloque E;
- no se autoaudita.

#### 03.C-2B — Auditor Semántico v1.0

Arquitectura congelada:

```text
Contrato → SCSO → SSE → IAS → PASS | RETURN
```

Reglas esenciales:

- audita el contrato congelado exacto;
- verifica identidad del paquete;
- usa SHA-256 sobre los bytes UTF-8 exactos del contrato;
- ancla evidencia a rangos literales del contrato;
- demuestra cobertura Contrato→SSE y SSE→IAS;
- no diseña, no corrige y no completa omisiones;
- un `PASS` queda ligado al RGE exacto auditado;
- cualquier cambio del RGE invalida el PASS anterior y exige nueva auditoría.

#### 03.C-2C

La referencia operativa conservada es **v1.3**. Su función en la arquitectura sigue siendo producir únicamente un RGE aprobado por 03.C-2B, sin alterar la semántica autorizada.

**Limitación de esta revisión:** no se recibió el archivo de 03.C-2C; su versión y contrato no fueron revalidados contra los demás archivos en esta ronda.

### 5.4 Rama externa — 03.C-3 BORRADOR v0.1

03.C-3 es paralela a la rama generativa.

Puede:

- localizar recursos auténticos;
- comparar candidatos;
- verificar correspondencia con la NVD;
- evaluar autenticidad, fidelidad técnica y legibilidad;
- registrar fuente, autoría, licencia y localizador;
- descargar/adquirir cuando sea viable;
- entregar `RECURSO_EXTERNO_RESUELTO`;
- devolver conflicto a 03.C-1.

No puede:

- cambiar procedencia;
- crear una NVD nueva;
- redirigir unilateralmente una necesidad a generación;
- alterar el objetivo perceptivo.

**Estado:** todavía es `BORRADOR v0.1`; no debe describirse como componente congelado del ecosistema.

### 5.5 Híbridos

Una NVD híbrida se resuelve con las dos ramas:

```text
componente externo → 03.C-3
componente generativo → 03.C-2A → 03.C-2B → 03.C-2C
```

El ensamblaje no autoriza reinterpretar la función cognitiva de ninguno de los componentes.

---

## 6. Productos didácticos

### 6.1 03.D — Composición Dual NUMA v2.1

**Salida:**

- `presentacion_sesion_N.md`;
- `guia_docente_sesion_N.md`.

03.D v2.1 es consumidor downstream del subsistema 03.C.

Entradas visuales:

- 03.C-1 v1.2;
- 03.C-3 cuando existe componente EXTERNO;
- RGE con `PASS` de 03.C-2B + `RECURSO_GENERATIVO_RESUELTO` de 03.C-2C cuando existe componente GENERATIVO;
- ambas ramas para HÍBRIDO.

#### Regla de integración sin reinterpretación

03.D puede decidir:

- ubicación;
- tamaño relativo;
- secuencia;
- relación texto–imagen;
- momento de explotación didáctica.

03.D no puede cambiar:

- procedencia;
- objetivo perceptivo;
- función;
- familia representacional;
- tratamiento externo;
- agrupación;
- criterio de satisfacción;
- identidad del recurso externo;
- semántica de un RGE aprobado.

#### Compuerta visual

Estados operativos:

- `ADMISIBLE_EXTERNO`;
- `ADMISIBLE_GENERATIVO`;
- `ADMISIBLE_HÍBRIDO`;
- `OMISIBLE_NO_CRÍTICO`;
- `BLOQUEO_VISUAL`.

Una NVD V1/V2 destinada a presentación o guía y no satisfecha bloquea el cierre completo.

El antiguo archivo `instrucciones_recursos_propios_sesion_N.md` deja de ser salida de 03.D: el diseño/producción generativa pertenece a 03.C-2A → 03.C-2B → 03.C-2C.

### 6.2 03.E — Capítulo de Libro Autónomo v2.4

03.E v2.4 comparte la misma frontera visual contractual que 03.D, pero la aplica a un producto autónomo para alumno.

Reglas específicas:

- solo integra NVD con destino `Capítulo: sí`;
- una NVD V1/V2 crítica debe estar resuelta antes de declarar el capítulo completo;
- no admite “imagen pendiente” en un capítulo final;
- preserva fuente, licencia y atribución de recursos externos;
- conserva trazabilidad NVD → recurso;
- mantiene IDs internos en zonas protegidas, no en la lectura normal del alumno;
- no altera semántica de recursos generativos con PASS.

La integración editorial puede resolver pies, ubicación y secuencia, pero no cambiar contratos upstream.

### 6.3 Estado de la interfaz visual downstream

**BRECHA CERRADA.**

Desde esta guía v4.1:

```text
03.C-1
   ├─ EXTERNO → 03.C-3
   ├─ GENERATIVO → 03.C-2A → 03.C-2B → 03.C-2C
   └─ HÍBRIDO → 03.C-3 + 03.C-2A → 03.C-2B → 03.C-2C
          ↓
paquete visual resuelto
          ↓
03.D v2.1 / 03.E v2.4
```

Ya no se considera vigente la antigua `Ficha Visual v1.8` como interfaz contractual de 03.D/03.E.

## 7. Auditoría y mejora: etapa 04

### 7.1 04.A — Auditoría de Coherencia v2.5

04.A v2.5 opera con **cuatro capas independientes**:

1. **Fase 0 — trazabilidad de competencias**;
2. **Fases A/B — coherencia de nivel**;
3. **Fase E — legibilidad editorial**;
4. **Fase V — fidelidad de integración visual**.

Secuencia:

```text
Fase 0 → Fase A → Fase B → Fase E → Fase V → Fase C
```

#### Fase V — frontera correcta

Fase V no vuelve a auditar la semántica del RGE.

Verifica downstream:

```text
NVD contractual
   ↓
recurso autorizado
   ↓
destino autorizado
   ↓
integración observada
```

Diagnósticos visuales:

- `Fidelidad visual plena`;
- `Fidelidad visual condicionada`;
- `Integración visual parcial`;
- `Integración visual incoherente`;
- `Bloqueo visual contractual`;
- `No aplicable`;
- `No verificable por falta de insumo`.

04.A identifica además el **propietario de corrección**.

#### Zona protegida

Los Anexos F de 03.D y Z de 03.E siguen siendo zonas internas legítimas para IDs y metadatos. No se penalizan por contener códigos.

### 7.2 04.B — Implementación de Mejoras v1.2

04.B sigue siendo **editorial, no diagnóstica**.

Consume 04.A v2.5 y aplica la regla de propiedad contractual.

Estados:

- `EJECUTABLE_DOWNSTREAM`;
- `ESCALAR_03C1`;
- `ESCALAR_03C2A_2B`;
- `ESCALAR_03C3`;
- `REGENERAR_03C2C`;
- `BLOQUEADA_FALTA_EVIDENCIA`.

Solo `EJECUTABLE_DOWNSTREAM` autoriza edición directa por 04.B. `REGENERAR_03C2C` significa repetir producción con el mismo PASS exacto, sin modificar el RGE.

Puede:

- restaurar recurso autorizado;
- corregir ubicación, pie o referencia;
- restaurar atribución;
- retirar sustitución no autorizada;
- reinstalar el recurso correcto.

No puede:

- seleccionar nuevo recurso externo;
- rediseñar o modificar RGE;
- declarar/modificar PASS o RETURN;
- cambiar procedencia, destino, función, tratamiento o criterio de satisfacción;
- generar un visual nuevo por iniciativa propia.

### 7.3 Bucle recomendado de calidad

```text
03.D / 03.E
     ↓
   04.A
     ↓
hallazgos + propuestas
     ↓
¿propietario downstream?
   ├─ sí → 04.B → documento revisado
   └─ no → retorno upstream correspondiente
                ↓
          regenerar / resolver
                ↓
             03.D / 03.E
                ↓
              04.A
```

La reauditoría 04.A es especialmente recomendable cuando se corrigieron brechas materiales de nivel, trazabilidad o fidelidad visual.

## 8. 05 — Compilador de Libro v1.1

05 es un post-procesador del ecosistema.

Entrada recomendada:

- 2 o más capítulos 03.E v2.4+;
- capítulos directamente cerrados o corregidos por 04.B;
- Documento Maestro o datos de asignatura para portada/identidad.

No audita y no corrige.

### Estados de compilabilidad

Cada capítulo debe clasificarse como:

- `APTO_PARA_COMPILAR`;
- `COMPILABLE_CON_ADVERTENCIAS`;
- `BLOQUEADO_PARA_COMPILACIÓN`.

En modo Flexible pueden entrar los dos primeros. Un capítulo bloqueado no se incluye silenciosamente.

### Verificaciones nuevas en v1.1

05 verifica además:

- integridad de assets visuales;
- asociación figura ↔ pie;
- rutas/localizadores;
- preservación de fuente, licencia y atribución;
- preservación íntegra del Anexo Z;
- ausencia de bloqueos visuales contractuales críticos;
- bibliografía consolidada sin renumerar citas internas de cada capítulo.

### Frontera funcional

05:

- compila;
- ordena;
- verifica el conjunto;
- preserva.

05 no:

- reaudita 03.E;
- implementa mejoras;
- revalida RGE;
- sustituye recursos externos;
- corrige capítulos;
- reinterpreta trazabilidad visual.

## 9. Cadenas de trazabilidad transversales

### 9.1 Competencias

```text
01 v1.6 (§21)
→ 02 v2.8 (Eslabones de competencia cubiertos + matriz de cobertura)
→ 03.A v1.12 (suficiencia conceptual)
→ 03.D / 03.E (desarrollo del producto)
→ 04.A v2.5 (auditoría de trazabilidad)
→ 04.B v1.2 (corrección, si se autoriza)
```

### 9.2 Ponderación

```text
01 tabla 7.b
→ 02 hereda pesos
→ 03.A hereda/calibra conceptos
→ 03.D distribuye tiempo
→ 03.E calibra extensión
→ 04.A contrasta coherencia del documento
```

### 9.3 Actividades oficiales

```text
01 IDs AC-NN / AI-NN
→ 02 actividad por sesión + estado + producto parcial
→ 03.D ejecución sincrónica
→ 03.E actividad vinculada
→ 04.A verifica trazabilidad y legibilidad
```

### 9.4 Continuidad conceptual

```text
01 matriz de continuidad conceptual
→ 02 continuidad por sesión
→ 03.A clasificación / reserva / propedéutico
→ 03.E continuidad explícita
→ 04.A verifica función curricular
```

### 9.5 Recursos visuales

```text
03.A + 03.B
→ 03.C-1
→ EXTERNO: 03.C-3
→ GENERATIVO: 03.C-2A → 03.C-2B → 03.C-2C
→ HÍBRIDO: ambas ramas
→ interfaz visual compatible
→ 03.D / 03.E
```

### 9.6 Legibilidad por audiencia

```text
03.D v2.1 / 03.E v2.4
→ política de audiencia + Anexo F/Z
→ 04.A Fase E
→ 04.B correcciones de legibilidad
```

---

## 10. Conceptos que no deben confundirse

### 10.1 Peso ≠ estado ≠ actividad

| Entidad | Describe | Fuente principal |
|---|---|---|
| **Peso pedagógico** | importancia relativa del subtema | 01 tabla 7.b |
| **Estado operativo** | impartida / próxima / pendiente | calendario de 01 |
| **Actividad oficial** | tarea formal del temario | 01 §7.c y §8 |

### 10.2 Concepto ≠ competencia

- **Concepto:** contenido disciplinar que puede ser Núcleo, Panorama, Propedéutico, Contexto o Reservado.
- **Competencia:** capacidad declarada que debe tener una cadena de eslabones operativos.

La matriz de continuidad conceptual y la matriz de trazabilidad de competencias son distintas y no se sustituyen.

### 10.3 NVD ≠ RGE ≠ recurso externo

- **NVD:** necesidad visual decidida por 03.C-1.
- **RGE:** contrato generativo ejecutable diseñado por 03.C-2A.
- **EXT / recurso externo:** recurso existente localizado y validado por 03.C-3.

### 10.4 Auditoría semántica ≠ auditoría académica/visual downstream

- **03.C-2B:** audita semántica de un RGE antes de generación.
- **04.A:** audita trazabilidad curricular, nivel académico, legibilidad y fidelidad de integración visual de un documento terminado.

04.A puede verificar que un recurso con PASS fue integrado correctamente, pero **no vuelve a certificar el RGE**.

No son intercambiables.

---

## 11. Matriz resumida de entradas y salidas

| Skill | Entrada mínima principal | Salida principal |
|---|---|---|
| 01 v1.6 | Temario + calendario + encuadre | Documento Maestro |
| 02 v2.8 | Documento Maestro con §21 | Briefs de 36 campos + matriz de cobertura |
| 03.A v1.12 | Brief v2.8 | Ficha Teórica |
| 03.B v1.4 | Brief v2.7+ | Ficha Normativa |
| 03.C-1 v1.2 | Brief + definición conceptual/normativa suficiente | Estrategia Visual / NVD |
| 03.C-2A v1.3 | NVD GENERATIVA/HÍBRIDA | diseño RGE + paquete cerrado para auditoría |
| 03.C-2B v1.1 | RGE congelado + paquete íntegro | PASS o RETURN + huella auditada |
| 03.C-2C v0.1 | RGE con PASS + huella exacta | RECURSO_GENERATIVO_RESUELTO + archivo + hash |
| 03.C-3 v0.1 | NVD EXTERNA/HÍBRIDA | recurso externo resuelto o conflicto upstream |
| 03.C-2C | RGE con PASS | recurso visual generado |
| 03.D v2.1 | Brief + 03.A + 03.B + 03.C-1 + recursos visuales admisibles | presentación + guía docente |
| 03.E v2.4 | Brief + 03.A + 03.B + 03.C-1 + recursos visuales admisibles + perfil | capítulo autónomo |
| 04.A v2.5 | documento + contexto + evidencia visual condicional | informe de cuatro capas + propuestas + propietario |
| 04.B v1.2 | documento + informe 04.A + perfil + evidencia condicional | documento revisado + registro + escalamiento |
| 05 v1.1 | 2+ capítulos compilables | libro + reporte de compilación |

## 12. Regeneración: qué rehacer cuando cambia algo

| Cambio | Regeneración mínima recomendada |
|---|---|
| Cambia temario, calendario, evaluación o competencias | Regenerar 01 → 02 → downstream afectado |
| Cambia §21 o un eslabón de competencia | 02 → 03.A → 03.C-1 si afecta lo visual → 03.D/03.E → 04.A |
| Cambia solo una sesión del Maestro | Brief de esa sesión + 03.A/03.B + visual + 03.D/03.E afectados |
| Cambia el Brief de una sesión | 03.A/03.B y todo downstream de esa sesión |
| Cambia 03.A | reevaluar 03.C-1 y regenerar 03.D/03.E afectados |
| Cambia 03.B | reevaluar 03.C-1 y productos que citen/usen la norma |
| Cambia una NVD en 03.C-1 | invalidar y rehacer ramas visuales asociadas + reintegrar 03.D/03.E |
| Cambia un RGE después de PASS | invalidar PASS → 03.C-2B de nuevo → 03.C-2C solo tras nuevo PASS |
| 03.C-2B emite RETURN | volver a 03.C-2A, corregir y reauditar íntegramente |
| 03.C-3 declara conflicto | volver a 03.C-1; 03.C-3 no cambia procedencia |
| Cambia un recurso externo validado | 03.C-3 → reintegrar 03.D/03.E → Fase V de 04.A |
| Cambia o se corrompe una producción generativa | si RGE/PASS no cambian, repetir 03.C-2C; si cambia contrato, volver a 03.C-2A → 03.C-2B → 03.C-2C |
| 04.A emite propuesta downstream | ejecutar 04.B |
| 04.A asigna propietario upstream | retornar a 03.C correspondiente; 04.B no corrige |
| 04.B modifica un documento | reauditar con 04.A si se requiere verificar cierre |
| Se corrige un capítulo | recompilar 05 |
| Se rompe un asset al compilar | corregir fuente/capítulo upstream; 05 no sustituye el recurso |
| Cambia perfil de estilo | regenerar 03.E o ejecutar revisión explícitamente autorizada |

## 13. Estados bloqueantes y rutas de retorno

| Condición | Acción correcta |
|---|---|
| Competencia huérfana sin decisión en 01 | No emitir Maestro como completo |
| Eslabón huérfano en conjunto de briefs | 02 se emite incompleto y se corrige upstream |
| Insuficiencia conceptual para eslabón | 03.A reporta; no inventa contenido |
| NVD sin contrato suficiente | 03.C-1 debe resolver antes de ejecutar ramas |
| RGE con RETURN | Regresa a 03.C-2A |
| RGE modificado después de PASS | Nueva auditoría 03.C-2B |
| Recurso externo no viable | CONFLICTO_UPSTREAM a 03.C-1 |
| NVD V1/V2 destinada a 03.D/03.E no satisfecha | Bloqueo visual del producto |
| Recurso generativo sin PASS | No ejecutar 03.C-2C; volver a 03.C-2A/03.C-2B según causa |
| Contrato recibido por 03.C-2C no coincide con huella auditada | Bloquear producción y volver a 03.C-2A/03.C-2B |
| Sustitución externa no autorizada | Restaurar recurso o volver a 03.C-3 |
| Cambio de destino/función/procedencia necesario | Volver a 03.C-1 |
| Propuesta visual de 04.A cuyo propietario no es downstream | 04.B escala; no edita |
| Audiencia no declarada y 04.B debe aplicar propuesta de legibilidad | Detener implementación hasta declarar audiencia |
| Capítulo `BLOQUEADO_PARA_COMPILACIÓN` | 05 no lo incluye |
| Asset crítico faltante en capítulo | 05 bloquea ese capítulo; no sustituye el asset |
| Capítulo faltante | 05 reporta hueco; no inventa capítulo |

## 14. Reglas de oro actualizadas

1. **01 es la fuente curricular primaria.**
2. **Toda competencia declarada debe tener trazabilidad o decisión explícita.**
3. **02 v2.8 verifica al conjunto de briefs, no solo a cada brief individual.**
4. **03.A no inventa conceptos para cubrir eslabones.**
5. **03.B prioriza normativa mexicana antes de internacional.**
6. **03.C-1 decide la estrategia visual; downstream no la reinterpreta.**
7. **03.C-2A diseña; 03.C-2B audita y autoriza; 03.C-2C ejecuta y produce.**
8. **Un PASS solo vale para el RGE exacto auditado y habilita producción, no integración.**
9. **Solo `RECURSO_GENERATIVO_RESUELTO` de 03.C-2C puede integrarse downstream.**
9. **03.C-3 resuelve recursos externos; no decide procedencia.**
10. **03.C-3 sigue siendo borrador hasta cierre formal.**
11. **03.D v2.1 y 03.E v2.4 consumen el subsistema visual nuevo.**
12. **Una NVD V1/V2 crítica no satisfecha bloquea el producto al que está destinada.**
13. **03.D y 03.E pueden explotar didácticamente un recurso, pero no cambiar su contrato.**
14. **Anexo F y Anexo Z son zonas protegidas de trazabilidad interna.**
15. **04.A v2.5 audita cuatro capas independientes.**
16. **04.A Fase V verifica integración; no recertifica RGE.**
17. **04.B v1.2 implementa solo correcciones downstream.**
18. **Toda corrección visual debe respetar su propietario contractual.**
19. **04.B no busca, selecciona, genera ni rediseña recursos visuales.**
20. **Después de una mejora material, 04.A puede verificar el cierre de forma independiente.**
21. **05 v1.1 compila; no corrige, no reaudita y no revalida recursos.**
22. **05 no incluye silenciosamente capítulos bloqueados.**
23. **05 preserva assets, pies, atribuciones, licencias y Anexo Z.**
24. **La bibliografía global no debe romper las citas internas de capítulos.**
25. **Conceptos, competencias, actividades y recursos visuales usan trazabilidades distintas.**
26. **Nunca ocultar una incompatibilidad de versión mediante una suposición silenciosa.**
27. **No tratar 03.C-2B y 04.A como el mismo tipo de auditoría.**
28. **Los documentos para alumno deben usar lenguaje natural; los códigos internos se conservan solo donde la política de audiencia los autoriza.**
29. **La interfaz visual downstream 03.C → 03.D/03.E se considera cerrada desde v2.1/v2.4.**
30. **El cierre global todavía depende de 03.C-3 estable y de revalidar 03.C-2C.**

## 15. Archivos esperados por asignatura

```text
/asignatura/
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
    registro_produccion_generativa_sesion_N.md
    /recursos_generados/

    ficha_recursos_externos_sesion_N.md          # cuando aplique 03.C-3
    /recursos_externos/

    presentacion_sesion_N.md
    guia_docente_sesion_N.md
    capitulo_N_[slug].md

    informe_04A_[documento].md                   # nombre operativo sugerido
    registro_cambios_04B_[documento].md          # si se ejecuta 04.B

  libro_[asignatura].md
  reporte_compilacion_[asignatura].md
```

Cambios respecto a v4.0:

- se elimina `instrucciones_recursos_propios_sesion_N.md` como salida esperada de 03.D;
- la trazabilidad de generación propia vive en 03.C-2A / 03.C-2B / 03.C-2C;
- los capítulos pueden contener Anexo Z interno y trazabilidad visual protegida;
- 05 preserva esos anexos por capítulo y no los consolida en un único anexo global.

> Los nombres de archivos de 04.A/04.B siguen siendo convenciones organizativas sugeridas salvo que sus ejecuciones fijen otro basename.

## 16. Antes de ejecutar el flujo completo

Verificar, como mínimo:

1. 01 es v1.6 y contiene §21, §22 y §23.
2. 02 es v2.8 y usa 36 campos.
3. 03.A es v1.12 y recibe `Eslabones de competencia cubiertos`.
4. 03.B es v1.4.
5. 03.C-1 es v1.2.
6. 03.C-2A es v1.2.
7. 03.C-2B es v1.0 y su interfaz es PASS/RETURN.
8. 03.C-3, si se usa, sigue tratándose como BORRADOR v0.1.
10. 03.D es v2.1.
11. 03.E es v2.4.
12. 04.A es v2.5.
13. 04.B es v1.2.
14. 05 es v1.1.
15. El perfil de estilo es v2.0 cuando 03.E o 04.B lo requieran.
16. Toda NVD V1/V2 destinada a un producto está satisfecha antes del cierre.
17. Todo generativo integrado tiene PASS trazable.
18. Todo externo integrado corresponde al recurso validado por 03.C-3.
19. Los productos para alumno no filtran códigos internos fuera de excepciones autorizadas.
20. Los Anexos F/Z se conservan como zonas protegidas.
21. 04.A no duplica 03.C-2B.
22. 04.B no ejecuta correcciones cuyo propietario sea upstream.
23. Antes de compilar con 05, cada capítulo tiene estado de compilabilidad válido.
24. Ningún capítulo bloqueado se incorpora silenciosamente al libro.

## 17. Brechas y tareas pendientes detectadas en esta revisión

### Prioridad alta — probar y cerrar 03.C-2C

`03.C-2C v0.1` ya cubre la función de producción material que faltaba en el nuevo subsistema visual.

Debe probarse con:

- un diagrama;
- una infografía;
- una comparativa;
- una escena sintética;
- una NVD híbrida.

La prueba debe validar:

- gate de `ID_RGE + HUELLA_RGE_AUDITADO + PASS`;
- producción sin reinterpretación;
- QA técnico;
- máximo de 2 intentos;
- hash del archivo;
- handoff `RECURSO_GENERATIVO_RESUELTO`;
- reutilización por hash desde el orquestador autónomo.

### Prioridad alta — cerrar 03.C-3

`03.C-3 BORRADOR v0.1` sigue siendo la pieza externa provisional.

Pendientes:

- contrato final de entrada/salida;
- estados terminales;
- derechos/licencias;
- handoff exacto hacia 03.D/03.E;
- comportamiento en HÍBRIDO;
- pruebas de conflicto y retorno a 03.C-1.

### Prioridad media — prueba punta a punta

Ejecutar una sesión real completa:

```text
01 → 02 → 03.A/B → 03.C-1
   → [03.C-2A → 03.C-2B → 03.C-2C] y/o 03.C-3
   → 03.D + 03.E
   → 04.A
   → 04.B si aplica
   → 04.A de cierre
   → 05
```

La prueba debe buscar incompatibilidades reales de handoff, no solo coherencia documental.

### Prioridad media — actualizar el orquestador autónomo

La skill `00.- SKILL_Orquestador-Autonomo-del-Flujo_v1.0` fue creada antes de incorporar 03.C-2C.

Debe actualizarse para:

- eliminar cualquier dependencia de 03Cbis;
- incorporar 03.C-2C;
- tratar `PASS` como autorización de producción;
- reutilizar `RECURSO_GENERATIVO_RESUELTO` por hash;
- regenerar 03.C-2C con el mismo PASS cuando solo falla/cambia el archivo;
- volver a 03.C-2A/2B si cambia el contrato.

## 18. Estado real del ecosistema

**Estado general: OPERATIVO Y ALINEADO, CON DOS PIEZAS 03.C AÚN EN BORRADOR.**

Cerrado o suficientemente estable para uso:

- 01 v1.6;
- 02 v2.8;
- 03.A v1.12;
- 03.B v1.4;
- 03.C-1 v1.2;
- 03.C-2A v1.3;
- 03.C-2B v1.1;
- 03.D v2.1;
- 03.E v2.4;
- 04.A v2.5;
- 04.B v1.2;
- 05 v1.1.

Piezas nuevas/provisionales:

- 03.C-2C v0.1 — ejecutor generativo;
- 03.C-3 v0.1 — recursos externos.

La antigua 03Cbis queda fuera de la arquitectura vigente.

El subsistema generativo actual es:

```text
03.C-1
→ 03.C-2A
→ 03.C-2B
   ├─ RETURN → 03.C-2A
   └─ PASS → 03.C-2C
                 ↓
      RECURSO_GENERATIVO_RESUELTO
```

El ecosistema no debe declararse completamente congelado hasta:

1. probar y cerrar 03.C-2C;
2. cerrar 03.C-3;
3. ejecutar al menos una prueba punta a punta.

## 19. Próxima secuencia recomendada de mantenimiento

```text
1. Probar 03.C-2C v0.1 con recursos reales
2. Corregir y congelar 03.C-2C
3. Cerrar 03.C-3 como versión estable
4. Actualizar 03.D / 03.E / 04.A / 04.B si aún contienen referencias heredadas
5. Actualizar 00 — Orquestador Autónomo
6. Ejecutar prueba punta a punta
7. Corregir solo defectos reproducibles de interfaz
8. Congelar contratos visuales
9. Diseñar 06 cuando el flujo académico esté congelado
```

No se recomienda recuperar 03Cbis. La responsabilidad que faltaba quedó separada en 03.C-2C.

---

**Última actualización:** 2026-10-11  
**Versión de la guía:** v4.2  
**Base de revisión:** 01 v1.6, 02 v2.8, 03.A v1.12, 03.B v1.4, 03.C-1 v1.2, 03.C-2A v1.3, 03.C-2B v1.1, 03.C-2C v0.1 BORRADOR, 03.C-3 v0.1 BORRADOR, 03.D v2.1, 03.E v2.4, 04.A v2.5, 04.B v1.2 y 05 v1.1.
**Mantenido por:** Ing. Christian Ramón Chi
