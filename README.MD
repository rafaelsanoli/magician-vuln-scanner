# Magician Vulnerability Scanner

Este script realiza varreduras de vulnerabilidades em sites, buscando falhas como XSS, SQLi e outros problemas comuns. Ele também tenta realizar ataques controlados (como XSS e SQLi) e gera relatórios em formato JSON e HTML com análise de riscos.

## Requisitos

1. Python 3.x
2. Bibliotecas:
   - requests
   - beautifulsoup4
   - lxml
   - pyyaml
   - jinja2
   - openai (se necessário)
   - pyinstaller (para .exe)

Você pode instalar as dependências com o comando:
```bash
pip install -r requirements.txt
```

## Como Usar


Usando como script Python

    1. Clone o repositório ou baixe os arquivos.

    2. Instale as dependências.

    3. Execute o script com:

```bash
    python main.py
```

4. O script pedirá a URL do alvo, e depois iniciará a varredura.

## Gerar um arquivo .pyz]

Para criar um arquivo executável .pyz:

```bash
python -m zipapp . -o smart_vuln_scanner.pyz
```

## Gerar um arquivo .exe

1. Instale o PyInstaller:

```bash
pip install pyinstaller
```

2. Execute o comando:

```bash
pyinstaller --onefile --distpath . --workpath build --specpath . main.py
```
O arquivo .exe será gerado no diretório dist.

## Relatório
Após a varredura, o relatório será salvo em formato JSON e HTML.


## Funcionalidades

- **Rastreamento de Endpoints**: Descobre as páginas e recursos de um site.
- **Checagem de Vulnerabilidades**: Verifica as falhas comuns (XSS, SQLi, etc.).
- **Análise por IA**: Utiliza IA para detectar possíveis falhas.
- **Tentativas de Exploração**: Realiza testes automatizados para ver se é possível explorar vulnerabilidades.
- **Geração de Relatórios**: Criação de relatórios detalhados em JSON e HTML, com classificação de risco.

## Como Funciona

1. **Crawl**: O script faz um rastreamento do site e encontra os endpoints.
2. **Scan de Vulnerabilidades**: Verifica as falhas nos endpoints encontrados.
3. **Exploração**: Realiza tentativas de exploração controladas.
4. **Relatório**: Gera um relatório detalhado sobre as vulnerabilidades e a gravidade delas.

## Instalação

Clone o repositório e instale as dependências com o comando:

```bash
pip install -r requirements.txt
```

## Executando
Para executar o scanner, use o comando:

```bash
python main.py
```
## Contribuindo

1. Fork o repositório.

2. Crie uma branch para a sua feature (git checkout -b feature/fooBar).

3. Comite suas alterações (git commit -am 'Add some fooBar').

4. Faça o push para a branch (git push origin feature/fooBar).

5. Abra um pull request.