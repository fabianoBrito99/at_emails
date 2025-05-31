import os
import pandas as pd
from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv
from .registro import carregar_registro, salvar_registro

# Carregar variáveis de ambiente
load_dotenv()

SMTP_SERVIDOR = os.getenv("SMTP_SERVIDOR")
SMTP_PORTA = int(os.getenv("SMTP_PORTA"))
SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_SENHA = os.getenv("SMTP_SENHA")

PASTA_BASE = 'emails'
CAMINHO_INDEX = 'config/index_dlo.xlsx'
CAMINHO_REGISTRO = 'registro/emails_enviados.xlsx'

def enviar_email(destinatario, assunto, corpo, lista_anexos):
    msg = EmailMessage()
    msg['Subject'] = assunto
    msg['From'] = SMTP_EMAIL
    msg['To'] = destinatario
    msg.set_content(corpo)

    for anexo_path in lista_anexos:
        with open(anexo_path, 'rb') as f:
            msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename=os.path.basename(anexo_path))

    with smtplib.SMTP(SMTP_SERVIDOR, SMTP_PORTA) as smtp:
        smtp.starttls()
        smtp.login(SMTP_EMAIL, SMTP_SENHA)
        smtp.send_message(msg)

def processar_emails():
    index_df = pd.read_excel(CAMINHO_INDEX, dtype=str)
    index_agencia_email = dict(zip(index_df['agencia'], index_df['email']))
    registro_df = carregar_registro(CAMINHO_REGISTRO)

    for mes in os.listdir(PASTA_BASE):
        pasta_mes = os.path.join(PASTA_BASE, mes)
        if not os.path.isdir(pasta_mes):
            continue

        arquivos_por_agencia = {}
        for arquivo in os.listdir(pasta_mes):
            if not arquivo.endswith('.pdf'):
                continue

            agencia = arquivo.split('_')[0]
            if ((registro_df['mes'] == mes) & (registro_df['agencia'] == agencia) & (registro_df['arquivo'] == arquivo)).any():
                continue

            arquivos_por_agencia.setdefault(agencia, []).append(os.path.join(pasta_mes, arquivo))

        for agencia, lista_anexos in arquivos_por_agencia.items():
            email_destino = index_agencia_email.get(agencia)
            if not email_destino:
                print(f'❌ Agência {agencia} não encontrada.')
                continue

            assunto = f'TESTE Documento(s) DLO - Agência {agencia} - {mes}'
            corpo = f'Prezados,\n\nSegue(m) em anexo o(s) documento(s) DLO da agência {agencia} referente ao mês {mes}.\n\nAtenciosamente,\nEquipe Automatizada'

            try:
                enviar_email(email_destino, assunto, corpo, lista_anexos)
                for anexo in lista_anexos:
                    registro_df.loc[len(registro_df)] = [mes, agencia, os.path.basename(anexo)]
                print(f'✅ E-mail enviado para {email_destino} com {len(lista_anexos)} anexo(s).')
            except Exception as e:
                print(f'❌ Erro ao enviar para {agencia}: {e}')

    salvar_registro(CAMINHO_REGISTRO, registro_df)
