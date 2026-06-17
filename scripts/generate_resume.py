#!/usr/bin/env python3
import os
import re
import argparse
import markdown
import weasyprint

def resolve_snippets(content, base_dir):
    """
    Recursively resolves MkDocs-style snippets: --8<-- "path/to/file.md"
    """
    pattern = re.compile(r'--8<--\s+["\']?([^"\']+)["\']?')
    
    def replace_match(match):
        file_path = match.group(1)
        full_path = os.path.join(base_dir, file_path)
        if os.path.exists(full_path):
            with open(full_path, 'r', encoding='utf-8') as f:
                nested_content = f.read()
            # Recursively resolve any snippets inside the nested file
            return resolve_snippets(nested_content, base_dir)
        else:
            print(f"Warning: Snippet file not found: {full_path}")
            return f"<!-- Missing snippet: {file_path} -->"
            
    return pattern.sub(replace_match, content)

def build_pdf(template_path, output_path, css_path):
    print(f"Reading template from: {template_path}")
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template file not found: {template_path}")
        
    with open(template_path, 'r', encoding='utf-8') as f:
        raw_content = f.read()
        
    # Resolve snippets relative to the project root (current working directory)
    project_root = os.getcwd()
    resolved_markdown = resolve_snippets(raw_content, project_root)
    
    # Clean up section numbers from headers to make them resume-standard
    resolved_markdown = re.sub(
        r'^##\s+\d+\.\s+Categorized Skill Matrix', 
        '## Technical Skills', 
        resolved_markdown, 
        flags=re.MULTILINE
    )
    resolved_markdown = re.sub(
        r'^##\s+\d+\.\s+The Innovation Lab.*', 
        '## Innovation Lab (Personal R&D)', 
        resolved_markdown, 
        flags=re.MULTILINE
    )
    resolved_markdown = re.sub(
        r'^##\s+\d+\.\s+Education & Certifications', 
        '## Education & Certifications', 
        resolved_markdown, 
        flags=re.MULTILINE
    )
    
    # Convert Markdown to HTML
    # Using 'extra' extension for tables, attributes, definition lists, etc.
    html_body = markdown.markdown(resolved_markdown, extensions=['extra', 'admonition', 'meta'])
    
    # Wrap in HTML document structure
    html_document = f"""<!DOCTYPE html>
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
</html>
"""
    
    print(f"Generating PDF using WeasyPrint at: {output_path}")
    print(f"Applying stylesheet: {css_path}")
    
    # Compile PDF
    weasyprint.HTML(string=html_document, base_url=project_root).write_pdf(
        output_path,
        stylesheets=[css_path]
    )
    print("PDF generated successfully!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate resume PDF from Markdown templates.")
    parser.add_argument(
        '-t', '--template',
        default='templates/resume_master.md',
        help="Path to the source markdown template (default: templates/resume_master.md)"
    )
    parser.add_argument(
        '-o', '--output',
        default='resume_master.pdf',
        help="Path to save the generated PDF (default: resume_master.pdf)"
    )
    parser.add_argument(
        '-c', '--css',
        default='templates/resume_print.css',
        help="Path to the print stylesheet (default: templates/resume_print.css)"
    )
    
    args = parser.parse_args()
    
    # Ensure directories exist
    os.makedirs(os.path.dirname(args.output) if os.path.dirname(args.output) else '.', exist_ok=True)
    
    try:
        build_pdf(args.template, args.output, args.css)
    except Exception as e:
        print(f"Error generating PDF: {e}")
        exit(1)
