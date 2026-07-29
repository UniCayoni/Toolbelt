from pathlib import Path
import json

gm = Path(r"d:\GreyMatter\.cursor")
files = [
    "skills/codebase-recon/SKILL.md",
    "skills/docs-research/SKILL.md",
    "skills/research-protocol/SKILL.md",
    "skills/author-agents-md/SKILL.md",
    "skills/draft-adr/SKILL.md",
    "rules/research-protocol-grades.mdc",
    "rules/draft-is-not-sot.mdc",
    "rules/research-before-write.mdc",
    "rules/research-skill-coexistence.mdc",
]
for f in files:
    p = gm / f
    print("OK" if p.exists() else "MISS", f, p.stat().st_size if p.exists() else 0)

# Patch markers in skills
for skill, needle in [
    ("codebase-recon", "Using `codebase-recon`"),
    ("codebase-recon", "either is OK"),
    ("docs-research", "in_use"),
    ("docs-research", "only when an OpenAPI"),
    ("research-protocol", "short smokes may keep grades"),
]:
    text = (gm / "skills" / skill / "SKILL.md").read_text(encoding="utf-8")
    print("PATCH", skill, needle, needle in text)

rbw = (gm / "rules" / "research-before-write.mdc").read_text(encoding="utf-8")
print("PATCH rbw implementation", "implementation" in rbw)
print("PATCH rbw docs/research allowed", "docs/research" in rbw)

sp = Path(r"C:\Users\Jonyc\.cursor\plugins\cache\cursor-public\superpowers\d884ae04edebef577e82ff7c4e143debd0bbec99")
pj = json.loads((sp / ".cursor-plugin" / "plugin.json").read_text(encoding="utf-8"))
print("local_version", pj["version"])
print("evals_local", (sp / "evals").exists())
print("v2_notes", (Path(r"d:\GreyMatter\docs\research\notes\smoke") / "v2-recon-superpowers.md").exists(),
      (Path(r"d:\GreyMatter\docs\research\notes\smoke") / "v2-docs-cursor.md").exists())
