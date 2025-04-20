from crawler import crawl_site
from vulns import check_vulnerabilities
from analyzer import analyze_with_ai
from auth import authenticate
from attacker import attempt_exploits
from report import generate_report
import json


def run_scan(target_url, config, output_path):
    print(f"[+] Iniciando varredura em: {target_url}")
    session = authenticate(target_url, config)
    endpoints = crawl_site(target_url, config, session=session)

    print("[+] Endpoints encontrados:")
    for url in endpoints:
        print(" -", url)

    print("\n[+] Iniciando checagem de vulnerabilidades...")
    results = []
    for url in endpoints:
        vulns = check_vulnerabilities(url, session=session)
        analysis = analyze_with_ai(url, config, session=session)
        exploits = attempt_exploits(url, session=session)
        results.append({
            "url": url,
            "vulnerabilities": vulns,
            "ai_analysis": analysis,
            "exploit_attempts": exploits
        })

    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
        print(f"\n[+] Relatório JSON salvo em {output_path}")

    generate_report(results, config)