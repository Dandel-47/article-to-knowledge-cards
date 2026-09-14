#!/usr/bin/env python3
"""Quick validation for the make-knowledge-cards skill structure."""

import sys
import os
import re
import json

SKILL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "skills", "make-knowledge-cards")

def check_file(path, label):
    if not os.path.isfile(path):
        return False, f"[FAIL] {label}: file not found -> {path}"
    return True, f"[OK]   {label}: {path}"

def validate_skill_md(path):
    errors = []
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check frontmatter
    fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        errors.append("SKILL.md: missing frontmatter block (--- ... ---)")
        return errors

    fm = fm_match.group(1)

    # Check name field
    name_match = re.search(r'^name:\s*"?(.+?)"?\s*$', fm, re.MULTILINE)
    if not name_match:
        errors.append('SKILL.md: missing "name" field in frontmatter')
    elif name_match.group(1).strip().strip('"') != "make-knowledge-cards":
        errors.append(f'SKILL.md: name should be "make-knowledge-cards", got "{name_match.group(1)}"')

    # Check description field
    desc_match = re.search(r'^description:\s*"?(.+?)"?\s*$', fm, re.MULTILINE)
    if not desc_match:
        errors.append('SKILL.md: missing "description" field in frontmatter')
    else:
        desc = desc_match.group(1).strip().strip('"')
        if len(desc) > 200:
            errors.append(f"SKILL.md: description too long ({len(desc)} chars, max 200)")

    # Check key content sections
    body = content[fm_match.end():]
    required_sections = ["Card Format", "Knowledge Point Selection Rules"]
    for section in required_sections:
        if section not in body:
            errors.append(f"SKILL.md: missing section \"{section}\"")

    return errors

def validate_openai_yaml(path):
    errors = []
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check for interface block
    if "interface:" not in content:
        errors.append("openai.yaml: missing 'interface:' block")
        return errors

    # Check required fields
    required_fields = ["display_name", "short_description", "default_prompt"]
    for field in required_fields:
        if field not in content:
            errors.append(f"openai.yaml: missing field '{field}'")

    # Check default_prompt references the skill name
    if "make-knowledge-cards" not in content:
        errors.append("openai.yaml: default_prompt should reference '$make-knowledge-cards'")

    return errors

def main():
    print("=" * 60)
    print("  make-knowledge-cards - Quick Validation")
    print("=" * 60)
    print()

    all_errors = []
    passed = 0
    failed = 0

    # 1. Check directory exists
    if not os.path.isdir(SKILL_DIR):
        print(f"[FAIL] Skill directory not found: {SKILL_DIR}")
        print("\nValidation FAILED.")
        sys.exit(1)
    print(f"[OK]   Skill directory: {SKILL_DIR}")
    passed += 1

    # 2. Check SKILL.md
    skill_md = os.path.join(SKILL_DIR, "SKILL.md")
    ok, msg = check_file(skill_md, "SKILL.md")
    print(msg)
    if ok:
        passed += 1
        errors = validate_skill_md(skill_md)
        if errors:
            for e in errors:
                print(f"       {e}")
            failed += len(errors)
        else:
            print("       [OK]   Frontmatter valid (name + description)")
            print("       [OK]   Required sections present")
    else:
        failed += 1

    # 3. Check agents/openai.yaml
    yaml_path = os.path.join(SKILL_DIR, "agents", "openai.yaml")
    ok, msg = check_file(yaml_path, "agents/openai.yaml")
    print(msg)
    if ok:
        passed += 1
        errors = validate_openai_yaml(yaml_path)
        if errors:
            for e in errors:
                print(f"       {e}")
            failed += len(errors)
        else:
            print("       [OK]   Interface block valid")
            print("       [OK]   Required fields present (display_name, short_description, default_prompt)")
    else:
        failed += 1

    # 4. Check no extra scripts in skill directory
    extra_files = []
    for root, dirs, files in os.walk(SKILL_DIR):
        for fname in files:
            if fname not in ("SKILL.md", "openai.yaml"):
                extra_files.append(os.path.join(root, fname))

    if extra_files:
        print(f"[WARN] Extra files found in skill directory (review if needed):")
        for ef in extra_files:
            print(f"       {ef}")
    else:
        print("[OK]   No unnecessary files in skill directory")
        passed += 1

    # Summary
    print()
    print("-" * 60)
    if failed == 0:
        print(f"  Result: PASSED  ({passed} checks passed, 0 failures)")
        print("-" * 60)
        sys.exit(0)
    else:
        print(f"  Result: FAILED  ({passed} checks passed, {failed} failures)")
        print("-" * 60)
        sys.exit(1)

if __name__ == "__main__":
    main()
