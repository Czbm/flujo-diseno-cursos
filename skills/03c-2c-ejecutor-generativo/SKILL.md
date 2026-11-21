---
name: 03c-2c-ejecutor-generativo
description: Ejecuta la produccion tecnica de Recursos Generativos Educativos certificados con PASS por 03.C-2B.
stage_id: "03.C-2C"
version: "0.1"
status: draft
---

# SKILL: 03.C-2C — Ejecutor de Recursos Generativos
### Versión 0.1 — BORRADOR OPERATIVO

> **Rol:** ejecutor técnico de recursos generativos ya aprobados.
>
> **Posición:** downstream de 03.C-2B `PASS`, upstream de 03.D / 03.E.
>
> **Principio rector:** **producir sin reinterpretar**.
>
> Esta skill no diseña el recurso, no decide su semántica y no audita el contrato. Su función es convertir un **RGE exacto, ya auditado y aprobado**, en un **archivo visual utilizable y trazable**.

---

# 0. Propósito

03.C-2C existe para cerrar la brecha entre:

```text
RGE aprobado por 03.C-2B
        ↓
      PASS
        ↓
   [producción]
        ↓
archivo visual utilizable
```

La salida terminal de esta skill es:

```text
RECURSO_GENERATIVO_RESUELTO
```

Este estado significa que:

1. existe un RGE exacto;
2. ese RGE obtuvo `PASS` en 03.C-2B;
3. la huella auditada coincide con el contrato recibido;
4. el recurso fue producido;
5. el archivo existe y es técnicamente utilizable;
6. el resultado respeta de forma observable el contrato aprobado;
7. el archivo fue registrado con identidad y hash;
8. puede entregarse a 03.D / 03.E.

---

# 1. Posición en el subsistema 03.C

```text
                         03.C-1
                  Orquestador Visual
                         │
              ┌──────────┴───────────┐
              │                      │
          GENERATIVO               HÍBRIDO
              │                      │
              ▼                      ▼
           03.C-2A                03.C-2A
       Diseñador RGE            Diseñador RGE
              │                      │
              ▼                      ▼
           03.C-2B                03.C-2B
     Auditor Semántico       Auditor Semántico
              │                      │
        PASS / RETURN          PASS / RETURN
              │                      │
             PASS                   PASS
              ▼                      ▼
           03.C-2C                03.C-2C
     Ejecutor Generativo      Ejecutor Generativo
              │                      │
              ▼                      ▼
RECURSO_GENERATIVO_RESUELTO   componente generativo resuelto
                                     │
                                     ├── + componente 03.C-3
                                     ▼
                              RECURSO_HÍBRIDO_RESUELTO
```

Después:

```text
RECURSO_GENERATIVO_RESUELTO
          │
     ┌────┴────┐
     ▼         ▼
   03.D       03.E
```

---

# 2. Pregunta que responde esta skill

03.C-2C responde únicamente:

> **¿Cómo producir fielmente el recurso visual definido por este RGE exacto y aprobado, sin cambiar su significado?**

No responde:

- ¿Hace falta un recurso visual?
- ¿Qué función didáctica debe tener?
- ¿Qué procedencia debe usar?
- ¿Qué contenido debe representar?
- ¿Qué relaciones deben existir?
- ¿Qué arquitectura debería usarse?
- ¿La semántica del RGE es correcta?
- ¿Debe cambiarse el contrato?
- ¿Qué recurso externo sería mejor?

Esas preguntas pertenecen a otras skills.

---

# 3. Autoridad contractual

La autoridad se distribuye así:

| Decisión | Autoridad |
|---|---|
| necesidad visual / NVD | 03.C-1 |
| procedencia | 03.C-1 |
| función visual | 03.C-1 |
| destino | 03.C-1 |
| familia representacional | 03.C-1 |
| diseño generativo | 03.C-2A |
| contenido del RGE | 03.C-2A |
| whitelist / blacklist | 03.C-2A |
| relaciones | 03.C-2A |
| arquitectura | 03.C-2A |
| auditoría semántica | 03.C-2B |
| PASS / RETURN | 03.C-2B |
| producción técnica | **03.C-2C** |
| selección de recurso externo | 03.C-3 |
| integración didáctica downstream | 03.D / 03.E |

## 3.1 Regla absoluta

03.C-2C **no puede modificar ninguna decisión cuya autoridad pertenezca a 03.C-1, 03.C-2A o 03.C-2B**.

---

# 4. Entradas obligatorias

Para cada recurso generativo:

| Campo | Obligatorio |
|---|---|
| `ID_NVD` | Sí |
| `ID_RGE` | Sí |
| contrato RGE literal auditado | Sí |
| `HUELLA_RGE_AUDITADO` | Sí |
| veredicto `PASS` de 03.C-2B | Sí |
| referencia al informe 03.C-2B | Sí |
| motor de producción autorizado | Sí |
| formato de salida autorizado | Sí |
| orientación / relación de aspecto | Sí |
| ruta o convención de salida | Sí |
| criterios técnicos observables | Sí |
| whitelist | Sí |
| blacklist | Sí |
| arquitectura visual | Sí |
| Style Lock o equivalente | Cuando aplique |
| restricciones de texto | Cuando aplique |

## 4.1 Entrada inválida

Si falta cualquiera de:

- `ID_RGE`;
- `PASS`;
- `HUELLA_RGE_AUDITADO`;
- contrato auditado;
- motor;
- formato;

resultado:

```text
BLOQUEADO_ENTRADA_INCOMPLETA
```

No producir.

---

# 5. Gate de identidad antes de producir

Antes de llamar a cualquier motor:

## 5.1 Verificar contrato exacto

Calcular SHA-256 del contrato RGE recibido usando la misma representación canónica exigida por 03.C-2B.

Comparar:

```text
HASH_RGE_RECIBIDO
==
HUELLA_RGE_AUDITADO
```

Si no coincide:

```text
CONTRATO_DISTINTO_DEL_AUDITADO
```

y detener.

## 5.2 Verificar identidad

Debe coincidir:

```text
ID_RGE recibido
=
ID_RGE auditado
```

## 5.3 Verificar PASS

Solo se acepta:

```text
PASS
```

No se acepta:

- RETURN;
- pendiente;
- aprobado informalmente;
- “parece correcto”;
- captura de pantalla del contrato;
- versión corregida después del PASS;
- resumen parcial del RGE.

## 5.4 Resultado del gate

Estados:

```text
GATE_IDENTIDAD_PASS
GATE_IDENTIDAD_BLOCK
```

---

# 6. Principios de ejecución

## P1. Fidelidad antes que creatividad

El ejecutor no mejora conceptualmente el recurso.

## P2. Producción ≠ diseño

La producción resuelve microdecisiones gráficas, no decisiones semánticas.

## P3. PASS = permiso de producir

`PASS` no significa que el archivo ya exista.

## P4. El archivo debe ser trazable

Todo archivo debe poder rastrearse hasta:

```text
ID_NVD
→ ID_RGE
→ HUELLA_RGE_AUDITADO
→ PASS
→ ejecución
→ archivo
→ HASH_ARCHIVO
```

## P5. Error técnico no invalida automáticamente el contrato

Si el motor genera mal un contrato correcto, se reintenta producción sin alterar el RGE.

## P6. Error contractual no se parchea en producción

Si producir exige cambiar el contrato:

```text
CONFLICTO_DE_CONTRATO
→ 03.C-2A
→ nueva 03.C-2B
```

---

# 7. Decisiones permitidas a 03.C-2C

Siempre que no cambien semántica:

- márgenes;
- separación;
- alineación;
- escala relativa;
- balance espacial;
- microajustes tipográficos;
- distribución interna dentro de la arquitectura prescrita;
- ruteo técnico de conectores;
- posición fina de anotaciones;
- tamaño de iconos;
- adaptación del wording técnico del prompt al motor;
- conversión del contrato a sintaxis requerida por herramienta;
- resolución final;
- compresión;
- perfil de exportación;
- nombre de archivo;
- carpeta de salida.

---

# 8. Decisiones prohibidas

03.C-2C no puede:

- añadir conceptos;
- quitar conceptos obligatorios;
- cambiar categorías;
- cambiar jerarquías;
- cambiar causalidad;
- cambiar origen/destino de relaciones;
- añadir procesos;
- añadir datos;
- inventar medidas;
- añadir texto disciplinar no autorizado;
- eliminar relaciones obligatorias;
- convertir flujo en ciclo;
- convertir comparación en jerarquía;
- cambiar familia representacional;
- cambiar función primaria;
- cambiar procedencia;
- cambiar destino;
- cambiar whitelist;
- cambiar blacklist;
- cambiar arquitectura;
- cambiar criterio de satisfacción;
- cambiar tratamiento externo;
- cambiar RGE;
- declarar PASS;
- corregir un RGE fallido;
- reinterpretar una ambigüedad contractual.

---

# 9. Fases de ejecución

```text
Fase 1 — Verificación de identidad
Fase 2 — Preflight técnico
Fase 3 — Compilación para motor
Fase 4 — Producción
Fase 5 — Verificación técnica y observable
Fase 6 — Reintento controlado
Fase 7 — Registro, hash y handoff
```

---

# 10. Fase 1 — Verificación de identidad

## 10.1 Checklist

- ¿ID_NVD existe?
- ¿ID_RGE existe?
- ¿PASS existe?
- ¿HUELLA_RGE_AUDITADO existe?
- ¿el contrato recibido coincide byte/canónicamente?
- ¿el RGE no fue modificado después del PASS?
- ¿la versión del informe 03.C-2B es identificable?

## 10.2 Resultado

```text
IDENTIDAD_VERIFICADA
```

o:

```text
CONTRATO_DISTINTO_DEL_AUDITADO
```

---

# 11. Fase 2 — Preflight técnico

El preflight técnico verifica **producibilidad**, no semántica.

## 11.1 Motor

Preguntas:

- ¿el motor existe?
- ¿está disponible?
- ¿puede producir el tipo de recurso?
- ¿puede producir el formato requerido?
- ¿puede respetar relación de aspecto?
- ¿puede producir texto legible si es necesario?
- ¿puede respetar restricciones de transparencia si existen?
- ¿puede respetar editabilidad si fue exigida?

## 11.2 Formato

Validar:

- PNG;
- JPG/JPEG;
- SVG;
- WebP;
- PDF;
- otro formato explícitamente autorizado.

No cambiar formato por preferencia del ejecutor.

## 11.3 Dimensiones

Si el contrato define:

```text
ancho
alto
aspect ratio
orientación
```

son vinculantes dentro de tolerancia técnica permitida.

## 11.4 Dependencia de texto

Clasificar:

```text
TEXTO_CRITICO
TEXTO_SECUNDARIO
SIN_TEXTO
```

Si el motor no puede producir texto suficientemente fiable y el contrato exige texto crítico:

```text
BLOQUEADO_MOTOR_INADECUADO
```

No improvisar otra representación.

## 11.5 Editabilidad

Si:

```text
EDITABILIDAD_REQUERIDA = SI
```

y el motor solo produce raster:

```text
BLOQUEADO_FORMATO_INCOMPATIBLE
```

## 11.6 Resultado

```text
PREFLIGHT_TECNICO_PASS
PREFLIGHT_TECNICO_BLOCK
```

---

# 12. Fase 3 — Compilación para motor

03.C-2C puede transformar el contrato RGE a una instrucción ejecutable para la herramienta.

## 12.1 Puede

- reordenar instrucciones;
- convertir campos tabulares a lenguaje natural;
- repetir restricciones críticas;
- hacer explícita la arquitectura;
- declarar tamaño/formato;
- declarar orientación;
- declarar fondo;
- declarar Style Lock;
- declarar whitelist;
- declarar blacklist;
- declarar relaciones;
- declarar finalidad del recurso.

## 12.2 No puede

- resumir eliminando contenido obligatorio;
- reinterpretar términos;
- introducir sinónimos disciplinares con cambio de alcance;
- fusionar relaciones;
- inventar descripciones visuales con significado nuevo;
- suavizar una prohibición.

## 12.3 Trazabilidad de compilación

Registrar:

```text
HASH_RGE_AUDITADO
HASH_INSTRUCCION_EJECUTADA
MOTOR
VERSION_MOTOR
FECHA
```

`HASH_INSTRUCCION_EJECUTADA` no sustituye `HUELLA_RGE_AUDITADO`.

---

# 13. Fase 4 — Producción

## 13.1 Ejecución

Invocar el motor autorizado con:

- instrucción compilada;
- formato;
- dimensiones;
- relación de aspecto;
- transparencia cuando aplique;
- parámetros técnicos permitidos.

## 13.2 Salida temporal

Nunca escribir directamente sobre un recurso aprobado existente.

Usar:

```text
/tmp_generacion/
```

o equivalente.

## 13.3 Nombre temporal

```text
tmp_[ID_RGE]_intento_[N].[ext]
```

---

# 14. Fase 5 — Verificación técnica

La verificación ocurre sobre el archivo producido.

## 14.1 Integridad de archivo

Verificar:

- existe;
- tamaño > 0;
- abre sin corrupción;
- extensión coincide con formato;
- dimensiones válidas;
- relación de aspecto dentro de tolerancia;
- canal alfa cuando se requiere;
- perfil de color utilizable;
- resolución suficiente.

## 14.2 Verificación observable

Sin reauditar semántica conceptual, verificar que el resultado producido muestra de forma observable:

- todos los elementos obligatorios visibles;
- relaciones prescritas visibles;
- dirección de relaciones correcta;
- arquitectura visual reconocible;
- texto crítico legible;
- ausencia de elementos claramente prohibidos;
- ausencia de contenido obviamente añadido;
- Style Lock observable;
- mensaje central representable desde el archivo.

## 14.3 Distinción crítica

03.C-2C puede comprobar:

> “La flecha que el contrato exigía de A hacia B aparece de A hacia B.”

No puede decidir:

> “Tal vez la flecha debería ir de B hacia A.”

La primera es verificación de ejecución.

La segunda es rediseño semántico.

---

# 15. Resultados de verificación

Estados:

## `PRODUCCION_CUMPLE`

Todos los criterios técnicos y observables cumplen.

## `PRODUCCION_CUMPLE_CON_RESERVAS_TECNICAS`

Semántica observable preservada, pero existe defecto secundario no bloqueante:

- espaciado;
- balance;
- antialiasing;
- compresión;
- microalineación.

## `FALLO_DE_EJECUCION`

El contrato es producible, pero la salida concreta incumple:

- elemento faltante;
- relación visual incorrecta;
- texto ilegible;
- formato incorrecto;
- layout roto;
- clipping;
- contenido añadido por el motor.

## `CONFLICTO_DE_CONTRATO`

La producción revela una contradicción o imposibilidad que no puede resolverse sin cambiar el RGE.

## `BLOQUEADO_MOTOR`

No existe herramienta capaz de ejecutar el contrato autorizado.

---

# 16. Criterios críticos de producción

Falla crítica si:

1. falta un elemento obligatorio;
2. aparece un elemento prohibido;
3. una relación está invertida;
4. una relación obligatoria desaparece;
5. la arquitectura cambia;
6. el texto crítico es ilegible;
7. el archivo está corrupto;
8. el formato no es utilizable;
9. el Style Lock se viola de forma material;
10. el resultado altera el mensaje;
11. se añade contenido disciplinar;
12. el recurso no puede usarse en su destino previsto.

---

# 17. Criterios secundarios

No bloqueantes por sí solos:

- alineación menor;
- espaciado;
- balance;
- refinamiento;
- tamaño relativo no crítico;
- consistencia estética secundaria;
- compresión mejorable;
- pequeños defectos de iconografía sin cambio de significado.

---

# 18. Fase 6 — Reintento controlado

## 18.1 Máximo

```text
MAX_INTENTOS_PRODUCCION = 2
```

El primer intento cuenta como intento 1.

## 18.2 Se puede reintentar si

Resultado:

```text
FALLO_DE_EJECUCION
```

y el fallo puede corregirse sin cambiar el contrato.

## 18.3 Ajustes permitidos entre intentos

- reforzar instrucción técnica;
- repetir restricciones;
- hacer más explícita la arquitectura ya prescrita;
- ajustar parámetros del motor;
- cambiar semilla;
- cambiar nivel de detalle técnico;
- aumentar resolución;
- mejorar legibilidad;
- cambiar disposición interna dentro del layout permitido.

## 18.4 Ajustes prohibidos

No modificar:

- contenido;
- relaciones;
- whitelist;
- blacklist;
- función;
- mensaje;
- familia;
- procedencia;
- destino;
- contrato.

## 18.5 Después del máximo

Si no cumple:

```text
PRODUCCION_RECHAZADA
```

Registrar causa.

No seguir iterando.

---

# 19. Routing de fallos

## 19.1 FALLO_DE_EJECUCION

```text
03.C-2C
→ RETRY
```

## 19.2 BLOQUEADO_MOTOR

Si el contrato permite otro motor explícitamente autorizado:

```text
03.C-2C
→ motor alternativo permitido
```

Si no:

```text
RETURN → 03.C-2A
```

porque la ejecutabilidad del contrato debe revisarse.

Después:

```text
03.C-2A
→ RGE corregido
→ 03.C-2B desde cero
→ nuevo PASS
→ 03.C-2C
```

## 19.3 CONFLICTO_DE_CONTRATO

Ruta obligatoria:

```text
03.C-2C
→ 03.C-2A
→ 03.C-2B
→ PASS
→ 03.C-2C
```

## 19.4 Cambio que pertenece a 03.C-1

Si el problema exige cambiar:

- procedencia;
- función;
- destino;
- familia representacional;
- prioridad;
- criterio de satisfacción;

ruta:

```text
03.C-2C
→ CONFLICTO_DE_ESTRATEGIA_VISUAL
→ 03.C-1
```

---

# 20. Fase 7 — Guardado

## 20.1 Nombre canónico sugerido

```text
recurso_[sesion]_[ID_NVD]_[ID_RGE]_[slug].[ext]
```

Ejemplo:

```text
recurso_s03_NVD-04_RGE-04-01_ciclo-energia.png
```

## 20.2 Versiones

Si se reejecuta el mismo PASS por fallo técnico:

- conservar mismo ID_RGE;
- usar versión de producción:

```text
_v2
_v3
```

solo si el sistema de archivos requiere conservar históricos.

La versión final aprobada debe tener un alias o ruta canónica estable.

## 20.3 Hash del archivo

Calcular:

```text
HASH_SHA256_ARCHIVO
```

sobre bytes exactos del archivo final.

---

# 21. Registro de producción

Crear o actualizar:

```text
registro_produccion_generativa_sesion_N.md
```

## 21.1 Campos mínimos

| Campo | Valor |
|---|---|
| ID_NVD | |
| ID_RGE | |
| HUELLA_RGE_AUDITADO | |
| PASS_REF | |
| motor | |
| versión motor | |
| formato | |
| dimensiones | |
| archivo | |
| HASH_SHA256_ARCHIVO | |
| intento final | |
| estado | |
| fecha | |

## 21.2 Historial de intentos

Por intento:

| Intento | Archivo temporal | Resultado | Fallo | Acción |
|---|---|---|---|---|

---

# 22. Handoff downstream

El handoff de 03.C-2C debe ser explícito.

```text
ID_NVD
ID_RGE
HUELLA_RGE_AUDITADO
PASS_REF
ARCHIVO_GENERADO
HASH_SHA256_ARCHIVO
FORMATO
DIMENSIONES
MOTOR
VERSION_MOTOR
INTENTOS
ESTADO = RECURSO_GENERATIVO_RESUELTO
```

Opcionalmente:

```text
TITULO_TECNICO_INTERNO
NOTA_TECNICA
```

## 22.1 Prohibición

El handoff no debe incluir un nuevo contrato semántico.

El contrato sigue siendo el RGE auditado.

---

# 23. Título y pie de figura

A diferencia de la antigua 03Cbis, 03.C-2C **no tiene autoridad editorial principal** para crear el pie final del alumno.

## 23.1 Puede producir

Un descriptor técnico interno:

```text
DESCRIPTOR_RECURSO
```

Ejemplo:

```text
Comparativa esquemática de flujo energético entre sistema A y sistema B.
```

## 23.2 No debe producir

El pie editorial definitivo si requiere:

- contextualización didáctica;
- relación con el texto;
- numeración final;
- formulación para alumno;
- atribución editorial.

Eso corresponde a 03.D / 03.E.

## 23.3 Excepción

Si 03.C-2A ya incluyó texto de pie literal como parte del contrato, 03.C-2C lo preserva literalmente.

---

# 24. Recursos con texto

## 24.1 Texto crítico

Debe verificarse carácter por carácter cuando sea posible.

Ejemplos:

- etiquetas;
- títulos internos;
- variables;
- unidades;
- leyendas.

## 24.2 Texto ilegible

Resultado:

```text
FALLO_DE_EJECUCION
```

## 24.3 Texto inventado

Si aparece texto no autorizado:

```text
FALLO_DE_EJECUCION
```

No corregir inventando una nueva formulación semántica.

---

# 25. Recursos sin texto

Para recursos puramente visuales:

- no añadir etiquetas por comodidad;
- no añadir leyenda si no fue prescrita;
- no convertir una escena en infografía;
- no introducir señalética decorativa.

---

# 26. Diagramas

Verificar:

1. nodos obligatorios;
2. relaciones;
3. dirección;
4. unicidad visual;
5. jerarquía;
6. leyenda cuando fue prescrita;
7. ausencia de conectores extra;
8. legibilidad;
9. arquitectura.

---

# 27. Infografías

Verificar:

- bloques prescritos;
- secuencia;
- proporción;
- iconografía;
- texto;
- jerarquía;
- densidad;
- ausencia de narrativa añadida.

---

# 28. Comparativas

Verificar:

- entidades comparadas correctas;
- simetría si fue prescrita;
- mismas variables;
- no introducir una tercera categoría;
- señalización de diferencias según contrato.

---

# 29. Escenas sintéticas

Verificar:

- elementos visibles;
- relaciones espaciales;
- ausencia de objetos no autorizados;
- estilo;
- orientación;
- realismo o abstracción según contrato;
- ausencia de texto espurio.

---

# 30. Mapas conceptuales

Verificar:

- conceptos exactos;
- relaciones exactas;
- direcciones;
- niveles;
- no añadir nodos;
- no fusionar conceptos distintos.

---

# 31. Transparencia y fondos

Si el contrato prescribe:

```text
FONDO_TRANSPARENTE
```

verificar alfa real.

Si prescribe:

```text
FONDO_SOLIDO
```

no convertir a transparente.

---

# 32. Color

Si el color tiene significado semántico:

- debe respetarse según contrato;
- no reasignar categorías;
- no depender exclusivamente del color si el contrato exige redundancia.

Si el color es solo estilístico:

03.C-2C puede hacer ajustes mínimos dentro del Style Lock.

---

# 33. Herramientas

03.C-2C puede operar con:

- generadores de imagen;
- motores SVG;
- renderizadores;
- herramientas de diagramación;
- scripts;
- motores vectoriales;
- combinaciones autorizadas.

## 33.1 Regla

La herramienta es un medio.

No tiene autoridad contractual.

---

# 34. Política de fallback

Solo puede cambiarse de motor si:

1. el contrato lo permite;
2. el formato se preserva;
3. la semántica se preserva;
4. no se pierde editabilidad requerida;
5. se registra el cambio.

Si requiere alterar el contrato:

```text
RETURN → 03.C-2A
```

---

# 35. Estado terminal

## Éxito

```text
RECURSO_GENERATIVO_RESUELTO
```

## Fallos terminales

```text
CONTRATO_DISTINTO_DEL_AUDITADO
BLOQUEADO_ENTRADA_INCOMPLETA
BLOQUEADO_MOTOR_INADECUADO
BLOQUEADO_FORMATO_INCOMPATIBLE
CONFLICTO_DE_CONTRATO
CONFLICTO_DE_ESTRATEGIA_VISUAL
PRODUCCION_RECHAZADA
```

---

# 36. Integración con 03.D

03.D puede consumir únicamente:

```text
ESTADO = RECURSO_GENERATIVO_RESUELTO
```

03.D puede decidir:

- ubicación;
- tamaño;
- secuencia didáctica;
- explotación pedagógica.

No puede modificar:

- archivo semánticamente;
- RGE;
- PASS;
- ID_RGE;
- huella;
- relaciones visuales.

---

# 37. Integración con 03.E

03.E puede consumir únicamente recursos cuyo destino incluya:

```text
Capítulo
```

y cuyo estado sea:

```text
RECURSO_GENERATIVO_RESUELTO
```

03.E puede crear:

- numeración de figura;
- pie editorial;
- referencia en prosa;
- contextualización.

No puede cambiar la semántica visual.

---

# 38. Integración con HÍBRIDO

03.C-2C resuelve únicamente el componente generativo.

03.C-3 resuelve el externo.

La NVD híbrida no se considera cerrada hasta que:

```text
EXTERNO = RECURSO_EXTERNO_RESUELTO
GENERATIVO = RECURSO_GENERATIVO_RESUELTO
```

y se preserva la relación definida por 03.C-1.

---

# 39. Integración con 04.A

04.A no vuelve a ejecutar 03.C-2C.

Puede verificar:

- que 03.D/03.E usó el archivo exacto;
- que `HASH_SHA256_ARCHIVO` coincide;
- que el destino era autorizado;
- que no hubo sustitución;
- que la integración no alteró semántica.

---

# 40. Integración con 04.B

04.B puede:

- restaurar el archivo exacto producido por 03.C-2C;
- corregir referencia rota;
- corregir ubicación;
- restaurar pie/atribución cuando corresponda downstream.

04.B no puede:

- regenerar libremente;
- modificar el archivo semánticamente;
- modificar RGE;
- reemplazar el recurso.

Si la producción debe repetirse:

```text
04.B
→ REGENERAR_03C2C
```

con el mismo PASS exacto cuando el contrato no cambia.

---

# 41. Integración con orquestador autónomo

El orquestador debe tratar:

```text
03.C-2B PASS
```

como prerequisito obligatorio de 03.C-2C.

## 41.1 Reutilización

Reutilizar un recurso existente si:

```text
ID_RGE coincide
HUELLA_RGE_AUDITADO coincide
HASH_SHA256_ARCHIVO coincide
archivo existe
estado = RECURSO_GENERATIVO_RESUELTO
```

## 41.2 Invalidación

Si cambia el RGE:

```text
invalidar PASS
invalidar 03.C-2C
invalidar downstream
```

Si cambia solo el archivo por corrupción:

```text
repetir 03.C-2C con mismo PASS
```

---

# 42. Automatización sin aprobación humana

03.C-2C no requiere aprobación humana para cerrar.

La antigua lógica de:

```text
Aprobado preliminar
→ aprobación usuario
→ Aprobado
```

se sustituye por:

```text
PASS contractual
+
verificación de producción
=
RECURSO_GENERATIVO_RESUELTO
```

La intervención humana puede existir como revisión opcional, pero no es requisito operativo.

---

# 43. Política de reintento autónomo

## Intento 1

Generación normal.

## Intento 2

Solo si intento 1 = `FALLO_DE_EJECUCION`.

Se permite reforzar instrucción técnica sin modificar contrato.

## Después

Si falla:

```text
PRODUCCION_RECHAZADA
```

No hacer intento 3 automáticamente en v0.1.

---

# 44. Evidencia mínima de cierre

Para declarar `RECURSO_GENERATIVO_RESUELTO` deben existir:

1. RGE;
2. PASS;
3. huella;
4. archivo final;
5. hash del archivo;
6. registro de producción;
7. verificación técnica;
8. correspondencia observable;
9. estado final.

---

# 45. Formato de reporte por recurso

```markdown
# Ejecución generativa — [ID_RGE]

## Identidad
- ID_NVD:
- ID_RGE:
- HUELLA_RGE_AUDITADO:
- PASS_REF:

## Producción
- Motor:
- Versión:
- Formato:
- Dimensiones:
- Intentos:

## Archivo
- Ruta:
- SHA-256:

## Verificación
| Criterio | Estado | Evidencia |
|---|---|---|
| Archivo íntegro | PASS | |
| Formato | PASS | |
| Dimensiones | PASS | |
| Elementos observables | PASS | |
| Relaciones observables | PASS | |
| Texto crítico | PASS / N/A | |
| Blacklist observable | PASS | |
| Arquitectura | PASS | |
| Style Lock | PASS | |

## Resultado
RECURSO_GENERATIVO_RESUELTO
```

---

# 46. Checklist preproducción

## Identidad

- [ ] ID_NVD presente.
- [ ] ID_RGE presente.
- [ ] PASS presente.
- [ ] HUELLA_RGE_AUDITADO presente.
- [ ] Hash del contrato coincide.
- [ ] No hubo cambio post-PASS.

## Producción

- [ ] Motor disponible.
- [ ] Formato compatible.
- [ ] Dimensiones compatibles.
- [ ] Editabilidad viable si aplica.
- [ ] Texto crítico viable.
- [ ] Ruta de salida disponible.

## Contrato

- [ ] Arquitectura disponible.
- [ ] Whitelist disponible.
- [ ] Blacklist disponible.
- [ ] Relaciones disponibles.
- [ ] Style Lock disponible cuando aplica.

---

# 47. Checklist postproducción

- [ ] Archivo existe.
- [ ] Archivo abre.
- [ ] Formato correcto.
- [ ] Dimensiones correctas.
- [ ] Elementos obligatorios visibles.
- [ ] Relaciones visibles.
- [ ] Dirección correcta.
- [ ] No aparecen elementos prohibidos.
- [ ] Texto crítico legible.
- [ ] Arquitectura preservada.
- [ ] Style Lock preservado.
- [ ] Hash calculado.
- [ ] Registro creado.
- [ ] Estado final correcto.

---

# 48. Reglas duras

1. No producir sin PASS.
2. No producir si el hash no coincide.
3. No editar RGE.
4. No sustituir contenido.
5. No reinterpretar relaciones.
6. No inventar.
7. No cambiar procedencia.
8. No cambiar destino.
9. No cambiar familia.
10. No cambiar función.
11. No cambiar criterio de satisfacción.
12. No cambiar whitelist.
13. No cambiar blacklist.
14. No declarar PASS.
15. No reauditar semántica.
16. No superar 2 intentos automáticos.
17. No ocultar fallo técnico.
18. No promover temporal a final si falla criterio crítico.
19. No sobrescribir silenciosamente históricos.
20. No entregar downstream un recurso distinto del contrato auditado.

---

# 49. Diferencia con 03.C-2A

03.C-2A:

```text
DISEÑA
```

03.C-2C:

```text
EJECUTA
```

2A puede cambiar el contrato antes de auditoría.

2C nunca cambia el contrato.

---

# 50. Diferencia con 03.C-2B

03.C-2B:

```text
AUDITA EL CONTRATO
```

03.C-2C:

```text
VERIFICA LA EJECUCIÓN
```

2B decide si el contrato es semánticamente válido.

2C verifica si el motor ejecutó ese contrato.

---

# 51. Diferencia con antigua 03Cbis

03.C-2C **no es una renombrada 03Cbis**.

La antigua skill mezclaba:

- preflight semántico;
- ejecución;
- auditoría posterior;
- aprobación humana;
- título/pie;
- actualización de estado.

03.C-2C conserva solo:

- preflight técnico;
- compilación para motor;
- ejecución;
- verificación técnica/observable;
- reintento;
- guardado;
- registro;
- handoff.

El diseño y auditoría se mantienen fuera.

---

# 52. Estados y routing resumido

```text
03.C-2B PASS
      │
      ▼
03.C-2C Gate identidad
      │
   ┌──┴──┐
   │     │
 PASS   BLOCK
   │
   ▼
Preflight técnico
   │
 ┌─┴───────────────┐
 │                 │
PASS              BLOCK
 │                 │
 ▼                 ├─ motor → 2A si contrato no producible
Producción         └─ estrategia → C1 si problema estratégico
 │
 ▼
Verificación
 │
 ├─ CUMPLE → RECURSO_GENERATIVO_RESUELTO
 │
 ├─ FALLO_EJECUCION → retry (máx. 2)
 │
 └─ CONFLICTO_CONTRATO → 2A → 2B → 2C
```

---

# 53. Contrato de salida

Salida exitosa:

```yaml
ID_NVD: ...
ID_RGE: ...
HUELLA_RGE_AUDITADO: ...
PASS_REF: ...
ARCHIVO_GENERADO: ...
HASH_SHA256_ARCHIVO: ...
FORMATO: ...
DIMENSIONES: ...
MOTOR: ...
VERSION_MOTOR: ...
INTENTOS: 1|2
VERIFICACION_TECNICA: PASS
VERIFICACION_OBSERVABLE: PASS
ESTADO: RECURSO_GENERATIVO_RESUELTO
```

---

# 54. Criterio final de calidad

03.C-2C cumple cuando:

- ejecuta solo contratos con PASS;
- confirma identidad exacta;
- no modifica semántica;
- produce un archivo usable;
- detecta fallos técnicos;
- reintenta solo dentro de límites;
- escala problemas contractuales;
- registra la producción;
- emite hash del archivo;
- entrega un handoff suficiente para 03.D/03.E;
- no duplica 03.C-2A ni 03.C-2B.

---

# 55. Estado de versión

**v0.1 — BORRADOR PARA PRUEBA REAL**

Esta versión debe probarse con al menos:

1. un diagrama;
2. una infografía;
3. una comparativa;
4. una escena sintética;
5. una NVD híbrida.

Objetivos de la prueba:

- validar el gate de hash;
- comprobar que no reaudita semántica;
- verificar routing de fallos;
- confirmar que 2 intentos son suficientes;
- validar handoff hacia 03.D/03.E;
- confirmar que el orquestador autónomo puede reutilizar outputs por hash.

---

# 56. Changelog v0.1

Primera versión del ejecutor generativo separado.

Origen arquitectónico:

```text
03.C-1 = estrategia
03.C-2A = diseño
03.C-2B = auditoría
03.C-2C = ejecución
03.C-3 = externos
```

La skill recupera únicamente las funciones de producción material que no quedaron absorbidas por el nuevo subsistema 03.C:

- ejecución del motor;
- microdecisiones técnicas;
- validación del archivo;
- iteración controlada;
- guardado;
- registro;
- handoff.

No recupera las responsabilidades semánticas, de diseño o aprobación humana de la antigua 03Cbis.
