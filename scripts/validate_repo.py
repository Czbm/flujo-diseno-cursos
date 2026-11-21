#!/usr/bin/env python3
"""Validador ligero del repositorio Flujo de Diseno de Cursos.

Usa solo la biblioteca estandar de Python para poder ejecutarse en cualquier
entorno local o en GitHub Actions sin instalar dependencias externas.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

LOCAL_PATH_PATTERN = re.compile(r"(?:[A-Za-z]:\\(?:Users|Mi unidad|00_PROYECTOS)|/Users/[A-Za-z0-9_.-]+/)")
REQUIRED_FRONTMATTER_KEYS = ("name", "description", "stage_id", "version", "status")


def parse_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return None
    lines = text.splitlines()
    end_idx = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_idx = idx
            break
    if end_idx is None:
        return None

    data: dict[str, str] = {}
    for line in lines[1:end_idx]:
        if ":" in line:
            key, val = line.split(":", 1)
            data[key.strip()] = val.strip().strip('"').strip("'")
    return data


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    # 1. Validar plugin.json
    plugin_path = ROOT / "plugin.json"
    if not plugin_path.exists():
        errors.append("Falta plugin.json en la raiz del repositorio.")
    else:
        try:
            plugin = json.loads(plugin_path.read_text(encoding="utf-8"))
            for field in ("name", "description"):
                if not plugin.get(field):
                    errors.append(f"plugin.json: falta el campo obligatorio '{field}'.")
        except json.JSONDecodeError as exc:
            errors.append(f"plugin.json invalido: {exc}")

    # 2. Validar manifest.yaml (existencia de todas las rutas declaradas)
    manifest_path = ROOT / "manifest.yaml"
    declared_paths: set[str] = set()
    if not manifest_path.exists():
        errors.append("Falta manifest.yaml en la raiz del repositorio.")
    else:
        for line in manifest_path.read_text(encoding="utf-8").splitlines():
            match = re.match(r"^\s*path:\s*['\"]?([^'\"]+)['\"]?\s*$", line)
            if match:
                rel = match.group(1).strip()
                declared_paths.add(rel)
                if not (ROOT / rel).exists():
                    errors.append(f"manifest.yaml apunta a una ruta inexistente: {rel}")

    # 3. Validar cada SKILL.md y agents/*.md
    skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
    agent_files = sorted((ROOT / "agents").glob("*.md"))

    if not skill_files:
        errors.append("No se encontraron skills en skills/*/SKILL.md.")

    for md_file in [*skill_files, *agent_files]:
        rel = md_file.relative_to(ROOT).as_posix()
        text = md_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{rel}: falta frontmatter YAML valido.")
        else:
            for key in REQUIRED_FRONTMATTER_KEYS:
                if not fm.get(key):
                    errors.append(f"{rel}: falta la clave '{key}' en frontmatter.")
            if md_file.name == "SKILL.md" and fm.get("name") != md_file.parent.name:
                errors.append(
                    f"{rel}: frontmatter name '{fm.get('name')}' no coincide con la carpeta '{md_file.parent.name}'."
                )

        if rel not in declared_paths:
            errors.append(f"{rel}: no esta registrado en manifest.yaml.")

    # 4. Detectar rutas locales absolutas accidentales en archivos Markdown
    for md_file in ROOT.rglob("*.md"):
        if ".git" in md_file.parts:
            continue
        rel = md_file.relative_to(ROOT).as_posix()
        if rel in ("CONTRIBUTING.md",):
            continue
        text = md_file.read_text(encoding="utf-8")
        if LOCAL_PATH_PATTERN.search(text):
            warnings.append(f"{rel}: contiene posibles rutas locales absolutas (revisar antes de publicar).")

    print(f"Skills validadas: {len(skill_files)} | Agentes validados: {len(agent_files)}")
    for w in warnings:
        print(f"[WARN] {w}")
    for e in errors:
        print(f"[ERROR] {e}")

    if errors:
        print(f"\nValidacion fallida con {len(errors)} error(es).")
        return 1

    print("\nValidacion exitosa: estructura, frontmatter y manifest sincronizados.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
