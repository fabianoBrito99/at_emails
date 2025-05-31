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


### 🔐 Como gerar uma senha de aplicativo no Gmail:

#### Se tiver ativar o 2FA:
- Acesse:[app PassWord](https://myaccount.google.com/apppasswords)

- Se estiver com 2FA ativado, você verá uma tela para criar Senhas de app (escolha "Mail" e "Outro → Python").
- Gere uma senha de 16 caracteres para “Mail” com nome personalizado (ex: Automação Python)
- Use essa senha no campo `SMTP_SENHA` do `.env

#### Se não tiver ativado o 2FA:

1. Vá em [Google Security](https://myaccount.google.com/security)
2. Ative a verificação em duas etapas
3. Após isso, acesse a opção **Senhas de app**
4. Gere uma senha de 16 caracteres para “Mail” com nome personalizado (ex: Automação Python)
5. Use essa senha no campo `SMTP_SENHA` do `.env`

---

## 6. O que são funções em Python?

Funções são blocos de código reutilizáveis. Por exemplo:
#### Python
```python
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Maria")
```

- Simples, sem declarar tipo de dado, nem ponto e vírgula

#### C
```C:

#include <stdio.h>

void saudacao(char nome[]) {
    printf("Olá, %s!
", nome);
}

int main() {
    saudacao("Maria");
    return 0;
}
```

- Tipagem obrigatória, uso de ponto e vírgula, e função main()

#### Java
```Java:

public class Saudacao {
    public static void saudacao(String nome) {
        System.out.println("Olá, " + nome + "!");
    }

    public static void main(String[] args) {
        saudacao("Maria");
    }
}
```
- Uso de classes, métodos estáticos e sintaxe mais detalhada

#### C#
```C#
using System;

class Saudacao {
    static void Saudacao(string nome) {
        Console.WriteLine($"Olá, {nome}!");
    }

    static void Main() {
        Saudacao("Maria");
    }
}

```
- Uso de classes, métodos estáticos e sintaxe mais detalhada

#### Assembly
```Assembly
section .data
    msg db 'Olá, Maria!', 0xA   ; string + quebra de linha
    len equ $ - msg             ; comprimento da string

section .text
    global _start

_start:
    ; syscall write (stdout)
    mov edx, len        ; tamanho da mensagem
    mov ecx, msg        ; endereço da string
    mov ebx, 1          ; file descriptor (stdout)
    mov eax, 4          ; syscall número 4: sys_write
    int 0x80            ; chamada de sistema

    ; syscall exit
    mov eax, 1          ; syscall número 1: sys_exit
    xor ebx, ebx        ; código de saída 0
    int 0x80

```
### 🧾 O que isso faz:
- Define uma mensagem `"Olá, Maria!"` na seção de dados.

- Usa instruções para chamar o serviço do sistema operacional e escreve no terminal.

- Depois, termina o programa com `sys_exit`.

⚠️ Assembly é muito próximo do hardware e exige conhecimento de registradores (eax, ebx, etc.) e interrupções do sistema (int 0x80).


### ✅ Moral da comparação:

- Python: simples, direto, ideal para automações rápidas.

- C/Java/C#: mais verbosos, exigem estrutura, mas poderosos em aplicações maiores.

- Assembly: extremamente próximo do hardware, difícil de ler e escrever.
  


Funções deste projeto:

Funções são blocos de código reutilizáveis, que organizam e encapsulam comportamentos.

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

