# Guía para contribuir

Gracias por tu interés en mejorar el **Flujo de Diseño de Cursos**. Como este ecosistema se basa en **contratos explícitos entre etapas**, seguir estas reglas nos ayuda a evolucionar sin romper compatibilidad downstream.

## 1. Regla de oro: protección de contratos

Cada skill (`01` a `05`) tiene un contrato de entrada y salida definido en su `SKILL.md` y mapeado en `manifest.yaml`.

- **Cambio menor (patch/minor):** mejora redacción, ejemplos, precisión o casos borde sin alterar campos obligatorios de salida.
- **Cambio de contrato (*breaking*):** agrega, renombra o elimina secciones/campos obligatorios que consumen etapas posteriores (`depends_on` en `manifest.yaml`).
  - Debe declararse explícitamente en el Pull Request.
  - Debe actualizar la versión en el frontmatter de la skill, en `manifest.yaml` y registrar la nota en `CHANGELOG.md`.
  - Si impacta a una skill downstream, indica qué etapa requiere actualización o inclúyela en el mismo PR.

## 2. Convenciones de archivos

- No incluyas sufijos de versión (`_v1.2`) en nombres de archivo; el versionado vive en el frontmatter YAML (`version:`), en `manifest.yaml` y en Git tags.
- No subas rutas locales absolutas (`C:\...`, `L:\...`, `/Users/...`) ni datos privados de alumnos o instituciones.
- Mantén el núcleo de las skills (`skills/`) agnóstico a una sola institución o estilo docente. Los estilos particulares van en `profiles/`.

## 3. Cómo enviar un Pull Request

1. Haz fork y crea una rama descriptiva:
   - `feat/03c-2c-cierre-contrato`
   - `fix/04a-regla-trazabilidad`
   - `docs/golden-example-sesion`
2. Realiza tus cambios y ejecuta la validación local:
   ```bash
   python scripts/validate_repo.py
   ```
3. Abre el Pull Request completando la plantilla y describe cómo probaste el cambio.

## 4. Áreas prioritarias (`help wanted`)

- Pruebas reales y cierre de contrato para `03.C-2C` (Ejecutor Generativo) y `03.C-3` (External Resources).
- Especificación e implementación de la etapa `06` (Exportador a PDF/DOCX/PPTX).
- Factorización de plantillas extensas hacia subcarpetas `references/` dentro de las skills más grandes (`03.D`, `03.E`, `04.A`).
- Creación de un *Golden Example* completo en `examples/`.
