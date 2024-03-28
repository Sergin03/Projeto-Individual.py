# Lista para armazenar os registros dos candidatos
registros_candidatos = []

print('\n')
print('Escolha uma opção abaixo: ')
print('\n')
opcao = input(' 1 - Cadastrar Candidato \n 2 - Exibir Nota \n 3 - Sair\n')
print('\n\n')

while opcao == "1" or opcao == "2":
    if opcao == "1":

        try:
            entrevista = input("Digite a nota da entrevista (apenas números): ")
            teste_teorico = input("Digite a nota do teste teorico (apenas números): ")
            teste_pratico = input("Digite a nota do teste pratico (apenas números): ")
            soft_skills = input("Digite a nota do soft_skills do candidato (apenas números): ")

        except ValueError:
            print("Por favor, digite apenas números inteiros.")

        registro = {
            'Entrevista': entrevista,
            'Teste Teórico': teste_teorico,
            'Teste Prático': teste_pratico,
            'Soft Skills': soft_skills,
        }
        registros_candidatos.append(registro)
        print(f"e{entrevista}_t{teste_teorico}_p{teste_pratico}_s{soft_skills}")

        opcao = input(' 1 - Cadastrar Candidato \n 2 - Exibir Nota \n 3 - Sair\n')
    elif opcao =='2':

        nota_entrevista = int(input("Digite a nota mínima na entrevista: "))
        nota_teste_teorico = int(input("Digite a nota mínima no teste teórico: "))
        nota_teste_pratico = int(input("Digite a nota mínima no teste prático: "))
        nota_soft_skills = int(input("Digite a nota mínima em soft skills: "))
        
        for registro in registros_candidatos:
            nota_entrevista_candidato = int(registro['Entrevista'])
            nota_teste_teorico_candidato = int(registro['Teste Teórico'])
            nota_teste_pratico_candidato = int(registro['Teste Prático'])
            nota_soft_skills_candidato = int(registro['Soft Skills'])
            4
            if (nota_entrevista_candidato >= nota_entrevista and
                nota_teste_teorico_candidato >= nota_teste_teorico and
                nota_teste_pratico_candidato >= nota_teste_pratico and
                nota_soft_skills_candidato >= nota_soft_skills):
                
                print(f"e{nota_entrevista_candidato}_t{nota_teste_teorico_candidato}_p{nota_teste_pratico_candidato}_s{nota_soft_skills_candidato}")
        opcao = input(' 1 - Cadastrar Candidato \n 2 - Exibir Nota \n 3 - Sair\n')
