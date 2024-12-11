import os

# Diretório base onde as pastas dos meses já estão criadas
diretorio_base = "C:/Users/vitor/OneDrive/Repositórios/Estudo-Geral-"

# Loop para adicionar o arquivo Planejamento_semanal.md em cada semana já existente
for mes in range(1, 13):
    nome_pasta_mes = f"Mes_{str(mes).zfill(2)}"
    caminho_pasta_mes = os.path.join(diretorio_base, nome_pasta_mes)
    
    # Verifica se a pasta do mês existe
    if os.path.exists(caminho_pasta_mes):
        print(f"Iniciando para o mês: {nome_pasta_mes}")
        
        # Loop para percorrer as semanas dentro do mês
        for semana_num in range(1, 6):  # Assumindo até 5 semanas por mês
            nome_pasta_semana = f"Semana_{str(semana_num).zfill(2)}"
            caminho_pasta_semana = os.path.join(caminho_pasta_mes, nome_pasta_semana)
            
            # Verifica se a pasta da semana existe
            if os.path.exists(caminho_pasta_semana):
                print(f"  Pasta da semana encontrada: {nome_pasta_semana}")
                
                # Cria o arquivo Planejamento_semanal.md dentro de cada pasta de semana
                caminho_arquivo_semanal = os.path.join(caminho_pasta_semana, "Planejamento_Semanal.md")
                if not os.path.exists(caminho_arquivo_semanal):
                    with open(caminho_arquivo_semanal, "w") as arquivo_semanal:
                        arquivo_semanal.write(f"# Planejamento Semanal\n\n## *Este é o planejamento para a semana {str(semana_num).zfill(2)}.*\n")
                    print(f"     Criado o arquivo: Planejamento_semanal.md")
                else:
                    print(f"     O arquivo Planejamento_semanal.md já existe em {nome_pasta_semana}")
            else:
                print(f"  A pasta da semana {nome_pasta_semana} não foi encontrada. Pulando...")
    else:
        print(f"A pasta {nome_pasta_mes} não existe, pulando...")










