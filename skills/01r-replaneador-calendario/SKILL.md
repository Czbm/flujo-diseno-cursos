---
name: 01r-replaneador-calendario
description: Replanea extraordinariamente el Documento Maestro ante cambios de calendario preservando compatibilidad contractual con Briefs 02.
stage_id: "01.R"
version: "0.1"
status: draft
---

# SKILL: 01.R — Replaneador de Documento Maestro por Cambio de Calendario
### Versión 0.1 — BORRADOR OPERATIVO EXTRAORDINARIO

> **Rol:** replaneador extraordinario del Documento Maestro.
>
> **Posición:** fuera del flujo normal.
>
> **Entrada principal:** Documento Maestro vigente generado por 01 + Briefs vigentes generados por 02 + cambio extraordinario de calendario.
>
> **Salida principal:** nuevo Documento Maestro compatible con 02 v2.8.
>
> **Salida auxiliar:** informe de replaneación.
>
> **Principio rector:** **congelar lo ya ocurrido, cancelar lo imposible y replanear únicamente el futuro.**

---

# 0. Propósito

01.R se activa cuando un curso ya planeado sufre un cambio extraordinario de calendario que invalida una o más fechas previamente disponibles.

Ejemplos:

- suspensión institucional;
- contingencia climática;
- cierre del plantel;
- jornada extraordinaria;
- día inhábil no previsto;
- emergencia;
- pérdida irreversible de una fecha;
- reducción de horas disponibles;
- otra contingencia que cambie la capacidad real del curso.

Esta skill **no crea el curso desde cero**.

Consume el estado vigente del curso y produce un **nuevo Documento Maestro replaneado** que pueda volver a entrar al flujo normal a través de:

```text
Documento Maestro replanteado
        ↓
02.-SKILL-Briefs-Sesion_v2.8
        ↓
nuevos Briefs
        ↓
03.A / 03.B / 03.C / 03.D / 03.E / 04 / 05
```

01.R **no genera los nuevos Briefs**.

Esa responsabilidad sigue perteneciendo exclusivamente a 02.

---

# 1. Posición arquitectónica

## 1.1 Flujo normal

```text
01
↓
02
↓
03...
```

## 1.2 Flujo extraordinario

```text
Documento Maestro vigente
+
Briefs vigentes
+
evento extraordinario
        ↓
      01.R
        ↓
Documento Maestro replanteado
        ↓
      02 v2.8
        ↓
Briefs replanteados
        ↓
flujo normal
```

## 1.3 Regla

01.R no reemplaza permanentemente a 01.

Solo se invoca cuando existe un Documento Maestro previo que debe replanearse.

---

# 2. Compatibilidad

## 2.1 Upstream esperado

- Documento Maestro generado por **01 v1.6** o compatible.
- Briefs generados por **02 v2.8** o compatible.

## 2.2 Downstream obligatorio

- **02 v2.8**.

## 2.3 Contrato de salida

El Documento Maestro replanteado debe conservar todas las secciones necesarias para que 02 v2.8 pueda operar sin adaptadores.

Como mínimo:

- fundamento curricular;
- propósito;
- competencias;
- metodología;
- ponderación;
- actividades oficiales;
- matriz actividad × sesión;
- continuidad conceptual;
- calendario;
- planeación resumida por sesión;
- evaluación;
- **§21 matriz de trazabilidad de competencias**;
- **§22 control de consistencia**;
- **§23 anexos / trazabilidad**.

---

# 3. Qué hace

01.R:

1. identifica la fecha o sesión que deja de estar disponible;
2. determina qué sesiones ya ocurrieron;
3. congela esas sesiones como retrospectivas;
4. marca la sesión afectada como cancelada;
5. calcula la capacidad restante;
6. identifica contenido, actividades, conceptos y competencias afectados;
7. redistribuye únicamente el futuro;
8. recalcula matrices globales;
9. preserva IDs históricos;
10. produce un nuevo Documento Maestro completo;
11. produce un informe de replaneación.

---

# 4. Qué NO hace

01.R no:

- genera Briefs;
- ejecuta 02;
- modifica retrospectivamente lo ya impartido;
- inventa contenido nuevo;
- inventa competencias;
- cambia porcentajes oficiales de evaluación;
- cambia IDs de actividades oficiales;
- renumera sesiones automáticamente;
- elimina trazabilidad histórica;
- borra el Documento Maestro anterior;
- sustituye el temario oficial;
- modifica por comodidad sesiones ya impartidas;
- altera evidencias ya realizadas;
- finge que una carga imposible cabe en menos tiempo.

---

# 5. Entradas obligatorias

## 5.1 Documento Maestro vigente

Debe contener estructura compatible con 01 v1.6.

## 5.2 Briefs vigentes

Se usan como **evidencia histórica y contextual**, no como plantilla de salida.

Permiten comprobar:

- qué estaba previsto por sesión;
- qué sesiones ya fueron desarrolladas;
- actividades asignadas;
- eslabones de competencia;
- continuidad;
- prerequisitos.

## 5.3 Fecha no disponible

Campo obligatorio:

```text
FECHA_CANCELADA
```

Ejemplo:

```text
2026-11-17
```

## 5.4 Fecha de corte

Campo recomendado:

```text
FECHA_CORTE
```

Define el momento desde el cual se ejecuta la replaneación.

Si el usuario no la proporciona pero el contexto temporal es inequívoco, puede derivarse.

Si no puede determinarse con seguridad:

```text
BLOQUEADO_FECHA_CORTE_AMBIGUA
```

## 5.5 Motivo

Opcional:

```text
MOTIVO_EVENTO
```

Se registra únicamente para trazabilidad.

---

# 6. Fuentes de verdad

Orden de autoridad:

1. Documento Maestro vigente.
2. Briefs vigentes.
3. indicación explícita del usuario sobre la fecha cancelada.
4. fecha de corte.
5. información de ejecución ya registrada.
6. inferencias mínimas documentadas.

Los Briefs no pueden contradecir silenciosamente al Maestro.

Si existe conflicto:

```text
CONFLICTO_MAESTRO_BRIEFS
```

y debe resolverse conservadoramente según §31.

---

# 7. Modelo temporal

Cada sesión debe clasificarse en uno de estos estados:

```text
RETROSPECTIVA
CANCELADA
REPLANIFICADA
SIN_CAMBIO_FUTURA
```

## 7.1 RETROSPECTIVA

Sesión ya ocurrida antes de `FECHA_CORTE`.

Es académicamente inmutable salvo corrección documental evidente.

## 7.2 CANCELADA

Sesión cuya fecha dejó de estar disponible.

Permanece en trazabilidad histórica pero no consume capacidad futura.

## 7.3 REPLANIFICADA

Sesión futura cuyo contenido, actividad, propósito o carga cambia por la contingencia.

## 7.4 SIN_CAMBIO_FUTURA

Sesión futura que puede conservarse exactamente.

---

# 8. IDs estables

## 8.1 Regla dura

Los IDs de sesión no se renumeran.

Ejemplo:

```text
S4
S5 CANCELADA
S6
S7
```

No convertir:

```text
S6 → S5
S7 → S6
```

## 8.2 Motivo

Evita romper:

- archivos;
- actividades;
- referencias;
- matrices;
- capítulos;
- recursos visuales;
- auditorías;
- hashes;
- trazabilidad histórica.

---

# 9. Separación entre ID, fecha, orden y estado

Cada sesión debe poder distinguir:

```text
ID_SESION
FECHA
ORDEN_EFECTIVO
ESTADO_REPLANEACION
ESTADO_OPERATIVO
```

El ID es estable.

La fecha puede cambiar.

El orden efectivo puede cambiar solo si es necesario y queda documentado.

El estado operativo sigue siendo compatible con 01 v1.6.

---

# 10. Relación con el estado operativo de 01 v1.6

01 v1.6 usa:

```text
impartida
próxima
pendiente
```

01.R debe preservar compatibilidad con ese campo.

Mapeo recomendado:

| Estado 01.R | Estado operativo compatible |
|---|---|
| RETROSPECTIVA | impartida |
| CANCELADA | pendiente + marca extraordinaria de cancelación |
| REPLANIFICADA | próxima o pendiente según fecha |
| SIN_CAMBIO_FUTURA | próxima o pendiente |

La marca `CANCELADA` vive en la capa de replaneación y en la descripción/calendario, sin redefinir la semántica original de peso pedagógico.

---

# 11. Regla de peso pedagógico

El peso pedagógico sigue perteneciendo al temario.

No se modifica porque una sesión se cancele.

La tabla 7.b debe conservar:

- todos los subtemas;
- peso alto / medio / bajo;
- justificación.

La replaneación puede mover **dónde** se trabaja un subtema.

No cambia su peso solo por contingencia.

---

# 12. Congelamiento retrospectivo

## 12.1 Regla principal

Todo lo ya impartido se considera realidad histórica.

01.R no debe reescribirlo para “hacer cuadrar” la nueva planeación.

## 12.2 Elementos congelados

Por sesión retrospectiva:

- fecha;
- duración real si está registrada;
- unidad;
- temas;
- subtemas;
- actividad realizada;
- evidencia;
- eslabones de competencia cubiertos;
- actividad oficial ya ejecutada;
- continuidad ya ocurrida;
- peso pedagógico heredado.

## 12.3 Correcciones permitidas

Solo:

- error tipográfico;
- inconsistencia documental evidente;
- dato confirmado por evidencia más fuerte.

Debe registrarse como:

```text
CORRECCION_RETROSPECTIVA_DOCUMENTAL
```

Nunca como replaneación pedagógica.

---

# 13. Sesión cancelada

## 13.1 Conservación

La sesión cancelada permanece en el nuevo Maestro.

Debe incluir:

```text
ID_SESION: S[N]
FECHA_ORIGINAL: ...
ESTADO_REPLANEACION: CANCELADA
EJECUTABLE: NO
```

## 13.2 Tratamiento

Su contenido se clasifica en:

```text
YA_CUBIERTO_ANTES
PENDIENTE_OBLIGATORIO
PENDIENTE_REUBICABLE
COMPLEMENTARIO
ELIMINABLE_CON_JUSTIFICACION
```

## 13.3 Prohibición

No borrar la sesión del historial.

---

# 14. Capacidad disponible

Calcular:

```text
CAPACIDAD_ORIGINAL_FUTURA
CAPACIDAD_PERDIDA
CAPACIDAD_RESTANTE
CARGA_PENDIENTE
```

La unidad preferente es minutos cuando las sesiones tienen duraciones distintas.

## 14.1 Capacidad perdida

```text
CAPACIDAD_PERDIDA =
duración de sesión cancelada
```

## 14.2 Capacidad restante

Suma de minutos de sesiones futuras disponibles.

## 14.3 Factibilidad

Si:

```text
CARGA_PENDIENTE <= CAPACIDAD_RESTANTE
```

replaneación potencialmente factible.

Si:

```text
CARGA_PENDIENTE > CAPACIDAD_RESTANTE
```

activar política de priorización.

---

# 15. Prioridad de redistribución

Orden obligatorio:

1. competencias obligatorias;
2. eslabones de competencia incompletos;
3. evaluaciones oficiales comprometidas;
4. prerrequisitos para sesiones posteriores;
5. conceptos nucleares de peso alto;
6. conceptos de peso medio;
7. aplicaciones necesarias;
8. ejemplos;
9. ampliaciones;
10. material complementario.

---

# 16. Acciones permitidas sobre contenido futuro

Cada componente afectado puede recibir:

```text
REUBICAR
CONDENSAR
INTEGRAR
MOVER_A_COMPLEMENTARIO
ELIMINAR_CON_JUSTIFICACION
MANTENER
```

## 16.1 REUBICAR

Mover a otra sesión futura.

## 16.2 CONDENSAR

Reducir tiempo sin eliminar el núcleo conceptual.

## 16.3 INTEGRAR

Fusionar pedagógicamente con contenido compatible de otra sesión.

## 16.4 MOVER_A_COMPLEMENTARIO

Convertir parte no nuclear en estudio autónomo si el diseño del curso lo permite.

## 16.5 ELIMINAR_CON_JUSTIFICACION

Solo para material no crítico.

Nunca para:

- competencia obligatoria;
- evidencia oficial;
- prerrequisito indispensable;
- concepto de peso alto sin cobertura alternativa.

---

# 17. Regla de no sobrecarga

Una sesión futura no puede absorber contenido ilimitadamente.

Para cada sesión:

```text
CARGA_REPLANIFICADA
<=
CAPACIDAD_SESION
```

salvo tolerancia explícita justificada.

Si se supera:

```text
SOBRECARGA_DE_SESION
```

y debe redistribuirse de nuevo.

---

# 18. Competencias

01.R debe reconstruir §21.

Para cada competencia:

```text
introduce
desarrolla
aplica
evalúa
```

## 18.1 Pasado

Eslabones ya cubiertos permanecen fijos.

## 18.2 Futuro

Eslabones originalmente asignados a la sesión cancelada deben:

- reubicarse;
- reclasificarse con justificación;
- o declararse inviables.

## 18.3 Regla de cierre

No emitir Maestro como `Completo` si queda una competencia huérfana sin decisión explícita.

---

# 19. Actividades oficiales

Los IDs `AC-NN` / `AI-NN` permanecen estables.

## 19.1 Actividades ya realizadas

No se modifican retrospectivamente.

## 19.2 Actividades futuras

Puede modificarse:

- sesión de inicio;
- desarrollo;
- consolidación;
- entrega;
- retroalimentación;
- cierre.

No puede modificarse:

- porcentaje oficial;
- criterio oficial;
- identidad de la actividad;

salvo que el Documento Maestro original ya autorizara otra alternativa.

---

# 20. Matriz actividad × sesión

Debe reconstruirse completa.

La sesión cancelada:

```text
no aplica
```

para cualquier estado futuro no realizado.

Los estados ya realizados antes de la cancelación se conservan históricamente.

Cada actividad debe seguir cumpliendo:

```text
inicia/desarrolla
→ entrega
→ cierra
```

cuando corresponda.

---

# 21. Continuidad conceptual

Reconstruir §9.

Para cada concepto:

- preservar introducción ya ocurrida;
- preservar desarrollo ya ocurrido;
- recalcular desarrollo futuro;
- recalcular aplicación;
- recalcular evaluación.

No crear continuidad ficticia.

---

# 22. Evaluación

## 22.1 Porcentajes

Nunca modificar porcentajes oficiales.

## 22.2 Fechas

Pueden reprogramarse si la contingencia lo exige.

## 22.3 Evidencias ya entregadas

Quedan congeladas.

## 22.4 Evidencias futuras

Reubicar sin alterar su peso.

Si una evidencia ya no puede realizarse:

```text
CONFLICTO_EVALUACION_NO_RESUELTO
```

y el Maestro no puede declararse completo.

---

# 23. Prerrequisitos

Antes de mover contenido a una sesión:

verificar que sus prerrequisitos estén:

- ya cubiertos;
- o programados antes.

Está prohibido:

```text
APLICAR antes de DESARROLLAR
EVALUAR antes de INTRODUCIR/DESARROLLAR
```

salvo justificación disciplinar explícita.

---

# 24. Calendario replanteado

La §10 del nuevo Maestro debe conservar la estructura compatible con 01 v1.6.

Añadir de forma no disruptiva información de contingencia.

Ejemplo:

| Sesión | Fecha | Duración | Unidad | Tema | Subtemas | Actividad | Evidencia | Estado |
|---|---|---:|---|---|---|---|---|---|
| S4 | ... | 120 | U2 | ... | ... | ... | ... | impartida |
| S5 | fecha cancelada | 120 | U2 | sesión cancelada por contingencia | — | — | — | pendiente |
| S6 | ... | 120 | U2 | ... replanteado | ... | ... | ... | próxima |

Inmediatamente después de la tabla, registrar:

```text
S5: CANCELADA — NO EJECUTABLE
```

para no alterar el contrato original del campo `estado`.

---

# 25. Planeación resumida por sesión

§11 debe actualizarse.

## 25.1 Retrospectivas

Copiar fielmente el propósito/evidencia histórica.

## 25.2 Cancelada

Declarar:

```text
Sesión cancelada por contingencia.
Sin ejecución.
Contenido redistribuido según informe de replaneación.
```

## 25.3 Futuras

Reescribir propósito y evidencia según nueva distribución.

---

# 26. Metodología

Modificar §5 únicamente si la reducción de tiempo exige un cambio real de estrategia.

Ejemplos:

- más integración de contenidos;
- reducción de exposición;
- aumento de trabajo autónomo;
- sesiones mixtas;
- reorganización de práctica.

No reescribir metodología si no cambia materialmente.

---

# 27. Ponderación

## 27.1 §7.a

Actualizar sesiones asignadas por unidad.

## 27.2 §7.b

Conservar pesos de subtemas salvo error previo.

## 27.3 §7.c

Conservar IDs y criterios oficiales.

Actualizar únicamente distribución temporal.

---

# 28. Secciones 21, 22 y 23

## 28.1 §21 — Trazabilidad de competencias

Debe recalcularse completamente.

## 28.2 §22 — Control de consistencia

Debe declarar:

```text
Completo
Condicionado
Incompleto
```

según resultado real de la replaneación.

## 28.3 §23 — Anexos / trazabilidad

Añadir:

- Documento Maestro baseline;
- Briefs baseline;
- fecha de corte;
- fecha cancelada;
- motivo;
- decisiones automáticas;
- redistribuciones;
- contenidos eliminados;
- supuestos;
- limitaciones;
- referencia al informe de replaneación.

---

# 29. Uso de los Briefs originales

Los Briefs vigentes cumplen tres funciones:

1. confirmar granularidad de cada sesión;
2. identificar dependencias y eslabones;
3. ayudar a congelar el pasado.

No se transforman directamente.

No se usan como plantilla para producir nuevos Briefs.

Después de 01.R:

```text
nuevo Maestro → 02 v2.8 → nuevos Briefs
```

---

# 30. Detección de sesiones retrospectivas

Regla principal:

```text
FECHA_SESION < FECHA_CORTE
→ RETROSPECTIVA
```

Si existen registros explícitos de impartición, tienen prioridad sobre inferencia por fecha.

Una fecha anterior no garantiza impartición si hay evidencia de suspensión previa.

---

# 31. Conflictos entre Maestro y Briefs

## 31.1 Maestro dice impartida, Brief existe y coincide

Aceptar.

## 31.2 Maestro dice pendiente, pero existe evidencia inequívoca de impartición

Marcar:

```text
CONFLICTO_ESTADO_HISTORICO
```

Usar evidencia real solo si está documentada.

## 31.3 Maestro y Brief difieren en contenido

No fusionar arbitrariamente.

Prioridad:

```text
realidad ejecutada documentada
> Maestro formal
> Brief
```

Registrar decisión en informe.

---

# 32. Factibilidad de replaneación

Estados:

```text
REPLANEACION_FACTIBLE
REPLANEACION_FACTIBLE_CON_REDUCCION
REPLANEACION_CONDICIONADA
REPLANEACION_INVIABLE
```

## 32.1 FACTIBLE

Todo cabe sin eliminar contenido significativo.

## 32.2 FACTIBLE_CON_REDUCCION

Se elimina/traslada contenido no crítico.

## 32.3 CONDICIONADA

Permanece alguna restricción no bloqueante documentada.

## 32.4 INVIABLE

No puede conservarse:

- competencia obligatoria;
- evaluación oficial;
- prerrequisito crítico;

con la capacidad restante.

---

# 33. Política de replaneación automática

En ausencia de instrucciones adicionales:

1. congelar pasado;
2. conservar evaluación;
3. conservar competencias;
4. conservar peso alto;
5. preservar secuencia;
6. reducir ejemplos;
7. condensar peso medio;
8. mover ampliaciones a complementario;
9. eliminar solo contenido de baja prioridad;
10. no exceder capacidad.

---

# 34. No renumeración

Además de sesiones, conservar:

- IDs de competencias;
- IDs de actividades;
- IDs de unidades;
- IDs de evidencias;
- nombres institucionales.

Solo crear nuevos IDs si la replaneación requiere un elemento realmente nuevo y el contrato original lo permite.

---

# 35. Output 1 — Documento Maestro replanteado

Nombre recomendado:

```text
documento_maestro_[asignatura]_replaneado_[fecha].md
```

Ejemplo:

```text
documento_maestro_topografia_replaneado_2026-11-17.md
```

Debe ser autocontenido.

No debe requerir consultar el Maestro anterior para que 02 pueda usarlo.

---

# 36. Metadata del nuevo Maestro

Añadir en encabezado:

```text
Tipo de planeación: REPLANEACION_EXTRAORDINARIA
Baseline: [archivo]
Skill de origen: 01.R v0.1
Fecha de corte: [...]
Fecha cancelada: [...]
Estado de replaneación: [...]
Documento sustituido operativamente: [...]
```

Esto no reemplaza los metadatos normales del Maestro.

---

# 37. Output 2 — Informe de replaneación

Nombre:

```text
informe_replaneacion_[asignatura]_[fecha].md
```

No es insumo obligatorio de 02.

Es un artefacto de trazabilidad.

---

# 38. Estructura del informe

```markdown
# Informe de replaneación

## 1. Baseline
- Documento Maestro:
- Briefs:
- Fecha de corte:
- Fecha cancelada:
- Motivo:

## 2. Estado temporal
| Sesión | Fecha | Estado anterior | Estado nuevo |

## 3. Capacidad
- Capacidad original futura:
- Capacidad perdida:
- Capacidad restante:
- Carga pendiente:

## 4. Impacto
### Competencias
### Conceptos
### Actividades
### Evaluaciones
### Prerrequisitos

## 5. Redistribución
| Elemento | Origen | Destino | Acción | Justificación |

## 6. Sesiones modificadas
| Sesión | Cambio |

## 7. Sesiones intactas
| Sesión | Motivo de conservación |

## 8. Contenido reducido/eliminado
| Elemento | Acción | Justificación |

## 9. Cobertura final
### Competencias
### Conceptos
### Actividades

## 10. Riesgos
- ...

## 11. Estado
REPLANEACION_FACTIBLE / ...
```

---

# 39. Compatibilidad obligatoria con 02 v2.8

Antes de cerrar, verificar que 02 pueda extraer:

- datos operativos;
- calendario;
- peso por subtema;
- modo;
- alcance;
- actividades oficiales;
- articulación;
- continuidad;
- §21;
- eslabones de competencia.

## 39.1 Regla

El nuevo Maestro debe permitir a 02 generar **36 campos por Brief** sin usar el Maestro anterior.

---

# 40. Tratamiento de sesión cancelada en 02

01.R no modifica 02.

Por tanto, el Maestro debe expresar la cancelación de forma que 02 pueda reconocerla sin romper su contrato.

Recomendación para el nuevo Maestro:

```text
Tipo especial: sesión cancelada por contingencia
Ejecución downstream: NO
Actividad oficial: no aplica
Propósito: trazabilidad histórica de calendario
```

Si 02 v2.8 no reconoce explícitamente `CANCELADA`, el Brief derivado puede conservarse como registro pero debe quedar marcado en el Maestro como **NO EJECUTABLE**.

Este punto deberá probarse en una ejecución real.

---

# 41. Regla de downstream

Una sesión `CANCELADA`:

```text
NO debe avanzar a 03.A / 03.B / 03.C / 03.D / 03.E
```

Los Briefs de sesiones retrospectivas pueden existir como referencia histórica.

Los Briefs de sesiones futuras replanteadas son los que alimentan producción nueva.

---

# 42. Regla para sesiones retrospectivas y downstream

Si una sesión retrospectiva ya tiene productos 03.* válidos:

```text
REUTILIZAR
```

No regenerar por el mero hecho de haber creado un Maestro replanteado.

El orquestador debe comparar el contenido sustantivo de esa sesión, no solo el hash global del nuevo Maestro.

---

# 43. Delta de replaneación

El informe debe producir un delta explícito:

```text
SESIONES_RETROSPECTIVAS
SESIONES_CANCELADAS
SESIONES_REPLANIFICADAS
SESIONES_FUTURAS_SIN_CAMBIO
```

Esto permitirá invalidación mínima downstream.

---

# 44. Ejemplo

## Estado original

```text
S1  impartida
S2  impartida
S3  impartida
S4  próxima
S5  pendiente
S6  pendiente
S7  pendiente
S8  pendiente
```

Se cancela la fecha de S5.

## Resultado 01.R

```text
S1 RETROSPECTIVA
S2 RETROSPECTIVA
S3 RETROSPECTIVA

S4 REPLANIFICADA
S5 CANCELADA
S6 REPLANIFICADA
S7 REPLANIFICADA
S8 REPLANIFICADA
```

Redistribución:

```text
C3 desarrolla: S5 → S6
Tema X: S5 → S6
Actividad AI-02 consolida: S5 → S7
Ejemplo ampliado Y: S5 → MATERIAL_COMPLEMENTARIO
```

Después:

```text
Documento Maestro replanteado
→ 02 v2.8
→ nueva colección de Briefs
```

---

# 45. Criterio de mínima modificación

Ante varias replaneaciones válidas, preferir la que:

1. modifica menos sesiones;
2. preserva secuencia original;
3. conserva evaluaciones;
4. conserva competencias;
5. evita sobrecarga;
6. reduce menos contenido;
7. altera menos dependencias downstream.

---

# 46. Manejo de varias fechas canceladas

v0.1 puede aceptar:

```text
FECHAS_CANCELADAS = [fecha1, fecha2, ...]
```

pero la interfaz primaria es una fecha.

Si hay varias:

- tratarlas como un único evento;
- recalcular capacidad total;
- no ejecutar replaneaciones independientes acumulativas si pueden resolverse conjuntamente.

---

# 47. Cambio de duración sin cancelación

También puede manejar:

```text
DURACION_REDUCIDA
```

Ejemplo:

```text
S8: 120 min → 60 min
```

Se trata como pérdida parcial de capacidad.

---

# 48. Reprogramación

Si la sesión no se pierde sino que cambia de fecha:

```text
REPROGRAMADA
```

No redistribuir contenido salvo que el cambio altere prerrequisitos.

En ese caso actualizar calendario y matrices necesarias.

---

# 49. Prohibición de compensación ficticia

No declarar:

```text
"se cubrirá más rápido"
```

sin ajustar:

- minutos;
- carga;
- metodología;
- alcance.

Toda condensación debe ser explícita.

---

# 50. Control de calidad

Antes de entregar:

## Temporal

- [ ] Fecha cancelada identificada.
- [ ] Fecha de corte definida.
- [ ] Sesiones retrospectivas congeladas.
- [ ] Sesión cancelada conservada.
- [ ] IDs no renumerados.

## Curricular

- [ ] Competencias completas o decisión explícita.
- [ ] §21 recalculada.
- [ ] Continuidad conceptual consistente.
- [ ] Actividades oficiales completas.
- [ ] Evaluación suma lo mismo que baseline.
- [ ] Porcentajes no modificados.
- [ ] Prerrequisitos válidos.

## Capacidad

- [ ] Capacidad perdida calculada.
- [ ] Capacidad restante calculada.
- [ ] No hay sobrecarga silenciosa.
- [ ] Reducciones justificadas.

## Documento

- [ ] §7.b conserva todos los pesos.
- [ ] §8 actualizada.
- [ ] §9 actualizada.
- [ ] §10 actualizada.
- [ ] §11 actualizada.
- [ ] §21 actualizada.
- [ ] §22 actualizada.
- [ ] §23 registra replaneación.
- [ ] Documento autocontenido.
- [ ] Consumible por 02 v2.8.

---

# 51. Estados terminales

## Éxito

```text
DOCUMENTO_MAESTRO_REPLANEADO_COMPLETO
```

## Éxito condicionado

```text
DOCUMENTO_MAESTRO_REPLANEADO_CONDICIONADO
```

## Fallos

```text
BLOQUEADO_FECHA_CORTE_AMBIGUA
CONFLICTO_MAESTRO_BRIEFS
REPLANEACION_INVIABLE
CONFLICTO_EVALUACION_NO_RESUELTO
COMPETENCIA_HUERFANA_POST_REPLANEACION
SOBRECARGA_NO_RESUELTA
```

---

# 52. Routing tras cierre

Si:

```text
DOCUMENTO_MAESTRO_REPLANEADO_COMPLETO
```

o:

```text
DOCUMENTO_MAESTRO_REPLANEADO_CONDICIONADO
```

entonces:

```text
RUN 02 v2.8
```

01.R termina ahí.

No ejecuta 02 por sí misma.

---

# 53. Integración futura con Orquestador Autónomo

01.R permanece fuera del flujo normal.

El orquestador solo debe invocarla si recibe explícitamente un evento extraordinario de calendario.

Ejemplo:

```text
EVENTO = CANCELACION_DE_FECHA
FECHA = ...
```

Entonces:

```text
Maestro vigente + Briefs vigentes
→ 01.R
→ nuevo Maestro
→ 02
→ invalidación mínima downstream
```

Sin evento extraordinario:

```text
01.R = NO_APLICA
```

---

# 54. Reutilización downstream

El nuevo Maestro cambia globalmente, pero no debe provocar por sí solo regeneración total.

Después de generar los nuevos Briefs:

- Brief retrospectivo sustantivamente idéntico → reutilizar downstream;
- Brief futuro idéntico → reutilizar downstream;
- Brief replaneado → invalidar downstream;
- Brief cancelado → retirar del grafo activo.

---

# 55. Regla de trazabilidad histórica

Nunca sobrescribir silenciosamente:

- Documento Maestro original;
- Briefs originales.

El nuevo Maestro debe señalar su baseline.

Recomendación:

```text
baseline → conservar
replaneado → nuevo archivo
```

---

# 56. Nombre de la skill

Nombre canónico:

```text
01.R — Replaneador de Documento Maestro por Cambio de Calendario
```

Versión:

```text
v0.1
```

Estado:

```text
BORRADOR OPERATIVO EXTRAORDINARIO
```

---

# 57. Criterio final de calidad

01.R cumple cuando:

- conserva intacto el pasado real;
- identifica correctamente la sesión cancelada;
- preserva IDs;
- redistribuye solo el futuro;
- no cambia pesos oficiales;
- no modifica porcentajes de evaluación;
- mantiene competencias completas;
- evita sobrecarga;
- produce un Documento Maestro autocontenido;
- ese Maestro puede ser consumido directamente por 02 v2.8;
- genera un informe de trazabilidad;
- no duplica las funciones de 02;
- no altera el flujo normal cuando no existe contingencia.

---

# 58. Estado de versión

**v0.1 — BORRADOR PARA PRUEBA REAL**

Prueba mínima recomendada:

1. un curso con varias sesiones ya impartidas;
2. una fecha futura cancelada;
3. al menos una competencia afectada;
4. al menos una actividad oficial afectada;
5. una sesión futura que pueda conservarse;
6. una sesión futura que deba replanearse;
7. generación posterior con 02 v2.8.

La prueba debe verificar especialmente que los Briefs producidos por 02 sean coherentes sin consultar el Maestro anterior.

---

# 59. Changelog v0.1

Primera versión.

Decisiones arquitectónicas:

1. 01.R se mantiene fuera del flujo normal.
2. No sustituye 01.
3. No genera Briefs.
4. Consume Maestro + Briefs como baseline.
5. Produce un nuevo Documento Maestro.
6. El nuevo Maestro es consumido por 02 v2.8.
7. El pasado queda congelado.
8. La sesión cancelada conserva ID.
9. Solo el futuro se redistribuye.
10. Se recalculan matrices globales.
11. Se preservan §21, §22 y §23.
12. Se produce informe auxiliar de replaneación.
13. No se renumeran sesiones.
14. No se modifican porcentajes oficiales.
15. Se prioriza mínima modificación.
