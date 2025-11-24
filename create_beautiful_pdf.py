#!/usr/bin/env pdf_venv/bin/python3
"""
Create a beautiful PDF from the work plan markdown file.
"""

import markdown2
from weasyprint import HTML, CSS
from pathlib import Path

# File paths
input_file = "/Users/rodrigofaerman/Library/CloudStorage/GoogleDrive-rodrigo@alephant.ai/My Drive/ALEPHANT/[PEOPLE + COMPANIES]/[CLIENTS]/[ACTIVE]/[SARAH ZOMER]/PLANO_TRABALHO_4_FASES.md"
output_file = "/Users/rodrigofaerman/Library/CloudStorage/GoogleDrive-rodrigo@alephant.ai/My Drive/ALEPHANT/[PEOPLE + COMPANIES]/[CLIENTS]/[ACTIVE]/[SARAH ZOMER]/PLANO_TRABALHO_4_FASES.pdf"

# Read markdown content
with open(input_file, 'r', encoding='utf-8') as f:
    markdown_content = f.read()

# Convert markdown to HTML
html_content = markdown2.markdown(
    markdown_content,
    extras=['tables', 'fenced-code-blocks', 'header-ids', 'metadata', 'break-on-newline']
)

# Create beautiful HTML with CSS styling
html_template = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Plano de Trabalho 4 Fases - Sarah Zomer</title>
    <style>
        @page {{
            size: A4;
            margin: 2.5cm 2cm;
            @bottom-center {{
                content: "Página " counter(page) " de " counter(pages);
                font-size: 9pt;
                color: #666;
                font-family: 'Helvetica', sans-serif;
            }}
        }}

        body {{
            font-family: 'Helvetica', 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 100%;
            margin: 0;
            padding: 0;
        }}

        h1 {{
            color: #1a1a1a;
            font-size: 28pt;
            font-weight: bold;
            margin-top: 0;
            margin-bottom: 20pt;
            padding-bottom: 10pt;
            border-bottom: 3px solid #2c5aa0;
            page-break-after: avoid;
        }}

        h2 {{
            color: #2c5aa0;
            font-size: 20pt;
            font-weight: bold;
            margin-top: 30pt;
            margin-bottom: 15pt;
            page-break-before: always;
            page-break-after: avoid;
            border-left: 4px solid #2c5aa0;
            padding-left: 12pt;
        }}

        h2:first-of-type {{
            page-break-before: auto;
        }}

        h3 {{
            color: #4a7db8;
            font-size: 16pt;
            font-weight: bold;
            margin-top: 20pt;
            margin-bottom: 12pt;
            page-break-after: avoid;
        }}

        h4 {{
            color: #5a8cc7;
            font-size: 13pt;
            font-weight: bold;
            margin-top: 15pt;
            margin-bottom: 10pt;
            page-break-after: avoid;
        }}

        p {{
            margin: 0 0 10pt 0;
            text-align: justify;
        }}

        strong, b {{
            color: #1a1a1a;
            font-weight: bold;
        }}

        ul, ol {{
            margin: 10pt 0;
            padding-left: 25pt;
        }}

        li {{
            margin-bottom: 6pt;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 15pt 0;
            page-break-inside: avoid;
        }}

        th {{
            background-color: #2c5aa0;
            color: white;
            font-weight: bold;
            padding: 10pt;
            text-align: left;
            border: 1px solid #1a3d6b;
        }}

        td {{
            padding: 8pt 10pt;
            border: 1px solid #ddd;
        }}

        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}

        tr:hover {{
            background-color: #f0f5fa;
        }}

        hr {{
            border: none;
            border-top: 2px solid #e0e0e0;
            margin: 25pt 0;
        }}

        code {{
            background-color: #f4f4f4;
            padding: 2pt 5pt;
            border-radius: 3pt;
            font-family: 'Courier New', monospace;
            font-size: 9pt;
        }}

        pre {{
            background-color: #f8f8f8;
            padding: 12pt;
            border-left: 4px solid #2c5aa0;
            border-radius: 4pt;
            overflow-x: auto;
            page-break-inside: avoid;
        }}

        pre code {{
            background-color: transparent;
            padding: 0;
        }}

        blockquote {{
            border-left: 4px solid #ccc;
            padding-left: 15pt;
            margin-left: 0;
            font-style: italic;
            color: #666;
        }}

        /* Status indicators */
        .status {{
            display: inline-block;
            padding: 2pt 8pt;
            border-radius: 3pt;
            font-size: 9pt;
            font-weight: bold;
        }}

        /* Cover page styling */
        .cover-page {{
            text-align: center;
            padding-top: 100pt;
            page-break-after: always;
        }}

        .cover-title {{
            font-size: 36pt;
            font-weight: bold;
            color: #2c5aa0;
            margin-bottom: 20pt;
        }}

        .cover-subtitle {{
            font-size: 18pt;
            color: #666;
            margin-bottom: 40pt;
        }}

        .cover-info {{
            font-size: 12pt;
            color: #888;
            margin-top: 60pt;
        }}

        /* Prevent orphaned headings */
        h1, h2, h3, h4, h5, h6 {{
            page-break-inside: avoid;
        }}

        /* Keep tables together when possible */
        table {{
            page-break-inside: auto;
        }}

        tr {{
            page-break-inside: avoid;
            page-break-after: auto;
        }}
    </style>
</head>
<body>
    <div class="cover-page">
        <div class="cover-title">Plano de Trabalho 4 Fases</div>
        <div class="cover-subtitle">Projeto Sarah Zomer</div>
        <div class="cover-info">
            <p><strong>Duração:</strong> 4 meses (Outubro 2025 - Janeiro 2026)</p>
            <p><strong>Formato:</strong> Mentoria Intensiva + Consultoria Hands-On</p>
            <p><strong>Última Atualização:</strong> 20 de outubro de 2025</p>
            <p><strong>Responsável:</strong> Rodrigo Faerman</p>
        </div>
    </div>

    {html_content}
</body>
</html>
"""

# Generate PDF
print("Generating PDF...")
HTML(string=html_template).write_pdf(output_file)
print(f"PDF created successfully: {output_file}")
