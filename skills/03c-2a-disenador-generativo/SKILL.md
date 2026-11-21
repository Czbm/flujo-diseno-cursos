---
name: 03c-2a-disenador-generativo
description: Disena especificaciones tecnicas y pedagogicas para Recursos Generativos Educativos (RGE) solicitados por 03.C-1.
stage_id: "03.C-2A"
version: "1.3"
status: stable
---

# Skill: 03.C - 2A — Diseñador de Recursos Generativos — v1.3

## Estado del documento

**Tipo:** skill estable de diseño generativo  
**Origen:** 03.C - 2.generative v1.9  
**Upstream contractual:** 03.C - 1. Skill - orquestador-visual v1.2  
**Downstream inmediato:** 03.C - 2B — Auditor Semántico de Recursos Generativos  
**Downstream posterior:** 03.C-2C — Ejecutor de Recursos Generativos v0.1  
**Estado:** VERSIÓN ESTABLE

---

# 0. Posición en el flujo

03.C-2A constituye la **capa de diseño generativo** del subsistema visual.

Opera después de 03.C-1 y únicamente sobre NVD cuyo contrato canónico declare:

- `procedencia = GENERATIVO`; o
- `procedencia = HÍBRIDO` y exista un componente generativo asignado a 03.C-2A.

Su función es convertir una prescripción visual ya decidida por 03.C-1 en uno o más **Recursos Generativos Ejecutables — RGE**, cerrados desde el punto de vista de diseño, pero **todavía no autorizados para producción**.

03.C-2A diseña.  
03.C-2B audita y autoriza o devuelve.  
03.C-2C produce el recurso generativo aprobado.

```text
[01] Documento Maestro
        │
        ▼
[02] Brief de Sesión
        │
        ├──────────────► [03.A] Ficha Teórica
        │
        └──────────────► [03.B] Ficha Normativa
                               │
                               ▼
                 [03.C-1] Orquestador Visual
                               │
                  GENERATIVO / HÍBRIDO
                               │
                               ▼
                  [03.C-2A] Diseñador
                               │
                    RGE_CERRADO_PARA_AUDITORÍA
                               │
                               ▼
                  [03.C-2B] Auditor Semántico
                         │             │
                       PASS          RETURN
                         │             │
                         ▼             └────► 03.C-2A
                  [03.C-2C] Ejecutor Generativo
                         │
                         ▼
             RECURSO_GENERATIVO_RESUELTO
                         │
                  ┌──────┴──────┐
                  ▼             ▼
                [03.D]        [03.E]
```

---

# 1. Propósito

03.C-2A transforma cada NVD generativa prescrita por 03.C-1 en uno o más **Recursos Generativos Ejecutables — RGE**.

Para cada NVD aplicable debe:

1. heredar sin modificar el contrato pedagógico de 03.C-1;
2. crear la arquitectura visual detallada;
3. definir jerarquía, componentes y relaciones;
4. aplicar el Style Lock vigente;
5. construir el contrato gráfico ejecutable;
6. fijar whitelist y blacklist semánticas;
7. clasificar cualquier valor visible no heredado;
8. elegir motor de producción y formato;
9. redactar una instrucción de producción autosuficiente;
10. definir criterios de aceptación críticos y secundarios;
11. declarar restricciones;
12. preparar un RGE estable que 03.C-2B pueda auditar sin reinterpretar;
13. mantener trazabilidad `NVD → RGE`.

03.C-2A **no certifica** que el RGE esté semánticamente cerrado.

Su salida es:

**Ficha de Diseño Generativo de la Sesión**

y, cuando exista al menos un RGE en estado `RGE_CERRADO_PARA_AUDITORÍA`, obligatoriamente:

**Paquete de RGE Cerrados para Auditoría**, emitido como espejo contractual íntegro del Bloque E para 03.C-2B.

---

# 2. Principio rector

## 03.C-2A diseña la solución; no redefine la necesidad y no se autoaudita

03.C-1 decide:

> qué necesita verse, por qué, con qué familia representacional, prioridad, procedencia, función y criterio de satisfacción.

03.C-2A decide:

> cómo se construye el componente generativo para satisfacer esa prescripción.

03.C-2B decide:

> si el RGE final contiene exclusivamente contenido autorizado y puede avanzar a producción mediante `PASS`, o debe regresar mediante `RETURN`.

03.C-2C decide únicamente microdecisiones técnicas de ejecución compatibles con el contrato exacto auditado y produce el archivo final trazable.

---

# 3. Frontera de competencia

## 3.1 Esta skill SÍ debe

1. Consumir la Ficha de Estrategia Visual vigente.
2. Filtrar NVD `GENERATIVO` y componentes generativos de NVD `HÍBRIDO`.
3. Heredar el ID `NVD-XX`.
4. Crear IDs `RGE-XX-YY`.
5. Diseñar arquitectura visual detallada.
6. Definir jerarquía interna.
7. Definir relaciones obligatorias.
8. Definir gramática visual de relaciones.
9. Definir retícula y composición.
10. Aplicar Style Lock.
11. Crear contrato gráfico ejecutable.
12. Crear whitelist semántica.
13. Crear blacklist semántica.
14. Clasificar valores visibles.
15. Elegir motor de producción.
16. Elegir formato, orientación, relación de aspecto y resolución.
17. Redactar instrucciones de producción autosuficientes.
18. Definir criterios de aceptación.
19. Definir restricciones.
20. Resolver integración híbrida cuando aplique.
21. Entregar el RGE a 03.C-2B en estado `RGE_CERRADO_PARA_AUDITORÍA`.
22. Corregir un RGE devuelto por 03.C-2B sin alterar el contrato upstream.
23. Reportar conflicto a 03.C-1 cuando una corrección exija cambiar la estrategia visual.

## 3.2 Esta skill NO debe

1. Decidir qué conceptos requieren apoyo visual.
2. Crear nuevas NVD por iniciativa propia.
3. Cambiar procedencia.
4. Cambiar prioridad.
5. Cambiar función primaria o secundaria.
6. Cambiar problema cognitivo.
7. Cambiar objetivo perceptivo.
8. Cambiar mensaje cognitivo central.
9. Cambiar criterio de satisfacción.
10. Buscar recursos externos.
11. Resolver licencias.
12. Generar el archivo visual final.
13. Inventar contenido disciplinar.
14. Inventar datos, medidas, normas, fórmulas o fuentes.
15. Asignar slides exactos no heredados.
16. Usar 03.C v1.11 como dependencia operacional.
17. Reinterpretar silenciosamente una NVD difícil.
18. Construir inventarios, matrices o pruebas de auditoría semántica propias de 03.C-2B.
19. Declarar resultados de clausura o aprobación semántica.
20. Declarar estados de producción reservados a 03.C-2C.
21. Auditar su propia instrucción final.
22. Autorizar directamente la producción sin PASS de 03.C-2B.

---

# 4. Insumos y precedencia contractual

## 4.1 Insumo obligatorio principal

`ficha_estrategia_visual_sesion_[N]_v1.2.md`

Debe encontrarse en:

`LISTA_PARA_EJECUCIÓN`

o contener NVD explícitamente autorizadas para reejecución.

## 4.2 Insumos de contexto

- Documento Maestro vigente.
- Brief de Sesión vigente.
- 03.A — Ficha Teórica vigente.
- 03.B — Ficha Normativa vigente, cuando aplique.
- `lineamientos_visuales_[asignatura]_vigente.md`, cuando exista.

## 4.3 Precedencia

Cuando exista contradicción:

1. contrato canónico de la NVD en 03.C-1;
2. Documento Maestro;
3. Brief;
4. 03.A;
5. 03.B;
6. Style Lock, únicamente para decisiones formales.

03.C-2A no debe resolver contradicciones pedagógicas por inferencia.

## 4.4 Fuentes semánticas permitidas

Todo contenido disciplinar visible debe derivar de:

- 03.C-1;
- Brief;
- 03.A;
- 03.B;
- Documento Maestro.

Cualquier fuente diferente requiere devolución al upstream correspondiente.

---

# 5. Compuerta de elegibilidad

Una NVD es elegible si:

```text
procedencia = GENERATIVO
```

o:

```text
procedencia = HÍBRIDO
y
componente generativo asignado = 03.C-2A
```

No es elegible si:

- `procedencia = EXTERNO`;
- `procedencia = NINGUNO`;
- está bloqueada por 03.C-1;
- carece de criterio de satisfacción;
- la prescripción requiere modificar decisiones que pertenecen al Orquestador.

---

# 6. Contrato heredado de 03.C-1

Para cada NVD se heredan como vinculantes:

- ID NVD;
- concepto;
- problema cognitivo;
- objetivo perceptivo;
- mensaje cognitivo central;
- familia representacional;
- especificación representacional;
- elementos necesarios;
- elementos innecesarios;
- prioridad;
- función primaria;
- funciones secundarias;
- unidades visuales;
- modo de agrupación;
- destino;
- restricciones;
- criterio de satisfacción;
- procedencia;
- tratamiento externo, cuando aplique a híbridos.

03.C-2A puede operacionalizar estos campos, nunca sustituirlos.

---

# 6.1 Regla de canonicalidad interna, vistas derivadas y espejo contractual

Dentro de 03.C-2A, el **Bloque E — Contratos RGE** es la única fuente canónica interna para cada recurso.

Se distinguen dos clases de salida secundaria:

### A. Vistas derivadas compactas

Incluyen:

- tablas consolidadas;
- índices;
- estados por NVD;
- resúmenes de trazabilidad;
- síntesis arquitectónicas.

Estas vistas son **no autoritativas**.

Una vista derivada compacta **no se redacta, interpreta ni redecide semánticamente**. Debe copiar literalmente desde Bloque E los campos controlados que muestre:

- ID RGE;
- NVD padre;
- procedencia;
- prioridad;
- motor;
- formato;
- tipo de instrucción;
- estado contractual;
- convención de archivo;
- cualquier otro campo marcado como canónico.

Si una vista derivada compacta difiere del Bloque E:

`INCONSISTENCIA_DE_VISTA_DERIVADA`

Consecuencias:

1. el RGE no puede cerrarse para auditoría;
2. se conserva Bloque E;
3. se descarta y regenera la vista derivada;
4. queda prohibido corregir Bloque E para hacerlo coincidir con una vista secundaria.

La igualdad exigida es literal en campos controlados. No se permiten sinónimos, reclasificación de motor ni normalización editorial.

### B. Espejo contractual para 03.C-2B

El archivo:

`paquete_rge_para_auditoria_sesion_[N]_03c2a_v1.3.md`

**no es un resumen ni una reinterpretación del Bloque E**.

Es un **espejo contractual de transporte**.

Por cada RGE debe contener una copia íntegra y literal del contrato canónico correspondiente del Bloque E, desde su encabezado `E.RGE-XX-YY` hasta su campo final de estado.

Reglas:

1. no resumir;
2. no condensar;
3. no reformular;
4. no normalizar redacción;
5. no eliminar campos;
6. no fusionar campos;
7. no cambiar el orden interno;
8. no sustituir tablas por prosa;
9. no sustituir una instrucción multilínea por una síntesis;
10. no cambiar signos, cifras, unidades, etiquetas ni texto visible;
11. no añadir contenido dentro del bloque copiado;
12. no eliminar contenido aparentemente redundante.

Solo se permiten fuera de los bloques copiados:

- portada del paquete;
- metadatos de transporte;
- índice/resumen compacto;
- declaración final de entrega a 03.C-2B.

El contenido contractual copiado debe conservar identidad textual con Bloque E.

Resultado obligatorio:

`IDENTIDAD_PAQUETE_BLOQUE_E = OK | FALLA`

Si existe cualquier diferencia dentro de un contrato copiado:

`INCONSISTENCIA_DE_ESPEJO_CONTRACTUAL`

y el paquete no puede emitirse.

---

# 6.2 Regla de aislamiento de versiones

La versión de 03.C-2A y las versiones de sus insumos son dominios independientes.

```text
VERSIÓN_03C2A != VERSIÓN_DOCUMENTO_MAESTRO
VERSIÓN_03C2A != VERSIÓN_BRIEF
VERSIÓN_03C2A != VERSIÓN_03A
VERSIÓN_03C2A != VERSIÓN_03B
VERSIÓN_03C2A != VERSIÓN_03C1
VERSIÓN_03C2A != VERSIÓN_STYLE_LOCK
```

Cada versión de insumo se copia exclusivamente desde la identificación del propio insumo.

Queda prohibido:

- inferir la versión de un insumo a partir de la versión de esta skill;
- completar una versión ausente con `v1.0`;
- homogeneizar versiones por conveniencia editorial;
- modificar localizadores de fuente para hacerlos coincidir con la versión de 03.C-2A.

Si la versión exacta de un insumo no está disponible, usar:

`VERSIÓN_NO_CONFIRMADA`

y mantener el nombre exacto del archivo o identificador disponible.

Una discrepancia de versión detectada antes del cierre bloquea la entrega hasta corregir el metadato desde la fuente correspondiente.

---

# 7. Unidad básica: Recurso Generativo Ejecutable — RGE

Cada unidad producida por 03.C-2A es un `RGE`.

Un RGE debe ser:

- identificable;
- trazable a una NVD;
- visualmente especificado;
- técnicamente ejecutable;
- semánticamente acotado mediante whitelist/blacklist;
- autosuficiente como contrato de producción;
- estable antes de auditoría.

Un RGE todavía no es un recurso final ni un recurso autorizado para producir.

---

# 8. IDs y cardinalidad

## 8.1 ID padre

`NVD-XX`

## 8.2 ID hijo

`RGE-XX-YY`

Ejemplo:

```text
NVD-04
├── RGE-04-01
└── RGE-04-02
```

## 8.3 Regla de cardinalidad

La cantidad de RGE debe respetar:

- `unidades_visuales_estimadas`;
- `modo_agrupación_visual`;
- necesidad real de separación ejecutiva.

03.C-2A no puede multiplicar recursos por comodidad técnica si ello altera la estrategia de 03.C-1.

---

# 9. NVD híbridas

03.C-2A diseña únicamente el componente generativo.

Modos permitidos:

- `SEPARADO`
- `MARCO_CON_SLOTS_EXTERNOS`
- `ENSAMBLAJE_POSTERIOR`
- `NO_APLICA`

Reglas:

1. el componente generativo no suplanta autenticidad externa;
2. los slots o interfaces con 03.C-3 deben declararse;
3. el RGE debe distinguir contenido propio de contenido externo esperado;
4. 03.C-2A no inventa el contenido del componente externo.

---

# 10. Arquitectura visual

## 10.1 Principio

La arquitectura debe derivarse de la semántica y del objetivo perceptivo, no de preferencias estéticas.

## 10.2 Vocabulario de arquitectura primaria

- `SISTEMA_PARALELO`
- `ENTRADA_PROCESO_SALIDA`
- `FLUJO_SECUENCIAL`
- `CICLO`
- `MATRIZ`
- `COMPARATIVA`
- `RED`
- `ÁRBOL`
- `CAPAS`
- `ESPACIAL`
- `JERARQUÍA`
- `AXONOMÉTRICA`
- `DOBLE_PANEL`
- `MULTIPANEL`
- `INFOGRAFÍA_MODULAR`
- `MIXTA`
- `NO_APLICA`

Cada RGE declara exactamente una arquitectura primaria.

Puede declarar una arquitectura secundaria cuando sea necesaria para describir organización interna sin cambiar la primaria.

---

# 11. Relaciones obligatorias

Cada relación significativa debe declarar:

| Campo | Descripción |
|---|---|
| ID | `R1`, `R2`, ... |
| Origen | componente fuente |
| Destino | componente destino |
| Dirección | orientación relacional |
| Tipo semántico | vocabulario controlado |
| Significado | interpretación disciplinar autorizada |

Tipos:

- `FLUJO`
- `SECUENCIA`
- `CAUSA_EFECTO`
- `DEPENDENCIA`
- `PERTENENCIA`
- `INTERCAMBIO`
- `EQUIVALENCIA`
- `CONTRASTE`
- `CORRESPONDENCIA`
- `JERARQUÍA`
- `PROYECCIÓN`
- `TRANSFORMACIÓN`
- `NO_APLICA`

---

# 12. Gramática visual

Toda relación relevante debe tener una convención gráfica explícita.

Ejemplo:

| Tipo semántico | Convención gráfica | Dirección | Etiqueta |
|---|---|---|---|
| PROYECCIÓN | línea discontinua | vertical | "Proyección ortogonal" |
| CONTRASTE | paneles paralelos | horizontal | no obligatoria |
| FLUJO | flecha simple | izquierda→derecha | verbo conectivo |

Una misma relación no debe representarse con convenciones contradictorias dentro del RGE.

---

# 13. Jerarquía visual

Cada RGE debe declarar:

1. nivel primario;
2. nivel secundario;
3. nivel de apoyo;
4. leyenda o notas, si aplica.

Debe existir correspondencia entre jerarquía visual y jerarquía cognitiva.

---

# 14. Contrato gráfico ejecutable

Debe especificar, cuando aplique:

- formato compositivo;
- retícula;
- zonas funcionales;
- contenedores;
- dirección dominante;
- posiciones relativas;
- conectores;
- tratamiento de texto;
- slots externos;
- reglas de leyenda;
- densidad;
- uso del color;
- prohibiciones gráficas;
- parámetros técnicos necesarios.

Los valores puramente gráficos se consideran `GRÁFICO_INTERNO`.

---

# 15. Style Lock

## 15.1 Fuente

Usar:

`lineamientos_visuales_[asignatura]_vigente.md`

cuando exista.

En ausencia, derivar un perfil local coherente con el Documento Maestro y marcarlo para persistencia posterior.

## 15.2 El Style Lock puede fijar

- fondo;
- tipografía;
- jerarquía;
- paleta;
- trazos;
- bordes;
- iconografía;
- densidad;
- leyendas;
- prohibiciones formales.

No puede introducir contenido disciplinar.

---

# 16. Motor de producción

Valores:

- `IA_IMAGEN`
- `DIAGRAMA_ESTRUCTURADO`
- `VECTOR_PROGRAMÁTICO`
- `COMPOSICIÓN_MIXTA`

## 16.1 IA_IMAGEN

Adecuado para contenido pictórico sintético donde la geometría exacta no sea crítica.

## 16.2 DIAGRAMA_ESTRUCTURADO

Preferido para diagramas, matrices, redes, comparativas, esquemas y láminas con texto exacto.

## 16.3 VECTOR_PROGRAMÁTICO

Preferido cuando se requiere reproducibilidad geométrica, datos controlados o construcción algorítmica.

## 16.4 COMPOSICIÓN_MIXTA

Usar cuando el RGE combina varias técnicas o integra slots externos.

---

# 17. Formato de salida

Valores preferentes:

- `PNG`
- `JPG`
- `SVG`
- `PDF`
- `OTRO_JUSTIFICADO`

03.C-2A debe especificar:

- formato preferente;
- orientación;
- relación de aspecto;
- resolución mínima;
- editabilidad;
- transparencia, cuando aplique.

---

# 18. Clasificación de valores

Toda cifra, fórmula, magnitud, etiqueta técnica o valor paramétrico relevante debe clasificarse exactamente en una de estas clases:

## A. `DISCIPLINAR_HEREDADO`

Contenido visible exacto respaldado por fuente semántica permitida.

Requiere:

- fuente;
- localizador;
- soporte exacto.

## B. `DIDÁCTICO_ILUSTRATIVO`

Ejemplo visible elegido para operacionalizar una relación prescrita cuando upstream no fija valores exactos.

Debe:

- declararse ilustrativo;
- no presentarse como oficial, típico, real, normativo o canónico;
- respetar relaciones heredadas;
- incluir justificación.

## C. `GRÁFICO_INTERNO`

Parámetro no disciplinar destinado a composición:

- píxeles;
- coordenadas;
- radios;
- opacidades;
- márgenes;
- tamaños de cajas;
- proporciones;
- semillas aleatorias.

No requiere fuente disciplinar y no debe mostrarse como dato técnico del dominio.

### Regla de exclusión

Todo valor visible que no pueda clasificarse de forma legítima debe eliminarse del RGE o provocar conflicto.

---

# 19. Regla de soporte exacto

Una fuente temática no autoriza automáticamente un valor concreto.

Ejemplo:

```text
"el metro es unidad legal"
```

no autoriza:

```text
"usar curvas 10 m, 20 m, 30 m"
```

si el valor exacto no está heredado.

Si upstream autoriza una relación pero no un valor, 03.C-2A puede:

1. omitir el valor; o
2. declararlo `DIDÁCTICO_ILUSTRATIVO`.

---

# 20. Whitelist semántica

Cada RGE debe contener una whitelist explícita.

Esquema:

| ID | Contenido autorizado | Tipo | Clase de valor | Fuente semántica | Localizador | Modo de uso | Justificación |
|---|---|---|---|---|---|---|---|

Modos:

- `HEREDADO_LITERAL`
- `DERIVADO_CONTROLADO`
- `DIDÁCTICO_ILUSTRATIVO`

Reglas:

1. no usar categorías vagas para justificar adiciones concretas;
2. equipos, tecnologías, normas, fórmulas y relaciones específicas deben enumerarse cuando vayan a aparecer;
3. una síntesis puede autorizarse solo si no amplía semántica;
4. la whitelist define el límite de diseño permitido, pero **03.C-2A no certifica por sí misma que la instrucción final no lo exceda**.

La última comprobación pertenece a 03.C-2B.

---

# 21. Blacklist semántica

Cada RGE debe declarar contenido explícitamente prohibido.

Puede incluir:

- conceptos fuera de alcance;
- fórmulas reservadas para sesiones posteriores;
- tecnologías no autorizadas;
- marcas;
- escenas engañosas;
- elementos visuales que induzcan una relación incorrecta;
- texto que pueda convertir un ejemplo ilustrativo en afirmación normativa.

---

# 22. Instrucción de producción autosuficiente

## 22.1 Tipo

Cada RGE declara exactamente un:

- `PROMPT_GENERATIVO`
- `ESPECIFICACIÓN_VECTORIAL`
- `ESPECIFICACIÓN_PROGRAMÁTICA`
- `ESPECIFICACIÓN_MIXTA`

Correspondencia normal:

| Motor | Tipo normal |
|---|---|
| IA_IMAGEN | PROMPT_GENERATIVO |
| DIAGRAMA_ESTRUCTURADO | ESPECIFICACIÓN_VECTORIAL o ESPECIFICACIÓN_PROGRAMÁTICA |
| VECTOR_PROGRAMÁTICO | ESPECIFICACIÓN_PROGRAMÁTICA |
| COMPOSICIÓN_MIXTA | ESPECIFICACIÓN_MIXTA |

## 22.2 Requisitos

La instrucción debe integrar:

1. propósito;
2. mensaje central;
3. elementos obligatorios;
4. relaciones;
5. arquitectura;
6. gramática visual;
7. jerarquía;
8. Style Lock;
9. restricciones;
10. formato;
11. orientación;
12. finalidad didáctica;
13. indicaciones de legibilidad;
14. texto exacto requerido;
15. prohibición de inventar información;
16. reglas de integración híbrida, si aplica.

La instrucción debe quedar **cerrada para auditoría**: 03.C-2A no debe seguir editándola mientras 03.C-2B la audita.

## 22.3 Motores estructurados y programáticos

No redactar falsos prompts de imagen cuando se requieren instrucciones geométricas o programáticas.

Describir:

- estructura;
- componentes;
- relaciones;
- coordenadas/proporciones gráficas;
- datos visibles autorizados;
- reglas de exportación;
- pruebas de aceptación.

---

# 23. Criterios de aceptación

## 23.1 Críticos

Como mínimo:

- fidelidad al objetivo perceptivo;
- fidelidad al mensaje central;
- presencia de elementos obligatorios;
- respeto de relaciones;
- respeto de arquitectura;
- respeto de restricciones;
- coherencia con familia representacional;
- legibilidad;
- formato técnico;
- soporte exacto de `DISCIPLINAR_HEREDADO`;
- declaración de `DIDÁCTICO_ILUSTRATIVO`;
- ausencia de contenido expresamente prohibido.

03.C-2A define estos criterios; 03.C-2B los usa como contexto contractual para la auditoría semántica y 03.C-2C los aplica sobre la salida producida como criterios observables de ejecución. Ninguno sustituye la auditoría semántica de 03.C-2B.

## 23.2 Secundarios

- balance espacial;
- coherencia cromática;
- consistencia iconográfica;
- claridad de leyenda;
- economía visual;
- bajo ruido;
- buen uso de espacio negativo.

Los secundarios nunca compensan un crítico incumplido.

---

# 24. Estados del RGE en 03.C-2A

Valores que 03.C-2A puede asignar:

- `BORRADOR_CONTRATO`
- `BLOQUEADO`
- `RGE_CERRADO_PARA_AUDITORÍA`
- `DEVUELTO_POR_AUDITORÍA`
- `CORREGIDO_PARA_REAUDITORÍA`

03.C-2A **no puede asignar estados de aprobación semántica ni de producción**.

En particular:
- `PASS` / `RETURN` pertenecen exclusivamente a 03.C-2B;
- estados de producción como `RECURSO_GENERATIVO_RESUELTO`, `FALLO_DE_EJECUCION` o equivalentes pertenecen a 03.C-2C o downstream.

La ficha y el paquete de 03.C-2A deben usar exclusivamente los estados definidos en esta sección.

---

# 25. Regla de congelación del RGE

Antes de entregar a 03.C-2B:

1. la instrucción de producción debe estar completa;
2. whitelist y blacklist deben estar cerradas;
3. arquitectura y relaciones no deben estar pendientes;
4. los textos visibles previstos deben estar definidos;
5. el motor y formato deben estar fijados;
6. no debe existir un conflicto abierto.

Entonces:

`RGE_CERRADO_PARA_AUDITORÍA`

Desde ese momento 03.C-2A no modifica el RGE hasta recibir:

- `PASS`, o
- `RETURN`.

---

# 26. Handoff a 03.C-2B

## 26.1 Paquete contractual

03.C-2A entrega un paquete de transporte que contiene, por cada RGE, **el contrato completo del Bloque E copiado literalmente**.

El paquete no reconstruye un contrato reducido.

Cada bloque copiado debe incluir íntegramente:

- encabezado e ID RGE;
- trazabilidad;
- contrato pedagógico heredado;
- objetivo operativo;
- elementos obligatorios;
- relaciones obligatorias;
- elementos opcionales;
- elementos prohibidos;
- arquitectura visual;
- contrato gráfico ejecutable;
- gramática visual;
- Style Lock;
- integración híbrida;
- motor;
- whitelist;
- blacklist;
- instrucción final de producción;
- criterios críticos;
- criterios secundarios;
- restricciones;
- convención de archivo;
- estado contractual.

Si el contrato del Bloque E contiene campos adicionales, también deben copiarse.

**Regla de transporte:** el paquete puede envolver los contratos con metadatos documentales, pero no puede modificar el interior de ningún contrato.

## 26.2 Prueba de identidad antes del handoff

La identidad entre el Bloque E y el paquete contractual **NO** puede declararse mediante juicio semántico, inspección visual, equivalencia conceptual, semejanza aparente ni autodeclaración. Debe comprobarse mediante comparación textual exacta de cada contrato RGE.

Para cada `RGE-XX-YY`, extraer del Bloque E el contrato completo comprendido desde `## E.RGE-XX-YY` hasta el final de `### 20. Estado`, incluyendo íntegramente:

- encabezados;
- texto;
- tablas;
- listas;
- signos;
- cifras;
- unidades;
- fórmulas;
- bloques de código;
- instrucción final de producción;
- estructura interna.

Extraer del paquete para 03.C-2B el contrato correspondiente utilizando exactamente los mismos límites contractuales.

Comparar ambos contenidos **carácter por carácter**.

Está prohibido normalizar, resumir, corregir, sustituir o reinterpretar antes de realizar la comparación:

- palabras;
- sinónimos;
- mayúsculas/minúsculas;
- signos;
- cifras;
- unidades;
- caracteres Unicode;
- texto multilingüe;
- contenido de tablas;
- contenido de bloques de código;
- cualquier otra parte del contrato.

La comparación produce únicamente uno de dos estados:

`IDENTIDAD_RGE = OK`

cuando:

`N_DIFERENCIAS = 0`

o:

`IDENTIDAD_RGE = FALLA`

cuando:

`N_DIFERENCIAS > 0`

Si `IDENTIDAD_RGE = FALLA`, registrar obligatoriamente:

- ID RGE;
- posición o línea de la primera diferencia;
- fragmento correspondiente del Bloque E;
- fragmento correspondiente del paquete;
- número total de diferencias detectadas.

Ante cualquier `IDENTIDAD_RGE = FALLA`:

1. el paquete queda bloqueado;
2. se prohíbe declarar `IDENTIDAD_PAQUETE_BLOQUE_E = OK`;
3. se conserva intacto el Bloque E;
4. se descarta y regenera únicamente la copia contractual correspondiente del paquete;
5. se repite la comparación completa del RGE corregido.

La agregación final exige:

`N_RGE_PAQUETE = N_RGE_BLOQUE_E`

y que todos los RGE cumplan simultáneamente:

`IDENTIDAD_RGE = OK`

`N_DIFERENCIAS = 0`

Solo bajo esas condiciones puede asignarse:

`IDENTIDAD_PAQUETE_BLOQUE_E = OK`

Si cualquiera de esas condiciones falla, asignar obligatoriamente:

`IDENTIDAD_PAQUETE_BLOQUE_E = FALLA`

`INCONSISTENCIA_DE_ESPEJO_CONTRACTUAL`

Queda expresamente prohibido asignar `IDENTIDAD_PAQUETE_BLOQUE_E = OK` basándose únicamente en:

- lectura visual;
- equivalencia semántica;
- semejanza de contenido;
- coincidencia de campos principales;
- ausencia aparente de diferencias;
- afirmación del propio ejecutor.

El estado `OK` requiere evidencia de comparación textual exacta.

Como prueba mínima de regresión, si Bloque E contiene:

`el alumno deberá poder visualizar`

y el paquete contiene:

`el alumno候補 podrá visualizar`

el resultado obligatorio es:

`IDENTIDAD_RGE = FALLA`

`N_DIFERENCIAS > 0`

`IDENTIDAD_PAQUETE_BLOQUE_E = FALLA`

`INCONSISTENCIA_DE_ESPEJO_CONTRACTUAL`

aunque ambas expresiones pudieran parecer semánticamente relacionadas.

## 26.3 Inmutabilidad

03.C-2B audita exactamente los contratos recibidos en el espejo contractual.

No puede:

- reescribir la instrucción;
- sustituir elementos;
- añadir contenido;
- cambiar arquitectura;
- cambiar whitelist;
- completar omisiones del paquete por inferencia.

Solo puede devolver:

`PASS`

o:

`RETURN`.

## 26.4 RETURN

Cuando 03.C-2B devuelve un RGE, debe indicar al menos:

- ID RGE;
- fragmento o elemento observado;
- motivo;
- categoría del fallo;
- acción requerida;
- evidencia literal.

03.C-2A corrige primero el **Bloque E canónico**, nunca el paquete.

Después:

1. regenera vistas derivadas;
2. regenera el espejo contractual completo;
3. vuelve a ejecutar `IDENTIDAD_PAQUETE_BLOQUE_E`;
4. cambia el estado a `CORREGIDO_PARA_REAUDITORÍA` cuando corresponda;
5. reenvía el paquete completo.

---

# 27. Bucle de corrección acotado

Se permiten como máximo dos ciclos locales completos por RGE:

```text
Ciclo 1:
03.C-2A → 03.C-2B

si RETURN:
03.C-2A corrige

Ciclo 2:
03.C-2A → 03.C-2B
```

Si el segundo ciclo vuelve a `RETURN` por una causa que no puede resolverse sin alterar el contrato de 03.C-1:

`CONFLICTO DE ESTRATEGIA VISUAL`

y se devuelve a 03.C-1 en modo `REVISIÓN`.

La finalidad es impedir refinamiento local indefinido.

---

# 28. Protocolo de conflicto

Códigos aplicables:

- `C03_REPRESENTACION_GENERATIVA_NO_ES_TECNICAMENTE_VIABLE`
- `C04_RIESGO_DE_ERROR_CONCEPTUAL`
- `C05_AUTENTICIDAD_RESULTA_NECESARIA`
- `C07_SOLUCION_HIBRIDA_RESULTA_NECESARIA`
- `C08_RECURSO_PRESCRITO_ES_REDUNDANTE`
- `C09_RESTRICCION_NORMATIVA_O_DOCUMENTAL`
- `C10_OTRO_JUSTIFICADO`

Formato:

| Campo | Valor |
|---|---|
| NVD | [...] |
| RGE | [...] |
| Skill que reporta | 03.C-2A |
| Código | C03–C10 |
| Evidencia | [...] |
| Contrato original | [...] |
| Problema | [...] |
| Recomendación | [...] |
| Estado | abierto |

03.C-2A recomienda; 03.C-1 decide.

---

# 29. Estructura de salida

Archivo principal:

`ficha_diseno_generativo_sesion_[N]_03c2a_v1.3.md`

Paquete contractual de auditoría:

`paquete_rge_para_auditoria_sesion_[N]_03c2a_v1.3.md`

Este paquete es obligatorio cuando exista al menos un RGE en estado `RGE_CERRADO_PARA_AUDITORÍA` y debe funcionar como espejo contractual íntegro del Bloque E.

Style Lock, cuando corresponda:

`lineamientos_visuales_[asignatura]_vigente.md`

03.C-2A no produce:

- imágenes finales;
- inventarios o matrices de auditoría semántica;
- reporte de auditoría;
- veredictos de aprobación semántica;
- catálogo externo;
- URLs;
- licencias.

---

# 30. Estructura de la Ficha de Diseño Generativo

```text
A. Metadatos y estado
B. NVD elegibles y trazabilidad
C. Style Lock aplicado
D. Arquitectura generativa por NVD
E. Contratos RGE
F. Integración híbrida
G. Advertencias para producción
H. Conflictos y bloqueos
I. Validación de diseño
J. Handoff a 03.C-2B
```

---

# 31. Plantilla de contrato RGE

## E.RGE-XX-YY — [Nombre]

### 0. Trazabilidad

- ID RGE
- NVD padre
- concepto heredado
- procedencia
- prioridad
- función primaria
- funciones secundarias
- destino
- slide exacto heredado o `NO_DEFINIDO`
- criterio de satisfacción

### 1. Contrato pedagógico heredado

- problema cognitivo
- objetivo perceptivo
- mensaje central
- familia representacional
- especificación representacional

### 2. Objetivo operativo

[...]

### 3. Elementos obligatorios

[...]

### 4. Relaciones obligatorias

| ID | Origen | Destino | Dirección | Tipo | Significado |
|---|---|---|---|---|---|

### 5. Elementos opcionales

[...]

### 6. Elementos prohibidos heredados

[...]

### 7. Arquitectura visual

- primaria
- secundaria
- dirección dominante
- categorías
- jerarquía
- límite conceptual
- zonas relacionales
- bloque de síntesis
- leyenda

### 8. Contrato gráfico ejecutable

[...]

### 9. Gramática visual

[...]

### 10. Style Lock

[...]

### 11. Integración híbrida

[...]

### 12. Motor

[...]

### 13. Whitelist semántica

| ID | Contenido | Tipo | Clase | Fuente | Localizador | Modo | Justificación |
|---|---|---|---|---|---|---|---|

### 14. Blacklist semántica

[...]

### 15. Instrucción final de producción

[...]

### 16. Criterios críticos

[...]

### 17. Criterios secundarios

[...]

### 18. Restricciones

[...]

### 19. Convención de archivo

[...]

### 20. Estado

`RGE_CERRADO_PARA_AUDITORÍA`

---

# 32. Validación interna de diseño

03.C-2A sí debe validar su **diseño**, pero no realizar auditoría semántica exhaustiva.

Checklist:

## I.1 Elegibilidad

- [ ] NVD elegible.
- [ ] procedencia compatible.
- [ ] contrato canónico disponible.

## I.2 Fidelidad upstream

- [ ] problema cognitivo sin cambios.
- [ ] objetivo perceptivo sin cambios.
- [ ] mensaje central sin cambios.
- [ ] prioridad sin cambios.
- [ ] funciones sin cambios.
- [ ] criterio de satisfacción sin cambios.

## I.3 Diseño visual

- [ ] arquitectura definida.
- [ ] relaciones definidas.
- [ ] gramática consistente.
- [ ] jerarquía clara.
- [ ] contrato gráfico ejecutable.
- [ ] Style Lock aplicado.

## I.4 Semántica de diseño

- [ ] whitelist presente.
- [ ] blacklist presente.
- [ ] cada valor visible clasificado.
- [ ] fuentes y localizadores registrados.
- [ ] no se inventan normas, equipos, datos o fórmulas por conveniencia.
- [ ] no se amplía deliberadamente la semántica heredada.

**Nota:** este checklist no sustituye la auditoría literal de 03.C-2B.

## I.5 Producción

- [ ] motor adecuado.
- [ ] formato adecuado.
- [ ] instrucción autosuficiente.
- [ ] criterios críticos definidos.
- [ ] restricciones definidas.

## I.6 Híbridos

- [ ] componente generativo claramente delimitado.
- [ ] slots externos declarados.
- [ ] no se suplanta autenticidad.

## I.7 Cierre para auditoría

- [ ] RGE estable.
- [ ] no existen campos pendientes.
- [ ] instrucción final congelada.
- [ ] estado = `RGE_CERRADO_PARA_AUDITORÍA`.

---

# 33. Reglas de operación

1. 03.C-1 es la fuente canónica upstream.
2. Solo procesar NVD GENERATIVO o componente generativo de HÍBRIDO.
3. Todo RGE tiene un NVD padre.
4. Ningún RGE cambia procedencia, prioridad, funciones, problema, objetivo o satisfacción.
5. Arquitectura se elige por semántica.
6. Relaciones significativas se documentan.
7. Todo RGE tiene contrato gráfico ejecutable.
8. Todo contenido disciplinar visible previsto debe poder vincularse a una fuente permitida.
9. Todo valor visible se clasifica.
10. `GRÁFICO_INTERNO` nunca se presenta como verdad disciplinar.
11. `DIDÁCTICO_ILUSTRATIVO` se declara como ejemplo.
12. La whitelist limita el espacio semántico de diseño.
13. La blacklist explicita exclusiones.
14. La instrucción de producción debe ser autosuficiente.
15. No producir un falso prompt para motores estructurados o programáticos.
16. No asignar slide exacto si no fue heredado.
17. Un híbrido no sustituye el componente externo.
18. 03.C-2A no genera estructuras de auditoría semántica.
19. 03.C-2A no ejecuta auditoría de clausura.
20. 03.C-2A no declara veredictos de aprobación semántica.
21. 03.C-2A no declara estados reservados a producción.
22. El único estado de salida normal es `RGE_CERRADO_PARA_AUDITORÍA`.
23. Después de cerrar un RGE, no modificarlo durante su auditoría.
24. Todo RETURN de 03.C-2B debe corregirse sobre evidencia literal.
25. Una corrección local no puede alterar el CPH heredado.
26. Si una corrección exige cambio de estrategia, reportar conflicto.
27. Máximo dos ciclos locales de auditoría por RGE antes de escalar.
28. 03.Cbis solo recibe RGE que hayan pasado 03.C-2B.
29. El paquete para 03.C-2B debe copiar íntegramente cada contrato RGE de Bloque E.
30. Queda prohibido resumir o reformular contratos dentro del paquete de auditoría.
31. Toda corrección posterior a RETURN se realiza primero en Bloque E y luego se regeneran las salidas secundarias.

---

# 33.1 Compuerta final de consistencia contractual

Antes de asignar `RGE_CERRADO_PARA_AUDITORÍA`, ejecutar obligatoriamente:

## A. Consistencia Bloque E → vistas derivadas

- [ ] Cada fila de tabla consolidada fue copiada desde Bloque E.
- [ ] `motor` coincide literalmente.
- [ ] `formato` coincide literalmente.
- [ ] `tipo de instrucción` coincide literalmente.
- [ ] `estado` coincide literalmente.
- [ ] `ID RGE` y `NVD padre` coinciden literalmente.
- [ ] No existe ninguna corrección manual en una vista derivada.

Resultado:

`CONSISTENCIA_VISTAS_DERIVADAS = OK | FALLA`

Si `FALLA`:

`INCONSISTENCIA_DE_VISTA_DERIVADA`

y se prohíbe el cierre.

## B. Aislamiento de versiones

- [ ] versión de 03.C-2A tomada de esta skill;
- [ ] versión del Documento Maestro tomada del Documento Maestro;
- [ ] versión del Brief tomada del Brief;
- [ ] versión de 03.A tomada de 03.A;
- [ ] versión de 03.B tomada de 03.B;
- [ ] versión de 03.C-1 tomada de 03.C-1;
- [ ] versión del Style Lock tomada del archivo de Style Lock;
- [ ] ningún número de versión fue propagado por similitud.

Resultado:

`AISLAMIENTO_DE_VERSIONES = OK | FALLA`

Si `FALLA`, el paquete no puede emitirse.

## C. Identidad del espejo contractual Bloque E → paquete

- [ ] El número de contratos RGE del paquete coincide con Bloque E.
- [ ] Cada contrato del paquete contiene todos los campos de su contrato fuente.
- [ ] El orden interno es idéntico.
- [ ] Las tablas se conservan completas.
- [ ] La instrucción final de producción se copia íntegra, sin resumen.
- [ ] No existe reformulación editorial dentro de los bloques copiados.
- [ ] No existe contenido añadido dentro de los bloques copiados.
- [ ] No existe contenido omitido.

Resultado:

`IDENTIDAD_PAQUETE_BLOQUE_E = OK | FALLA`

Si `FALLA`:

`INCONSISTENCIA_DE_ESPEJO_CONTRACTUAL`

y se prohíbe emitir el paquete.

## D. Handoff neutral


- [ ] 03.C-2A no prescribe algoritmos internos de 03.C-2B.
- [ ] Solo espera `PASS` o `RETURN`.
- [ ] No aparecen estados de producción reservados a 03.C-2C.

## E. Cierre

Solo puede emitirse `RGE_CERRADO_PARA_AUDITORÍA` cuando:

```text
VALIDACIÓN_DE_DISEÑO = OK
AND CONSISTENCIA_VISTAS_DERIVADAS = OK
AND AISLAMIENTO_DE_VERSIONES = OK
AND IDENTIDAD_PAQUETE_BLOQUE_E = OK
AND RESIDUOS_DE_LEGADO = 0
```

---

# 34. Criterio final de calidad de 03.C-2A

03.C-2A cumple si:

- cada NVD elegible se transforma en RGE ejecutable;
- las decisiones upstream se preservan;
- existe trazabilidad `NVD → RGE`;
- arquitectura, relaciones y jerarquía son coherentes;
- el Style Lock está aplicado;
- whitelist y blacklist están completas como límites de diseño;
- valores visibles están clasificados;
- motor y formato son adecuados;
- la instrucción final es autosuficiente;
- los criterios de aceptación permiten evaluar la salida;
- los híbridos respetan autenticidad externa;
- no se inventa semántica disciplinar deliberadamente;
- no se realiza autoclausura;
- el RGE queda congelado y entregado a 03.C-2B;
- todas las vistas derivadas coinciden literalmente con Bloque E;
- las versiones de insumos permanecen aisladas de la versión de la skill;
- cualquier RETURN se corrige sin modificar el contrato de 03.C-1;
- conflictos irresolubles se escalan al Orquestador.

La calidad de 03.C-2A se mide por **calidad del diseño contractual**, no por aprobar su propia semántica.

---

# 35. Estado de versión

**Versión:** v1.3
**Estado:** VERSIÓN ESTABLE  
**Deriva de:** 03.C - 2.generative v1.9  
**Cambio arquitectónico principal:** separación entre diseño (03.C-2A) y auditoría (03.C-2B)  
**Upstream:** 03.C-1 v1.2  
**Downstream inmediato:** 03.C-2B  
**Downstream de producción:** 03.C-2C v0.1, únicamente después de PASS de 03.C-2B

---

# 36. Elementos heredados de 03.C-2 v1.9

Se conservan conceptualmente:

- CPH heredado;
- sistema NVD→RGE;
- arquitectura visual;
- relaciones;
- gramática visual;
- jerarquía;
- contrato gráfico;
- Style Lock;
- motores;
- formatos;
- clasificación de valores;
- soporte exacto;
- whitelist;
- blacklist;
- instrucciones autosuficientes;
- criterios de aceptación;
- estados de bloqueo;
- protocolo de conflicto;
- integración híbrida;
- trazabilidad.

Se eliminan de 03.C-2A y se reservan para 03.C-2B:

- extracción e inventario de auditoría sobre la superficie final;
- matrices de correspondencia semántica;
- pruebas locales de equivalencia o cobertura;
- mecanismos de clausura semántica;
- veredictos PASS/RETURN;
- autorización de producción.

---

# 37. Decisiones cerradas en v1.0

1. El estado contractual normal se fija como `RGE_CERRADO_PARA_AUDITORÍA`.
2. El máximo de correcciones locales se fija en dos ciclos completos por RGE; cualquier tercer intento exige escalamiento a 03.C-1 cuando el problema no pueda resolverse sin alterar upstream.
3. 03.C-2A consume el Style Lock vigente. Si no existe, puede proponer un perfil local provisional, pero no convertirlo silenciosamente en estándar institucional.
4. El paquete hacia 03.C-2B debe contener los contratos RGE completos y congelados; no debe reducirlos a resúmenes que obliguen al auditor a reconstruir contexto.
5. La denominación formal permanece `03.C-2A — Diseñador de Recursos Generativos`.
6. 03.C-2A no prescribe el método interno de auditoría de 03.C-2B. Solo define el contrato de entrada y acepta como resultados `PASS` o `RETURN`. Un `PASS` habilita exclusivamente la ejecución posterior por 03.C-2C.

---

# 38. Fuente canónica interna y vistas derivadas

## 38.1 Fuente canónica

Dentro de la salida de 03.C-2A, el **Bloque E — Contratos RGE** es la única fuente canónica de cada recurso.

Para cada `RGE-XX-YY`, son canónicos en su contrato individual:

- ID;
- NVD padre;
- procedencia;
- arquitectura;
- motor;
- formato;
- tipo de instrucción;
- whitelist;
- blacklist;
- instrucción final;
- criterios;
- restricciones;
- estado contractual.

## 38.2 Vistas derivadas y espejo contractual

Son **vistas derivadas compactas** y no pueden redactarse de forma independiente:

- tabla de NVD elegibles;
- tabla consolidada de RGE;
- resumen de motores y formatos;
- estado global del documento;
- resúmenes de trazabilidad;
- síntesis arquitectónicas.

Toda vista derivada compacta debe regenerarse exclusivamente desde el Bloque E y copiar literalmente los campos controlados que muestre.

El `paquete_rge_para_auditoria_sesion_[N]_03c2a_v1.3.md` **no se clasifica como vista derivada compacta**.

Es un **espejo contractual de transporte** y debe contener la copia íntegra y literal de cada contrato RGE del Bloque E, conforme a §6.1.B y §26.

Por tanto:

- las vistas derivadas compactas copian campos controlados;
- el paquete contractual copia contratos completos;
- ninguno de los dos puede reinterpretar Bloque E.

## 38.3 Regla de inconsistencia

Si una vista derivada contradice al contrato individual en cualquier campo contractual:

```text
INCONSISTENCIA_DE_VISTA_DERIVADA
→ RGE no puede cerrarse
→ regenerar la vista desde Bloque E
```

Nunca se corrige el contrato canónico para hacerlo coincidir con una tabla resumen salvo que exista una razón de diseño independiente y documentada.

Ejemplo bloqueante:

```text
Bloque E: Motor = DIAGRAMA_ESTRUCTURADO
Tabla resumen: Motor = VECTOR_PROGRAMÁTICO
→ INCONSISTENCIA_DE_VISTA_DERIVADA
→ cierre prohibido
```

---

# 39. Contrato obligatorio de metadatos de salida

Toda `Ficha de Diseño Generativo` debe declarar exactamente:

| Campo | Valor requerido |
|---|---|
| Skill | `03.C-2A — Diseñador de Recursos Generativos` |
| Versión | versión activa de 03.C-2A |
| Destinatario inmediato | `03.C-2B — Auditor Semántico de Recursos Generativos` |
| Estado global normal | `RGE_CERRADOS_PARA_AUDITORÍA` |

No se permite reutilizar metadatos de una versión monolítica anterior.

La tabla de NVD/RGE debe expresar únicamente estados pertenecientes a 03.C-2A. Para recursos correctamente cerrados debe usar:

`RGE_CERRADO_PARA_AUDITORÍA`

No debe declarar disponibilidad directa para producción ni saltar 03.C-2B. El destinatario inmediato sigue siendo 03.C-2B; solo un `PASS` habilita el handoff posterior a 03.C-2C.

---

# 40. Limpieza obligatoria de legado

Antes de emitir cualquier salida, 03.C-2A ejecuta una comprobación textual de frontera.

Debe detectar y eliminar de sus productos cualquier:

- identificador de skill monolítica anterior;
- versión histórica presentada como versión activa;
- estado que autorice producción antes de auditoría;
- nombre de etapa inexistente o híbrida entre 03.C-2A y 03.C-2B;
- método de auditoría prescrito para 03.C-2B;
- instrucción que afirme que 03.C-2A certificó cierre semántico.

La aparición de cualquiera de esos residuos implica:

`SALIDA_03C2A_INCONSISTENTE`

y prohíbe emitir el paquete de handoff.

---

# 41. Handoff neutral hacia 03.C-2B

03.C-2A define únicamente la interfaz, no el algoritmo de auditoría.

El paquete debe indicar:

```text
03.C-2B recibe el RGE congelado.
Resultado permitido:
- PASS
- RETURN
```

03.C-2A no debe especificar:

- tablas internas que 03.C-2B deba construir;
- nombres de pruebas internas;
- fórmulas de clausura;
- conteos de auditoría;
- métodos de extracción;
- estructura interna del razonamiento auditor.

Esto permite diseñar y versionar 03.C-2B de manera independiente.

---

# 42. Compuerta adicional de cierre de diseño

Un RGE solo puede alcanzar `RGE_CERRADO_PARA_AUDITORÍA` si se cumplen simultáneamente:

```text
CPH_PRESERVADO = SÍ
DISEÑO_COMPLETO = SÍ
INSTRUCCIÓN_FINAL_CONGELADA = SÍ
WHITELIST_PRESENTE = SÍ
BLACKLIST_PRESENTE = SÍ
MOTOR_Y_FORMATO_DEFINIDOS = SÍ
VISTAS_DERIVADAS_CONSISTENTES = SÍ
IDENTIDAD_PAQUETE_BLOQUE_E = OK
METADATOS_03C2A_CORRECTOS = SÍ
RESIDUOS_DE_LEGADO = 0
```

Si cualquier condición falla:

`BORRADOR_CONTRATO` o `BLOQUEADO`

según corresponda.

---

# 43. Cambios históricos v0.1 → v1.0

1. Se separó diseño generativo de auditoría semántica.
2. Bloque E quedó definido como única fuente canónica interna por RGE.
3. Se introdujeron vistas derivadas regenerables y bloqueo por inconsistencia.
4. Se estableció aislamiento estricto de versiones de insumos.
5. Se eliminó autoclausura semántica de 03.C-2A.
6. Se fijó el handoff neutral `PASS | RETURN` hacia 03.C-2B.

---

# 44. Cambios v1.0 → v1.1

1. El paquete para 03.C-2B deja de tratarse como resumen contractual.
2. Se define formalmente como **espejo contractual de transporte** del Bloque E.
3. Cada contrato RGE debe copiarse completo y literalmente desde Bloque E.
4. Se prohíben resumen, condensación, normalización, reformulación, fusión u omisión dentro del contrato copiado.
5. Se introduce `IDENTIDAD_PAQUETE_BLOQUE_E = OK | FALLA`.
6. Se introduce `INCONSISTENCIA_DE_ESPEJO_CONTRACTUAL`.
7. La compuerta final exige identidad completa entre Bloque E y paquete de auditoría.
8. Un `RETURN` se corrige primero en Bloque E; después se regeneran vistas y paquete.
9. El paquete de auditoría pasa a ser obligatorio cuando existan RGE cerrados para auditoría.
10. Se conserva sin cambios la separación funcional `03.C-2A → 03.C-2B → 03.Cbis`.

---

# 45. Cambios v1.1 → v1.2

1. §1 se alinea con §29: el paquete de auditoría deja de describirse como opcional y pasa a ser obligatorio cuando exista al menos un RGE cerrado para auditoría.
2. §26 elimina la instrucción editorial residual que había quedado incrustada antes de §26.2.
3. §33.1 incorpora `IDENTIDAD_PAQUETE_BLOQUE_E = OK` en la fórmula efectiva de cierre contractual.
4. §33.1 corrige la duplicidad de encabezados: `D. Handoff neutral` y `E. Cierre`.
5. §38.2 separa formalmente las vistas derivadas compactas del espejo contractual de transporte.
6. El paquete para 03.C-2B deja de clasificarse como vista derivada y queda definido únicamente como copia íntegra literal del Bloque E.
7. No se modifican arquitectura, contratos RGE, estados, motores, whitelist/blacklist, handoff `PASS | RETURN` ni límites de competencia.

---


# 45.1 Cambios v1.2 → v1.3

1. Se elimina 03Cbis como downstream vigente de 03.C-2A.
2. Se incorpora `03.C-2C — Ejecutor de Recursos Generativos v0.1` como downstream de producción.
3. Se formaliza la secuencia `03.C-2A → 03.C-2B → 03.C-2C`.
4. `PASS` queda definido como autorización de producción, no como recurso terminado.
5. `RETURN` continúa retornando exclusivamente a 03.C-2A.
6. Los estados de producción se reservan a 03.C-2C.
7. Se añade §41.1 con el contrato post-PASS hacia 03.C-2C.
8. Se establece que cualquier modificación post-PASS invalida el PASS y obliga a nueva auditoría.
9. Se conserva sin cambios Bloque E como fuente canónica.
10. Se conserva sin cambios el espejo contractual íntegro hacia 03.C-2B.
11. Se conserva la prohibición de autoclausura semántica.
12. Se actualiza el nombre del paquete a `..._03c2a_v1.3.md`.
13. Se eliminan dependencias operativas activas de la antigua 03Cbis.

# 46. Estado de la versión

**Versión:** v1.3  
**Estado:** VERSIÓN ESTABLE — candidata a congelación tras prueba real  
**Upstream contractual:** 03.C-1 v1.2  
**Downstream inmediato:** 03.C-2B v1.0  
**Downstream de producción:** 03.C-2C v0.1, solo después de `PASS`  
**Interfaz inmediata:** `PASS | RETURN`  
**Fuente canónica interna:** Bloque E — Contratos RGE  
**Regla de transporte:** copia íntegra literal Bloque E → paquete 03.C-2B  
**Autoclausura semántica:** PROHIBIDA  
**Producción material:** PROHIBIDA EN 03.C-2A

La siguiente prueba debe verificar exclusivamente que:

1. las vistas compactas copien literalmente sus campos controlados;
2. el paquete contenga contratos íntegros idénticos a Bloque E;
3. las versiones upstream permanezcan aisladas;
4. no reaparezca lógica de auditoría propia de 03.C-2B.
