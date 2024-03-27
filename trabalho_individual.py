
registros_candidatos = []

# Loop para cadastrar os candidatos
while True:
    candidato = input("Digite o nome do candidato (ou digite 'sair' para encerrar): ")
    resultadoString = 'ex_tx_px_sx'
    if candidato.lower() == 'sair':
        break

    # Validar e capturar valores para entrevista, teste teórico, teste prático, soft skills e média
    while True:
        try:
            entrevista = int(input("Digite o valor da entrevista (apenas números inteiros): "))
            teste_teorico = int(input("Digite o valor do teste teorico (apenas números inteiros): "))
            teste_pratico = int(input("Digite o valor do teste pratico (apenas números inteiros): "))
            soft_skills = int(input("Digite o valor do soft_skills do candidato (apenas números inteiros): "))
            break
        except ValueError:
            print("Por favor, digite apenas números inteiros.")

    # Adicionar o registro à lista de registros de candidatos
    registro = f"Candidato: {candidato}, Entrevista: {entrevista}, Teste Teórico: {teste_teorico}, Teste Prático: {teste_pratico}, Soft Skills: {soft_skills} "
    registros_candidatos.append(registro)
    print (f"e{entrevista}_t{teste_teorico}_p{teste_pratico}_s{soft_skills}")

    parar = input('Deseja adicionar outro candidato? (s/n): ')
    if parar.lower() == 'n':
        break

# Exibir todos os registros de candidatos
print("\nRegistros de candidatos:")
for registro in registros_candidatos:
    print(registro)
