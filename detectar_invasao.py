# Função para detectar tentativas de invasão em registros de log
def detectar_invasao(registros):
    # Variáveis para rastrear o ID do usuário atual e suas falhas consecutivas
    usuario_atual = None
    tentativas_consecutivas = 0
    invasor_detectado = None


    # Percorre cada registro de log
    for registro in registros:
        usuario, status = registro.split(":")  # Separa o id_usuario e o status


        # Verifica se o usuário atual é o mesmo da iteração anterior
        if usuario == usuario_atual:
            if status == "falha":
                tentativas_consecutivas += 1
            else:
                tentativas_consecutivas = 0  # Se for sucesso, reinicia o contador de falhas
        else:
            # Se mudar de usuário, verifica se o usuário anterior teve mais de 3 falhas consecutivas
            if usuario_atual and tentativas_consecutivas > 3:
                invasor_detectado = usuario_atual


            # Atualiza para o novo usuário e reinicia a contagem de tentativas falhas
            usuario_atual = usuario
            tentativas_consecutivas = 1 if status == "falha" else 0  # Reseta contagem


    # Após o loop, verifica se o último usuário teve mais de 3 tentativas de falha
    if usuario_atual and tentativas_consecutivas > 3:
        invasor_detectado = usuario_atual


    # Retorna o resultado final
    return invasor_detectado if invasor_detectado else "Nenhum invasor detectado"


# Função principal para executar o programa
def main():
    # Solicita ao usuário que insira os registros de log
    entrada = input()
    
    # Converte a entrada para uma lista de registros
    registros = [registro.strip() for registro in entrada.split(",")]


    # Chama a função para detectar tentativas de invasão
    resultado = detectar_invasao(registros)


    # Imprime o resultado
    print(resultado)


# Chama a função principal para executar o programa
if __name__ == "__main__":
    main()
