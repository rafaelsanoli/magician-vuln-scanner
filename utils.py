import yaml
import logging
import os
import requests

def load_config(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def call_openai(prompt, config):
    if config.get("use_openai", False):
        import openai
        openai.api_key = config.get("openai_api_key")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um especialista em segurança web."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    else:
        return "[IA LOCAL AQUI] Integração com modelo local ainda não implementada."