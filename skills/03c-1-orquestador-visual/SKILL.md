---
name: 03c-1-orquestador-visual
description: Define la estrategia visual contractual por NVD y clasifica cada necesidad visual en recurso externo, generativo o hibrido.
stage_id: "03.C-1"
version: "1.2"
status: stable
---

# Skill: 03.C - 1. Skill - orquestador-visual — v1.2

## Posición en el flujo

Esta skill constituye la **capa de análisis, diagnóstico y decisión pedagógica del subsistema visual**.

Opera después de que la sesión dispone de suficiente definición conceptual y normativa, y antes de ejecutar cualquier proceso de búsqueda de recursos existentes o generación de recursos propios.

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
                  [03.C - 1] Orquestador Visual
                               │
                  ┌────────────┼─────────────┐
                  │            │             │
                  ▼            ▼             ▼
              EXTERNO       GENERATIVO     HÍBRIDO
                  │            │             │
                  ▼            ▼             ├─────────────┐
      [03.C - 3] External   [03.C - 2]       │             │
             Resources       Generative      ▼             ▼
                  │            │        External       Generative
                  │            │        Resources
                  │            │             │             │
                  │            │             └──────┬──────┘
                  │            │                    │
                  │            ▼                    ▼
                  │       [03.Cbis]           Recursos combinados
                  │       Generador IA
                  │            │
                  └────────────┴───────────────┐
                                              ▼
                                         [03.D] / [03.E]
```

---

# 1. Propósito

Esta skill analiza una sesión desde el punto de vista de la **comprensión visual del estudiante** y determina:

1. qué conceptos, procesos, relaciones, objetos o fenómenos requieren apoyo visual;
2. cuáles no requieren recurso visual;
3. qué problema cognitivo debe resolver cada recurso;
4. qué función didáctica debe cumplir;
5. qué tipo de representación visual es pedagógicamente más adecuado;
6. si la necesidad debe resolverse mediante:
   - recurso externo existente;
   - recurso generativo propio;
   - combinación híbrida;
   - ningún recurso visual;
7. qué nivel de prioridad tiene cada necesidad;
8. dónde debe utilizarse el recurso resultante;
9. qué downstream skill debe ejecutar cada necesidad.

Su salida principal es la:

**Ficha de Estrategia Visual de la Sesión**

que funciona como **contrato vinculante común** para:

- **03.C - 2.generative**
- **03.C - 3.External-Resources**
- posteriormente, **03.D** y **03.E**.

---

# 2. Principio rector

## La visualización es una decisión pedagógica, no una consecuencia de disponibilidad

La existencia de una imagen en internet no implica que dicha imagen sea la representación adecuada.

La posibilidad de generar una imagen mediante IA tampoco implica que deba generarse.

El criterio principal será siempre:

> **¿Qué representación permite que el estudiante comprenda mejor este concepto, relación, proceso u objeto dentro del objetivo específico de esta sesión?**

---

# 3. Frontera de competencia

## 3.1 Esta skill SÍ debe

1. Analizar el Brief de Sesión.
2. Analizar la clasificación conceptual procedente de 03.A.
3. Considerar restricciones o elementos normativos procedentes de 03.B.
4. Identificar necesidades visuales explícitas e implícitas.
5. Determinar si una representación visual aporta valor cognitivo real.
6. Definir el objetivo didáctico de cada necesidad visual.
7. Clasificar el problema cognitivo que debe resolver.
8. Definir el tipo general de representación recomendado.
9. Determinar la procedencia preferente:
   - EXTERNO;
   - GENERATIVO;
   - HÍBRIDO;
   - NINGUNO.
10. Establecer prioridad.
11. Establecer destino didáctico preliminar.
12. Emitir requerimientos suficientemente claros para que las skills downstream ejecuten sin reinterpretar la intención pedagógica.

---

## 3.2 Esta skill NO debe

1. Buscar imágenes en internet.
2. Descargar archivos.
3. Seleccionar URLs concretas.
4. Elegir entre recursos web específicos.
5. Crear prompts de generación de imagen.
6. Definir parámetros de render.
7. Generar imágenes.
8. Definir paleta, tipografía o Style Lock detallado.
9. Diseñar retículas específicas.
10. Decidir posiciones exactas de nodos, flechas o componentes gráficos.
11. Crear contratos gráficos ejecutables.
12. Modificar contenido disciplinar.
13. Inventar relaciones conceptuales.
14. Inventar datos, normas, medidas, autores o referencias.
15. Convertir automáticamente toda necesidad conceptual en una necesidad visual.

---

## 3.3 Naturaleza contractual y vocabulario controlado

La salida de esta skill es un **contrato de decisión visual**, no una recomendación abierta.

Los campos estructurales definidos por esta skill deberán utilizar exclusivamente los valores enumerados en este documento. No se permiten sinónimos, abreviaturas alternativas ni reformulaciones libres en los campos de control.

### Valores cerrados obligatorios

- `procedencia`: `EXTERNO | GENERATIVO | HÍBRIDO | NINGUNO`
- `prioridad`: `V1 | V2 | V3 | V4`
- `función_primaria`: `A | B | C | D`
- `funciones_secundarias`: subconjunto de `A | B | C | D` sin repetir la función primaria; usar `NINGUNA` si no aplica
- `problema_cognitivo`: `CV-01 | CV-02 | CV-03 | CV-04 | CV-05 | CV-06 | CV-07 | CV-08 | CV-09 | CV-10`
- `estado_nvd`: `PRESCRITA | EN_EJECUCIÓN | SATISFECHA | BLOQUEADA`
- `estado_cobertura_conceptual`: `NVD_NUEVA | CUBIERTA_POR_NVD | NINGUNO`
- `tratamiento_externo`: `EXTERNO_PURO | EXTERNO_CON_ANOTACIÓN | NO_APLICA`
- `familia_representacional`: `FOTOGRAFÍA | ESCENA_DOCUMENTAL | PLANO | MAPA | CARTOGRAFÍA | CAPTURA_SOFTWARE | DOCUMENTO_TÉCNICO | CORTE | DESPIECE | ESQUEMA | DIAGRAMA_CONCEPTUAL | FLUJO | SECUENCIA | CICLO | RED | ÁRBOL | CAPAS | MATRIZ | COMPARATIVA | GRÁFICA | VISUALIZACIÓN_DATOS | INFOGRAFÍA | RECURSO_TÉCNICO_COMPUESTO | RECURSO_MIXTO`
- `modo_agrupación_visual`: `RECURSO_ÚNICO | COMPUESTO_EN_UNA_LÁMINA | SECUENCIA_DE_RECURSOS`

`especificación_representacional` es un campo narrativo obligatorio para toda NVD activa. Describe los componentes semánticos que debe contener la familia prescrita, pero no puede introducir una familia adicional contradictoria ni decisiones gráficas ejecutables.

`unidades_visuales_estimadas` es un entero positivo `>=1` para toda NVD activa. No expresa cantidad definitiva de archivos: expresa cuántas unidades perceptivas independientes se prevé que el estudiante deberá procesar.

Los campos narrativos justificativos sí admiten lenguaje natural, pero no pueden contradecir los valores estructurales.

---

# 4. Insumos y compuerta de ejecución

## 4.1 Insumos obligatorios

- Documento Maestro vigente.
- Brief de Sesión vigente.
- 03.A — Ficha Teórica correspondiente a la sesión.

## 4.2 Insumo normativo condicional

03.B — Ficha Normativa es obligatoria antes de ejecutar esta skill cuando la sesión contenga cualquiera de los siguientes elementos:

- normativa;
- tolerancias;
- especificaciones;
- procedimientos regulados;
- requisitos oficiales;
- documentación técnica cuya interpretación visual dependa de reglas normativas.

Si ninguno de esos elementos aplica, registrar literalmente en metadatos:

`Ficha Normativa de referencia: No aplica`

## 4.3 Orden de ejecución vinculante

El orden válido es:

```text
01 → 02 → 03.A ─┐
                 ├→ 03.C-1 Orquestador Visual
          03.B ──┘  (03.B cuando aplique)
```

03.C-1 no debe ejecutarse directamente desde el Brief si 03.A todavía no existe.

Cuando 03.B sea aplicable, 03.C-1 tampoco debe cerrarse hasta disponer de la Ficha Normativa correspondiente.

## 4.4 Modos de ejecución

La skill admite dos modos:

- `INICIAL`: crea la estrategia visual de la sesión y deja todas las NVD activas en estado `PRESCRITA`.
- `REVISIÓN`: recibe retroalimentación de 03.C-2 o 03.C-3, reevalúa únicamente las NVD afectadas y registra cualquier cambio de estrategia sin alterar silenciosamente las decisiones previas.

---

# 5. Unidad básica de trabajo: Necesidad Visual

La unidad fundamental de esta skill no es una imagen.

Es una:

**Necesidad Visual Didáctica — NVD**

Cada NVD describe una dificultad o intención pedagógica cuya comprensión puede beneficiarse de una representación visual.

---

# 6. Sistema de IDs

Cada necesidad visual recibe un ID persistente con formato:

`NVD-XX`

Ejemplos:

- NVD-01
- NVD-02
- NVD-03

El ID pertenece a la **necesidad pedagógica**, no al archivo final.

Una necesidad puede resolverse posteriormente mediante uno o varios recursos.

Ejemplo:

```text
NVD-04
├── EXT-03
└── GEN-H02
```

Esto significa que una sola necesidad pedagógica fue resuelta mediante una estrategia híbrida.

---

# 7. Regla de persistencia

El ID `NVD-XX` deberá mantenerse durante todo el pipeline:

- Ficha de Estrategia Visual;
- 03.C - 2.generative;
- 03.C - 3.External-Resources;
- registro de recursos resultantes;
- 03.D;
- 03.E;
- auditoría posterior.

Los recursos downstream deberán declarar siempre qué `NVD-XX` satisfacen.

---

# 8. Pregunta principal de análisis

Para cada concepto o relación relevante de la sesión, la skill debe preguntar:

> **¿Existe una dificultad de comprensión que pueda reducirse mediante una representación visual?**

Si la respuesta es **no**, el concepto no debe generar automáticamente un recurso.

Registrar:

`Decisión visual: NINGUNO`

cuando proceda.

---

# 9. Principio de economía visual

No generar necesidades visuales por decoración, variedad estética o simple disponibilidad de imágenes.

Una representación visual debe justificar al menos una de las siguientes funciones:

- reconocer;
- localizar;
- distinguir;
- comparar;
- relacionar;
- secuenciar;
- comprender estructura;
- comprender funcionamiento;
- comprender transformación;
- evidenciar;
- analizar;
- interpretar datos;
- contextualizar espacialmente;
- contextualizar temporalmente;
- reducir abstracción;
- preparar una operación o práctica.

---

## 9.1 Regla de suficiencia visual y no duplicación

Antes de crear una nueva NVD, comprobar si la necesidad ya queda satisfecha por otra NVD existente.

Para cada concepto evaluado se debe asignar uno de estos estados de cobertura:

- `NVD_NUEVA`: requiere una necesidad visual propia.
- `CUBIERTA_POR_NVD`: no requiere una NVD nueva porque otra necesidad ya cubre suficientemente su comprensión. Debe indicarse el ID correspondiente.
- `NINGUNO`: no requiere representación visual.

### Regla de suficiencia

Una NVD puede cubrir más de un concepto únicamente cuando todos ellos comparten el mismo objetivo perceptivo y el mismo mensaje cognitivo central.

No fusionar conceptos en una sola NVD si requieren observaciones, razonamientos o acciones perceptivas diferentes.

Ejemplo válido:

`Concepto B → CUBIERTA_POR_NVD: NVD-03`

Esta regla evita crear recursos redundantes y permite que una sola solución visual satisfaga varias necesidades conceptuales relacionadas.

---

# 10. Clasificación de problemas cognitivos visuales

Cada NVD deberá clasificarse según una categoría primaria.

## CV-01 — Reconocimiento

El alumno necesita reconocer cómo luce físicamente un objeto, instrumento, componente, documento, fenómeno o situación.

Ejemplos de representación:

- fotografía;
- vista real;
- documento auténtico;
- captura real.

Preferencia inicial:

**EXTERNO**, salvo justificación contraria.

---

## CV-02 — Estructura

El alumno necesita comprender:

- partes;
- componentes;
- jerarquía;
- capas;
- organización interna;
- composición.

Representaciones posibles:

- corte;
- despiece;
- esquema estructural;
- árbol;
- capas;
- diagrama jerárquico.

Procedencia:

**EXTERNO o GENERATIVO**, según necesidad de autenticidad o control semántico.

---

## CV-03 — Relación

El alumno necesita comprender cómo se relacionan dos o más entidades.

Relaciones típicas:

- causa-efecto;
- dependencia;
- pertenencia;
- intercambio;
- correspondencia;
- influencia;
- equivalencia;
- oposición.

Representaciones posibles:

- red;
- diagrama conceptual;
- sistema;
- mapa relacional.

Preferencia inicial:

**GENERATIVO** cuando la relación debe ajustarse específicamente a la sesión.

---

## CV-04 — Proceso / Secuencia

El alumno necesita comprender:

- pasos;
- orden;
- procedimiento;
- transformación;
- flujo;
- ciclo;
- retroalimentación.

Representaciones posibles:

- flujo;
- secuencia;
- ciclo;
- entrada-proceso-salida.

Procedencia:

**EXTERNO o GENERATIVO** según fidelidad requerida.

---

## CV-05 — Comparación / Discriminación

El alumno necesita distinguir entre:

- correcto / incorrecto;
- antes / después;
- alternativa A / alternativa B;
- caso normal / caso patológico;
- procedimiento adecuado / deficiente.

Representaciones posibles:

- comparativa;
- matriz;
- paneles paralelos;
- pares visuales.

Procedencia:

frecuentemente **HÍBRIDO o GENERATIVO**.

---

## CV-06 — Espacio / Localización

El alumno necesita comprender:

- posición;
- orientación;
- territorio;
- escala;
- relación espacial;
- distribución.

Representaciones posibles:

- mapa;
- planta;
- corte;
- sección;
- cartografía;
- esquema espacial.

Procedencia:

preferentemente **EXTERNO** cuando exista información real u oficial.

---

## CV-07 — Evidencia / Caso real

El recurso debe demostrar que un fenómeno, condición o problema existe en la realidad.

Representaciones posibles:

- fotografía documental;
- plano real;
- registro de campo;
- documento técnico;
- captura auténtica.

Procedencia:

**EXTERNO obligatorio**, salvo imposibilidad documentada.

---

## CV-08 — Datos / Magnitudes

El alumno necesita interpretar:

- cantidades;
- variaciones;
- tendencias;
- distribuciones;
- proporciones;
- diferencias.

Representaciones posibles:

- gráfica;
- tabla;
- matriz;
- visualización de datos;
- perfil.

Procedencia:

dependerá de la procedencia de los datos.

---

## CV-09 — Síntesis conceptual

El alumno necesita integrar múltiples componentes de una explicación en una sola representación.

Representaciones posibles:

- infografía sintética;
- diagrama compuesto;
- mapa conceptual;
- modelo sistémico.

Preferencia inicial:

**GENERATIVO**, debido a la necesidad de control semántico.

---

## CV-10 — Preparación para práctica

El recurso debe preparar al alumno para una actividad posterior:

- identificación de instrumental;
- lectura de elementos;
- operación;
- interpretación;
- toma de decisiones.

Procedencia:

**EXTERNO**, **GENERATIVO** o **HÍBRIDO**, dependiendo de si la preparación exige reconocimiento real y/o explicación abstracta.

---

# 11. Decisión de procedencia

Cada NVD deberá clasificarse en uno de cuatro estados.

---

## P-EXT — EXTERNO

Usar cuando la autenticidad es pedagógicamente significativa.

Indicadores:

- apariencia real;
- objeto físico;
- instrumento;
- obra;
- patología;
- plano real;
- cartografía oficial;
- documento auténtico;
- manual;
- captura de software;
- fotografía histórica;
- contexto territorial;
- evidencia documental.

Handoff:

**03.C - 3.External-Resources**

---

## P-GEN — GENERATIVO

Usar cuando el control semántico es más importante que la autenticidad documental.

Indicadores:

- relación conceptual específica;
- síntesis creada para la sesión;
- proceso simplificado;
- comparación controlada;
- diagrama pedagógico;
- integración de conceptos provenientes de varias fuentes;
- representación inexistente en una única fuente externa;
- necesidad de eliminar elementos irrelevantes;
- necesidad de mostrar únicamente variables seleccionadas.

Handoff:

**03.C - 2.generative**

---

## P-HYB — HÍBRIDO

Usar cuando la necesidad requiere simultáneamente:

1. contacto con evidencia o realidad;
2. explicación gráfica controlada.

Ejemplos:

- fotografía real + diagrama conceptual;
- plano real + esquema interpretativo;
- instrumento real + corte explicativo;
- captura de software + esquema de flujo;
- caso real + comparativa simplificada.

Handoff:

- **03.C - 3.External-Resources**
- **03.C - 2.generative**

Ambas skills deberán conservar el mismo ID `NVD-XX`.

### Regla de cardinalidad híbrida

Una NVD HÍBRIDA no está limitada a dos archivos. Puede resolverse mediante una relación `1:N` entre una necesidad pedagógica y varios recursos downstream.

Ejemplos válidos:

```text
NVD-05
├── EXT-02
├── EXT-03
└── GEN-H04
```

```text
NVD-08
├── EXT-07
├── GEN-H09
└── GEN-H10
```

Cada recurso deberá declarar el mismo `NVD-XX` padre y una función complementaria explícita.

No se permite multiplicar recursos dentro de una NVD híbrida sin justificar qué función cognitiva específica cumple cada uno.

### Tratamiento de recursos externos

Toda NVD con componente `EXTERNO` —incluidas las `HÍBRIDO`— deberá declarar uno de estos tratamientos:

- `EXTERNO_PURO`: el recurso auténtico puede utilizarse sin superposición explicativa adicional.
- `EXTERNO_CON_ANOTACIÓN`: el recurso auténtico debe conservarse como evidencia base, pero requiere marcas pedagógicas no sintéticas —por ejemplo flechas, recuadros, numeración, etiquetas, resaltado, zoom o callouts— para dirigir la observación del alumno.

La anotación no convierte el recurso en `GENERATIVO` ni en `HÍBRIDO` por sí sola. Solo se usa `HÍBRIDO` cuando además del recurso externo se requiere un recurso generativo autónomo con función cognitiva propia.

03.C-1 únicamente prescribe la necesidad de anotación. 03.C-3 deberá resolver o documentar la pauta de anotación sin inventar contenido disciplinar; 03.D/03.E podrán materializarla durante la composición final.

---

## P-NON — NINGUNO

Usar cuando:

- el concepto ya es suficientemente claro mediante texto o explicación;
- una imagen añadiría decoración sin mejorar comprensión;
- producirla introduciría simplificaciones engañosas;
- el tiempo de clase no justifica su explotación;
- la representación puede aumentar carga cognitiva;
- existe redundancia con otro recurso de mayor prioridad.

No se realiza handoff visual.

---

# 12. Regla de decisión EXTERNO vs GENERATIVO

La elección no depende de qué recurso resulte más fácil de obtener.

Debe aplicarse este criterio:

```text
¿La autenticidad del objeto o documento forma parte de lo que debe aprenderse?
│
├── SÍ ──► EXTERNO
│
└── NO
     │
     ▼
¿Es necesario controlar exactamente relaciones, elementos o simplificación?
│
├── SÍ ──► GENERATIVO
│
└── NO
     │
     ▼
¿Se necesitan simultáneamente autenticidad y explicación controlada?
│
├── SÍ ──► HÍBRIDO
│
└── NO ──► Evaluar EXTERNO, GENERATIVO o NINGUNO según economía visual
```

---

# 13. Prioridad de necesidad visual

Cada NVD recibe un nivel.

## V1 — Imprescindible

Sin el recurso existe riesgo significativo de comprensión incorrecta o insuficiente.

Debe resolverse antes de cerrar 03.D / 03.E.

---

## V2 — Alta utilidad

Mejora considerablemente comprensión, análisis o transferencia.

Debe resolverse salvo restricción operativa.

---

## V3 — Complementaria

Aporta contexto o refuerzo, pero la sesión sigue siendo comprensible sin el recurso.

Puede omitirse si existe sobrecarga visual.

---

## V4 — Profundización

Destinado principalmente a:

- guía docente;
- capítulo;
- anexo;
- ampliación.

No debe competir por espacio con recursos V1 o V2.

---

# 14. Relación con nivel conceptual

La presencia de un concepto en 03.A no implica automáticamente una necesidad visual.

Como orientación:

### Núcleo
Evaluar activamente necesidad visual.

### Panorama
Incluir visual únicamente si facilita comprensión global o diferenciación.

### Propedéutico
Priorizar representaciones simplificadas que preparen comprensión futura.

### Contexto
Normalmente no requiere recurso independiente.

### Reservado
No crear recurso visual salvo necesidad explícita de transición o referencia.

---

# 15. Regla de granularidad

Una NVD debe representar **una intención cognitiva principal**.

Evitar NVD demasiado amplias como:

> “Explicar todo el tema de nivelación”.

Preferir:

- NVD-01 — reconocer partes del nivel óptico;
- NVD-02 — comprender relación entre línea de colimación y horizontal;
- NVD-03 — distinguir lectura correcta e incorrecta del estadal.

---

# 16. Familia representacional y especificación semántica

Esta skill debe prescribir una **familia representacional canónica** para cada NVD activa, pero no diseñar todavía el recurso.

## 16.1 Familia representacional canónica

El campo estructural `familia_representacional` admite exclusivamente uno de los siguientes valores:

- `FOTOGRAFÍA`
- `ESCENA_DOCUMENTAL`
- `PLANO`
- `MAPA`
- `CARTOGRAFÍA`
- `CAPTURA_SOFTWARE`
- `DOCUMENTO_TÉCNICO`
- `CORTE`
- `DESPIECE`
- `ESQUEMA`
- `DIAGRAMA_CONCEPTUAL`
- `FLUJO`
- `SECUENCIA`
- `CICLO`
- `RED`
- `ÁRBOL`
- `CAPAS`
- `MATRIZ`
- `COMPARATIVA`
- `GRÁFICA`
- `VISUALIZACIÓN_DATOS`
- `INFOGRAFÍA`
- `RECURSO_TÉCNICO_COMPUESTO`
- `RECURSO_MIXTO`

### Uso de `RECURSO_TÉCNICO_COMPUESTO`

Usar cuando una misma NVD externa o híbrida necesita **dos o más componentes técnicos auténticos de distinta naturaleza perceptiva** que deben entenderse coordinadamente, por ejemplo:

- fotografía exterior de un instrumento + vista auténtica de ocular;
- fotografía de equipo + extracto de manual técnico;
- plano auténtico + detalle ampliado del mismo documento.

No utilizar esta familia solo porque una lámina tenga varios elementos. Si todos pertenecen a la misma familia perceptiva y forman una comparación o matriz, conservar la familia semántica correspondiente.

### Uso de `RECURSO_MIXTO`

Reservar para casos en los que ninguna familia anterior describe adecuadamente la naturaleza semántica principal. Debe justificarse expresamente. No usar como valor por defecto.

## 16.2 Especificación representacional

Cada NVD activa deberá incluir además el campo narrativo `especificación_representacional`. Este campo describe qué debe contener la representación sin definir todavía su diseño gráfico ejecutable.

Ejemplo:

```text
familia_representacional: RECURSO_TÉCNICO_COMPUESTO
especificación_representacional: fotografía auténtica del nivel óptico montado + vista auténtica del ocular con retícula sobre estadal graduado.
```

La especificación puede indicar componentes, correspondencias o necesidad de coordinación perceptiva, pero no debe fijar:

- retícula;
- distribución exacta;
- posiciones de nodos;
- número o forma de contenedores;
- estilo de conectores;
- gramática gráfica ejecutable;
- paleta;
- tipografía;
- prompt;
- parámetros de render.

Esas decisiones pertenecen a 03.C - 2.generative o a las etapas de composición correspondientes.

## 16.3 Regla de coherencia con tratamiento externo

Cuando `procedencia = EXTERNO` o `HÍBRIDO`, la redacción de `especificación_representacional` debe ser coherente con `tratamiento_externo`:

- Si `tratamiento_externo = EXTERNO_PURO`, la especificación no debe exigir flechas, etiquetas, resaltados, callouts, cotas guía ni otras superposiciones pedagógicas sobre el recurso externo. La explotación puede realizarse verbalmente o en la guía docente.
- Si la comprensión exige una superposición pedagógica sobre el recurso auténtico, debe declararse `EXTERNO_CON_ANOTACIÓN`.
- Mencionar explícitamente una anotación en `especificación_representacional` obliga a utilizar `EXTERNO_CON_ANOTACIÓN`.

La anotación no convierte por sí misma la NVD en `HÍBRIDO`; solo existe `HÍBRIDO` cuando también se requiere un recurso generativo autónomo con función cognitiva propia.

---

# 17. Función didáctica prevista

Cada NVD deberá declarar una sola **función primaria** y, cuando proceda, una o más **funciones secundarias**.

| Código | Función |
|---|---|
| A | Explicación principal |
| B | Análisis o actividad del alumno |
| C | Apoyo del docente |
| D | Profundización / consulta |

Reglas:

- `función_primaria` es obligatoria y solo admite un valor.
- `funciones_secundarias` puede contener cero o más valores distintos de la primaria.
- Si no existe función secundaria, escribir `NINGUNA`.
- Las skills downstream deben heredar ambas sin reinterpretarlas.

Ejemplo válido:

```text
función_primaria: A
funciones_secundarias: [B]
```

No usar valores ambiguos como `A / B` en un solo campo.

---

# 17.1 Presupuesto de unidades visuales

Una `NVD` no equivale necesariamente a un archivo ni a un estímulo visual único. Para controlar la carga perceptiva, cada NVD activa deberá declarar:

- `unidades_visuales_estimadas`: entero positivo `>=1`;
- `modo_agrupación_visual`: `RECURSO_ÚNICO | COMPUESTO_EN_UNA_LÁMINA | SECUENCIA_DE_RECURSOS`.

Definiciones:

- `RECURSO_ÚNICO`: una unidad perceptiva principal resuelve la NVD.
- `COMPUESTO_EN_UNA_LÁMINA`: varios componentes coordinados se perciben como una sola unidad didáctica.
- `SECUENCIA_DE_RECURSOS`: la NVD requiere dos o más unidades visuales sucesivas que no deben fusionarse.

El Orquestador no diseña todavía la lámina ni determina el número definitivo de archivos. Este campo sirve para comprobar que la estrategia global sea compatible con la densidad visual prescrita en B.2.

Antes de cerrar la ficha, sumar `unidades_visuales_estimadas` y justificar cualquier desviación significativa respecto al presupuesto visual global de la sesión.

---

# 18. Destino previsto

Cada necesidad puede marcar uno o varios destinos:

- Presentación;
- Guía docente;
- Actividad;
- Capítulo 03.E;
- Anexo;
- Material complementario.

La skill no asignará todavía un número definitivo de slide salvo que el Brief o la estructura de sesión ya lo determine.

---

# 19. Estructura del documento de salida

La skill genera:

`ficha_estrategia_visual_sesion_[N]_v1.2.md`

con los siguientes bloques:

```text
A. Metadatos
B. Diagnóstico visual global de la sesión
C. Mapa de necesidades visuales
D. Fichas NVD individuales
E. Estrategia de procedencia
F. Matriz de handoff
G. Cobertura conceptual
H. Riesgos y restricciones
I. Dependencias entre recursos
J. Validación estructural
K. Estado de cierre y seguimiento
L. Registro de revisiones estratégicas
```

---

# A. Metadatos

| Campo | Valor |
|---|---|
| Asignatura | [...] |
| Clave | [...] |
| Sesión | [...] |
| Tema | [...] |
| Subtemas | [...] |
| Tipo de sesión | [...] |
| Contexto geográfico | [...] |
| Brief de referencia | [...] |
| Ficha Teórica de referencia | [...] |
| Ficha Normativa de referencia | [...] / No aplica |
| Versión del Orquestador Visual | v1.2 |
| Modo de ejecución | INICIAL / REVISIÓN |
| Fecha de análisis | YYYY-MM-DD |
| Estado | completa / incompleta |

---

# B. Diagnóstico visual global de la sesión

## B.1 Objetivo visual de la sesión

Redactar en 2–5 líneas:

- qué deberá poder reconocer;
- qué deberá poder comprender;
- qué deberá poder distinguir;
- qué deberá poder interpretar visualmente el alumno.

---

## B.2 Densidad visual recomendada

Valores:

- baja;
- media;
- alta.

Justificar según:

- cantidad de conceptos núcleo;
- complejidad relacional;
- duración;
- actividades;
- carga cognitiva prevista.

---

## B.3 Estrategia dominante

Seleccionar una o varias:

- reconocimiento de realidad;
- comprensión estructural;
- comprensión de relaciones;
- comprensión de procesos;
- comparación;
- lectura espacial;
- análisis documental;
- interpretación de datos;
- síntesis conceptual.

---

## B.4 Presupuesto visual global

Registrar:

| Campo | Valor |
|---|---|
| Unidades visuales estimadas totales | [...] |
| Presupuesto compatible con densidad B.2 | sí / no |
| Justificación si excede presupuesto | [...] / No aplica |

La suma deberá derivarse de las fichas D y no estimarse de forma independiente.

---

# C. Mapa de necesidades visuales

## Regla de fuente canónica

**El bloque D — Fichas individuales de Necesidad Visual es la única fuente de verdad contractual de cada NVD.**

Los bloques C, E, F y K son vistas derivadas. Deben copiar literalmente los valores estructurales vigentes de D y nunca introducir, corregir, completar o reinterpretar datos por cuenta propia.

Si existe cualquier discrepancia entre D y una vista derivada, prevalece D y la ficha se considera `INCOMPLETA` hasta regenerar las vistas derivadas.


| NVD | Concepto / relación | Nivel conceptual | Problema cognitivo | Función primaria | Funciones secundarias | Prioridad | Familia representacional | Procedencia | Tratamiento externo | Unidades visuales est. | Agrupación | Destino | Handoff | Estado NVD |
|---|---|---|---|---|---|---|---|---|---|---:|---|---|---|---|
| NVD-01 | [...] | Núcleo | CV-01 | A | NINGUNA | V1 | Fotografía | EXTERNO | EXTERNO_PURO | 1 | RECURSO_ÚNICO | Presentación + Libro | 03.C-3 | PRESCRITA |
| NVD-02 | [...] | Núcleo | CV-03 | A | NINGUNA | V1 | Diagrama conceptual | GENERATIVO | NO_APLICA | 1 | RECURSO_ÚNICO | Presentación + Libro | 03.C-2 | PRESCRITA |
| NVD-03 | [...] | Núcleo | CV-05 | B | A | V2 | COMPARATIVA | HÍBRIDO | EXTERNO_CON_ANOTACIÓN | 1 | COMPUESTO_EN_UNA_LÁMINA | Actividad | 03.C-2 + 03.C-3 | PRESCRITA |

---

# D. Fichas individuales de Necesidad Visual

Usar una ficha por cada `NVD-XX`.

## D.NVD-XX — [Nombre]

**ID:** NVD-XX  
**Concepto o relación objetivo:** [...]  
**Subtema:** [...]  
**Nivel conceptual:** [...]  
**Peso pedagógico:** [...]  
**Función primaria:** A / B / C / D  
**Funciones secundarias:** NINGUNA / [A, B, C, D sin repetir primaria]  
**Prioridad:** V1 / V2 / V3 / V4  

### 1. Dificultad de comprensión

¿Qué podría resultar abstracto, invisible, ambiguo o difícil de distinguir para el estudiante?

[...]

### 2. Objetivo perceptivo

Después de observar el recurso, el alumno deberá poder:

[...]

### 3. Mensaje cognitivo central

Una sola frase.

[...]

### 4. Problema cognitivo

CV-01 / CV-02 / CV-03 / CV-04 / CV-05 / CV-06 / CV-07 / CV-08 / CV-09 / CV-10

Justificación:

[...]

### 5. Familia y especificación representacional

**familia_representacional:** [valor cerrado del §16.1]

**especificación_representacional:**
[...]

### 6. Elementos que necesariamente deben poder observarse

- [...]
- [...]
- [...]

### 7. Elementos que NO son necesarios para esta necesidad

- [...]
- [...]
- [...]

### 8. Procedencia recomendada

EXTERNO / GENERATIVO / HÍBRIDO / NINGUNO

### 9. Justificación de procedencia

[...]

### 9.1 Tratamiento externo

`EXTERNO_PURO | EXTERNO_CON_ANOTACIÓN | NO_APLICA`

Regla:
- EXTERNO e HÍBRIDO deben usar `EXTERNO_PURO` o `EXTERNO_CON_ANOTACIÓN`.
- GENERATIVO y NINGUNO deben usar `NO_APLICA`.

Si usa `EXTERNO_CON_ANOTACIÓN`, describir únicamente qué observación debe guiarse; no diseñar todavía la anotación gráfica.

Si `tratamiento_externo = EXTERNO_PURO`, `especificación_representacional` no puede exigir anotaciones o superposiciones gráficas. Si las exige, cambiar obligatoriamente a `EXTERNO_CON_ANOTACIÓN`.

### 9.2 Presupuesto de unidades visuales

**Unidades visuales estimadas:** [entero >=1]  
**Modo de agrupación visual:** RECURSO_ÚNICO / COMPUESTO_EN_UNA_LÁMINA / SECUENCIA_DE_RECURSOS

Justificación breve:
[...]

### 10. Destino

- Presentación: sí / no
- Guía docente: sí / no
- Actividad: sí / no
- Capítulo: sí / no
- Anexo: sí / no

### 11. Handoff

- 03.C - 2.generative: sí / no
- 03.C - 3.External-Resources: sí / no

### 12. Dependencias

¿Requiere otro recurso para completar la explicación?

[...]

### 13. Riesgo de mala representación

¿Qué error visual o simplificación podría deformar el concepto?

[...]

### 14. Criterio de satisfacción

La NVD se considerará satisfecha cuando:

[...]

### 15. Estado NVD

`PRESCRITA | EN_EJECUCIÓN | SATISFECHA | BLOQUEADA`

En una ejecución `INICIAL`, toda NVD creada deberá salir como `PRESCRITA`.

---

## D.1 Contrato mínimo obligatorio por NVD

Son obligatorios en toda NVD activa:

- ID;
- concepto o relación objetivo;
- subtema;
- nivel conceptual;
- función primaria;
- funciones secundarias;
- prioridad;
- dificultad de comprensión;
- objetivo perceptivo;
- mensaje cognitivo central;
- problema cognitivo;
- familia representacional;
- especificación representacional;
- elementos que deben observarse;
- procedencia;
- justificación de procedencia;
- tratamiento externo;
- unidades visuales estimadas;
- modo de agrupación visual;
- destino;
- handoff;
- riesgo de mala representación;
- criterio de satisfacción;
- estado NVD.

Son condicionales:

- peso pedagógico: obligatorio cuando el Brief lo declare;
- elementos no necesarios: obligatorio para GENERATIVO e HÍBRIDO, recomendable para EXTERNO;
- dependencias: obligatorio solo cuando existan; de lo contrario escribir `No aplica`;
- rasgo de autenticidad indispensable: obligatorio para EXTERNO e HÍBRIDO;
- control semántico indispensable: obligatorio para GENERATIVO e HÍBRIDO;
- descripción de anotación: obligatoria solo cuando `tratamiento_externo = EXTERNO_CON_ANOTACIÓN`.

No se permite cerrar una NVD con campos obligatorios vacíos.

---

# E. Estrategia de procedencia

## E.1 Recursos externos prescritos

| NVD | Necesidad | Tipo de recurso externo requerido | Rasgo de autenticidad indispensable | Tratamiento externo | Unidades visuales est. | Prioridad |
|---|---|---|---|---|---:|---|

Este bloque será consumido por:

**03.C - 3.External-Resources**

No incluir URLs ni candidatos concretos.

---

## E.2 Recursos generativos prescritos

| NVD | Necesidad | Representación requerida | Control semántico indispensable | Unidades visuales est. | Prioridad |
|---|---|---|---:|---|

Este bloque será consumido por:

**03.C - 2.generative**

No incluir prompts ni decisiones gráficas ejecutables.

---

## E.3 Recursos híbridos prescritos

| NVD | Componente externo | Tratamiento externo | Componente generativo | Relación entre ambos | Unidades visuales est. | Prioridad |
|---|---|---|---|---|---:|---|

---

## E.4 Necesidades sin recurso

| Concepto | Motivo para no visualizar |
|---|---|

### Regla de derivación del bloque E

E se construye exclusivamente a partir de D. No puede modificar procedencia, prioridad, tratamiento externo, presupuesto de unidades ni criterio cognitivo.

---

# F. Matriz de handoff

| NVD | 03.C-2 Generative | 03.C-3 External | Ambos | Sin acción |
|---|:---:|:---:|:---:|:---:|
| NVD-01 |  | X |  |  |
| NVD-02 | X |  |  |  |
| NVD-03 |  |  | X |  |

Regla:

Una NVD no puede enviarse simultáneamente como `GENERATIVO` y `EXTERNO` salvo que esté declarada explícitamente como `HÍBRIDO`.

F se deriva de los campos `procedencia` y `handoff` del bloque D. No es una segunda fuente de decisión.

---

# G. Cobertura conceptual

## G.1 Conceptos Núcleo

| Concepto | Estado de cobertura | NVD asociada / NVD que cubre | Justificación |
|---|---|---|---|

---

## G.2 Panorama

| Concepto | Estado de cobertura | NVD asociada / NVD que cubre | Justificación |
|---|---|---|---|

---

## G.3 Propedéutico

| Concepto | Estado de cobertura | NVD asociada / NVD que cubre | Justificación |
|---|---|---|---|

---

## G.4 Contexto y Reservado

Registrar únicamente excepciones relevantes.

---

# H. Riesgos y restricciones

Registrar:

- riesgo de simplificación excesiva;
- riesgo de confusión entre conceptos;
- necesidad de autenticidad documental;
- normativa que limite la representación;
- datos que no deben inventarse;
- escalas que deban conservarse;
- advertencias para generación;
- advertencias para búsqueda;
- limitaciones de proyección;
- riesgo de saturación visual.

---

# I. Dependencias entre recursos

Registrar relaciones entre NVD cuando sea necesario.

Ejemplo:

```text
NVD-01 — fotografía real del instrumento
        ↓ prepara
NVD-02 — diagrama simplificado de funcionamiento
        ↓ permite
NVD-03 — actividad de diagnóstico de error
```

Tipos de dependencia:

- prepara;
- complementa;
- compara;
- amplía;
- demuestra;
- explica;
- aplica.

---

# J. Validación estructural

Antes de cerrar la ficha comprobar:

- [ ] Todos los conceptos Núcleo fueron evaluados visualmente.
- [ ] No se generaron recursos automáticamente solo por existir un concepto.
- [ ] Cada NVD tiene un problema cognitivo definido.
- [ ] Cada NVD tiene objetivo perceptivo.
- [ ] Cada NVD tiene mensaje cognitivo central.
- [ ] Cada NVD activa tiene `familia_representacional` válida y `especificación_representacional` no vacía.
- [ ] Cada NVD tiene procedencia.
- [ ] Toda procedencia está justificada.
- [ ] Cada NVD tiene prioridad.
- [ ] Cada NVD declara una sola función primaria y funciones secundarias sin duplicar la primaria.
- [ ] Cada NVD declara `unidades_visuales_estimadas` y `modo_agrupación_visual`.
- [ ] Toda NVD EXTERNO o HÍBRIDO declara `tratamiento_externo`.
- [ ] Toda NVD con `EXTERNO_CON_ANOTACIÓN` describe qué observación requiere guía sin diseñar la anotación.
- [ ] Ninguna NVD con `EXTERNO_PURO` exige anotaciones, flechas, etiquetas, resaltados, callouts o cotas guía en su `especificación_representacional`.
- [ ] Toda mención explícita de anotación o superposición pedagógica en `especificación_representacional` corresponde a `EXTERNO_CON_ANOTACIÓN`.
- [ ] `RECURSO_TÉCNICO_COMPUESTO` se utiliza solo cuando existen dos o más componentes técnicos auténticos coordinados de distinta naturaleza perceptiva.
- [ ] Cada NVD tiene destino.
- [ ] Cada NVD tiene handoff explícito.
- [ ] Las necesidades híbridas declaran ambos componentes.
- [ ] Las decisiones NINGUNO están justificadas.
- [ ] No existen URLs.
- [ ] No existen búsquedas realizadas.
- [ ] No existen prompts de IA.
- [ ] No existe contrato gráfico ejecutable.
- [ ] No se inventó contenido disciplinar.
- [ ] No se alteró el contenido de 03.A o 03.B.
- [ ] El documento puede ser consumido por 03.C-2 y 03.C-3 sin reinterpretar la intención pedagógica.
- [ ] Los valores estructurales utilizan únicamente vocabulario controlado.
- [ ] Ningún concepto tiene más de una NVD redundante sin justificación.
- [ ] Todo concepto cubierto por otra NVD declara `CUBIERTA_POR_NVD` y el ID correspondiente.
- [ ] Toda NVD HÍBRIDA declara la función diferenciada de cada componente previsto.
- [ ] Los bloques C, E, F y K coinciden literalmente con los valores canónicos del bloque D.
- [ ] No existe ninguna discrepancia de destino, función, prioridad, procedencia, tratamiento externo, unidades visuales o estado entre D y sus vistas derivadas.
- [ ] La suma de unidades visuales estimadas es compatible con la densidad declarada en B.2 o existe justificación explícita en B.4.

---

# K. Estado de cierre y seguimiento

Este bloque resume el estado contractual del subsistema visual de la sesión.

## K.1 Matriz de estado por NVD

| NVD | Procedencia | Prioridad | Unidades visuales est. | Handoff | Estado | Recurso(s) asociado(s) | Observación |
|---|---|---|---:|---|---|---|---|
| NVD-01 | EXTERNO | V1 | 1 | 03.C-3 | PRESCRITA | pendiente | [...] |
| NVD-02 | GENERATIVO | V1 | 1 | 03.C-2 | PRESCRITA | pendiente | [...] |

### Estados permitidos

- `PRESCRITA`: estrategia definida; todavía no ejecutada.
- `EN_EJECUCIÓN`: downstream inició búsqueda o generación.
- `SATISFECHA`: uno o más recursos cumplen el criterio de satisfacción.
- `BLOQUEADA`: existe un conflicto abierto que impide satisfacer la NVD.

## K.2 Resumen cuantitativo

| Indicador | Valor |
|---|---:|
| NVD totales | [...] |
| NVD V1 | [...] |
| NVD V2 | [...] |
| NVD V3 | [...] |
| NVD V4 | [...] |
| EXTERNO | [...] |
| GENERATIVO | [...] |
| HÍBRIDO | [...] |
| Unidades visuales estimadas totales | [...] |
| PRESCRITAS | [...] |
| EN_EJECUCIÓN | [...] |
| SATISFECHAS | [...] |
| BLOQUEADAS | [...] |

## K.3 Estado global de estrategia visual

Valores permitidos:

- `LISTA_PARA_EJECUCIÓN`: todas las NVD tienen contrato completo y no existen bloqueos estructurales.
- `INCOMPLETA`: faltan datos contractuales obligatorios.
- `EN_REVISIÓN`: existe al menos un conflicto estratégico abierto.
- `CERRADA`: todas las NVD V1 y V2 están SATISFECHAS; las V3/V4 pendientes están explícitamente aceptadas como no críticas.

En ejecución `INICIAL`, el resultado normal es `LISTA_PARA_EJECUCIÓN`.

K es una vista de seguimiento derivada del bloque D y de la ejecución downstream. Cuando cambie el estado de una NVD, D y K deberán mantenerse sincronizados; si no lo están, el estado global será `INCOMPLETA`.

---

# L. Registro de revisiones estratégicas

Este bloque permanece vacío en una ejecución inicial salvo que exista corrección durante la misma elaboración.

En modo `REVISIÓN`, registrar una fila por cambio aprobado:

| Fecha | NVD | Código conflicto | Decisión anterior | Decisión nueva | Justificación | Impacto downstream |
|---|---|---|---|---|---|---|

Nunca sobrescribir ni eliminar filas previas.

---

# 20. Reglas de handoff hacia 03.C - 2.generative

03.C - 2.generative deberá recibir únicamente las NVD clasificadas como:

- GENERATIVO;
- HÍBRIDO.

Por cada NVD deberá heredar sin modificar:

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
- unidades visuales estimadas;
- modo de agrupación visual;
- destino;
- restricciones;
- criterio de satisfacción.

A partir de estos datos, 03.C - 2.generative podrá decidir:

- arquitectura visual detallada;
- jerarquía;
- relaciones gráficas;
- Style Lock;
- composición;
- whitelist;
- blacklist;
- contrato gráfico;
- prompt;
- formato;
- resolución;
- criterios de aceptación.

---

# 21. Reglas de handoff hacia 03.C - 3.External-Resources

03.C - 3.External-Resources deberá recibir únicamente las NVD clasificadas como:

- EXTERNO;
- HÍBRIDO.

Por cada NVD deberá heredar sin modificar:

- ID NVD;
- concepto;
- problema cognitivo;
- objetivo perceptivo;
- mensaje cognitivo central;
- tipo de recurso requerido;
- rasgo de autenticidad indispensable;
- prioridad;
- función primaria;
- funciones secundarias;
- tratamiento externo;
- unidades visuales estimadas;
- modo de agrupación visual;
- destino;
- restricciones;
- criterio de satisfacción.

A partir de estos datos, 03.C - 3.External-Resources podrá:

- definir consultas;
- buscar;
- comparar candidatos;
- verificar;
- seleccionar;
- descargar;
- documentar fuente;
- registrar atribución;
- evaluar calidad técnica;
- establecer pauta de explotación docente;
- proponer recorte, zoom o anotación pedagógica no sintética cuando `tratamiento_externo = EXTERNO_CON_ANOTACIÓN`, sin alterar el contenido disciplinar.

---

# 22. Regla de no reinterpretación downstream

03.C - 2.generative y 03.C - 3.External-Resources son skills de **ejecución especializada**.

No deben cambiar por iniciativa propia:

- objetivo perceptivo;
- problema cognitivo;
- mensaje central;
- prioridad;
- procedencia;
- función primaria;
- funciones secundarias;
- tratamiento externo;
- unidades visuales estimadas;
- modo de agrupación visual;
- criterio de satisfacción.

Si una ejecución demuestra que la estrategia prescrita no es viable, la skill no deberá sustituir silenciosamente la decisión.

Debe registrar:

`CONFLICTO DE ESTRATEGIA VISUAL`

y devolver el caso al Orquestador Visual.

---

# 23. Protocolo formal de conflicto y retroalimentación

## 23.1 Causas válidas de conflicto

Solo podrán abrirse conflictos por una o más de estas causas:

- `C01_NO_EXISTE_RECURSO_EXTERNO_ADECUADO`
- `C02_RECURSO_EXTERNO_NO_CUMPLE_CRITERIO_SATISFACCION`
- `C03_REPRESENTACION_GENERATIVA_NO_ES_TECNICAMENTE_VIABLE`
- `C04_RIESGO_DE_ERROR_CONCEPTUAL`
- `C05_AUTENTICIDAD_RESULTA_NECESARIA`
- `C06_CONTROL_SEMANTICO_RESULTA_NECESARIO`
- `C07_SOLUCION_HIBRIDA_RESULTA_NECESARIA`
- `C08_RECURSO_PRESCRITO_ES_REDUNDANTE`
- `C09_RESTRICCION_NORMATIVA_O_DOCUMENTAL`
- `C10_OTRO_JUSTIFICADO`

`C10_OTRO_JUSTIFICADO` exige explicación explícita.

## 23.2 Registro mínimo del conflicto

| Campo | Valor |
|---|---|
| NVD | [...] |
| Skill que reporta | 03.C-2 / 03.C-3 |
| Código de conflicto | C01–C10 |
| Evidencia | [...] |
| Decisión original | EXTERNO / GENERATIVO / HÍBRIDO |
| Recomendación downstream | [...] |
| Estado | abierto / resuelto |

## 23.3 Autoridad de cambio

03.C-2 y 03.C-3 pueden **recomendar** cambios, pero no pueden cambiar la procedencia contractual.

Solo 03.C-1, ejecutado en modo `REVISIÓN`, puede aprobar alguno de estos cambios:

```text
EXTERNO → HÍBRIDO
EXTERNO → GENERATIVO
GENERATIVO → HÍBRIDO
GENERATIVO → EXTERNO
HÍBRIDO → EXTERNO
HÍBRIDO → GENERATIVO
CUALQUIERA → NINGUNO
```

Toda modificación deberá registrar:

- valor anterior;
- valor nuevo;
- código de conflicto;
- justificación;
- fecha de revisión.

## 23.4 Regla de trazabilidad de revisiones

Una revisión nunca elimina la decisión anterior. La conserva como antecedente en el Bloque L — Registro de revisiones estratégicas.

---

# 24. Principio de neutralidad tecnológica

El Orquestador Visual no debe decidir con base en las capacidades de una herramienta específica.

Debe expresar la necesidad pedagógica independientemente de:

- modelo generativo;
- motor de búsqueda;
- software gráfico;
- navegador;
- plataforma;
- formato de archivo final.

Las skills downstream resolverán las decisiones instrumentales.

---

# 25. Principio de trazabilidad

La cadena completa deberá poder reconstruirse:

```text
Concepto disciplinar
        ↓
Necesidad Visual NVD-XX
        ↓
Problema cognitivo
        ↓
Objetivo perceptivo
        ↓
Representación prescrita
        ↓
Procedencia
        ↓
03.C-2 / 03.C-3
        ↓
Recurso final
        ↓
Uso en 03.D / 03.E
```

---

# 26. Criterio de éxito de la skill

La ejecución del Orquestador Visual será satisfactoria cuando pueda responder, para cada recurso futuro:

1. **por qué existe;**
2. **qué dificultad de comprensión resuelve;**
3. **qué debe observar el alumno;**
4. **por qué se eligió esa familia representacional y qué debe contener;**
5. **por qué debe buscarse, generarse o combinarse;**
6. **qué importancia tiene;**
7. **dónde será utilizado;**
8. **qué skill debe producirlo o localizarlo.**

Si alguna de estas preguntas no puede responderse, la estrategia visual aún está incompleta.

---

# 27. Resultado esperado

Al finalizar, la skill entrega una ficha que no contiene todavía recursos visuales.

Contiene:

**decisiones pedagógicas visuales auditables, trazables y ejecutables como contrato downstream.**

Su función es impedir que las siguientes etapas tengan que decidir simultáneamente:

- qué mostrar;
- por qué mostrarlo;
- cómo representarlo;
- dónde obtenerlo;
- cómo producirlo.

El Orquestador decide:

> **qué necesita verse y qué clase de solución visual debe resolverlo.**

03.C - 2.generative decide:

> **cómo construir el recurso propio.**

03.C - 3.External-Resources decide:

> **qué recurso existente satisface mejor el requerimiento.**

03.Cbis:

> **ejecuta la generación prescrita.**

03.D y 03.E:

> **integran y explotan didácticamente los recursos resultantes.**

---

# 28. Estado de versión

**Versión:** v1.2  
**Estado:** estable / contractual — validada tras dos pruebas de aplicación sobre sesión real  
**Rol:** orquestador visual previo a 03.C - 2.generative y 03.C - 3.External-Resources.

### Cambios contractuales respecto de v1.1

1. `representación recomendada` se normaliza como dos campos distintos: `familia_representacional` (vocabulario cerrado) + `especificación_representacional` (descripción semántica narrativa).
2. Se incorpora `RECURSO_TÉCNICO_COMPUESTO` para necesidades externas o híbridas que coordinan dos o más componentes técnicos auténticos de distinta naturaleza perceptiva.
3. Se formaliza la coherencia obligatoria entre `especificación_representacional` y `tratamiento_externo`: una especificación que exija superposición pedagógica no puede declararse `EXTERNO_PURO`.
4. Se añaden validaciones explícitas para detectar contradicciones entre anotación prescrita y tratamiento externo.

### Cambios contractuales heredados de v1.1 respecto de v1.0

1. El bloque D es la **única fuente canónica** de cada NVD; C, E, F y K son vistas derivadas.
2. `función_didáctica` se normaliza como `función_primaria` + `funciones_secundarias`.
3. Se incorporan `unidades_visuales_estimadas` y `modo_agrupación_visual` para controlar economía y carga perceptiva.
4. Se incorpora `tratamiento_externo = EXTERNO_PURO | EXTERNO_CON_ANOTACIÓN | NO_APLICA`.
5. Se mantienen validaciones explícitas de sincronización entre D y sus vistas derivadas.

Esta versión se considera apta para congelar el contrato upstream del subsistema visual antes de adaptar 03.C - 2.generative y 03.C - 3.External-Resources. Las modificaciones posteriores que alteren vocabulario controlado, campos obligatorios, estados, handoffs o reglas de autoridad deberán incrementar versión y revisarse contra ambas skills consumidoras.
