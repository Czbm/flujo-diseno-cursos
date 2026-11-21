---
name: 03c-2b-auditor-semantico
description: Audita semanticamente los disenos de RGE de 03.C-2A y emite dictamen vinculante PASS o RETURN antes de produccion.
stage_id: "03.C-2B"
version: "1.1"
status: stable
---

# Skill: 03.C - 2B — Auditor Semántico de Recursos Generativos — v1.1

## Estado del documento

**Tipo:** skill de auditoría semántica independiente  
**Origen arquitectónico:** separación de 03.C-2 en diseñador + auditor  
**Upstream contractual:** 03.C-2A — Diseñador de Recursos Generativos v1.3  
**Downstream inmediato:** 03.Cbis — Generador de Recursos Visuales, únicamente después de `PASS`  
**Interfaz de salida:** `PASS | RETURN`  
**Estado:** BORRADOR PARA PRUEBA REAL

---

# 0. Posición en el flujo

03.C-2B constituye la **capa independiente de auditoría semántica** del subsistema visual generativo.

Opera después de 03.C-2A y antes de 03.Cbis.

```text
03.C-1
   │
   ▼
03.C-2A
   │
   │ RGE_CERRADO_PARA_AUDITORÍA
   │ + espejo contractual íntegro del Bloque E
   ▼
03.C-2B
   │
   ├── PASS ─────► 03.Cbis
   │
   └── RETURN ───► 03.C-2A
```

03.C-2A diseña.  
03.C-2B audita.  
03.Cbis produce.

03.C-2B **no diseña, no corrige y no genera**.

---

# 1. Propósito

03.C-2B determina, de manera independiente, si cada RGE congelado:

1. contiene únicamente semántica autorizada;
2. mantiene correspondencia con sus fuentes declaradas;
3. no amplía silenciosamente el contenido disciplinar;
4. no contradice whitelist, blacklist ni contrato heredado;
5. no introduce valores, relaciones, equipos, normas, textos o afirmaciones sin soporte;
6. puede pasar a 03.Cbis sin requerir reinterpretación semántica.

Su resultado por RGE es exactamente uno de dos:

`PASS`

o:

`RETURN`

No existen resultados intermedios de aprobación.

---

# 2. Principio rector

## Auditar la superficie ejecutable exacta, no la intención del diseñador

03.C-2B no pregunta:

> “¿Qué quiso decir 03.C-2A?”

Pregunta:

> “¿Qué contenido exacto puede llegar a interpretar o producir 03.Cbis a partir de este contrato congelado y está todo ese contenido autorizado?”

La auditoría se realiza sobre la **superficie contractual recibida**, no sobre una reconstrucción, resumen o versión corregida por el auditor.

---

# 3. Frontera de competencia

## 3.1 Esta skill SÍ debe

1. recibir RGE congelados de 03.C-2A;
2. comprobar que el paquete es auditable;
3. identificar la superficie semántica ejecutable de cada RGE;
4. extraer de forma independiente las unidades semánticas auditables;
5. contrastarlas contra whitelist, blacklist y fuentes declaradas;
6. comprobar valores, cifras, unidades, fórmulas, nombres, categorías y relaciones;
7. detectar ampliaciones semánticas;
8. detectar contradicciones internas relevantes para producción;
9. emitir evidencia literal de cada fallo;
10. emitir `PASS` o `RETURN`;
11. asociar el veredicto al contrato exacto auditado;
12. impedir que un RGE distinto del auditado herede un `PASS`.

## 3.2 Esta skill NO debe

1. diseñar arquitectura visual;
2. cambiar motor;
3. cambiar formato;
4. reescribir instrucciones;
5. añadir whitelist;
6. eliminar blacklist;
7. proponer nuevo contenido disciplinar;
8. corregir textos dentro del RGE;
9. completar omisiones por inferencia;
10. cambiar el contrato de 03.C-1;
11. modificar prioridad, procedencia o función;
12. crear una versión “mejorada” del RGE;
13. producir la imagen final;
14. aprobar parcialmente un RGE;
15. convertir un `RETURN` en `PASS` por equivalencia aproximada;
16. reutilizar evidencia de una auditoría anterior sin volver a auditar el contrato recibido.

---

# 4. Insumos obligatorios y compatibilidad upstream

## 4.1 Paquete contractual de 03.C-2A

Archivo esperado:

`paquete_rge_para_auditoria_sesion_[N]_03c2a_v1.3.md`

Debe declarar:

- skill emisora = `03.C-2A — Diseñador de Recursos Generativos`;
- versión emisora = `v1.3`;
- estado = `RGE_CERRADOS_PARA_AUDITORÍA`;
- `IDENTIDAD_PAQUETE_BLOQUE_E = OK`;
- número de RGE;
- contratos RGE íntegros.

## 4.2 Ficha de Diseño Generativo fuente

También es obligatorio disponer de:

`ficha_diseno_generativo_sesion_[N]_03c2a_v1.3.md`

03.C-2B utiliza esta ficha únicamente para verificar de forma independiente la identidad entre:

`Bloque E de la ficha`

y:

`espejo contractual del paquete`.

03.C-2B no confía de forma automática en la declaración upstream `IDENTIDAD_PAQUETE_BLOQUE_E = OK`.

Debe verificarla nuevamente.

Resultado:

`IDENTIDAD_ENTRADA_VERIFICADA_POR_2B = OK | FALLA`

Si `FALLA`:

`PAQUETE_NO_AUDITABLE`

y no se inicia la auditoría semántica.

## 4.3 Compatibilidad de versión upstream

03.C-2B v1.1 consume exclusivamente paquetes emitidos por:

`03.C-2A v1.3`

Resultado:

`UPSTREAM_COMPATIBLE = OK | FALLA`

Si la versión emisora es distinta:

`UPSTREAM_COMPATIBLE = FALLA`

→ `PAQUETE_NO_AUDITABLE`

→ `AUDITORÍA_BLOQUEADA`

03.C-2B no debe auditar paquetes de versiones anteriores por conveniencia.

## 4.4 Fuentes semánticas de soporte

03.C-2B debe disponer de las fuentes citadas por las whitelist de los RGE cuando sean necesarias para verificar soporte.

Pueden incluir únicamente fuentes autorizadas explícitamente por el flujo o por el propio contrato RGE:

- 03.C-1;
- 03.A;
- 03.B;
- Brief de Sesión;
- Documento Maestro;
- otras fuentes explícitamente declaradas en la whitelist o contrato upstream.

03.C-2B no sustituye una fuente ausente por conocimiento general.

Si una afirmación marcada como `DISCIPLINAR_HEREDADO` exige soporte y la fuente declarada no está disponible:

`FUENTE_REQUERIDA_NO_DISPONIBLE`

→ `RETURN`.

## 4.5 Disciplina de fuentes

La evidencia de una fila IAS puede provenir únicamente de:

1. la fuente autorizante declarada en la whitelist relacionada;
2. el localizador declarado;
3. una fuente upstream explícitamente vinculante para ese mismo contenido.

Queda prohibido:

- añadir tratados, manuales o bibliografía externa no declarada;
- usar conocimiento general del auditor como soporte;
- justificar una fila con una fuente distinta solo porque “dice algo parecido”;
- cambiar silenciosamente la fuente autorizante.

Si la fuente declarada no soporta el contenido:

`F02_WHITELIST_SIN_SOPORTE`

No se permite salvar la fila con otra fuente.

## 4.6 Precedencia

Para decidir autorización semántica:

1. contrato heredado de 03.C-1;
2. fuente exacta declarada en whitelist;
3. blacklist;
4. contrato RGE congelado.

La whitelist no puede autorizar algo que contradiga una fuente upstream vinculante.

---

# 5. Unidad de auditoría

La unidad de decisión es un **RGE individual**.

Cada RGE se audita de forma independiente.

Ejemplo:

```text
RGE-01-01 → PASS
RGE-02-01 → RETURN
RGE-04-01 → PASS
```

Un fallo en un RGE no convierte automáticamente en `RETURN` a los demás.

El paquete global puede declarar:

- `AUDITORÍA_COMPLETA_CON_RETURNS`, si existe al menos un `RETURN`;
- `AUDITORÍA_COMPLETA_PASS`, si todos los RGE obtienen `PASS`.

Estos estados son informativos del paquete.  
El veredicto vinculante permanece por RGE.

---

# 6. Inmutabilidad del contrato auditado

03.C-2B trabaja sobre el contrato recibido.

Durante la auditoría queda prohibido:

- corregir ortografía dentro del RGE;
- reformular frases;
- sustituir términos;
- completar tablas;
- cambiar una cifra;
- resolver una ambigüedad por contexto;
- añadir una fuente;
- añadir una entrada de whitelist;
- eliminar una entrada de blacklist.

Si una modificación es necesaria:

`RETURN`

La corrección pertenece a 03.C-2A.

---

# 7. Huella del contrato auditado

Antes de auditar cada RGE, calcular una huella determinista del **contrato exacto recibido**.

Algoritmo:

`SHA-256`

Campo:

`HUELLA_RGE_AUDITADO`

## 7.1 Rango exacto de bytes

La huella se calcula sobre los bytes UTF-8 exactos comprendidos desde:

- el primer byte del encabezado `## E.RGE-XX-YY`

hasta:

- el último byte perteneciente al contenido de `### 20. Estado`.

Debe incluir:

- encabezados Markdown;
- saltos de línea internos;
- tablas;
- listas;
- signos;
- caracteres Unicode;
- bloques de código;
- backticks;
- espacios que formen parte del contenido contractual;
- valor completo del estado.

Debe excluir únicamente:

- el separador documental posterior al contrato;
- encabezados del siguiente RGE;
- contenido de portada o metadatos externos al contrato.

Queda prohibido:

- reconstruir el contrato antes de hashearlo;
- normalizar saltos de línea;
- normalizar Unicode;
- recortar espacios internos;
- eliminar backticks;
- resumir o volver a serializar el contrato.

## 7.2 Verificación de huella

Registrar además:

`LONGITUD_BYTES_RGE_AUDITADO`

y:

`LONGITUD_CARACTERES_RGE_AUDITADO`

La huella solo es válida si fue calculada sobre el mismo bloque contractual que será auditado.

Resultado:

`HUELLA_RGE_VÁLIDA = SÍ | NO`

Si `NO`:

`RETURN`.

## 7.3 Vinculación del veredicto

El veredicto queda vinculado a:

```text
ID_RGE
+
HUELLA_RGE_AUDITADO
```

Si cambia un byte del contrato:

`HUELLA_RGE_AUDITADO` cambia

y cualquier `PASS` anterior deja de ser aplicable.

03.Cbis deberá producir únicamente a partir del mismo contrato que recibió `PASS`.

---

# 7.4 Superficie Contractual Semántica de Origen — SCSO

La SCSO no se construye mediante selección libre del auditor.

03.C-2B debe recorrer de forma determinista las secciones contractuales auditables del RGE y asignar una disposición explícita a **cada ítem contractual identificable**.

No se añade ninguna capa previa a SCSO.

## 7.4.1 Secciones contractuales de recorrido obligatorio

Las siguientes secciones deben recorrerse siempre, cuando existan en el contrato RGE:

1. `### 1. Contrato pedagógico heredado`
2. `### 2. Objetivo operativo`
3. `### 3. Elementos obligatorios`
4. `### 4. Relaciones obligatorias`
5. `### 5. Elementos opcionales`
6. `### 6. Elementos prohibidos heredados`
7. `### 7. Arquitectura visual`
8. `### 8. Contrato gráfico ejecutable`
9. `### 9. Gramática visual`
10. `### 11. Integración híbrida`
11. `### 13. Whitelist semántica`
12. `### 14. Blacklist semántica`
13. `### 15. Instrucción final de producción`
14. `### 16. Criterios críticos`
15. `### 18. Restricciones`

Las demás secciones se revisan si contienen contenido ejecutable o semántico, pero no sustituyen este recorrido mínimo.

## 7.4.2 Unidad contractual de recorrido

Se considera **ítem contractual identificable** cualquiera de los siguientes:

- párrafo con afirmación o instrucción autónoma;
- elemento de lista;
- fila de tabla;
- relación enumerada `R1`, `R2`, `R3`, etc.;
- entrada de whitelist;
- entrada de blacklist;
- texto visible prescrito;
- criterio crítico;
- restricción;
- componente híbrido;
- bloque de instrucción que contenga una unidad semántica distinta.

Cada ítem contractual identificable recibe exactamente una disposición:

`AUDITAR`

o:

`EXCLUIR_CON_JUSTIFICACIÓN`

No existe disposición implícita.

## 7.4.3 Identificador SRC

Todo ítem contractual con disposición `AUDITAR` recibe:

`SRC-RGE-XX-YY-NNN`

Todo ítem con disposición `EXCLUIR_CON_JUSTIFICACIÓN` también recibe ID SRC para mantener contabilidad contractual.

Cada registro SRC debe contener:

| Campo | Contenido |
|---|---|
| ID SRC | `SRC-RGE-XX-YY-NNN` |
| RGE | ID del RGE |
| Sección contractual | localizador exacto |
| Índice de ítem | orden dentro de la sección |
| Rango byte en contrato | intervalo UTF-8 `[inicio, fin)` dentro del bloque RGE hasheado |
| Fragmento literal | texto exacto extraído de ese rango; no reconstruido |
| Disposición | `AUDITAR | EXCLUIR_CON_JUSTIFICACIÓN` |
| Clase preliminar | clase funcional |
| Requiere SSE | `SÍ | NO_JUSTIFICADO` |
| Justificación de exclusión | obligatoria si `NO_JUSTIFICADO` |

Regla obligatoria:

```text
Disposición = AUDITAR
IFF
Requiere SSE = SÍ
```

y:

```text
Disposición = EXCLUIR_CON_JUSTIFICACIÓN
IFF
Requiere SSE = NO_JUSTIFICADO
```

## 7.4.3 bis Anclaje literal al contrato hasheado

La SCSO debe derivarse exclusivamente del mismo bloque de bytes utilizado para calcular `HUELLA_RGE_AUDITADO`.

Queda prohibido:

- reconstruir el contrato desde memoria;
- resumirlo antes de extraer SRC;
- parafrasear el contenido contractual en `Fragmento literal`;
- sustituir relaciones, valores, fórmulas o textos por equivalentes;
- reutilizar contenido de una ejecución anterior;
- conservar una huella declarada mientras se audita otro texto.

Para cada SRC debe verificarse:

```text
FRAGMENTO_LITERAL_SRC
==
DECODE_UTF8(
  BYTES_CONTRATO[
    RANGO_BYTE_INICIO:RANGO_BYTE_FIN
  ]
)
```

Resultado por SRC:

`ANCLAJE_SRC = OK | FALLA`

Resultado agregado por RGE:

`ANCLAJE_LITERAL_CONTRATO = OK | FALLA`

Registrar:

```text
N_SRC_ANCLAJE_OK
N_SRC_ANCLAJE_FALLA
LISTA_SRC_ANCLAJE_FALLA
```

Solo puede declararse:

`ANCLAJE_LITERAL_CONTRATO = OK`

si:

```text
N_SRC_ANCLAJE_FALLA = 0
AND LISTA_SRC_ANCLAJE_FALLA = []
```

Si un fragmento SRC no puede reproducirse exactamente desde el bloque contractual hasheado:

`ANCLAJE_LITERAL_CONTRATO = FALLA`

→ `AUDITORÍA_BLOQUEADA`.

Esta compuerta no añade una nueva capa de auditoría; verifica la integridad de extracción de SCSO.

## 7.4.4 Regla de completitud del recorrido

Para cada sección contractual obligatoria debe registrarse:

```text
N_ITEMS_CONTRACTUALES_DETECTADOS
N_ITEMS_CON_DISPOSICIÓN
N_ITEMS_SIN_DISPOSICIÓN
```

Debe cumplirse:

```text
N_ITEMS_SIN_DISPOSICIÓN = 0
```

Si una sección contiene un ítem identificable sin disposición:

`RECORRIDO_CONTRACTUAL = INCOMPLETO`

→ `RETURN`.

Resultado agregado:

`RECORRIDO_CONTRACTUAL = COMPLETO | INCOMPLETO`

`RECORRIDO_CONTRACTUAL = COMPLETO` solo es válido si también:

`ANCLAJE_LITERAL_CONTRATO = OK`

## 7.4.5 Cobertura Contrato → SSE

Definir:

```text
CONJUNTO_SRC_REQUIERE_SSE =
{ID SRC donde Requiere SSE = SÍ}

CONJUNTO_SRC_CUBIERTO =
{ID SRC requeridos que son referenciados por una o más SSE válidas}

SRC_SIN_COBERTURA =
CONJUNTO_SRC_REQUIERE_SSE - CONJUNTO_SRC_CUBIERTO
```

Resultado:

`COBERTURA_CONTRATO_SSE = COMPLETA | INCOMPLETA`

Solo puede declararse `COMPLETA` si:

```text
RECORRIDO_CONTRACTUAL = COMPLETO
AND SRC_SIN_COBERTURA = ∅
```

## 7.4.6 Métricas SRC

Registrar:

```text
N_SRC_TOTAL
N_SRC_REQUIERE_SSE
N_SRC_NO_JUSTIFICADO
N_SRC_CUBIERTO
N_SRC_SIN_COBERTURA
LISTA_SRC_SIN_COBERTURA
RECORRIDO_CONTRACTUAL
COBERTURA_CONTRATO_SSE
```

Definición estricta:

```text
N_SRC_CUBIERTO =
número de IDs pertenecientes a CONJUNTO_SRC_REQUIERE_SSE
que aparecen en CONJUNTO_SRC_CUBIERTO
```

Por tanto:

```text
N_SRC_CUBIERTO <= N_SRC_REQUIERE_SSE
```

Los SRC `NO_JUSTIFICADO` no cuentan como cubiertos.

---

# 8. Superficie Semántica Ejecutable — SSE

## 8.1 Definición

La **SSE** es el conjunto de contenidos del RGE que pueden:

- aparecer visibles en el recurso;
- determinar una relación visual con significado disciplinar;
- ordenar a 03.Cbis representar una entidad, valor, categoría o proceso;
- condicionar la interpretación pedagógica del recurso.

## 8.2 Regla de identificación estable

Después de construir la SCSO, 03.C-2B descompone la superficie ejecutable en fragmentos semánticamente auditables y asigna a cada uno un identificador estable:

`SSE-RGE-XX-YY-NNN`

Cada ID SSE debe registrar:

| Campo | Contenido |
|---|---|
| ID SSE | identificador estable |
| RGE | ID del RGE |
| ID SRC origen | uno o más `SRC-RGE-XX-YY-NNN` |
| Localizador contractual | sección/campo exacto del RGE |
| Fragmento literal | texto exacto de origen |
| Clase preliminar | entidad, relación, valor, texto visible, restricción u otra clase |
| Requiere IAS | `SÍ | NO_JUSTIFICADO` |
| Justificación de exclusión | obligatoria si `NO_JUSTIFICADO` |

La numeración SSE se deriva del orden de aparición en el contrato auditado.

No puede fijarse de antemano un número objetivo de fragmentos.

Queda prohibido forzar cantidades uniformes entre RGE.

## 8.3 Reglas SRC → SSE

1. cada SSE debe citar al menos un `ID SRC origen`;
2. cada `ID SRC origen` debe existir en la SCSO del mismo RGE;
3. un SSE no puede cubrir un SRC de otro RGE;
4. un SRC puede originar varias SSE si contiene varias unidades ejecutables;
5. varias SRC pueden converger en una SSE solo cuando describen literalmente la misma unidad ejecutable;
6. la cobertura Contrato→SSE se demuestra por IDs, no por semejanza textual;
7. una SSE excluida como `NO_JUSTIFICADO` puede cubrir un SRC solo si ambos son puramente gráficos y la exclusión queda justificada.

## 8.4 Campos auditables

Como mínimo revisar:

- contrato pedagógico heredado;
- objetivo operativo;
- elementos obligatorios;
- relaciones obligatorias;
- elementos prohibidos;
- arquitectura cuando contiene etiquetas o relaciones semánticas;
- contrato gráfico cuando contiene valores disciplinarios o textos visibles;
- gramática visual cuando codifica significado;
- integración híbrida;
- whitelist;
- blacklist;
- instrucción final de producción;
- criterios críticos cuando introducen contenido semántico;
- restricciones cuando introducen contenido semántico.

## 8.5 Campos normalmente no semánticos

No requieren atomización disciplinar salvo que contengan contenido del dominio:

- coordenadas puramente gráficas;
- tamaños de cajas;
- píxeles;
- márgenes;
- códigos hex;
- opacidad;
- tipografía;
- convención de nombre de archivo.

Estos campos pueden marcarse:

`Requiere IAS = NO_JUSTIFICADO`

solo cuando exista una justificación explícita de que el fragmento es puramente gráfico y no comunica contenido disciplinar.

## 8.6 Regla de no omisión

Todo fragmento SSE con:

`Requiere IAS = SÍ`

debe estar referenciado por al menos una fila IAS.

Todo SRC con:

`Requiere SSE = SÍ`

debe estar referenciado por al menos una SSE.

Queda prohibido declarar cobertura completa si cualquiera de esas dos condiciones falla.

---

# 9. Inventario de Auditoría Semántica — IAS

03.C-2B utiliza un único inventario operativo:

**IAS — Inventario de Auditoría Semántica**

No utiliza cadenas de autoauditoría múltiples.

No utiliza SSP, IAV, MAC ni mecanismos equivalentes de autoclausura heredados de 03.C-2.

Esquema obligatorio:

| Campo | Contenido |
|---|---|
| ID IAS | `IAS-RGE-XX-YY-NNN` |
| RGE | ID del RGE |
| ID SSE origen | uno o más IDs `SSE-RGE-XX-YY-NNN` |
| Localizador SSE | campo y posición exacta de origen |
| Fragmento literal | texto exacto auditado |
| Unidad auditable | unidad semántica mínima |
| Tipo | un único valor del vocabulario controlado de §10 |
| Whitelist relacionada | ID o `NINGUNA` |
| Fuente autorizante | fuente declarada o `NINGUNA` |
| Localizador de fuente | localizador exacto o `NO_DISPONIBLE` |
| Fuente de evidencia | fuente realmente usada para sostener la decisión |
| Localizador de evidencia | localizador realmente usado |
| Blacklist relacionada | entrada o `NINGUNA` |
| Resultado | `AUTORIZADO | FALLA` |
| Código de fallo | código o `NINGUNO` |
| Evidencia literal | cita breve o paráfrasis estricta atribuible a la fuente/localizador de evidencia |

## 9.1 Regla de exhaustividad demostrable

El IAS no es una muestra representativa.

La cobertura se demuestra mediante los IDs SSE, no mediante conteos autodeclarados.

Definir:

```text
CONJUNTO_SSE_REQUIERE_IAS =
{ID SSE donde Requiere IAS = SÍ}

CONJUNTO_SSE_CUBIERTO =
{ID SSE referenciados por una o más filas IAS válidas}

SSE_SIN_COBERTURA =
CONJUNTO_SSE_REQUIERE_IAS - CONJUNTO_SSE_CUBIERTO
```

Resultado obligatorio:

`COBERTURA_IAS = COMPLETA | INCOMPLETA`

Solo puede declararse:

`COBERTURA_IAS = COMPLETA`

si:

```text
SSE_SIN_COBERTURA = ∅
```

Si existe cualquier ID SSE requerido no referenciado en IAS:

`COBERTURA_IAS = INCOMPLETA`

→ `RETURN`.

## 9.2 Reglas de correspondencia SSE → IAS

1. cada fila IAS debe citar al menos un `ID SSE origen`;
2. cada `ID SSE origen` citado debe existir en el registro SSE del mismo RGE;
3. un IAS no puede cubrir un ID SSE de otro RGE;
4. una fila IAS puede cubrir varios IDs SSE solo cuando la misma unidad auditable los abarque realmente;
5. un ID SSE puede aparecer en varias filas IAS si contiene más de una unidad semántica independiente;
6. la cobertura se calcula por presencia explícita de ID, no por similitud textual;
7. una fila IAS inválida o con `Resultado = FALLA` puede demostrar que el fragmento fue auditado, pero no autoriza su contenido;
8. un fragmento `NO_JUSTIFICADO` no entra al conjunto de cobertura, pero su exclusión debe quedar registrada.

## 9.3 Registro obligatorio de cobertura

Antes del veredicto por RGE registrar:

```text
N_SSE_TOTAL
N_SSE_REQUIERE_IAS
N_SSE_NO_JUSTIFICADO
N_SSE_CUBIERTO
N_SSE_SIN_COBERTURA
LISTA_SSE_SIN_COBERTURA
COBERTURA_IAS
```

`PASS` exige:

```text
N_SSE_SIN_COBERTURA = 0
AND LISTA_SSE_SIN_COBERTURA = []
AND COBERTURA_IAS = COMPLETA
```

Queda prohibido justificar cobertura únicamente porque:

`N_UNIDADES_IAS = N_FRAGMENTOS_SSE`

o porque ambos conteos coincidan.

La igualdad de conteos no demuestra correspondencia.

---

# 10. Unidad semántica auditable

Una unidad auditable es el fragmento mínimo que conserva una afirmación o prescripción semántica verificable.

Tipos controlados exactos:

- `CONCEPTO`
- `ENTIDAD`
- `EQUIPO`
- `TECNOLOGÍA`
- `CATEGORÍA`
- `RELACIÓN`
- `VALOR`
- `UNIDAD`
- `FÓRMULA`
- `NORMA`
- `PROCEDIMIENTO`
- `TEXTO_VISIBLE`
- `RESTRICCIÓN_SEMÁNTICA`
- `EJEMPLO_ILUSTRATIVO`
- `PARÁMETRO_GRÁFICO`

Cada fila IAS debe usar **exactamente un** tipo.

Queda prohibido crear valores no definidos como:

- `CONCEPTO / RELACIÓN`;
- `MAGNITUD / UNIDAD`;
- `PARÁMETRO_CONTROL`;
- `TAXONOMÍA`;
- `ENTIDAD_EVALUATIVA`;
- `RELACIÓN / CONECTOR`;
- cualquier combinación mediante `/`;
- cualquier sinónimo no incluido en la lista.

Resultado:

`VOCABULARIO_IAS = OK | FALLA`

Si aparece un tipo no permitido:

`VOCABULARIO_IAS = FALLA`

→ `RETURN`.

Reglas:

1. una cifra y su unidad forman una unidad auditable de tipo `VALOR` cuando la magnitud completa es la afirmación;
2. la unidad legal puede auditarse además mediante una fila separada `UNIDAD` si tiene relevancia normativa;
3. una lista de equipos se separa por equipo cuando cada nombre puede autorizarse de forma independiente;
4. una relación causal, jerárquica, de pertenencia, correspondencia o equivalencia se audita como `RELACIÓN`;
5. una frase que contiene dos afirmaciones independientes se divide;
6. una etiqueta visible exacta se audita como `TEXTO_VISIBLE` cuando su redacción específica importa;
7. no crear átomos que añadan palabras o significado ausente del fragmento fuente.

---

# 11. Regla de literalidad de extracción y evidencia

Toda fila IAS debe conservar:

- ID SSE de origen;
- fragmento literal de la SSE;
- localizador exacto;
- unidad auditable derivada sin introducir contenido nuevo.

Está prohibido fabricar evidencia para hacer coincidir una unidad con la whitelist.

La auditoría parte de la SSE y busca autorización.

Nunca parte de la whitelist para inventar qué “debió haber dicho” la SSE.

## 11.1 Evidencia estructurada

Cada fila IAS debe declarar explícitamente:

`Fuente autorizante`

`Localizador de fuente`

`Fuente de evidencia`

`Localizador de evidencia`

`Evidencia literal`

## 11.2 Correspondencia obligatoria

Para toda fila que requiera fuente:

```text
FUENTE_DE_EVIDENCIA == FUENTE_AUTORIZANTE
```

y:

```text
LOCALIZADOR_DE_EVIDENCIA == LOCALIZADOR_DE_FUENTE
```

Si cualquiera difiere:

`FUENTE_FILA = FALLA`

→ `FUENTES_IAS = FALLA`

→ `RETURN`.

## 11.3 Evidencia literal sin metadatos ocultos

La columna `Evidencia literal` contiene exclusivamente:

- una cita breve;
- o una paráfrasis estricta del contenido localizado.

No debe contener nombres de documentos, versiones, secciones, localizadores o fuentes.

Queda prohibido escribir dentro de `Evidencia literal` expresiones como:

- `03.A`;
- `03.B`;
- `03.C-1`;
- `Brief`;
- `Documento Maestro`;
- `§B.10`;
- `§D.NVD-...`;
- `NOM-...`;
- cualquier segundo localizador o referencia documental.

Toda procedencia documental debe aparecer exclusivamente en los cuatro campos estructurados de fuente/localizador.

Si `Evidencia literal` contiene una referencia documental o localizador:

`EVIDENCIA_CONTAMINADA = SÍ`

→ `FUENTE_FILA = FALLA`

→ `RETURN`.

## 11.4 Múltiples fuentes

Si una unidad necesita soporte de más de una fuente:

1. dividir la unidad en filas IAS separadas, una por fuente; o
2. usar múltiples fuentes solo si la whitelist upstream las declara explícitamente como parte del mismo permiso.

No se permite añadir una segunda fuente solo en el texto de evidencia.

## 11.5 Resultado agregado

Cada fila registra:

`FUENTE_FILA = OK | FALLA`

`EVIDENCIA_CONTAMINADA = SÍ | NO`

Y:

```text
FUENTES_IAS = AUTORIZADAS
IFF
todas las filas cumplen:
FUENTE_FILA = OK
AND EVIDENCIA_CONTAMINADA = NO
```

---

# 12. Clases de autorización

## 12.1 `HEREDADO_LITERAL`

Exige soporte suficiente en la fuente declarada.

Debe verificarse que:

- el concepto, entidad, relación o valor exista;
- no se haya ampliado su alcance;
- el localizador corresponda;
- el uso en la SSE sea compatible con el soporte.

## 12.2 `DIDÁCTICO_ILUSTRATIVO`

Puede autorizar valores o ejemplos no fijados upstream únicamente cuando:

- están declarados como ilustrativos;
- no contradicen el contrato heredado;
- no se presentan como reales, oficiales, normativos, típicos o universales;
- cumplen la justificación registrada.

## 12.3 `DERIVADO_CONTROLADO`

Solo puede cubrir contenido que se derive sin expansión semántica o parámetros de diseño no disciplinares.

No puede utilizarse para introducir:

- hechos nuevos;
- normas nuevas;
- equipos nuevos;
- valores disciplinares nuevos;
- relaciones disciplinares nuevas.

## 12.4 `GRÁFICO_INTERNO`

Parámetros puramente compositivos.

Debe fallar si un parámetro gráfico es presentado al estudiante como propiedad real del dominio.

---

# 13. Auditoría de whitelist

Para cada entrada de whitelist utilizada por la SSE, verificar:

1. que la entrada exista;
2. que su clase de valor sea compatible;
3. que la fuente declarada exista cuando se requiera;
4. que el localizador soporte la afirmación;
5. que el modo de uso corresponda;
6. que la justificación no amplíe el soporte;
7. que la SSE no exceda el contenido autorizado;
8. que la evidencia IAS proceda de la misma fuente y localizador declarados.

Una whitelist no se considera verdadera por estar escrita en el RGE.

03.C-2B debe contrastarla con la evidencia disponible.

Resultado adicional:

`FUENTES_IAS = AUTORIZADAS | FALLA`

Solo puede declararse `AUTORIZADAS` si todas las filas IAS que requieren fuente cumplen simultáneamente:

```text
FUENTE_EVIDENCIA = FUENTE_AUTORIZANTE_DECLARADA
AND LOCALIZADOR_EVIDENCIA = LOCALIZADOR_DECLARADO
AND SOPORTE_ENCONTRADO = SÍ
```

Si alguna fila:

- usa una fuente no declarada;
- usa un localizador distinto;
- se apoya en conocimiento general;
- usa una fuente alternativa para “salvar” el contenido;
- carece de soporte en la fuente declarada;

entonces:

`FUENTES_IAS = FALLA`

→ `RETURN`.

---

# 14. Auditoría de blacklist

Revisar la SSE contra todas las prohibiciones relevantes del RGE.

Si la SSE:

- ordena incluir un elemento prohibido;
- presupone una relación prohibida;
- introduce una marca prohibida;
- contradice una exclusión curricular;
- transforma un ejemplo en afirmación normativa;

resultado:

`FALLA`.

La ausencia de una entrada en whitelist no neutraliza una blacklist.

---

# 15. Auditoría de valores y magnitudes

Toda cifra o magnitud disciplinar visible debe ser:

- `DISCIPLINAR_HEREDADO` con soporte exacto; o
- `DIDÁCTICO_ILUSTRATIVO` correctamente declarado.

Comprobar:

- valor;
- unidad;
- signo;
- intervalo;
- igualdad/desigualdad;
- relación entre valores;
- significado asignado.

Ejemplo:

```text
Δh = 5 m
```

no queda autorizado únicamente porque upstream hable de equidistancia.

Debe existir soporte exacto o clasificación ilustrativa legítima.

---

# 16. Auditoría de relaciones

Toda relación semántica prescrita debe estar autorizada.

Auditar especialmente:

- causa → efecto;
- pertenencia;
- clasificación;
- correspondencia;
- equivalencia;
- contraste;
- secuencia;
- transformación;
- proyección;
- jerarquía.

No basta con que los nodos estén autorizados por separado.

La relación entre ellos también debe estar soportada o derivarse legítimamente sin expansión.

---

# 17. Auditoría de texto visible

Todo texto destinado a aparecer en el recurso debe ser evaluado como superficie final.

Comprobar:

- término técnico;
- afirmación;
- etiqueta;
- título semántico;
- leyenda;
- texto de síntesis;
- unidades;
- nomenclatura.

Una frase pedagógicamente razonable falla si introduce significado no autorizado.

---

# 18. Auditoría de integración híbrida

En RGE `HÍBRIDO`, 03.C-2B audita únicamente el componente generativo y su interfaz semántica con el componente externo.

Debe comprobar:

- que los slots externos no sean sustituidos por contenido inventado;
- que el componente generativo no presuponga atributos no garantizados del recurso externo;
- que la función cognitiva de cada componente permanezca separada;
- que el RGE no convierta una referencia externa futura en evidencia semántica ya disponible.

03.C-2B no audita licencia, URL ni calidad documental del recurso externo. Eso pertenece a 03.C-3.

---

# 19. Contradicciones internas

Un RGE falla si dos partes de su propia SSE prescriben significados incompatibles.

Ejemplos:

- whitelist permite una categoría y la instrucción usa otra;
- elemento obligatorio exige una relación y la instrucción la invierte;
- blacklist prohíbe una entidad y la instrucción la solicita;
- criterio crítico exige una magnitud diferente de la instrucción;
- contrato pedagógico y texto visible expresan relaciones opuestas.

Código:

`F09_CONTRADICCIÓN_INTERNA`

03.C-2B no elige cuál versión “debe prevalecer”.

Devuelve `RETURN`.

---

# 20. Códigos de fallo

Vocabulario inicial:

- `F01_CONTENIDO_NO_WHITELIST`
- `F02_WHITELIST_SIN_SOPORTE`
- `F03_VALOR_NO_AUTORIZADO`
- `F04_BLACKLIST_VIOLADA`
- `F05_RELACIÓN_NO_AUTORIZADA`
- `F06_TEXTO_VISIBLE_NO_AUTORIZADO`
- `F07_AMPLIACIÓN_SEMÁNTICA`
- `F08_ILUSTRATIVO_MAL_DECLARADO`
- `F09_CONTRADICCIÓN_INTERNA`
- `F10_FUENTE_REQUERIDA_NO_DISPONIBLE`
- `F11_PAQUETE_NO_AUDITABLE`
- `F12_OTRO_FALLO_SEMÁNTICO_JUSTIFICADO`

Cada fallo debe vincularse a evidencia literal.

---

# 21. Acciones requeridas en RETURN

03.C-2B no redacta la corrección.

Puede exigir únicamente una condición de corrección mediante:

- `ELIMINAR_CONTENIDO_NO_AUTORIZADO`
- `ALINEAR_CON_FUENTE_AUTORIZADA`
- `APORTAR_SOPORTE_EXACTO`
- `CORREGIR_CLASIFICACIÓN_DE_VALOR`
- `DECLARAR_COMO_ILUSTRATIVO`
- `CORREGIR_RELACIÓN`
- `RESOLVER_CONTRADICCIÓN`
- `REGENERAR_PAQUETE`
- `ESCALAR_A_03C1`

La acción indica **qué condición debe satisfacerse**, no el texto de reemplazo.

---

# 22. Regla de decisión por fila IAS

Una fila IAS recibe:

`AUTORIZADO`

solo si no existe una discrepancia material entre:

- unidad auditable;
- whitelist aplicable;
- fuente autorizante;
- localizador;
- clase de valor;
- blacklist;
- uso real en la SSE.

En cualquier otro caso:

`FALLA`.

No existe:

- `PARCIAL`;
- `CASI_AUTORIZADO`;
- `SEMÁNTICAMENTE_EQUIVALENTE`;
- `ACEPTABLE_POR_CONTEXTO`.

---

# 23. Regla de decisión por RGE

Un RGE obtiene `PASS` si y solo si:

```text
UPSTREAM_COMPATIBLE = OK
AND IDENTIDAD_ENTRADA_VERIFICADA_POR_2B = OK
AND PAQUETE_AUDITABLE = SÍ
AND HUELLA_RGE_VÁLIDA = SÍ
AND HUELLA_RGE_AUDITADO registrada
AND ANCLAJE_LITERAL_CONTRATO = OK
AND N_SRC_ANCLAJE_FALLA = 0
AND RECORRIDO_CONTRACTUAL = COMPLETO
AND N_SRC_SIN_COBERTURA = 0
AND LISTA_SRC_SIN_COBERTURA = []
AND COBERTURA_CONTRATO_SSE = COMPLETA
AND N_SSE_SIN_COBERTURA = 0
AND LISTA_SSE_SIN_COBERTURA = []
AND COBERTURA_IAS = COMPLETA
AND VOCABULARIO_IAS = OK
AND FUENTES_IAS = AUTORIZADAS
AND N_EVIDENCIAS_CONTAMINADAS = 0
AND N_FALLAS_IAS = 0
AND N_BLACKLIST_VIOLADA = 0
AND N_CONTRADICCIONES = 0
AND FUENTES_REQUERIDAS_DISPONIBLES = SÍ
```

Si cualquier condición falla:

`RETURN`

o, cuando la falla impida identificar o verificar el contrato de entrada:

`AUDITORÍA_BLOQUEADA`.

No se permite añadir nuevas capas de inventario para sostener esta decisión.

---

# 24. Formato de PASS

Por cada RGE aprobado:

```text
RGE: RGE-XX-YY
VEREDICTO: PASS
HUELLA_RGE_AUDITADO: [SHA-256]
LONGITUD_BYTES_RGE_AUDITADO: [n]
LONGITUD_CARACTERES_RGE_AUDITADO: [n]
ANCLAJE_LITERAL_CONTRATO: OK
N_SRC_ANCLAJE_FALLA: 0
RECORRIDO_CONTRACTUAL: COMPLETO
N_SRC_TOTAL: [n]
N_SRC_REQUIERE_SSE: [n]
N_SRC_NO_JUSTIFICADO: [n]
N_SRC_CUBIERTO: [n]
N_SRC_SIN_COBERTURA: 0
LISTA_SRC_SIN_COBERTURA: []
COBERTURA_CONTRATO_SSE: COMPLETA
N_SSE_TOTAL: [n]
N_SSE_REQUIERE_IAS: [n]
N_SSE_NO_JUSTIFICADO: [n]
N_SSE_CUBIERTO: [n]
N_SSE_SIN_COBERTURA: 0
LISTA_SSE_SIN_COBERTURA: []
COBERTURA_IAS: COMPLETA
VOCABULARIO_IAS: OK
FUENTES_IAS: AUTORIZADAS
N_EVIDENCIAS_CONTAMINADAS: 0
N_UNIDADES_AUDITADAS: [n]
N_FALLAS: 0
DESTINO_AUTORIZADO: 03.Cbis
```

---

# 25. Formato de RETURN

Por cada RGE devuelto:

| Campo | Contenido |
|---|---|
| RGE | `RGE-XX-YY` |
| Veredicto | `RETURN` |
| Huella auditada | SHA-256 |
| Código | `F01–F12` |
| Localizador SSE | ubicación exacta |
| Fragmento observado | texto literal |
| Unidad auditable | contenido puntual |
| Whitelist relacionada | ID o `NINGUNA` |
| Fuente declarada | fuente o `NINGUNA` |
| Evidencia | soporte o contradicción literal |
| Motivo | explicación breve y objetiva |
| Acción requerida | vocabulario de §21 |

Un RGE puede contener múltiples filas RETURN.

El veredicto global sigue siendo uno:

`RETURN`.

---

# 26. Reauditoría

Todo RGE corregido se audita desde cero.

Procedimiento:

1. recibir nuevo espejo contractual de 03.C-2A;
2. calcular nueva `HUELLA_RGE_AUDITADO`;
3. descartar como vinculantes los resultados IAS anteriores;
4. reconstruir la SSE;
5. reconstruir el IAS;
6. repetir toda la auditoría;
7. emitir nuevo `PASS` o `RETURN`.

No existe “PASS heredado” para las partes no modificadas.

El límite de ciclos lo gobierna 03.C-2A.

---

# 27. Escalamiento

Si el fallo no puede corregirse sin modificar decisiones propiedad de 03.C-1:

- procedencia;
- prioridad;
- objetivo perceptivo;
- mensaje central;
- familia representacional;
- criterio de satisfacción;
- estrategia visual;

03.C-2B debe indicar:

`ESCALAR_A_03C1`

y mantener:

`RETURN`.

03.C-2B no modifica el contrato upstream.

---

# 28. Handoff a 03.C-2C

Solo un RGE con `PASS` puede avanzar a 03.C-2C.

## 28.1 Significado exacto de PASS

En 03.C-2B:

```text
PASS = AUTORIZACIÓN_DE_PRODUCCIÓN
```

`PASS` no significa:

- recurso generado;
- recurso técnicamente verificado;
- recurso integrado;
- recurso listo por similitud visual.

La producción material pertenece exclusivamente a 03.C-2C.

## 28.2 Paquete mínimo de handoff

El handoff debe incluir:

- `ID_NVD`;
- `ID_RGE`;
- contrato RGE exacto auditado;
- `HUELLA_RGE_AUDITADO`;
- referencia al informe de auditoría;
- veredicto `PASS`;
- motor autorizado;
- formato;
- orientación / relación de aspecto;
- arquitectura;
- whitelist;
- blacklist;
- Style Lock cuando aplique;
- criterios y restricciones heredadas.

03.C-2B no recompila ni reescribe este contrato para producción.

## 28.3 Gate downstream obligatorio

03.C-2C debe comprobar antes de producir:

```text
ID_RGE_RECIBIDO = ID_RGE_AUDITADO
HASH_RGE_RECIBIDO = HUELLA_RGE_AUDITADO
VEREDICTO = PASS
```

Si la huella o la identidad no coinciden:

```text
CONTRATO_DISTINTO_DEL_AUDITADO
```

y la producción debe bloquearse.

## 28.4 Modificación post-PASS

Cualquier modificación contractual posterior al `PASS`, incluso si parece menor, produce:

```text
PASS_INVALIDADO
```

Ruta obligatoria:

```text
03.C-2A
→ nuevo RGE cerrado
→ 03.C-2B desde cero
→ nuevo PASS
→ 03.C-2C
```

No existe equivalencia por similitud.

## 28.5 Frontera de auditoría

03.C-2B audita el **contrato**.

03.C-2C verifica la **ejecución** del contrato aprobado.

03.C-2B no inspecciona ni aprueba archivos visuales producidos como parte de su `PASS`.

---

# 29. Estructura de salida

Archivo principal:

`ficha_auditoria_semantica_sesion_[N]_03c2b_v1.1.md`

Debe contener:

```text
A. Metadatos de auditoría
B. Compuerta de entrada
C. Registro de RGE y huellas
D. Verificación independiente de identidad Bloque E ↔ paquete
E. Auditoría por RGE
   E.n.1 Registro SCSO con IDs SRC
   E.n.2 Registro SSE con referencia a ID SRC
   E.n.3 IAS con referencia a ID SSE
   E.n.4 Cobertura Contrato → SSE
   E.n.5 Cobertura SSE → IAS
   E.n.6 Hallazgos
   E.n.7 Veredicto
F. Resumen de PASS / RETURN
G. Handoff a 03.Cbis
H. RETURN a 03.C-2A
```

03.C-2B no modifica el paquete de 03.C-2A.

---

# 30. Metadatos obligatorios de salida

La ficha debe declarar:

| Campo | Valor |
|---|---|
| Skill | `03.C-2B — Auditor Semántico de Recursos Generativos` |
| Versión | versión activa de 03.C-2B |
| Sesión | sesión auditada |
| Paquete fuente | nombre exacto |
| Versión 03.C-2A | versión declarada por el paquete |
| Fecha de auditoría | fecha |
| Total RGE | cantidad |
| PASS | cantidad |
| RETURN | cantidad |
| Estado global | estado informativo |

Estados globales:

- `AUDITORÍA_COMPLETA_PASS`
- `AUDITORÍA_COMPLETA_CON_RETURNS`
- `AUDITORÍA_BLOQUEADA`

---

# 31. Compuerta de entrada

Antes de auditar:

- [ ] paquete identificable;
- [ ] ficha de diseño fuente identificable;
- [ ] emisor = 03.C-2A;
- [ ] versión emisora = v1.3;
- [ ] `UPSTREAM_COMPATIBLE = OK`;
- [ ] estado contractual correcto;
- [ ] contratos RGE completos;
- [ ] IDs únicos;
- [ ] número de RGE coherente;
- [ ] identidad Bloque E ↔ paquete verificada independientemente por 03.C-2B;
- [ ] `IDENTIDAD_ENTRADA_VERIFICADA_POR_2B = OK`;
- [ ] fuentes requeridas disponibles o identificables.

La presencia de `IDENTIDAD_PAQUETE_BLOQUE_E = OK` en el paquete upstream es informativa, pero no sustituye la verificación independiente de 03.C-2B.

Si falla una condición estructural que impide saber qué contrato se audita:

`PAQUETE_NO_AUDITABLE`

y:

`AUDITORÍA_BLOQUEADA`.

No inventar contenido faltante.

---

# 32. Checklist de auditoría por RGE

## A. Integridad
- [ ] RGE identificable.
- [ ] estado contractual correcto.
- [ ] huella válida.

## B. Recorrido contractual
- [ ] SCSO extraída del mismo bloque byte a byte usado para `HUELLA_RGE_AUDITADO`.
- [ ] cada `Fragmento literal` coincide con su rango byte declarado.
- [ ] `ANCLAJE_LITERAL_CONTRATO = OK`.
- [ ] `N_SRC_ANCLAJE_FALLA = 0`.
- [ ] todas las secciones obligatorias recorridas.
- [ ] cada ítem contractual identificable tiene disposición.
- [ ] `N_ITEMS_SIN_DISPOSICIÓN = 0` en cada sección.
- [ ] `RECORRIDO_CONTRACTUAL = COMPLETO`.

## C. SRC
- [ ] cada ítem contractual tiene ID SRC.
- [ ] cada exclusión tiene justificación.
- [ ] `N_SRC_CUBIERTO <= N_SRC_REQUIERE_SSE`.

## D. Cobertura Contrato → SSE
- [ ] cada SRC requerido aparece en al menos una SSE.
- [ ] `SRC_SIN_COBERTURA = ∅`.
- [ ] `COBERTURA_CONTRATO_SSE = COMPLETA`.

## E. SSE
- [ ] IDs estables.
- [ ] referencia explícita a SRC.
- [ ] exclusiones justificadas.

## F. IAS
- [ ] referencia explícita a SSE.
- [ ] vocabulario cerrado.
- [ ] autorización evaluada.

## G. Cobertura SSE → IAS
- [ ] `SSE_SIN_COBERTURA = ∅`.
- [ ] `COBERTURA_IAS = COMPLETA`.

## H. Evidencia
- [ ] fuente autorizante declarada.
- [ ] localizador autorizante declarado.
- [ ] fuente de evidencia idéntica.
- [ ] localizador de evidencia idéntico.
- [ ] `Evidencia literal` no contiene nombres de fuentes ni localizadores.
- [ ] `N_EVIDENCIAS_CONTAMINADAS = 0`.
- [ ] `FUENTES_IAS = AUTORIZADAS`.

## I. Blacklist y coherencia
- [ ] cero violaciones de blacklist.
- [ ] cero contradicciones internas.

## J. Decisión
- [ ] todas las compuertas en OK → `PASS`.
- [ ] cualquier falla → `RETURN`.
- [ ] falla estructural de entrada → `AUDITORÍA_BLOQUEADA`.

---

# 33. Reglas de operación

1. Auditar el contrato recibido, no una interpretación.
2. No modificar el RGE.
3. No completar omisiones.
4. No diseñar soluciones.
5. Extraer IAS desde la SSE.
6. No fabricar evidencia desde whitelist.
7. Verificar soporte de whitelist cuando corresponda.
8. Auditar relaciones además de entidades.
9. Auditar valores además de conceptos.
10. Auditar textos visibles.
11. Aplicar blacklist.
12. Un solo fallo material obliga a `RETURN`.
13. `PASS` requiere cero fallas.
14. El veredicto se vincula a una huella exacta.
15. Cualquier cambio contractual invalida el PASS anterior.
16. Toda reauditoría inicia desde cero.
17. No usar conocimiento general para cubrir una fuente ausente.
18. No prescribir rediseño.
19. No generar recursos visuales.
20. Solo `PASS` puede avanzar a 03.Cbis.
21. 03.C-2B debe verificar independientemente Bloque E ↔ paquete.
22. No auditar paquetes de 03.C-2A distintos de v1.3 en esta versión.
23. IAS debe ser exhaustivo, no muestral.
24. Todo fragmento contractual potencialmente semántico debe tener ID SRC estable.
25. Todo SRC requerido debe estar referenciado por una SSE.
26. Todo fragmento SSE auditable debe tener ID estable.
27. Toda fila IAS debe referenciar explícitamente uno o más IDs SSE.
28. La cobertura se demuestra por diferencia de conjuntos en ambos enlaces: Contrato→SSE y SSE→IAS.
29. Todo tipo IAS debe pertenecer literalmente al vocabulario de §10.
30. No usar fuentes externas no declaradas para justificar una fila.
31. Toda fila IAS debe declarar fuente/localizador autorizante y fuente/localizador de evidencia.
32. Fuente y localizador de evidencia deben coincidir con los autorizantes.
33. La huella debe calcularse sobre bytes UTF-8 exactos del contrato recibido.
34. Todo SRC debe estar anclado a un rango byte del mismo contrato hasheado.
35. Un cambio de contenido con la misma huella declarada invalida la auditoría y bloquea el proceso.
36. La SCSO no puede reconstruirse desde una salida de auditoría anterior.

---

# 34. Criterio final de calidad

03.C-2B cumple si:

- audita de forma independiente;
- trabaja sobre la superficie ejecutable real;
- preserva evidencia literal;
- no confunde whitelist con prueba automática de verdad;
- detecta contenido no autorizado;
- detecta valores sin soporte;
- detecta relaciones no autorizadas;
- detecta blacklist violada;
- detecta contradicciones;
- no corrige el RGE;
- emite únicamente `PASS` o `RETURN`;
- un `PASS` queda vinculado al contrato exacto auditado;
- una reauditoría no hereda conclusiones anteriores.

La calidad de 03.C-2B se mide por **independencia, trazabilidad y capacidad de detectar desviaciones reales**, no por producir muchos artefactos de validación.

---

# 35. Prueba de regresión y criterio de cierre

v1.0 es la versión estable y cerrada de la arquitectura 03.C-2B.

## 35.1 Batería mínima de regresión

Debe detectar correctamente:

1. paquete upstream incompatible;
2. identidad Bloque E ↔ paquete falsa;
3. relación contractual omitida del recorrido;
4. ítem contractual sin disposición;
5. SRC requerido sin SSE;
6. SSE requerida sin IAS;
7. entidad no autorizada;
8. relación no autorizada;
9. cifra no autorizada;
10. blacklist violada;
11. tipo IAS no controlado;
12. fuente de evidencia distinta de la autorizante;
13. localizador de evidencia distinto;
14. evidencia literal que mencione una segunda fuente;
15. evidencia literal que incluya un segundo localizador;
16. conteo `N_SRC_CUBIERTO > N_SRC_REQUIERE_SSE`;
17. huella truncada o reconstruida;
18. mismo ID RGE con huella modificada;
19. contenido contractual distinto presentado con la misma huella declarada;
20. SRC cuyo `Fragmento literal` no coincida con su rango byte del contrato.

También debe existir al menos un caso limpio que produzca `PASS`.

## 35.2 Mutaciones deliberadas

La prueba final debe incluir mutaciones intencionales sobre contratos limpios.

Como mínimo:

- eliminar una relación Rn;
- insertar una entidad no whitelist;
- cambiar una cifra;
- cambiar una unidad;
- invertir una relación;
- introducir un término blacklist;
- cambiar una fuente de evidencia;
- añadir una segunda fuente dentro del texto de evidencia;
- eliminar una referencia SRC→SSE;
- eliminar una referencia SSE→IAS.

Cada mutación debe provocar `RETURN` o `AUDITORÍA_BLOQUEADA`, según corresponda.

## 35.3 Criterio de congelación

03.C-2B v0.5 puede congelarse si:

```text
TODOS_LOS_CASOS_LIMPIOS_ESPERADOS = PASS
AND TODAS_LAS_MUTACIONES_ESPERADAS = DETECTADAS
AND TODOS_LOS_SRC_ANCLADOS_AL_CONTRATO = SÍ
AND CERO_FALSOS_PASS
AND CERO_FALSOS_RETURN_EN_CASOS_LIMPIOS
```

No se exige demostrar que ningún LLM pueda cometer jamás una omisión.

No se añadirán nuevas capas de auditoría únicamente para perseguir fallos hipotéticos no observados.

La arquitectura de v1.0 se considera cerrada bajo estas reglas.

Los casos futuros que revelen un defecto real se atenderán mediante una nueva versión posterior únicamente si afectan el contrato funcional de la skill; no se abrirán nuevas capas preventivas por fallos hipotéticos.

---

# 35.1 Cambios v0.1 → v0.2

1. [Histórico v0.2] 03.C-2A v1.2 se volvió upstream compatible obligatorio en esa revisión.
2. La ficha de diseño fuente se vuelve insumo obligatorio para verificar Bloque E ↔ paquete.
3. `IDENTIDAD_PAQUETE_BLOQUE_E = OK` deja de aceptarse por confianza; 03.C-2B verifica independientemente.
4. Se introduce `IDENTIDAD_ENTRADA_VERIFICADA_POR_2B = OK | FALLA`.
5. Se introduce `UPSTREAM_COMPATIBLE = OK | FALLA`.
6. Se redefine la huella SHA-256 sobre bytes UTF-8 exactos del contrato y se registran longitudes.
7. IAS pasa de inventario potencialmente muestral a inventario exhaustivo.
8. Se introduce `COBERTURA_IAS = COMPLETA | INCOMPLETA`.
9. Se introduce `VOCABULARIO_IAS = OK | FALLA`.
10. Cada fila IAS debe usar exactamente un tipo del vocabulario controlado.
11. Se introduce `FUENTES_IAS = AUTORIZADAS | FALLA`.
12. Se prohíbe usar bibliografía, tratados o conocimiento general no declarados para justificar filas.
13. La fórmula de `PASS` incorpora compatibilidad upstream, identidad de entrada, huella válida, cobertura completa, vocabulario y fuentes autorizadas.
14. Se amplían las pruebas mínimas de regresión.

---

# 35.2 Cambios v0.2 → v0.3

1. La SSE deja de ser una lista descriptiva sin identidad y pasa a usar IDs estables `SSE-RGE-XX-YY-NNN`.
2. Cada fila IAS debe referenciar explícitamente uno o más IDs SSE de origen.
3. La cobertura deja de demostrarse por conteos y se calcula mediante diferencia de conjuntos.
4. Se introducen `CONJUNTO_SSE_REQUIERE_IAS`, `CONJUNTO_SSE_CUBIERTO` y `SSE_SIN_COBERTURA`.
5. Se prohíbe usar igualdad numérica entre SSE e IAS como evidencia de exhaustividad.
6. Se prohíbe fijar de antemano una cantidad objetivo o uniforme de fragmentos SSE por RGE.
7. Las exclusiones de SSE requieren `NO_JUSTIFICADO` con justificación explícita.
8. La evidencia IAS debe corresponder estrictamente a la fuente autorizante y al localizador declarados.
9. Se prohíben expresiones de soporte basadas en conocimiento general no localizado.
10. La fórmula de `PASS` exige lista vacía de SSE sin cobertura y disciplina estricta de evidencia.
11. Se mantienen sin cambios la arquitectura `SSE → IAS → PASS | RETURN`, la independencia de 03.C-2B y la prohibición de autocorrección.

---

# 35.3 Cambios v0.3 → v0.4

1. Se introduce la **Superficie Contractual Semántica de Origen — SCSO**.
2. Cada fragmento contractual potencialmente semántico recibe un ID `SRC-RGE-XX-YY-NNN`.
3. Se introduce cobertura demostrable `Contrato → SSE`.
4. Cada SSE debe referenciar uno o más IDs SRC.
5. Se introducen `CONJUNTO_SRC_REQUIERE_SSE`, `CONJUNTO_SRC_CUBIERTO` y `SRC_SIN_COBERTURA`.
6. `PASS` exige `COBERTURA_CONTRATO_SSE = COMPLETA`.
7. El IAS incorpora campos estructurados `Fuente de evidencia` y `Localizador de evidencia`.
8. Se introduce `FUENTE_FILA = OK | FALLA`.
9. Se exige coincidencia literal entre fuente/localizador autorizante y fuente/localizador de evidencia.
10. Se prohíbe ocultar fuentes adicionales dentro del texto libre de evidencia.
11. Se mantiene intacta la arquitectura general `Contrato → SCSO → SSE → IAS → PASS | RETURN`.
12. No se reintroducen SSP, IAV, MAC ni mecanismos de autoclausura heredados.

---

# 35.4 Cambios v0.4 → v0.5

1. SCSO deja de depender de selección libre y pasa a recorrido contractual obligatorio por sección.
2. Cada ítem contractual identificable recibe disposición explícita `AUDITAR | EXCLUIR_CON_JUSTIFICACIÓN`.
3. Se introduce `RECORRIDO_CONTRACTUAL = COMPLETO | INCOMPLETO`.
4. Se exige `N_ITEMS_SIN_DISPOSICIÓN = 0`.
5. Se corrige la definición de `N_SRC_CUBIERTO`: solo cuenta SRC requeridos efectivamente cubiertos.
6. Se impone `N_SRC_CUBIERTO <= N_SRC_REQUIERE_SSE`.
7. `Evidencia literal` deja de admitir nombres de fuentes, documentos o localizadores.
8. Se introduce `EVIDENCIA_CONTAMINADA = SÍ | NO`.
9. `PASS` exige `N_EVIDENCIAS_CONTAMINADAS = 0`.
10. Se define una batería de mutaciones deliberadas.
11. Se define un criterio explícito de congelación.
12. Se prohíbe añadir nuevas capas de auditoría para perseguir fallos hipotéticos no observados.
13. Se mantiene la arquitectura `Contrato → SCSO → SSE → IAS → PASS | RETURN`.

---

# 35.5 Cambios v0.5 → v1.0

1. Se congela la arquitectura `Contrato → SCSO → SSE → IAS → PASS | RETURN`.
2. Cada SRC incorpora `Rango byte en contrato`.
3. `Fragmento literal` debe provenir exactamente del mismo bloque UTF-8 usado para `HUELLA_RGE_AUDITADO`.
4. Se introduce `ANCLAJE_SRC = OK | FALLA`.
5. Se introduce `ANCLAJE_LITERAL_CONTRATO = OK | FALLA`.
6. Se introducen `N_SRC_ANCLAJE_OK`, `N_SRC_ANCLAJE_FALLA` y `LISTA_SRC_ANCLAJE_FALLA`.
7. Un contenido distinto con la misma huella declarada bloquea la auditoría.
8. Se prohíbe reconstruir SCSO desde memoria, paráfrasis o salidas de auditorías anteriores.
9. `PASS` exige anclaje literal íntegro al contrato hasheado.
10. Se cierra formalmente 03.C-2B como versión estable v1.0.

---

# 35.6 Cambios v1.0 → v1.1

1. Se actualiza upstream obligatorio de `03.C-2A v1.2` a `03.C-2A v1.3`.
2. Se elimina la antigua 03Cbis como downstream vigente; la mención queda únicamente como referencia histórica.
3. Se incorpora `03.C-2C v0.1 — Ejecutor de Recursos Generativos` como downstream exclusivo de producción.
4. Se formaliza `PASS = AUTORIZACIÓN_DE_PRODUCCIÓN`.
5. Se aclara que `PASS` no implica que exista un archivo visual.
6. Se amplía el handoff con `ID_NVD`, `ID_RGE`, contrato exacto, huella, PASS, motor, formato, arquitectura, whitelist, blacklist, Style Lock y restricciones.
7. Se hace obligatorio el gate de identidad en 03.C-2C.
8. Cualquier modificación post-PASS invalida el PASS.
9. Se conserva intacta la arquitectura congelada `Contrato → SCSO → SSE → IAS → PASS | RETURN`.
10. Se conserva la independencia de 03.C-2B: no diseña, no corrige y no produce.
11. Se distingue formalmente auditoría del contrato (2B) de verificación de ejecución (2C).
12. Se actualizan nombres de paquete/ficha upstream a v1.3 y salida 2B a v1.1.
13. Se corrige la referencia interna heredada que identificaba erróneamente a la propia skill como `v0.2`.

---

# 36. Estado de la versión

**Versión:** v1.1  
**Estado:** VIGENTE — CERRADA  
**Upstream compatible:** 03.C-2A v1.3  
**Downstream:** 03.Cbis únicamente después de `PASS`  
**Arquitectura congelada:** `Contrato → SCSO → SSE → IAS → PASS | RETURN`  
**Integridad de entrada:** Bloque E ↔ paquete verificada independientemente  
**Integridad contractual:** SHA-256 sobre bytes UTF-8 exactos  
**Anclaje SCSO:** cada SRC vinculado a rango byte del contrato hasheado  
**Recorrido contractual:** determinista por sección e ítem  
**Cobertura Contrato→SSE:** IDs SRC + diferencia de conjuntos  
**Cobertura SSE→IAS:** IDs SSE + diferencia de conjuntos  
**Vocabulario IAS:** cerrado  
**Evidencia:** fuente/localizador estructurados y texto libre descontaminado  
**Nuevas capas de auditoría:** PROHIBIDAS salvo revisión arquitectónica explícita futura  
**Autocorrección:** PROHIBIDA  
**Reescritura del RGE:** PROHIBIDA  
**Reauditoría tras RETURN:** DESDE CERO  
**Vinculación de PASS:** `ID_RGE + HUELLA_RGE_AUDITADO`  
**Criterio de mantenimiento:** solo defectos reales reproducibles justifican una versión posterior
