# Changelog

Todos los cambios relevantes del ecosistema se documentan en este archivo.

## [4.2.1] - 2026-11-21

### Añadido
- Nueva skill **`00.P` (`skills/00p-extractor-perfil-estilo/SKILL.md`, v1.0)** para extraer, calibrar o consolidar el perfil semántico y de estilo editorial del docente (Modo Corpus, Modo Entrevista guiada y Modo Consolidación), registrada en `manifest.yaml` y `README.md`.

### Modificado
- Actualizado el esquema de licenciamiento a **licencia dual**: **CC BY-SA 4.0** para skills, agentes, metodología y documentación (`LICENSE-CC-BY-SA-4.0`) + **Apache 2.0** para código y scripts (`LICENSE-APACHE`), con aclaración explícita en `LICENSE` sobre la propiedad de los cursos generados por usuarios.

## [4.2.0] - 2026-11-21

### Migración inicial a estructura Open Source + Plugin
- Estructuradas las 15 skills vigentes bajo el estándar `skills/<slug>/SKILL.md` con frontmatter YAML (`name`, `description`, `stage_id`, `version`, `status`).
- Promovido `00` Orquestador Autónomo (`v1.1`) a agente coordinador en `agents/orquestador-curso.md`.
- Desacoplado el perfil de estilo docente a `profiles/` (incluyendo `profiles/template-perfil-estilo.md` y `profiles/crc-referencia.md`).
- Añadidos `plugin.json`, `manifest.yaml`, `AGENTS.md`, `rules/AGENTS.md`, `CONTRIBUTING.md`, `scripts/validate_repo.py` y flujo CI de GitHub Actions.
- Eliminados sufijos de versión en nombres de archivo y archivos legados fuera del repositorio principal.
