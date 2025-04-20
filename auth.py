import requests

def authenticate(base_url, config):
    sess = requests.Session()
    auth = config.get("auth", {})
    if not auth.get("enabled", False):
        return sess

    login_url = auth.get("login_url")
    method = auth.get("method", "post").lower()
    data = auth.get("data", {})
    headers = auth.get("headers", {})

    try:
        if method == "post":
            resp = sess.post(login_url, data=data, headers=headers)
        else:
            resp = sess.get(login_url, params=data, headers=headers)
        if resp.status_code == 200:
            print("[+] Autenticação realizada com sucesso!")
        else:
            print(f"[!] Falha na autenticação: {resp.status_code}")
    except Exception as e:
        print(f"[!] Erro durante autenticação: {e}")

    return sess

