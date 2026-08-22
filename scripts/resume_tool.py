#!/usr/bin/env python3
"""
Single Source of Truth (SSOT) Resume, Portfolio, and Platform Exporter Engine.
Manages structured YAML records in `data/` and generates:
1. Markdown documents for MkDocs web portfolio (with interactive traceability matrix)
2. WeasyPrint print-ready PDFs (2-page concise and Master CV)
3. Platform-specific copy-ready export blocks (LinkedIn, Indeed, Plaintext ATS, JSON Resume)
4. CLI Skill & Traceability queries
"""

import os
import sys
import re
import argparse
import yaml
import markdown
import weasyprint

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")
DOCS_DIR = os.path.join(BASE_DIR, "docs")
SECTIONS_DIR = os.path.join(DOCS_DIR, "sections")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

def load_yaml(filename):
    filepath = os.path.join(DATA_DIR, filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Data file not found: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

class ResumeDatabase:
    def __init__(self):
        self.profile = load_yaml("profile.yaml")
        self.skills_data = load_yaml("skills.yaml")
        self.experience = load_yaml("experience.yaml")
        self.lab_and_community = load_yaml("lab_and_community.yaml")
        self.education = load_yaml("education.yaml")
        self.skill_map = self._build_skill_map()

    def _build_skill_map(self):
        mapping = {}
        for cat in self.skills_data.get("categories", []):
            cat_name = cat.get("name")
            cat_id = cat.get("id")
            for sk in cat.get("skills", []):
                sk_id = sk.get("id")
                mapping[sk_id] = {
                    "id": sk_id,
                    "name": sk.get("name"),
                    "short_name": sk.get("short_name", sk.get("name")),
                    "description": sk.get("description", ""),
                    "category_id": cat_id,
                    "category_name": cat_name,
                }
        return mapping

    def query_skill(self, query):
        query = query.lower()
        matched_skills = [
            sk for sk_id, sk in self.skill_map.items()
            if query in sk_id.lower() or query in sk["name"].lower() or query in sk["description"].lower()
        ]

        if not matched_skills:
            print(f"No skills found matching '{query}'.")
            return

        for sk in matched_skills:
            print("=" * 80)
            print(f"Skill: {sk['name']} [{sk['id']}]")
            print(f"Category: {sk['category_name']}")
            print(f"Description: {sk['description']}")
            print("-" * 80)
            print("Evidence in Professional Experience:")
            found_exp = False
            for exp in self.experience:
                role_match = sk["id"] in exp.get("skills", [])
                matching_bullets = [
                    b for b in exp.get("bullets", [])
                    if sk["id"] in b.get("skills", [])
                ]
                if role_match or matching_bullets:
                    found_exp = True
                    print(f"\n  • {exp['company']} | {exp['role']} ({exp['dates_display']})")
                    for b in matching_bullets:
                        b_text = b.get("long_text") or b.get("short_text") or ""
                        # Strip markdown asterisks for clean terminal output
                        clean_text = re.sub(r'\*\*(.*?)\*\*', r'\1', b_text)
                        print(f"    - [{b.get('title')}]: {clean_text}")

            if not found_exp:
                print("  (No direct role bullets explicitly tagged; verified in foundational skillset)")

            print("\nEvidence in Innovation Lab / Community R&D:")
            found_lab = False
            for item in self.lab_and_community:
                matching_projects = [
                    p for p in item.get("projects", [])
                    if sk["id"] in p.get("skills", []) or sk["id"] in item.get("skills", [])
                ]
                if matching_projects or sk["id"] in item.get("skills", []):
                    found_lab = True
                    print(f"\n  • {item['title']} ({item['dates_display']})")
                    for p in matching_projects:
                        clean_p = re.sub(r'\*\*(.*?)\*\*', r'\1', p.get('description', ''))
                        print(f"    - [{p.get('title')}]: {clean_p}")

            if not found_lab:
                print("  (None)")
            print("=" * 80 + "\n")

    def build_traceability_matrix_markdown(self):
        """Generates an interactive markdown/HTML skill matrix table for the web portfolio."""
        lines = []
        lines.append("## Competency & Evidence Matrix\n")
        lines.append("> [!NOTE]\n> Every technical competency is anchored directly to verified production deployments, infrastructure operations, and research milestones.\n\n")

        for cat in self.skills_data.get("categories", []):
            lines.append(f"### **{cat['name']}**\n")
            lines.append("| Core Competency | Demonstrated In / Milestone Proof |")
            lines.append("| :--- | :--- |")

            for sk in cat.get("skills", []):
                sk_id = sk.get("id")
                proofs = []

                # Find employment occurrences
                for exp in self.experience:
                    matching_bullets = [
                        b for b in exp.get("bullets", [])
                        if sk_id in b.get("skills", [])
                    ]
                    if matching_bullets:
                        b_titles = ", ".join([f"*{b.get('title')}*" for b in matching_bullets])
                        proofs.append(f"**{exp['company']}** ({exp['dates_display']}): {b_titles}")
                    elif sk_id in exp.get("skills", []):
                        proofs.append(f"**{exp['company']}** ({exp['dates_display']})")

                # Find lab / community occurrences
                for item in self.lab_and_community:
                    matching_projects = [
                        p for p in item.get("projects", [])
                        if sk_id in p.get("skills", []) or sk_id in item.get("skills", [])
                    ]
                    if matching_projects:
                        p_titles = ", ".join([f"*{p.get('title')}*" for p in matching_projects])
                        proofs.append(f"**{item['title']}**: {p_titles}")

                proof_str = "<br/>".join([f"• {p}" for p in proofs]) if proofs else "Foundation & Continuous Application"
                lines.append(f"| **{sk['name']}**<br/><small style='color: #666;'>{sk.get('description', '')}</small> | {proof_str} |")

            lines.append("\n")
        return "\n".join(lines)

    def generate_all_markdown_sections(self):
        """Generates all modular markdown files in docs/sections/ to maintain SSOT."""
        os.makedirs(SECTIONS_DIR, exist_ok=True)

        # 1. contact.md
        p = self.profile
        contact_html = f"""<div class="resume-header">
    <h1>{p['name']}</h1>
    <div class="subtitle">{p['title']}</div>
    <div class="contact-info">
        <span>{p['location']}</span>
        <span><a href="mailto:{p['email']}">{p['email']}</a></span>
        <span class="print-only"><a href="{p['site_url']}">{p['site_url'].replace('https://', '')}</a></span>
        <span class="web-only"><a href="{p['github_url']}">{p['github_url'].replace('https://', '')}</a></span>
        <span><a href="{p['linkedin_url']}">{p['linkedin_url'].replace('https://', '')}</a></span>
    </div>
</div>
"""
        with open(os.path.join(SECTIONS_DIR, "contact.md"), "w", encoding="utf-8") as f:
            f.write(contact_html)

        # 2. summary_executive.md
        with open(os.path.join(SECTIONS_DIR, "summary_executive.md"), "w", encoding="utf-8") as f:
            f.write(p["executive_summary"] + "\n")

        # 3. keywords.md
        kw_content = "## Strategic Core Competencies\n\n" + ", ".join([f"**{kw}**" for kw in p.get("keywords", [])]) + "\n"
        with open(os.path.join(SECTIONS_DIR, "keywords.md"), "w", encoding="utf-8") as f:
            f.write(kw_content)

        # 4. skills.md (Full Categorized)
        skills_md = ["## Skills\n"]
        for cat in self.skills_data.get("categories", []):
            skills_md.append(f"### **{cat['name']}**")
            for sk in cat.get("skills", []):
                skills_md.append(f"*   **{sk['short_name']}:** {sk['description']}")
            skills_md.append("")
        with open(os.path.join(SECTIONS_DIR, "skills.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(skills_md))

        # 5. skills_grid.md (3-column layout for 2-page print PDF)
        skills_grid_html = [
            '<div class="skills-section">',
            '    <div class="skills-column">',
            '        <strong>Data & Systems Engineering:</strong>',
            '        <ul>',
            '            <li>Python (Pandas, NumPy, Flask, SQLAlchemy)</li>',
            '            <li>ETL Pipeline & Data Validation</li>',
            '            <li>PostgreSQL, MySQL, MSSQL</li>',
            '            <li>Validation and QA Testing</li>',
            '            <li>Systems/Robotics Design</li>',
            '        </ul>',
            '    </div>',
            '    <div class="skills-column">',
            '        <strong>Systems & Distributed Scale:</strong>',
            '        <ul>',
            '            <li>Cisco UCS & Fabric Interconnect</li>',
            '            <li>OpenStack (Nova, Heat)</li>',
            '            <li>vSphere/ESXi, XenServer, Proxmox/KVM</li>',
            '            <li>Ceph Block Storage (RBD)</li>',
            '            <li>High-Availability (HA) Clustering</li>',
            '        </ul>',
            '    </div>',
            '    <div class="skills-column">',
            '        <strong>DevOps, Security & Leadership:</strong>',
            '        <ul>',
            '            <li>Ansible, SaltStack</li>',
            '            <li>CI/CD (GitHub Actions, Jenkins)</li>',
            '            <li>FreeIPA/LDAP, RBAC/HBAC</li>',
            '            <li>FedRAMP Compliance, Qualys</li>',
            '            <li>Monitoring, Diagnostics, Troubleshooting</li>',
            '            <li>FIRST Robotics Mentoring & Leadership</li>',
            '        </ul>',
            '    </div>',
            '</div>\n'
        ]
        with open(os.path.join(SECTIONS_DIR, "skills_grid.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(skills_grid_html))

        # 6. Experience files (Both full and short generated automatically from YAML)
        for i, exp in enumerate(self.experience, start=1):
            exp_id = exp["id"]
            prefix = f"exp_{i:02d}_{exp_id}"

            # Full version
            full_lines = [
                f"### **{exp['company']} | {exp['role']}**",
                f"**{exp['dates_display']} ({exp['location']})**\n",
                f"{exp['summary']}\n"
            ]
            for b in exp.get("bullets", []):
                if b.get("long_text"):
                    full_lines.append(f"*   **{b['title']}:** {b['long_text']}")
            full_lines.append(f"*   **Skills:** {exp['skills_display']}\n")

            with open(os.path.join(SECTIONS_DIR, f"{prefix}.md"), "w", encoding="utf-8") as f:
                f.write("\n".join(full_lines))

            # Short version
            short_lines = [
                f"### **{exp['company']} | {exp['role']}**",
                f"**{exp['dates_display']} ({exp['location']})**"
            ]
            for b in exp.get("bullets", []):
                if b.get("short_text"):
                    short_lines.append(f"*   **{b['title']}:** {b['short_text']}")
            short_skills = exp.get("skills_display_short") or exp.get("skills_display")
            short_lines.append(f"*   **Skills:** {short_skills}\n")

            with open(os.path.join(SECTIONS_DIR, f"{prefix}_short.md"), "w", encoding="utf-8") as f:
                f.write("\n".join(short_lines))

        # 7. lab.md
        lab_lines = ["## Innovation Lab & Community Leadership\n"]
        for item in self.lab_and_community:
            lab_lines.append(f"### **{item['title']}**")
            if "role" in item:
                lab_lines.append(f"**Role:** {item['role']} | **Timeline:** {item['dates_display']}\n")
            lab_lines.append(f"{item['summary']}\n")
            for p in item.get("projects", []):
                lab_lines.append(f"*   **{p['title']}:** {p['description']}")
            lab_lines.append("")
        with open(os.path.join(SECTIONS_DIR, "lab.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lab_lines))

        # 8. education.md
        edu = self.education
        edu_html = ['<div class="education-section">', '  <ul>']
        for item in edu.get("formal_and_professional", []):
            edu_html.append(f"    <li><strong>{item['institution']}:</strong> {item['detail']}</li>")
        for item in edu.get("military_and_technical_training", []):
            edu_html.append(f"    <li><strong>{item['organization']}:</strong> {item['role_or_course']}</li>")
        edu_html.append('  </ul>')
        if "certifications_url" in edu:
            edu_html.append(f'  For a list of legacy certifications, see <a href="{edu["certifications_url"]}">{edu["certifications_url"].replace("https://www.", "")}</a>')
        edu_html.append('</div>\n')

        with open(os.path.join(SECTIONS_DIR, "education.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(edu_html))

        # 9. Build interactive docs/index.md
        index_lines = [
            '--8<-- "docs/sections/contact.md"',
            '',
            '---',
            '',
            '## Professional Summary',
            '',
            '--8<-- "docs/sections/summary_executive.md"',
            '',
            '---',
            '',
            '--8<-- "docs/sections/skills.md"',
            '',
            '---',
            '',
            self.build_traceability_matrix_markdown(),
            '',
            '---',
            '',
            '## Professional Experience',
            ''
        ]
        for i, exp in enumerate(self.experience, start=1):
            index_lines.append(f'--8<-- "docs/sections/exp_{i:02d}_{exp["id"]}.md"')
            index_lines.append('')

        index_lines.extend([
            '---',
            '',
            '--8<-- "docs/sections/lab.md"',
            '',
            '---',
            '',
            '## Education & Certifications',
            '--8<-- "docs/sections/education.md"',
            '',
            '---',
            '',
            '--8<-- "docs/sections/keywords.md"',
            ''
        ])

        with open(os.path.join(DOCS_DIR, "index.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(index_lines))

        print("Successfully generated all markdown sections and web portfolio from YAML database!")

    def export_linkedin(self):
        """Outputs formatted, character-budgeted blocks for updating LinkedIn."""
        out = []
        out.append("=" * 80)
        out.append("LINKEDIN PROFILE UPDATE BLOCKS (COPY & PASTE READY)")
        out.append("=" * 80)
        out.append("\n" + "#" * 40)
        out.append("1. HEADLINE (Limit: 220 chars)")
        out.append("#" * 40)
        headline = "Senior Systems & Platform Engineer | FedRAMP & Cloud SecOps | Data Platforms (Python/Pandas/PostgreSQL) | Infrastructure-as-Code & Identity (Ansible/FreeIPA) | FIRST Robotics Mentor"
        out.append(f"{headline}  [{len(headline)} / 220 chars]\n")

        out.append("#" * 40)
        out.append("2. ABOUT SECTION (Limit: 2,600 chars)")
        out.append("#" * 40)
        about = self.profile["executive_summary"]
        out.append(about)
        out.append(f"\n[Length: {len(about)} / 2600 chars]\n")

        out.append("#" * 40)
        out.append("3. EXPERIENCE SECTIONS (Limit: 2,000 chars per role)")
        out.append("#" * 40)

        for exp in self.experience:
            role_header = f"COMPANY: {exp['company']}\nTITLE: {exp['role']}\nDATES: {exp['dates_display']}\nLOCATION: {exp['location']}"
            out.append("-" * 60)
            out.append(role_header)
            out.append("-" * 60)

            # Build clean unicode bullet text for LinkedIn
            lines = [exp["summary"], ""]
            for b in exp.get("bullets", []):
                bullet_content = b.get("linkedin_text") or b.get("long_text")
                if bullet_content:
                    # Strip markdown asterisks and replace with clean unicode bullet
                    clean_b = re.sub(r'\*\*(.*?)\*\*', r'\1', bullet_content)
                    lines.append(f"• {b['title']}: {clean_b}")

            role_body = "\n\n".join([line for line in lines if line != ""])
            out.append(role_body)
            char_count = len(role_body)
            status = "✅ PASS" if char_count <= 2000 else "⚠️ EXCEEDS 2000 CHARS"
            out.append(f"\n[Role Description Length: {char_count} / 2000 chars - {status}]")

            # Tagged skills for LinkedIn's "Skills associated with this role"
            role_skills_str = ", ".join([
                self.skill_map.get(s_id, {}).get("short_name", s_id)
                for s_id in exp.get("skills", [])
            ])
            out.append(f"* ASSOCIATED SKILLS TO TAG IN LINKEDIN:\n  {role_skills_str}\n")

        out.append("#" * 40)
        out.append("4. VOLUNTEERING / MENTORING SECTION (FIRST Robotics)")
        out.append("#" * 40)
        robotics = next((item for item in self.lab_and_community if item["id"] == "first_robotics"), None)
        if robotics:
            out.append(f"ORGANIZATION: FIRST Robotics\nROLE: {robotics['role']}\nTIMELINE: {robotics['dates_display']}\n")
            out.append(robotics["summary"] + "\n")
            for p in robotics.get("projects", []):
                clean_p = re.sub(r'\*\*(.*?)\*\*', r'\1', p['description'])
                out.append(f"• {p['title']}: {clean_p}")
            out.append(f"\nSKILLS TO TAG: Robotics Design, Embedded Systems, Troubleshooting, STEM Education, Technical Mentorship\n")

        out.append("#" * 40)
        out.append("5. FEATURED PROJECTS SECTION (Innovation Lab R&D)")
        out.append("#" * 40)
        lab = next((item for item in self.lab_and_community if item["id"] == "innovation_lab"), None)
        if lab:
            for p in lab.get("projects", []):
                clean_p = re.sub(r'\*\*(.*?)\*\*', r'\1', p['description'])
                out.append(f"PROJECT NAME: {p['title']}\nSUMMARY: {clean_p}\n")

        out.append("=" * 80)
        return "\n".join(out)

    def export_plaintext_ats(self):
        """Generates clean plaintext resume for ATS forms."""
        p = self.profile
        lines = [
            f"{p['name'].upper()}",
            f"{p['title']} | {p['location']}",
            f"Email: {p['email']} | Portfolio: {p['site_url']} | LinkedIn: {p['linkedin_url']}",
            "=" * 70,
            "\nPROFESSIONAL SUMMARY\n",
            p["executive_summary"],
            "\n" + "=" * 70,
            "\nCORE TECHNICAL COMPETENCIES\n"
        ]
        for cat in self.skills_data.get("categories", []):
            lines.append(f"• {cat['name']}: " + ", ".join([sk['name'] for sk in cat.get("skills", [])]))

        lines.extend(["\n" + "=" * 70, "\nPROFESSIONAL EXPERIENCE\n"])
        for exp in self.experience:
            lines.append(f"{exp['company'].upper()} | {exp['role']}")
            lines.append(f"{exp['dates_display']} | {exp['location']}")
            lines.append(f"{exp['summary']}\n")
            for b in exp.get("bullets", []):
                if b.get("long_text"):
                    clean_b = re.sub(r'\*\*(.*?)\*\*', r'\1', b['long_text'])
                    lines.append(f"  * {b['title']}: {clean_b}")
            lines.append(f"  * Core Technologies: {exp['skills_display']}\n")

        lines.extend(["=" * 70, "\nEDUCATION & TRAINING\n"])
        for item in self.education.get("formal_and_professional", []):
            lines.append(f"• {item['institution']}: {item['detail']}")
        for item in self.education.get("military_and_technical_training", []):
            lines.append(f"• {item['organization']}: {item['role_or_course']}")

        return "\n".join(lines)

def build_pdf_from_template(template_path, output_path, css_path):
    """Compiles WeasyPrint PDF with snippet resolution."""
    print(f"Reading template: {template_path}")
    with open(template_path, 'r', encoding='utf-8') as f:
        raw_content = f.read()

    # Resolve snippets
    pattern = re.compile(r'--8<--\s+["\']?([^"\']+)["\']?')
    def replace_match(match):
        file_path = os.path.join(BASE_DIR, match.group(1))
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as sf:
                return sf.read()
        return f"<!-- Missing snippet: {file_path} -->"

    resolved = pattern.sub(replace_match, raw_content)

    # Convert to HTML
    html_body = markdown.markdown(resolved, extensions=['extra', 'sane_lists', 'md_in_html', 'admonition', 'meta'])
    html_doc = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Resume - Brian Jarrett</title>
</head>
<body>
    <div class="resume-container">
        {html_body}
    </div>
</body>
</html>"""

    print(f"Compiling PDF -> {output_path}")
    weasyprint.HTML(string=html_doc, base_url=BASE_DIR).write_pdf(output_path, stylesheets=[css_path])
    print("PDF build complete!")

def main():
    parser = argparse.ArgumentParser(description="SSOT Resume, Portfolio, and Platform Export Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # 1. find-skill
    p_find = subparsers.add_parser("find-skill", help="Query skills and trace evidence across experience and lab records")
    p_find.add_argument("query", help="Skill ID or keyword to search")

    # 2. export
    p_export = subparsers.add_parser("export", help="Export profile to external platforms")
    p_export.add_argument("--platform", choices=["linkedin", "ats"], default="linkedin", help="Target platform")
    p_export.add_argument("-o", "--output", help="Optional file path to save export output")

    # 3. build-markdown
    subparsers.add_parser("build-markdown", help="Compile YAML database to docs/sections and web portfolio markdown")

    # 4. build-pdf
    p_pdf = subparsers.add_parser("build-pdf", help="Compile WeasyPrint print-ready PDFs")
    p_pdf.add_argument("--type", choices=["all", "2page", "master"], default="all", help="PDF variant to compile")

    # 5. build
    subparsers.add_parser("build", help="Full build: compile markdown sections, web index, and all PDFs")

    args = parser.parse_args()
    db = ResumeDatabase()

    if args.command == "find-skill":
        db.query_skill(args.query)

    elif args.command == "export":
        if args.platform == "linkedin":
            content = db.export_linkedin()
        elif args.platform == "ats":
            content = db.export_plaintext_ats()
        else:
            content = ""

        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Export saved to: {args.output}")
        else:
            print(content)

    elif args.command == "build-markdown":
        db.generate_all_markdown_sections()

    elif args.command == "build-pdf":
        db.generate_all_markdown_sections()
        if args.type in ["all", "master"]:
            build_pdf_from_template(
                os.path.join(TEMPLATES_DIR, "resume_master.md"),
                os.path.join(DOCS_DIR, "resume_master.pdf"),
                os.path.join(TEMPLATES_DIR, "resume_print.css")
            )
            # Copy to root
            with open(os.path.join(DOCS_DIR, "resume_master.pdf"), "rb") as src, open(os.path.join(BASE_DIR, "resume_master.pdf"), "wb") as dst:
                dst.write(src.read())

        if args.type in ["all", "2page"]:
            build_pdf_from_template(
                os.path.join(TEMPLATES_DIR, "resume_master_2page.md"),
                os.path.join(DOCS_DIR, "resume_master_2page.pdf"),
                os.path.join(TEMPLATES_DIR, "resume_print_2page.css")
            )
            # Copy to root
            with open(os.path.join(DOCS_DIR, "resume_master_2page.pdf"), "rb") as src, open(os.path.join(BASE_DIR, "resume_master_2page.pdf"), "wb") as dst:
                dst.write(src.read())

    elif args.command == "build" or args.command is None:
        print("Running complete SSOT build...")
        db.generate_all_markdown_sections()
        build_pdf_from_template(
            os.path.join(TEMPLATES_DIR, "resume_master.md"),
            os.path.join(DOCS_DIR, "resume_master.pdf"),
            os.path.join(TEMPLATES_DIR, "resume_print.css")
        )
        build_pdf_from_template(
            os.path.join(TEMPLATES_DIR, "resume_master_2page.md"),
            os.path.join(DOCS_DIR, "resume_master_2page.pdf"),
            os.path.join(TEMPLATES_DIR, "resume_print_2page.css")
        )
        with open(os.path.join(DOCS_DIR, "resume_master.pdf"), "rb") as src, open(os.path.join(BASE_DIR, "resume_master.pdf"), "wb") as dst:
            dst.write(src.read())
        with open(os.path.join(DOCS_DIR, "resume_master_2page.pdf"), "rb") as src, open(os.path.join(BASE_DIR, "resume_master_2page.pdf"), "wb") as dst:
            dst.write(src.read())
        print("SSOT build completed successfully!")

if __name__ == "__main__":
    main()
