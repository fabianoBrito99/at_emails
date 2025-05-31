# Automatização de Envios de E-mails com Anexos por Agência

## Objetivo do Projeto
Este projeto automatiza o envio de arquivos PDF para agências financeiras via e-mail, com controle de envio mensal e segurança de credenciais. É ideal para usuários que precisam despachar documentos mensais como DLOs, mas não têm experiência com programação.

---

## 1. O que é o Python?
O **Python** é uma linguagem de programação considerada "fácil" de aprender por sua simples sintaxes e por ser uma linguagem de auto nivel(mais proxima do ser humano), linguagens de baixo nivel como C, Java... são de baixo nivel mais proxima do computador e muito usada para automação de tarefas, análise de dados, inteligência artificial e muito mais.

### ✅ Vantagens do Python:
- Simples e intuitivo
- Muito bem documentado
- Possui milhares de bibliotecas prontas para uso

---

## 2. O que é uma biblioteca Python?
Bibliotecas são pacotes prontos com funções e recursos específicos. Por exemplo:
- `pandas`: manipula planilhas e tabelas de dados
- `smtplib`: envia e-mails
- `email.message`: constrói mensagens de e-mail
- `openpyxl`: trabalha com arquivos `.xlsx`

---

## 3. Estrutura do Projeto
Essa estrutura pode varear conforme sua nescessidade, isso tudo poderia ser executado em um script só mas por boa pratica sempre separe os script por facilitar o encontro de erros e a execução ser mais fluida
```
email_automacao/
├── .env                          # Arquivo oculto com credenciais seguras
├── main.py                      # Arquivo principal que executa a automação
├── config/
│   └── index_dlo.xlsx           # Planilha com agência e e-mail
├── registro/
│   └── emails_enviados.xlsx     # Controle dos arquivos já enviados
├── emails/
│   └── 2025-05/
│       ├── 0002_dlo-1.pdf
│       └── ...
├── modules/
    ├── envio.py                 # Responsável por enviar os e-mails
    └── registro.py              # Controle de registros enviados
```

---

## 4. Instalação do Python e Bibliotecas

### a) Instalar o Python:
Caso não tenha o Python, você provavelmente vai ter que abrir um chamado para a instalação dele
Baixe e instale em: https://www.python.org/downloads/

### b) Instalar bibliotecas:
Abra o terminal e execute:
```bash
pip install pandas openpyxl python-dotenv
```

---

## 5. O que é uma Variável de Ambiente?

Uma variável de ambiente é um dado sensível (como senhas) que não deve ser exposto no código. Guardamos isso no arquivo `.env`.

### Exemplo de `.env` seguro:
```env
SMTP_SERVIDOR=smtp.gmail.com
SMTP_PORTA=587
SMTP_EMAIL=seuemail@gmail.com
SMTP_SENHA=senha_de_app_segura
```

Nunca envie esse arquivo para o GitHub! Coloque ele no `.gitignore`.

---

## 6. O que são funções em Python?

Funções são blocos de código reutilizáveis. Por exemplo:
```python
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Maria")
```

coloque exemplo da função, e explique elas...

Neste projeto, temos funções como:
- `processar_emails()`
- `enviar_email()`
- `carregar_registro()`

---

## 7. Como funciona o `main.py`

O `main.py` apenas chama a função principal:
```python
from modules.envio import processar_emails

if __name__ == "__main__":
    processar_emails()
```

---

## 8. Como agendar a execução automaticamente (cron)

### Windows:
Use o **Agendador de Tarefas** para rodar `python main.py` de hora em hora.

### Linux/Mac:
Edite o `crontab`:
```bash
crontab -e
```
E adicione:
```
0 * * * * /usr/bin/python3 /caminho/para/email_automacao/main.py
```

---

## 9. Como saber se os e-mails foram enviados?

- O script exibe mensagens no terminal:
```
✅ E-mail enviado para agencia0027@exemplo.com com 2 anexo(s).
```
- O arquivo `registro/emails_enviados.xlsx` mostra quais já foram enviados.

---

## 10. Contribuições
Este projeto é voltado para facilitar tarefas repetitivas e pode ser expandido para enviar outros tipos de relatórios, integrar com bancos de dados, etc.

---

## 📈 Contato
Criado para fins educacionais e automatização corporativa interna. Para melhorias, contribuições ou dúvidas, entre em contato com o desenvolvedor do sistema.
