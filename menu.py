import os
from scanner import run_scan
from utils import load_config, setup_logging


def show_menu():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("""
          
 ██████ ██    ██ ███    ██ ██   ██ 
██       ██  ██  ████   ██  ██ ██  
██        ████   ██ ██  ██   ███   
██         ██    ██  ██ ██  ██ ██  
 ██████    ██    ██   ████ ██   ██ 
    █                               
                                   
          
 ██████  ██████   ██████  
██            ██ ██       
███████   █████  ███████  
██    ██      ██ ██    ██ 
 ██████  ██████   ██████  
                                 
                                                          
                                                                                      
          [1] Iniciar varredura
          [2] Exibir ajuda
          [3] Sair
    """)
    choice = input("Escolha uma opção: ")

    if choice == '1':
        target = input("\nDigite a URL alvo (ex: https://exemplo.com): ")
        config_path = "config.yaml"
        output_path = "report.json"

        config = load_config(config_path)
        setup_logging()
        run_scan(target, config, output_path)

        input("\n[!] Pressione ENTER para voltar ao menu.")
        show_menu()

    elif choice == '2':
        print("""
Este scanner inteligente realiza:
- Rastreamento de endpoints
- Checagem de vulnerabilidades comuns
- Análise assistida por IA
- Tentativas automatizadas de exploração
- Geração de relatório com classificação de risco

Use a opção 1 para iniciar a análise em um site de sua escolha.
        """)
        input("\n[!] Pressione ENTER para voltar ao menu.")
        show_menu()

    elif choice == '3':
        print("Saindo...")
        exit()

    else:
        input("Opção inválida. Pressione ENTER para tentar novamente.")
        show_menu()