import requests
import json
import os
from utils import call_openai


def analyze_with_ai(url, config, session=None):
    try:
        sess = session or requests
        resp = sess.get(url, timeout=config.get("timeout", 5))
        prompt = f"""
Analise a seguinte resposta HTTP do ponto de vista de segurança. Identifique falhas potenciais, headers ausentes, práticas ruins, e sugira melhorias:

URL: {url}

Headers:
{json.dumps(dict(resp.headers), indent=2)}

Body:
{resp.text[:2000]}  # Limitando o tamanho
"""
        result = call_openai(prompt, config)
        return result

    except Exception as e:
        return f"Erro ao analisar com IA: {e}"
