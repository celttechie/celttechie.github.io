#!/usr/bin/env python3
import os
import weasyprint

def generate_specimen():
    html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Resume Font Comparison Specimen - Round 2</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Fira+Sans:wght@400;500;700&family=IBM+Plex+Sans:wght@400;500;700&family=IBM+Plex+Serif:wght@400;700&display=swap');
        
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
            font-family: 'DejaVu Sans', sans-serif;
            color: #2d3748;
            line-height: 1.4;
            font-size: 10pt;
            margin: 0;
            padding: 0;
        }
        
        h1.main-title {
            font-size: 18pt;
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
            background-color: #f7fafc;
            border-width: 1.5px;
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

        /* Test classes for each font family */
        .font-dejavusans {
            font-family: 'DejaVu Sans', 'DejaVuSans', sans-serif;
        }
        .font-dejavuserif {
            font-family: 'DejaVu Serif', 'DejaVuSerif', serif;
        }
        .font-liberationsans {
            font-family: 'Liberation Sans', 'LiberationSans', sans-serif;
        }
        .font-liberationserif {
            font-family: 'Liberation Serif', 'LiberationSerif', serif;
        }
        .font-ibmplexsans {
            font-family: 'IBM Plex Sans', sans-serif;
        }
        .font-ibmplexserif {
            font-family: 'IBM Plex Serif', serif;
        }
        .font-firasans {
            font-family: 'Fira Sans', sans-serif;
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

    <h1 class="main-title">Brian Jarrett - Resume Specimen Sheet (Round 2)</h1>
    <p style="margin-bottom: 25px; font-size: 9.5pt; color: #718096; text-align: center;">
        Focusing on DejaVu and other highly precise, clean fonts optimized for clear technical readability.
    </p>

    <!-- 1. DEJAVU SANS -->
    <div class="specimen-card active-font">
        <div class="font-meta">1. DejaVu Sans <span class="tag">Clean System Sans-Serif</span></div>
        <div class="font-dejavusans">
            <div class="sample-header">Brian Jarrett</div>
            <div class="sample-subtitle">Systems Engineer | Grove, OK | celttechie@gmail.com</div>
            <div class="sample-section-title">Professional Summary</div>
            <div class="sample-body">
                <span class="sample-bold">Expert in diagnosing legacy infrastructure</span>, verifying data quality at the source to prevent the propagation of bad data and ensure the integrity of the final output, and architecting robust ETL pipelines that merge disparate inputs into high-integrity sources of truth.
            </div>
        </div>
    </div>

    <!-- 2. DEJAVU SERIF -->
    <div class="specimen-card">
        <div class="font-meta">2. DejaVu Serif <span class="tag">Sturdy System Serif</span></div>
        <div class="font-dejavuserif">
            <div class="sample-header">Brian Jarrett</div>
            <div class="sample-subtitle">Systems Engineer | Grove, OK | celttechie@gmail.com</div>
            <div class="sample-section-title">Professional Summary</div>
            <div class="sample-body">
                <span class="sample-bold">Expert in diagnosing legacy infrastructure</span>, verifying data quality at the source to prevent the propagation of bad data and ensure the integrity of the final output, and architecting robust ETL pipelines that merge disparate inputs into high-integrity sources of truth.
            </div>
        </div>
    </div>

    <!-- 3. LIBERATION SANS -->
    <div class="specimen-card">
        <div class="font-meta">3. Liberation Sans <span class="tag">Standard System Metric Sans</span></div>
        <div class="font-liberationsans">
            <div class="sample-header">Brian Jarrett</div>
            <div class="sample-subtitle">Systems Engineer | Grove, OK | celttechie@gmail.com</div>
            <div class="sample-section-title">Professional Summary</div>
            <div class="sample-body">
                <span class="sample-bold">Expert in diagnosing legacy infrastructure</span>, verifying data quality at the source to prevent the propagation of bad data and ensure the integrity of the final output, and architecting robust ETL pipelines that merge disparate inputs into high-integrity sources of truth.
            </div>
        </div>
    </div>

    <!-- 4. LIBERATION SERIF -->
    <div class="specimen-card">
        <div class="font-meta">4. Liberation Serif <span class="tag">Standard System Metric Serif</span></div>
        <div class="font-liberationserif">
            <div class="sample-header">Brian Jarrett</div>
            <div class="sample-subtitle">Systems Engineer | Grove, OK | celttechie@gmail.com</div>
            <div class="sample-section-title">Professional Summary</div>
            <div class="sample-body">
                <span class="sample-bold">Expert in diagnosing legacy infrastructure</span>, verifying data quality at the source to prevent the propagation of bad data and ensure the integrity of the final output, and architecting robust ETL pipelines that merge disparate inputs into high-integrity sources of truth.
            </div>
        </div>
    </div>

    <!-- 5. IBM PLEX SANS -->
    <div class="specimen-card">
        <div class="font-meta">5. IBM Plex Sans <span class="tag">High-Precision Technical Sans-Serif</span></div>
        <div class="font-ibmplexsans">
            <div class="sample-header">Brian Jarrett</div>
            <div class="sample-subtitle">Systems Engineer | Grove, OK | celttechie@gmail.com</div>
            <div class="sample-section-title">Professional Summary</div>
            <div class="sample-body">
                <span class="sample-bold">Expert in diagnosing legacy infrastructure</span>, verifying data quality at the source to prevent the propagation of bad data and ensure the integrity of the final output, and architecting robust ETL pipelines that merge disparate inputs into high-integrity sources of truth.
            </div>
        </div>
    </div>

    <!-- 6. IBM PLEX SERIF -->
    <div class="specimen-card">
        <div class="font-meta">6. IBM Plex Serif <span class="tag">Technical Engineering Serif</span></div>
        <div class="font-ibmplexserif">
            <div class="sample-header">Brian Jarrett</div>
            <div class="sample-subtitle">Systems Engineer | Grove, OK | celttechie@gmail.com</div>
            <div class="sample-section-title">Professional Summary</div>
            <div class="sample-body">
                <span class="sample-bold">Expert in diagnosing legacy infrastructure</span>, verifying data quality at the source to prevent the propagation of bad data and ensure the integrity of the final output, and architecting robust ETL pipelines that merge disparate inputs into high-integrity sources of truth.
            </div>
        </div>
    </div>

    <!-- 7. FIRA SANS -->
    <div class="specimen-card">
        <div class="font-meta">7. Fira Sans <span class="tag">Highly Legible Modern Sans-Serif</span></div>
        <div class="font-firasans">
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
    output_path = "/home/brian/.gemini/antigravity-cli/brain/375d4fda-3ad8-4fb3-aad8-15ec1fcbc3eb/font_specimen_comparison_round2.pdf"
    print(f"Generating round 2 specimen sheet at: {output_path}")
    weasyprint.HTML(string=html_content).write_pdf(output_path)
    print("Specimen generated successfully!")

if __name__ == "__main__":
    generate_specimen()
