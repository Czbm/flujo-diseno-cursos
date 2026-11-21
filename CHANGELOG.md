# Changelog

Todos los cambios relevantes del ecosistema se documentan en este archivo.

## [4.2.0] - 2026-11-21

### Migración inicial a estructura Open Source + Plugin
- Estructuradas las 15 skills vigentes bajo el estándar `skills/<slug>/SKILL.md` con frontmatter YAML (`name`, `description`, `stage_id`, `version`, `status`).
- Promovido `00` Orquestador Autónomo (`v1.1`) a agente coordinador en `agents/orquestador-curso.md`.
- Desacoplado el perfil de estilo docente a `profiles/` (incluyendo `profiles/template-perfil-estilo.md` y `profiles/crc-referencia.md`).
- Añadidos `plugin.json`, `manifest.yaml`, `AGENTS.md`, `rules/AGENTS.md`, `CONTRIBUTING.md`, `scripts/validate_repo.py` y flujo CI de GitHub Actions.
- Eliminados sufijos de versión en nombres de archivo y archivos legados fuera del repositorio principal.
