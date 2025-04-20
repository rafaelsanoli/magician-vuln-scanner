import json
from datetime import datetime
from jinja2 import Template


def generate_report(results, config):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    html_path = f"report_{timestamp}.html"

    severity_ranking = classify_severity(results)
    html_content = render_html_report(results, severity_ranking)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
        print(f"[+] Relatório HTML salvo em {html_path}")


def classify_severity(results):
    ranking = []
    for item in results:
        severity = "Baixo"
        for v in item["vulnerabilities"] + item["exploit_attempts"]:
            if "SQLi" in v or "SQL" in v:
                severity = "Crítico"
                break
            elif "XSS" in v:
                severity = "Alto"
            elif "ausente" in v or "header" in v.lower():
                severity = "Médio"
        ranking.append({"url": item["url"], "severity": severity})
    return ranking


def render_html_report(results, severity_ranking):
    template_str = """
    <html>
    <head>
        <title>Relatório de Segurança</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 30px; }
            h1 { color: #c0392b; }
            .vuln { background: #f2dede; padding: 10px; margin: 10px 0; border-radius: 5px; }
            .ai { background: #d9edf7; padding: 10px; margin: 10px 0; border-radius: 5px; }
            .exploit { background: #fcf8e3; padding: 10px; margin: 10px 0; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>Relatório de Segurança</h1>
        <p>Data de geração: {{ timestamp }}</p>

        {% for item, rank in data %}
        <hr>
        <h2>{{ item.url }}</h2>
        <p><strong>Gravidade:</strong> {{ rank.severity }}</p>

        <div class="vuln">
            <strong>Vulnerabilidades:</strong>
            <ul>
            {% for v in item.vulnerabilities %}
                <li>{{ v }}</li>
            {% endfor %}
            </ul>
        </div>

        <div class="exploit">
            <strong>Tentativas de Exploit:</strong>
            <ul>
            {% for e in item.exploit_attempts %}
                <li>{{ e }}</li>
            {% endfor %}
            </ul>
        </div>

        <div class="ai">
            <strong>Análise por IA:</strong>
            <pre>{{ item.ai_analysis }}</pre>
        </div>
        {% endfor %}

    </body>
    </html>
    """
    template = Template(template_str)
    return template.render(data=zip(results, severity_ranking), timestamp=datetime.now().strftime("%d/%m/%Y %H:%M"))

