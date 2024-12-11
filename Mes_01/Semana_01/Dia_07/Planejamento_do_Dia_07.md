# **Dia 07 de Janeiro - Planejamento de Estudo**

## **Python (2h)**

### **Objetivo**: Prática com arquivos e manipulação de dados.

### **Tópicos**:
- **Leitura e Escrita de Arquivos**:
  - Abertura de arquivos (`open()`).
  - Leitura de arquivos (`read()`, `readlines()`).
  - Escrita em arquivos (`write()`, `writelines()`).

### **Prática**:
- Criar um programa que leia um arquivo de texto e conte o número de palavras.
  ```python
  with open('exemplo.txt', 'r') as file:
      conteudo = file.read()
      palavras = conteudo.split()
      print(f"Total de palavras: {len(palavras)}")
  ```

- Criar um programa que escreva uma lista de números em um arquivo.
  ```python
  numeros = [1, 2, 3, 4, 5]
  with open('numeros.txt', 'w') as file:
      for num in numeros:
          file.write(f"{num}\n")
  ```

---

## **Matemática (2h)**

### **Objetivo**: Reforçar os conceitos de derivadas.



### **Tópicos**:
- **Derivadas**:
  - Revisão das regras de derivação.
  - Aplicações de derivadas em problemas de otimização.

### **Prática**:
- Resolver problemas de otimização simples, como maximizar ou minimizar uma função.
  - Exemplo: Maximizar a função \( f(x) = -x^2 + 4x \).

---
