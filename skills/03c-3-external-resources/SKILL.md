---
name: 03c-3-external-resources
description: Resuelve, documenta y atribuye recursos visuales externos autorizados por el Orquestador Visual 03.C-1.
stage_id: "03.C-3"
version: "0.1"
status: draft
---

# Skill: 03.C - 3. External Resources — BORRADOR v0.1

## 0. Identidad y posición en el flujo

**Nombre formal:** `03.C - 3. External Resources`  
**Versión:** `BORRADOR v0.1`  
**Derivada de:** `03.C-ext — Visuales Externos v1.0`  
**Rol:** ejecutor de recursos visuales externos prescritos por `03.C-1 Orquestador Visual`.  
**Upstream canónico:** `03.C-1 v1.2` o versión posterior explícitamente compatible.  
**Downstream principal:** `03.D`, `03.E` y cualquier consumidor visual autorizado por el contrato NVD.  
**Relación con rama generativa:** paralela e independiente de `03.C-2A → 03.C-2B → 03Cbis`.

Arquitectura:

```text
03.C-1
  │
  ├─ procedencia = EXTERNO
  │       ↓
  │    03.C-3
  │       ↓
  │  RECURSO_EXTERNO_RESUELTO
  │       ↓
  │    03.D / 03.E
  │
  └─ procedencia = HÍBRIDO
          ↓
     ┌────┴────┐
     ↓         ↓
   03.C-3    03.C-2A → 03.C-2B → 03Cbis
     │         │
     └────┬────┘
          ↓
   RECURSO_HÍBRIDO_RESUELTO
          ↓
       03.D / 03.E
```

03.C-3 **no decide procedencia**.

03.C-3 **no crea una NVD nueva**.

03.C-3 **no redirige por sí misma una NVD hacia generación**.

Si la estrategia prescrita no puede resolverse externamente, devuelve un conflicto a `03.C-1` para revisión.

---

# 1. Propósito

03.C-3 se encarga exclusivamente de:

1. recibir necesidades visuales ya prescritas por 03.C-1 con procedencia `EXTERNO` o componente externo de `HÍBRIDO`;
2. localizar recursos auténticos existentes;
3. verificar su correspondencia con el contrato visual heredado;
4. evaluar autenticidad, fidelidad técnica, legibilidad y posibilidad real de uso;
5. registrar fuente, autoría, procedencia, derechos/licencia y localizador;
6. adquirir o descargar el recurso cuando sea técnicamente y jurídicamente viable;
7. registrar alternativas y descartes relevantes;
8. entregar un paquete externo resuelto y trazable;
9. devolver conflicto a 03.C-1 cuando ningún recurso satisfactorio pueda cumplir el contrato.

La pregunta que responde 03.C-3 es:

> **¿Qué recurso externo existente satisface exactamente esta NVD prescrita y cómo queda trazado para su uso posterior?**

No responde:

> ¿Qué debería visualizarse?

Eso pertenece a 03.C-1.

---

# 2. Frontera de competencia

## 2.1 03.C-3 SÍ puede

- buscar fotografías, planos, cartografía, documentos técnicos, manuales, capturas de software, cortes, despieces y otros recursos externos compatibles;
- comparar candidatos;
- seleccionar el candidato externo que mejor cumpla el contrato heredado;
- realizar recortes no semánticos, conversión de formato y optimización técnica cuando no alteren significado;
- descargar o conservar copia local cuando esté permitido y sea técnicamente posible;
- registrar ruta local o referencia persistente;
- documentar atribución, derechos y condiciones de uso;
- prescribir zoom, recorte de visualización o ubicación didáctica si no modifican contenido;
- registrar que una anotación requerida por 03.C-1 debe ser aplicada downstream cuando `tratamiento_externo = EXTERNO_CON_ANOTACIÓN`;
- declarar conflicto cuando la estrategia no sea viable.

## 2.2 03.C-3 NO puede

- cambiar `procedencia`;
- cambiar `tratamiento_externo`;
- cambiar objetivo perceptivo;
- cambiar problema cognitivo;
- cambiar mensaje cognitivo central;
- cambiar prioridad;
- cambiar función primaria o secundaria;
- cambiar familia representacional;
- cambiar número de unidades visuales prescritas;
- cambiar modo de agrupación;
- cambiar criterio de satisfacción;
- convertir `EXTERNO` en `GENERATIVO`;
- convertir `EXTERNO` en `HÍBRIDO`;
- convertir `EXTERNO_PURO` en `EXTERNO_CON_ANOTACIÓN` por iniciativa propia;
- inventar contenido que no exista en la fuente;
- redactar prompts o contratos de producción para IA;
- producir imágenes generativas;
- certificar recursos de la rama 03.C-2A/2B;
- modificar 03.A, 03.B, Brief o Documento Maestro.

---

# 3. Contrato de entrada desde 03.C-1

03.C-3 consume exclusivamente NVD cuyo contrato indique:

```text
procedencia = EXTERNO
```

o:

```text
procedencia = HÍBRIDO
componente_externo = requerido
```

Cada NVD debe aportar, como mínimo:

| Campo heredado | Regla |
|---|---|
| ID NVD | obligatorio |
| Concepto | literal |
| Problema cognitivo | no reinterpretar |
| Objetivo perceptivo | no reinterpretar |
| Mensaje cognitivo central | no reinterpretar |
| Familia representacional | obligatoria |
| Especificación representacional | obligatoria |
| Elementos necesarios | obligatorios |
| Elementos innecesarios | respetar |
| Prioridad | heredada |
| Función primaria | heredada |
| Funciones secundarias | heredadas |
| Procedencia | `EXTERNO` o `HÍBRIDO` |
| Tratamiento externo | `EXTERNO_PURO` o `EXTERNO_CON_ANOTACIÓN` |
| Unidades visuales estimadas | heredadas |
| Modo de agrupación | heredado |
| Destino | heredado |
| Restricciones | heredadas |
| Criterio de satisfacción | obligatorio |

Si falta un campo contractual imprescindible:

`ENTRADA_03C3 = INCOMPLETA`

→ no iniciar búsqueda contractual.

---

# 4. Fuente canónica y regla de no reinterpretación

La fuente canónica del encargo es el registro individual de NVD de 03.C-1.

03.C-3 puede consultar 03.A, 03.B, Brief, Documento Maestro y fuentes externas **solo para verificar candidatos**, nunca para redefinir el contrato visual.

Si una fuente secundaria contradice el contrato de 03.C-1:

```text
CONFLICTO_UPSTREAM
```

y se devuelve a 03.C-1.

No se corrige silenciosamente.

---

# 5. Estados de ejecución

Estado por NVD externa:

```text
PENDIENTE_BUSQUEDA
EN_BUSQUEDA
CANDIDATOS_LOCALIZADOS
RECURSO_SELECCIONADO
RECURSO_ADQUIRIDO
RECURSO_VERIFICADO
SATISFECHA
CONFLICTO_ESTRATEGIA_VISUAL
BLOQUEADA
```

Un NVD solo puede terminar en:

```text
SATISFECHA
```

o:

```text
CONFLICTO_ESTRATEGIA_VISUAL
```

o:

```text
BLOQUEADA
```

---

# 6. Tipologías externas reconocidas

Las familias externas deben ser compatibles con la `familia_representacional` heredada.

Tipologías operativas admitidas:

1. fotografía de instrumental;
2. fotografía de campo;
3. escena documental;
4. plano técnico;
5. cartografía auténtica;
6. mapa;
7. documento técnico;
8. manual técnico;
9. corte;
10. despiece;
11. vista de ocular o retícula;
12. captura de software;
13. visualización de datos existente;
14. gráfica existente;
15. esquema técnico publicado;
16. diagrama de procedimiento publicado;
17. fotografía documental de error, patología o condición real;
18. recurso técnico compuesto existente.

La tipología externa **no sustituye** la familia representacional de 03.C-1.

---

# 7. Estrategia de búsqueda

## 7.1 Orden de preferencia de fuentes

Cuando sea aplicable:

1. organismos oficiales;
2. normas, guías y documentos institucionales;
3. fabricantes y manuales técnicos primarios;
4. repositorios académicos institucionales;
5. publicaciones científicas o profesionales;
6. bibliotecas y archivos técnicos;
7. Wikimedia Commons u otros repositorios con procedencia verificable;
8. fuentes secundarias profesionales;
9. otras fuentes web verificables.

## 7.2 Regla de consulta

Las consultas deben derivarse de:

- concepto;
- familia representacional;
- rasgo de autenticidad indispensable;
- elementos necesarios;
- contexto geográfico si es vinculante;
- restricciones;
- criterio de satisfacción.

No se busca por estética genérica.

## 7.3 Búsqueda suficiente

Una búsqueda puede cerrarse cuando:

- existe al menos un candidato que cumple todos los criterios críticos;
- su procedencia es verificable;
- su uso posterior es técnicamente viable;
- no existe un candidato claramente superior entre las fuentes prioritarias razonables.

No se exige exhaustividad infinita de internet.

---

# 8. Registro de candidatos

Cada candidato recibe:

`CAND-EXT-[NVD]-NN`

Campos:

| Campo | Contenido |
|---|---|
| ID candidato | estable |
| ID NVD | heredado |
| Título/descriptor | breve |
| Tipo externo | controlado |
| Fuente | organización/autor |
| URL/localizador | exacto |
| Fecha o edición | si existe |
| Resolución/formato | si aplica |
| Autenticidad | `ALTA | MEDIA | BAJA` |
| Fidelidad técnica | `ALTA | MEDIA | BAJA | NO_VERIFICABLE` |
| Legibilidad | `APTA | CONDICIONADA | NO_APTA` |
| Derechos/licencia | estado registrado |
| Tratamiento requerido | debe coincidir con 03.C-1 |
| Cumplimiento contractual | `CUMPLE | PARCIAL | NO_CUMPLE` |
| Observaciones | breves |

---

# 9. Matriz de cumplimiento contractual

Cada candidato debe evaluarse contra el contrato heredado.

| Criterio | Resultado |
|---|---|
| Objetivo perceptivo satisfecho | `SÍ | NO` |
| Mensaje central preservado | `SÍ | NO` |
| Familia representacional compatible | `SÍ | NO` |
| Elementos necesarios presentes | `SÍ | NO` |
| Elementos innecesarios no dominantes | `SÍ | NO` |
| Rasgo de autenticidad cumplido | `SÍ | NO` |
| Restricciones respetadas | `SÍ | NO` |
| Tratamiento externo compatible | `SÍ | NO` |
| Legibilidad suficiente | `SÍ | NO` |
| Criterio de satisfacción cumplido | `SÍ | NO` |

Resultado:

```text
CANDIDATO_APTO = SÍ
```

solo si todos los criterios críticos son `SÍ`.

---

# 10. EXTERNO_PURO y EXTERNO_CON_ANOTACIÓN

## 10.1 EXTERNO_PURO

El recurso debe poder cumplir el objetivo sin:

- flechas añadidas;
- etiquetas añadidas;
- resaltados añadidos;
- callouts;
- cotas guía añadidas;
- overlays semánticos.

Se permiten únicamente transformaciones técnicas no semánticas como:

- recorte;
- redimensionamiento;
- cambio de formato;
- compresión;
- corrección de orientación;
- ajuste mínimo de contraste si no altera información.

## 10.2 EXTERNO_CON_ANOTACIÓN

03.C-3 selecciona el recurso base externo.

No inventa libremente la anotación.

Debe registrar:

- qué zonas del recurso soportan el objetivo;
- qué anotación ya fue prescrita por 03.C-1;
- qué consumidor downstream debe aplicarla;
- qué contenido no puede ocultarse o alterarse.

La anotación no convierte el recurso en `HÍBRIDO`.

---

# 11. Recursos HÍBRIDOS

Cuando `procedencia = HÍBRIDO`, 03.C-3 resuelve únicamente el componente externo.

Debe registrar:

```text
ID_COMPONENTE_EXTERNO
FUNCIÓN_COGNITIVA_EXTERNA
INTERFAZ_CON_COMPONENTE_GENERATIVO
DEPENDENCIA_DE_ENSAMBLE
```

03.C-3 no modifica ni audita el componente generativo.

La entrega híbrida final solo puede considerarse resuelta cuando ambos componentes autorizados están disponibles.

---

# 12. Selección del recurso externo

El recurso seleccionado recibe:

`EXT-[NVD]-NN`

La selección debe justificar explícitamente:

1. por qué cumple mejor el objetivo perceptivo;
2. qué elementos contractuales demuestra;
3. por qué su autenticidad es adecuada;
4. qué limitaciones conserva;
5. qué tratamiento downstream requiere.

No seleccionar un recurso únicamente por:

- resolución alta;
- apariencia estética;
- popularidad;
- disponibilidad inmediata;
- coincidencia temática superficial.

---

# 13. Derechos, licencia y uso permitido

03.C-3 **no presume** que todo recurso encontrado puede copiarse o redistribuirse.

Debe registrar:

```text
DERECHOS = DOMINIO_PUBLICO | LICENCIA_ABIERTA | LICENCIA_ESPECIFICA |
           COPYRIGHT_IDENTIFICADO | DERECHOS_NO_CLAROS
```

y:

```text
USO_PERMITIDO = DESCARGA_Y_REUTILIZACION |
                SOLO_REFERENCIA |
                REQUIERE_ATRIBUCION |
                REQUIERE_REVISION_MANUAL
```

Reglas:

- no afirmar `fair use` como autorización automática;
- no eliminar marcas de agua, créditos o avisos de copyright;
- no descargar saltando controles de acceso, autenticación o medidas técnicas;
- si el recurso es pedagógicamente óptimo pero no es reutilizable, puede conservarse como referencia y debe buscarse una alternativa utilizable;
- la atribución es obligatoria cuando corresponda.

---

# 14. Adquisición y persistencia

Cuando la adquisición sea permitida:

ruta objetivo:

```text
[CARPETA_SESION]/recursos_externos/
```

Convención:

```text
EXT_[NVD]_[NN]_[slug].[ext]
```

Ejemplo:

```text
EXT_NVD05_01_reticula_estadal.jpg
```

Registrar:

- nombre local;
- formato;
- tamaño;
- dimensiones;
- hash SHA-256 cuando exista archivo local;
- método de adquisición;
- integridad de apertura.

Estados de adquisición:

```text
ADQUIRIDO
REFERENCIA_REMOTA_VERIFICADA
REQUIERE_ADQUISICION_MANUAL
NO_ADQUIRIBLE
```

La imposibilidad de descarga automática no equivale por sí sola a fallo semántico.

---

# 15. Verificación del archivo adquirido

Cuando exista copia local:

```text
ARCHIVO_VALIDO = SÍ | NO
```

Verificar como mínimo:

- archivo abre correctamente;
- MIME/extensión coherentes;
- dimensiones utilizables;
- no es una página HTML de error;
- no está corrupto;
- contenido coincide con el candidato seleccionado.

No usar un umbral fijo de KB como prueba suficiente de validez.

---

# 16. Pauta de explotación didáctica

Por cada `EXT` seleccionado registrar:

### 16.1 Qué debe observarse

- elementos concretos que justifican la selección.

### 16.2 Qué debe señalar el docente

- puntos perceptivos directamente relacionados con el contrato NVD.

### 16.3 Pregunta detonadora

- una pregunta que obligue a leer el recurso, no solo recordarlo.

### 16.4 Error o confusión que ayuda a disipar

- solo si deriva del problema cognitivo heredado.

### 16.5 Limitaciones

- qué no debe inferirse del recurso.

03.C-3 no inventa una nueva intención pedagógica.

---

# 17. Registro de fuentes

Cada `EXT` seleccionado debe contener:

| Campo | Contenido |
|---|---|
| ID EXT | estable |
| Título | exacto o descriptor |
| Autor/organización | verificable |
| Año/edición | si existe |
| URL principal | exacta |
| URL de archivo | si existe |
| Fecha de consulta | ISO |
| Derechos/licencia | estado |
| Atribución requerida | texto |
| Localizador interno | página/figura/sección si aplica |

---

# 18. Registro de descartes

Registrar únicamente descartes relevantes que expliquen una decisión de selección o conflicto.

Campos:

| Campo | Contenido |
|---|---|
| ID candidato | estable |
| NVD | heredada |
| Fuente | breve |
| Motivo controlado | código |
| Evidencia | concreta |

Códigos:

```text
D01_NO_CUMPLE_OBJETIVO
D02_FALTA_ELEMENTO_CRITICO
D03_INAUTENTICO_O_NO_VERIFICABLE
D04_ERROR_TECNICO
D05_ILEGIBLE
D06_TRATAMIENTO_INCOMPATIBLE
D07_DERECHOS_NO_COMPATIBLES
D08_ACCESO_NO_VIABLE
D09_REDUNDANTE
D10_OTRO_JUSTIFICADO
```

---

# 19. Conflicto de estrategia visual

Si ningún candidato externo puede satisfacer el contrato, 03.C-3 no cambia de procedencia.

Debe emitir:

```text
CONFLICTO_DE_ESTRATEGIA_VISUAL
```

con uno de los códigos upstream compatibles:

```text
C01_NO_EXISTE_RECURSO_EXTERNO_ADECUADO
C02_RECURSO_EXTERNO_NO_CUMPLE_CRITERIO_SATISFACCION
C04_RIESGO_DE_ERROR_CONCEPTUAL
C05_AUTENTICIDAD_RESULTA_NECESARIA
C06_CONTROL_SEMANTICO_RESULTA_NECESARIO
C07_SOLUCION_HIBRIDA_RESULTA_NECESARIA
C08_RECURSO_PRESCRITO_ES_REDUNDANTE
C09_RESTRICCION_NORMATIVA_O_DOCUMENTAL
C10_OTRO_JUSTIFICADO
```

Paquete de retorno mínimo:

```text
ID_NVD
PROCEDENCIA_ACTUAL
TRATAMIENTO_EXTERNO
CODIGO_CONFLICTO
RESUMEN_BUSQUEDA
MEJOR_CANDIDATO_ENCONTRADO
CRITERIO_QUE_NO_CUMPLE
EVIDENCIA
ACCION_REQUERIDA = REVISION_03C1
```

Solo 03.C-1 puede cambiar procedencia o estrategia.

---

# 20. Criterio de satisfacción por NVD

Una NVD externa puede declararse `SATISFECHA` si y solo si:

```text
CANDIDATO_APTO = SÍ
AND FUENTE_VERIFICADA = SÍ
AND AUTENTICIDAD_ADECUADA = SÍ
AND TRATAMIENTO_COMPATIBLE = SÍ
AND CRITERIO_SATISFACCION_03C1 = CUMPLIDO
AND ESTADO_DERECHOS_REGISTRADO = SÍ
AND REFERENCIA_PERSISTENTE = SÍ
```

Si el contrato exige disponibilidad offline, además:

```text
ARCHIVO_VALIDO = SÍ
```

---

# 21. Documento de salida

Nombre:

```text
ficha_recursos_externos_sesion_[N]_03c3_v0.1.md
```

Bloques:

```text
A. Metadatos
B. Contratos NVD recibidos
C. Registro de búsqueda por NVD
D. Candidatos evaluados
E. Recursos externos seleccionados
F. Adquisición e integridad
G. Pautas de explotación didáctica
H. Fuentes, derechos y atribución
I. Descartes relevantes
J. Conflictos y retornos a 03.C-1
K. Resumen de cobertura
L. Handoff a downstream
M. Validación final
```

---

# 22. Handoff de recurso externo resuelto

Por cada recurso satisfecho:

```text
ID_NVD
ID_EXT
ARCHIVO_LOCAL | URL_PERSISTENTE
HASH_SHA256_LOCAL | NO_APLICA
FUENTE
LOCALIZADOR
DERECHOS
ATRIBUCION
TRATAMIENTO_EXTERNO
FUNCIÓN_PRIMARIA
DESTINO
CRITERIO_SATISFACCION = CUMPLIDO
ESTADO = RECURSO_EXTERNO_RESUELTO
```

Downstream no puede sustituir el recurso por otro sin nueva validación de 03.C-3.

---

# 23. Validación final

## 23.1 Contrato

- [ ] Todas las NVD procesadas provienen de 03.C-1.
- [ ] Solo se procesaron NVD `EXTERNO` o componentes externos `HÍBRIDO`.
- [ ] No se cambió ningún campo heredado.
- [ ] No se cambió procedencia.
- [ ] No se cambió tratamiento externo.

## 23.2 Selección

- [ ] Cada EXT tiene fuente verificable.
- [ ] Cada EXT cumple el objetivo perceptivo.
- [ ] Cada EXT cumple elementos necesarios.
- [ ] Cada EXT respeta restricciones.
- [ ] Cada EXT cumple criterio de satisfacción.

## 23.3 Derechos e integridad

- [ ] Derechos/licencia registrados.
- [ ] No se afirmó fair use como permiso automático.
- [ ] No se eliminaron marcas de agua o créditos.
- [ ] Adquisición registrada.
- [ ] Archivo local validado cuando aplica.

## 23.4 Frontera

- [ ] No se redactaron prompts.
- [ ] No se diseñaron RGE.
- [ ] No se auditó contenido generativo.
- [ ] No se reinterpretó 03.C-1.
- [ ] Todo conflicto vuelve a 03.C-1.

---

# 24. Reglas de operación

1. 03.C-1 manda sobre la intención visual.
2. 03.C-3 resuelve únicamente la procedencia externa.
3. Una buena imagen temática no equivale a una imagen contractual satisfactoria.
4. La autenticidad debe ser verificable.
5. La selección debe ser trazable.
6. Los derechos deben registrarse, no suponerse.
7. La descarga no puede evadir controles de acceso.
8. La anotación no convierte automáticamente un recurso en híbrido.
9. Un recurso híbrido conserva funciones cognitivas diferenciadas entre componente externo y generativo.
10. Ningún conflicto autoriza a 03.C-3 a cambiar estrategia.
11. Los descartes deben ser informativos, no exhaustivos.
12. La búsqueda debe cerrarse cuando existe evidencia suficiente de satisfacción o de conflicto.
13. No se exige perseguir exhaustividad infinita de internet.
14. Los recursos downstream deben conservar atribución y trazabilidad.
15. Cualquier sustitución posterior requiere revalidación.

---

# 25. Estado de la versión

**Versión:** BORRADOR v0.1  
**Estado:** LISTA PARA REVISIÓN ARQUITECTÓNICA  
**Origen:** 03.C-ext v1.0  
**Arquitectura:** `03.C-1 → 03.C-3 → recurso externo resuelto | conflicto → 03.C-1`  
**Cambio principal:** 03.C-3 deja de descubrir necesidades visuales y pasa a ejecutar contratos NVD externos ya prescritos.  
**Generación IA:** fuera de competencia.  
**Cambio de procedencia:** prohibido.  
**Derechos:** registro explícito obligatorio.  
**Descarga:** condicionada por viabilidad técnica y derechos; no se evade acceso.  
**Downstream:** 03.D / 03.E y consumidores autorizados por 03.C-1.
