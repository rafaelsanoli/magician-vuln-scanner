import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

visited = set()

def crawl_site(url, config, session=None, depth=0, max_depth=2):
    if depth > max_depth or url in visited:
        return []
    visited.add(url)
    endpoints = [url]

    try:
        headers = {"User-Agent": config.get("user_agent", "SmartVulnScanner/1.0")}
        sess = session or requests
        resp = sess.get(url, headers=headers, timeout=config.get("timeout", 5))
        soup = BeautifulSoup(resp.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = urljoin(url, link['href'])
            if same_domain(url, href):
                endpoints += crawl_site(href, config, session, depth + 1, max_depth)
    except Exception as e:
        print(f"[!] Erro ao acessar {url}: {e}")

    return list(set(endpoints))

def same_domain(base, target):
    return urlparse(base).netloc == urlparse(target).netloc
