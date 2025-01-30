# Função para verificar se o corpo do e-mail contém palavras suspeitas de phishing
def verificar_phishing(mensagem):
    # Lista de palavras que indicam possíveis e-mails de phishing
    palavras_suspeitas = ["ganhe", "prêmio", "urgente", "desconto", "click",  "promoção"]
    
    # Variável para armazenar o resultado inicial
    resultado = "Seguro"
    
    # Verifica se alguma palavra suspeita está presente no corpo do e-mail
    for palavra in palavras_suspeitas:
        if palavra in mensagem.lower():  # Verifica se a palavra está no texto (sem diferenciar maiúsculas e minúsculas)
            resultado = "Phishing"
            break  # Sai do loop assim que encontrar a primeira palavra suspeita
    
    return resultado


# Leitura do corpo do e-mail
email_usuario = input()


# Chama a função e armazena o resultado
resultado = verificar_phishing(email_usuario)


# Exibe a classificação do e-mail
print(f"Classificação: {resultado}")
