#!/usr/bin/env python3
import os
import weasyprint

def generate_specimen():
    html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Resume Font Comparison Specimen</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Roboto:wght@400;500;700&family=Lato:wght@400;700&family=Lora:ital,wght@0,400;0,700;1,400&family=Merriweather:wght@400;700&display=swap');
        
        @page {
            size: letter;
            margin: 0.5in;
            @bottom-right {
                content: "Page " counter(page);
                font-family: 'Inter', sans-serif;
                font-size: 8pt;
                color: #a0aec0;
            }
        }
        
        body {
            font-family: 'Inter', sans-serif;
            color: #2d3748;
            line-height: 1.4;
            font-size: 10pt;
            margin: 0;
            padding: 0;
        }
        
        h1.main-title {
            font-size: 20pt;
            color: #1a365d;
            border-bottom: 2px solid #2b6cb0;
            padding-bottom: 8px;
            margin-top: 0;
            margin-bottom: 20px;
            text-align: center;
            font-weight: 700;
        }
        
        .specimen-card {
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            padding: 15px;
            margin-bottom: 20px;
            page-break-inside: avoid;
            background-color: #f7fafc;
        }
        
        .specimen-card.active-font {
            border-color: #3182ce;
            background-color: #f0fff4;
            border-width: 2px;
        }
        
        .font-meta {
            font-size: 11pt;
            font-weight: bold;
            color: #4a5568;
            margin-bottom: 10px;
            border-bottom: 1px dashed #cbd5e0;
            padding-bottom: 4px;
        }
        
        .font-meta span.tag {
            font-size: 8pt;
            background-color: #edf2f7;
            padding: 2px 6px;
            border-radius: 4px;
            margin-left: 8px;
            font-weight: normal;
        }
        
        .font-meta span.active-tag {
            background-color: #c6f6d5;
            color: #22543d;
        }

        /* Test classes for each font family */
        .font-dejavu {
            font-family: 'DejaVu Sans', 'DejaVuSans', 'Arimo', sans-serif;
        }
        .font-inter {
            font-family: 'Inter', sans-serif;
        }
        .font-roboto {
            font-family: 'Roboto', sans-serif;
        }
        .font-lato {
            font-family: 'Lato', sans-serif;
        }
        .font-lora {
            font-family: 'Lora', serif;
        }
        .font-merriweather {
            font-family: 'Merriweather', serif;
        }
        
        /* Sample element styling mimicking resume elements */
        .sample-header {
            font-size: 16pt;
            font-weight: 700;
            color: #1a365d;
            margin: 0 0 2px 0;
            text-transform: uppercase;
            letter-spacing: -0.5px;
        }
        
        .sample-subtitle {
            font-size: 10pt;
            font-weight: bold;
            color: #4a5568;
            margin-bottom: 8px;
        }
        
        .sample-section-title {
            font-size: 11pt;
            font-weight: 700;
            color: #2b6cb0;
            border-bottom: 1px solid #cbd5e0;
            margin-top: 12px;
            margin-bottom: 6px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .sample-body {
            font-size: 9.5pt;
            line-height: 1.35;
            color: #2d3748;
        }
        
        .sample-bold {
            font-weight: bold;
        }
    </style>
</head>
<body>

    <h1 class="main-title">Brian Jarrett - Resume Typography Specimen Sheet</h1>
    <p style="margin-bottom: 25px; font-size: 9.5pt; color: #718096; text-align: center;">
        This specimen displays your header, section layout, and body text rendered in each candidate font using WeasyPrint.
    </p>

    <!-- 1. DEJAVU SANS -->
    <div class="specimen-card">
        <div class="font-meta">1. DejaVu Sans <span class="tag">System Sans-Serif (Your Choice)</span></div>
        <div class="font-dejavu">
            <div class="sample-header">Brian Jarrett</div>
            <div class="sample-subtitle">Systems Engineer | Grove, OK | celttechie@gmail.com</div>
            <div class="sample-section-title">Professional Summary</div>
            <div class="sample-body">
                <span class="sample-bold">Expert in diagnosing legacy infrastructure</span>, verifying data quality at the source to prevent the propagation of bad data and ensure the integrity of the final output, and architecting robust ETL pipelines that merge disparate inputs into high-integrity sources of truth.
            </div>
        </div>
    </div>

    <!-- 2. INTER -->
    <div class="specimen-card active-font">
        <div class="font-meta">2. Inter <span class="tag active-tag">Current Choice (Neo-Grotesque Sans)</span></div>
        <div class="font-inter">
            <div class="sample-header">Brian Jarrett</div>
            <div class="sample-subtitle">Systems Engineer | Grove, OK | celttechie@gmail.com</div>
            <div class="sample-section-title">Professional Summary</div>
            <div class="sample-body">
                <span class="sample-bold">Expert in diagnosing legacy infrastructure</span>, verifying data quality at the source to prevent the propagation of bad data and ensure the integrity of the final output, and architecting robust ETL pipelines that merge disparate inputs into high-integrity sources of truth.
            </div>
        </div>
    </div>

    <!-- 3. ROBOTO -->
    <div class="specimen-card">
        <div class="font-meta">3. Roboto <span class="tag">Google Neo-Grotesque Sans</span></div>
        <div class="font-roboto">
            <div class="sample-header">Brian Jarrett</div>
            <div class="sample-subtitle">Systems Engineer | Grove, OK | celttechie@gmail.com</div>
            <div class="sample-section-title">Professional Summary</div>
            <div class="sample-body">
                <span class="sample-bold">Expert in diagnosing legacy infrastructure</span>, verifying data quality at the source to prevent the propagation of bad data and ensure the integrity of the final output, and architecting robust ETL pipelines that merge disparate inputs into high-integrity sources of truth.
            </div>
        </div>
    </div>

    <!-- 4. LATO -->
    <div class="specimen-card">
        <div class="font-meta">4. Lato <span class="tag">Warm / Semi-Geometric Sans-Serif</span></div>
        <div class="font-lato">
            <div class="sample-header">Brian Jarrett</div>
            <div class="sample-subtitle">Systems Engineer | Grove, OK | celttechie@gmail.com</div>
            <div class="sample-section-title">Professional Summary</div>
            <div class="sample-body">
                <span class="sample-bold">Expert in diagnosing legacy infrastructure</span>, verifying data quality at the source to prevent the propagation of bad data and ensure the integrity of the final output, and architecting robust ETL pipelines that merge disparate inputs into high-integrity sources of truth.
            </div>
        </div>
    </div>

    <!-- 5. LORA -->
    <div class="specimen-card">
        <div class="font-meta">5. Lora <span class="tag">Elegant / Contemporary Serif</span></div>
        <div class="font-lora">
            <div class="sample-header">Brian Jarrett</div>
            <div class="sample-subtitle">Systems Engineer | Grove, OK | celttechie@gmail.com</div>
            <div class="sample-section-title">Professional Summary</div>
            <div class="sample-body">
                <span class="sample-bold">Expert in diagnosing legacy infrastructure</span>, verifying data quality at the source to prevent the propagation of bad data and ensure the integrity of the final output, and architecting robust ETL pipelines that merge disparate inputs into high-integrity sources of truth.
            </div>
        </div>
    </div>

    <!-- 6. MERRIWEATHER -->
    <div class="specimen-card">
        <div class="font-meta">6. Merriweather <span class="tag">Editorial / Sturdy Serif</span></div>
        <div class="font-merriweather">
            <div class="sample-header">Brian Jarrett</div>
            <div class="sample-subtitle">Systems Engineer | Grove, OK | celttechie@gmail.com</div>
            <div class="sample-section-title">Professional Summary</div>
            <div class="sample-body">
                <span class="sample-bold">Expert in diagnosing legacy infrastructure</span>, verifying data quality at the source to prevent the propagation of bad data and ensure the integrity of the final output, and architecting robust ETL pipelines that merge disparate inputs into high-integrity sources of truth.
            </div>
        </div>
    </div>

</body>
</html>
"""
    output_path = "/home/brian/.gemini/antigravity-cli/brain/375d4fda-3ad8-4fb3-aad8-15ec1fcbc3eb/font_specimen_comparison.pdf"
    print(f"Generating specimen sheet at: {output_path}")
    weasyprint.HTML(string=html_content).write_pdf(output_path)
    print("Specimen generated successfully!")

if __name__ == "__main__":
    generate_specimen()
