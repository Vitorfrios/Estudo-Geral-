import os
import calendar
from datetime import date, timedelta

# Diretório base onde as pastas dos meses já estão criadas
diretorio_base = "C:/Users/vitor/OneDrive/Repositórios/Estudo-Geral-"

# Função para calcular as semanas e dias de um mês
def criar_semanas_e_dias(mes, ano=2025):
    # Começa o mês em uma data específica
    primeiro_dia = date(ano, mes, 1)
    
    # Calcula o último dia do mês
    ultimo_dia = date(ano, mes, calendar.monthrange(ano, mes)[1])
    
    # Define a semana de início
    semana_atual = 1
    dia_atual = primeiro_dia
    semanas = []

    # Enquanto não atingir o último dia do mês
    while dia_atual <= ultimo_dia:
        semana = []
        # Preenche a semana com os dias do mês
        for i in range(7):
            if dia_atual <= ultimo_dia:
                semana.append(dia_atual)
                dia_atual += timedelta(days=1)
        semanas.append(semana)
    return semanas

# Loop para criar a estrutura de semanas e dias dentro de cada mês
for mes in range(1, 13):
    nome_pasta_mes = f"Mes_{str(mes).zfill(2)}"
    caminho_pasta_mes = os.path.join(diretorio_base, nome_pasta_mes)
    
    # Verifica se a pasta do mês existe
    if os.path.exists(caminho_pasta_mes):
        print(f"Iniciando para o mês: {nome_pasta_mes}")

        # Cria as semanas e dias baseados no mês
        semanas = criar_semanas_e_dias(mes)
        
        # Loop para criar as semanas
        for semana_num, semana in enumerate(semanas, 1):
            nome_pasta_semana = f"Semana_{str(semana_num).zfill(2)}"
            caminho_pasta_semana = os.path.join(caminho_pasta_mes, nome_pasta_semana)
            
            # Cria a pasta da semana se não existir
            if not os.path.exists(caminho_pasta_semana):
                os.makedirs(caminho_pasta_semana)
                print(f"  Criada a pasta: {nome_pasta_semana}")
            
            # Loop para criar os dias da semana
            for dia in semana:
                nome_pasta_dia = f"Dia_{str(dia.day).zfill(2)}"
                caminho_pasta_dia = os.path.join(caminho_pasta_semana, nome_pasta_dia)
                
                # Cria a pasta do dia se não existir
                if not os.path.exists(caminho_pasta_dia):
                    os.makedirs(caminho_pasta_dia)
                    print(f"    Criada a pasta: {nome_pasta_dia}")

                # Cria o arquivo Planejamento_do_Dia_XX.md dentro de cada pasta de dia
                caminho_arquivo_md = os.path.join(caminho_pasta_dia, f"Planejamento_do_Dia_{str(dia.day).zfill(2)}.md")
                with open(caminho_arquivo_md, "w") as arquivo_md:
                    arquivo_md.write(f"# Planejamento do Dia {str(dia.day).zfill(2)}\n\n## *Este é o planejamento do dia {str(dia.day).zfill(2)}.*")
                print(f"     Criado o arquivo: Planejamento_do_Dia_{str(dia.day).zfill(2)}.md")
    else:
        print(f"A pasta {nome_pasta_mes} não existe, pulando...")
