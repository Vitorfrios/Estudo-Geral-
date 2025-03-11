import os

# Estrutura de pastas e arquivos
estrutura = {
    "01_Comece_por_aqui": [
        "01_Seja_bem_vindo(a).py",
        "02_Como_adicionar_seu_certificado_no_LinkedIn.py",
        "03_Acesse_o_Plano_de_Estudos_V2.py"
    ],
    "02_Python_I_Introducao_ao_Python": [
        "01_Apresentacao_do_Modulo.py",
        "02_O_que_e_o_Python.py",
        "03_Caracteristicas.py",
        "04_Aplicabilidade_da_Linguagem.py",
        "05_Dicas_sobre_o_Curso.py",
        "06_Instalando_o_Python_Windows.py",
        "07_Instalando_o_Python_Linux.py",
        "08_Instalando_o_Vs_Code.py",
        "09_Criando_o_Primeiro_Programa.py",
        "10_Entendendo_os_Tipos_de_Dados.py",
        "11_Quiz_1_Fundamentos_Python.py",
        "12_Lendo_Dados_com_o_Input.py",
        "13_Aprendendo_a_Concatenar_Valores.py",
        "14_Utilizando_Operadores_Aritmeticos_e_Relacionais.py",
        "15_Exercicio_1_Antecessor_e_Sucessor_Numero_Media_Notas.py",
        "16_Resolucao_1_Antecessor_e_Sucessor_Numero_Media_Notas.py",
        "17_Detalhando_a_Utilizacao_de_Strings.py",
        "18_Utilizando_Operacoes_com_Strings.py",
        "19_Gerando_Substrings_a_partir_de_uma_String.py",
        "20_Principais_Metodos_em_Strings.py",
        "21_Exercicio_2_Substituindo_caractere_repetido_Gerando_strings.py",
        "22_Resolucao_2_Substituindo_caractere_repetido_Gerando_strings.py",
        "23_Utilizando_o_Tipo_de_Dado_Lista.py",
        "24_Utilizando_Principais_Metodos_da_Listas.py",
        "25_Utilizando_o_Tipo_de_Dado_Tupla.py",
        "26_Utilizando_o_Tipo_de_Dado_Set.py",
        "27_Utilizando_o_Tipo_de_Dado_Dicionario.py",
        "28_Utilizando_Dicionarios_Aninhados.py",
        "29_Quizz_2_Collections.py",
        "30_Utilizando_Condicoes_com_If_Else.py",
        "31_Utilizando_Condicoes_com_If_Elif_e_Else.py",
        "32_Exercicio_3_Calculo_Distancia_Aumento_Funcionario.py",
        "33_Resolucao_3_Calculo_Distancia_Aumento_Funcionario.py",
        "34_Utilizando_o_Laco_de_Repeticao_For.py",
        "35_Utilizando_o_Laco_de_Repeticao_While.py",
        "36_Utilizando_List_Comprehension.py",
        "37_Exercicio_4_Lancamento_Foguete_Tabuada_de_numeros.py",
        "38_Resolucao_4_Lancamento_Foguete_Tabuada_de_numeros.py",
        "39_Utilizando_Funcoes.py",
        "40_Utilizando_Funcao_com_Argumentos.py",
        "41_Utilizando_Funcao_Recursiva.py",
        "42_Utilizando_Funcao_com_Args_e_Kwargs.py",
        "43_Funcao_Lambda.py",
        "44_Exercicio_5_Conta_letras_maiusculas_e_minusculas_Verifica_numero_par_impar.py",
        "45_Resolucao_5_Conta_letras_maiusculas_e_minusculas_Verifica_numero_par_impar.py",
        "46_Exercicio_Final_Gerenciamento_jogadores_e_times.py",
        "47_Resolucao_Exercicio_Final_Parte_1.py",
        "48_Resolucao_Exercicio_Final_Parte_2.py",
        "49_Encerramento.py",
        "50_Prova_Final_Com_Certificado.py"
    ],
    "03_Python_II_Modulos_e_PIP": [
        "01_Apresentacao_do_Modulo.py",
        "02_Motivacao_para_usar_Modulos.py",
        "03_O_que_e_um_Modulo.py",
        "04_Vantagens_de_usar_Modulos.py",
        "05_Criando_o_Primeiro_Modulo.py",
        "06_Exercicio_1_Modulo_Strings.py",
        "07_Resolucao_1_Modulo_Strings.py",
        "08_Modulos_Builtin.py",
        "09_Modulo_OS.py",
        "10_Exercicio_2_Agendamento_Desligamento.py",
        "11_Resolucao_2_Agendamento_Desligamento.py",
        "12_Modulo_HTTPServer.py",
        "13_Modulo_Webbrowser.py",
        "14_Modulo_Math.py",
        "15_Modulo_Statistic.py",
        "16_Modulo_Regex_I.py",
        "17_Exercicio_3_Verificar_conteudo_da_String.py",
        "18_Resolucao_3_Verificar_conteudo_da_String.py",
        "19_Modulo_Hashlib.py",
        "20_Modulo_Json.py",
        "21_Modulo_Collections.py",
        "22_Modulo_Random.py",
        "23_Exercicio_4_Advinhe_o_numero.py",
        "24_Resolucao_4_Advinhe_o_numero.py",
        "25_Modulo_Tkinter.py",
        "26_O_que_e_um_Gerenciador_de_Dependencias.py",
        "27_Conhecendo_o_Repositorio_Pypi.py",
        "28_Criando_Ambiente_Virtual_de_Desenvolvimento.py",
        "29_Comandos_Pip.py",
        "30_Conhecendo_a_biblioteca_Sketchpy.py",
        "31_Gerando_Instalador_App.py",
        "32_Encerramento.py",
        "33_Prova_Final_Com_Certificado.py"
    ],
    "04_Python_III_POO": [
        "01_Apresentacao_do_Modulo.py",
        "02_O_que_e_POO.py",
        "03_Criando_a_primeira_classe.py",
        "04_Instanciando_a_Classe.py",
        "05_Utilizando_construtor_e_str.py",
        "06_Utilizando_metodos.py",
        "07_Exercicio_1.py",
        "08_Resolucao_1.py",
        "09_Exercicio_2.py",
        "10_Resolucao_2.py",
        "11_Utilizando_Variavel_de_Classe.py",
        "12_Utilizando_Metodo_de_Classe.py",
        "13_Utilizando_Metodo_Estatico.py",
        "14_Compreendendo_o_Encapsulamento.py",
        "15_Fornecendo_Maior_Seguranca_com_Encapsulamento.py",
        "16_Metodos_Getter_e_Setter.py",
        "17_Quiz_1.py",
        "18_Compreendendo_a_Heranca.py",
        "19_Utilizando_a_Heranca_na_Pratica.py",
        "20_Utilizando_Metodo_Super.py",
        "21_Utilizando_Polimorfismo.py",
        "22_Utilizando_Composicao.py",
        "23_Exercicio_3.py",
        "24_Resolucao_3.py",
        "25_Compreendendo_o_Decorators.py",
        "26_Criando_Decorators.py",
        "27_Utilizando_o_Decorator_Property.py",
        "28_Exercicio_Final.py",
        "29_Resolucao_Exercicio_Final.py",
        "30_Encerramento.py",
        "31_Prova_Final_Com_Certificado.py"
    ]
}

# Função para criar pastas e arquivos
def criar_estrutura(estrutura):
    for pasta, arquivos in estrutura.items():
        os.makedirs(pasta, exist_ok=True)
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(pasta, arquivo)
            with open(caminho_arquivo, 'w') as f:
                f.write("# Arquivo criado automaticamente")

# Executar a função para criar a estrutura
criar_estrutura(estrutura)

print("Estrutura de pastas e arquivos criada com sucesso!")