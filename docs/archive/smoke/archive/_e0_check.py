from pathlib import Path

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
]
for f in files:
    p = gm / f
    print("OK" if p.exists() else "MISS", f, p.stat().st_size if p.exists() else 0)

for d in sorted((gm / "skills").iterdir()):
    if not d.is_dir():
        continue
    text = (d / "SKILL.md").read_text(encoding="utf-8")
    name = next((ln.split(":", 1)[1].strip() for ln in text.splitlines() if ln.startswith("name:")), "?")
    dmi = "disable-model-invocation: true" in text
    print(f"folder={d.name} name={name} match={d.name == name} dmi={dmi}")

sp = Path(r"C:\Users\Jonyc\.cursor\plugins\cache\cursor-public\superpowers\d884ae04edebef577e82ff7c4e143debd0bbec99")
skills = [x.name for x in (sp / "skills").iterdir() if x.is_dir()]
print("sp_skill_count", len(skills))
print("sp_skills", ",".join(sorted(skills)))
import json
pj = json.loads((sp / ".cursor-plugin" / "plugin.json").read_text(encoding="utf-8"))
print("local_version", pj["version"])
print("evals_local", (sp / "evals").exists())
print("package_scripts", json.loads((sp / "package.json").read_text(encoding="utf-8")).get("scripts"))
