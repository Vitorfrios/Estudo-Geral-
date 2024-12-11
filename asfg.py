import os

# Diretório base onde as pastas dos meses já estão criadas
diretorio_base = "C:/Users/vitor/OneDrive/Repositórios/Estudo-Geral-"

# Loop para criar a estrutura de semanas e dias dentro de cada mês
for mes in range(1, 13):
    nome_pasta_mes = f"Mes_{str(mes).zfill(2)}"
    caminho_pasta_mes = os.path.join(diretorio_base, nome_pasta_mes)
    
    # Verifica se a pasta do mês existe
    if os.path.exists(caminho_pasta_mes):
        print(f"Iniciando para o mês: {nome_pasta_mes}")

        # Loop para criar as semanas do mês (Semana_01 até Semana_04)
        for semana in range(1, 5):
            nome_pasta_semana = f"Sema_{str(semana).zfill(2)}"
            caminho_pasta_semana = os.path.join(caminho_pasta_mes, nome_pasta_semana)
            
            # Cria a pasta da semana se não existir
            if not os.path.exists(caminho_pasta_semana):
                os.makedirs(caminho_pasta_semana)
                print(f"  Criada a pasta: {nome_pasta_semana}")
            
            # Loop para criar os dias da semana (Dia_01 até Dia_07)
            for dia in range(1, 8):
                nome_pasta_dia = f"Dia_{str(dia).zfill(2)}"
                caminho_pasta_dia = os.path.join(caminho_pasta_semana, nome_pasta_dia)
                
                # Cria a pasta do dia se não existir
                if not os.path.exists(caminho_pasta_dia):
                    os.makedirs(caminho_pasta_dia)
                    print(f"    Criada a pasta: {nome_pasta_dia}")

                # Cria o arquivo Planejamento_do_Dia_XX.md dentro de cada pasta de dia
                caminho_arquivo_md = os.path.join(caminho_pasta_dia, f"Planejamento_do_Dia_{str(dia).zfill(2)}.md")
                with open(caminho_arquivo_md, "w") as arquivo_md:
                    arquivo_md.write(f"# Planejamento do Dia {str(dia).zfill(2)}\n\nEste é o planejamento do dia {str(dia).zfill(2)}.")
                print(f"     Criado o arquivo: Planejamento_do_Dia_{str(dia).zfill(2)}.md")
    else:
        print(f"A pasta {nome_pasta_mes} não existe, pulando...")
