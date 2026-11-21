# Reglas del ecosistema Flujo de Diseño de Cursos

- Respeta siempre la propiedad contractual entre etapas (`01` → `02` → `03.A/B/C` → `03.D/E` → `04.A` → `04.B` → `05`), según `manifest.yaml`.
- Nunca regeneres artefactos vigentes sin detectar primero qué insumos cambiaron (principio idempotente de `agents/orquestador-curso.md`).
- Para auditorías (`04.A`), prioriza ejecutar en un subagente limpio para mantener objetividad.
- Aplica el perfil de estilo que el usuario seleccione en `profiles/` (o una voz académica neutra si no especifica ninguno).
