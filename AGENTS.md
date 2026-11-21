# AGENTS.md — Instrucciones para agentes de IA

Este repositorio contiene el ecosistema **Flujo de Diseño de Cursos**: un conjunto modular de skills contractuales (`skills/*/SKILL.md`) y un agente orquestador (`agents/orquestador-curso.md`).

## Reglas de operación

1. **Fuente de verdad de versiones y dependencias:** consulta siempre `manifest.yaml` y `docs/guia-uso-flujo.md` antes de ejecutar o modificar etapas.
2. **Autoridad contractual:** cada skill es propietaria exclusiva de su contrato de salida. No modifiques silenciosamente el formato de salida de una skill sin verificar a sus consumidores downstream (`depends_on` en `manifest.yaml`).
3. **Aislamiento de auditoría:** cuando ejecutes `04.A` (`skills/04a-auditoria-coherencia/SKILL.md`), hazlo preferentemente en un subagente o contexto limpio distinto al que redactó `03.D` o `03.E` para evitar sesgo de confirmación.
4. **Perfil de estilo desacoplado:** utiliza el perfil de estilo que indique el usuario (o `profiles/template-perfil-estilo.md` como base). No asumas un perfil docente específico salvo que el usuario lo solicite.
5. **Validación antes de commit:** ejecuta `python scripts/validate_repo.py` para comprobar que el frontmatter, `manifest.yaml` y las rutas estén sanos.
