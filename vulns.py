import requests

def check_vulnerabilities(url, session=None):
    findings = []
    try:
        sess = session or requests
        resp = sess.get(url, timeout=5)

        # Header Security Check
        print(f"[*] Checando headers em: {url}")
        security_headers = ["Content-Security-Policy", "X-Frame-Options", "X-XSS-Protection"]
        for header in security_headers:
            if header not in resp.headers:
                findings.append(f"Header de segurança ausente: {header}")

        # XSS Test
        test_xss = url + "?q=<script>alert(1)</script>"
        test_resp = sess.get(test_xss, timeout=5)
        if "<script>alert(1)</script>" in test_resp.text:
            findings.append("Possível XSS")

        # SQLi Test (básico)
        test_sqli = url + "?id=1'"
        sqli_resp = sess.get(test_sqli, timeout=5)
        if any(err in sqli_resp.text.lower() for err in ["sql syntax", "mysql", "syntax error"]):
            findings.append("Possível SQL Injection")

    except Exception as e:
        findings.append(f"Erro: {e}")

    return findings