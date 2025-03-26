# MaxMin Select

## Descrição do Projeto
Este projeto implementa o algoritmo **MaxMin Select** utilizando a técnica de **Divisão e Conquista**. O objetivo do algoritmo é encontrar simultaneamente o maior e o menor elemento de uma lista de números com um número reduzido de comparações.

A abordagem utilizada divide o problema em partes menores e resolve recursivamente, combinando os resultados para obter o menor e o maior número da lista com eficiência.

## Como Executar o Projeto
### Requisitos
- Python 3.x instalado

### Passos
1. Clone o repositório:
   ```sh
   git clone https://github.com/Davidlh80/MaxMinSelect.git
   ```
2. Execute o programa:
   ```sh
   python main.py
   ```
3. Insira os numeros separados por espaco quando solicitado.
4. O programa retornará o menor e o maior elemento da lista.

### Exemplo de Uso
```sh
Digite os numeros separados por espaco: 3 1 9 2 7 8 5 4 6
Menor elemento: 1, Maior elemento: 9
```

### Explicação do Código Linha a Linha
```python
# Função principal que encontra simultaneamente o menor e o maior elemento de um array
def max_min_select(arr):
    # Função auxiliar recursiva que implementa o algoritmo de Divisão e Conquista
    def recursive_max_min(arr, left, right):
        # Caso base: se houver apenas um elemento, ele é tanto o menor quanto o maior
        if left == right: 
            return arr[left], arr[left]
        # Caso base: se houver dois elementos, compara-os e retorna na ordem correta
        elif right - left == 1: 
            return (arr[left], arr[right]) if arr[left] < arr[right] else (arr[right], arr[left])
        
        # Divide a lista em duas partes
        mid = (left + right) // 2  
        
        # Chama recursivamente para a primeira metade
        min1, max1 = recursive_max_min(arr, left, mid)
        # Chama recursivamente para a segunda metade
        min2, max2 = recursive_max_min(arr, mid + 1, right)
        
        # Retorna o menor entre os mínimos e o maior entre os máximos encontrados
        return min(min1, min2), max(max1, max2) 
    
    # Chama a função recursiva passando os índices inicial e final
    return recursive_max_min(arr, 0, len(arr) - 1)

# Executa apenas se o script for rodado diretamente
if __name__ == "__main__":
    try:
        # Lê a entrada do usuário
        arr = list(map(int, input("Digite os numeros separados por espaco: ").split()))
        
        # Verifica se a lista está vazia
        if not arr:
            raise ValueError("A lista não pode ser vazia")
        
        # Chama a função para encontrar o menor e o maior valor
        min_val, max_val = max_min_select(arr)
        
        # Exibe os resultados
        print(f"Menor elemento: {min_val}, Maior elemento: {max_val}")
    
    # Captura erros de entrada inválida e exibe mensagem
    except ValueError as e:
        print(f"Erro: {e}")

```

## Análise do Algoritmo

### Estrutura Recursiva e Divisão do Problema

O algoritmo divide a lista original recursivamente ao meio, o que caracteriza a abordagem de **Divisão e Conquista**.

- **Divisão**: Cada chamada recursiva divide a lista ao meio, o que reduz o problema em partes menores.
- **Conquista**: Uma vez que a lista é dividida em sublistas de um ou dois elementos, o algoritmo resolve o problema diretamente.
- **Combinação**: O algoritmo combina as soluções parciais para fornecer a resposta final.

### Comparações Realizadas

Quando a lista é dividida em subproblemas menores, a base da recursão é alcançada quando a lista possui apenas um ou dois elementos. O algoritmo faz as seguintes comparações:

- **Para um único elemento**: Não há necessidade de comparação, já que ele é tanto o menor quanto o maior elemento.
- **Para dois elementos**: Realiza-se uma comparação direta para determinar qual é o menor e qual é o maior.
- **Para sublistas maiores**: A solução é obtida recursivamente, e o algoritmo então combina as soluções dos subproblemas, realizando mais comparações para determinar o menor valor entre os menores e o maior valor entre os maiores.

### Contagem de Operações
O algoritmo divide a lista ao meio recursivamente até obter sublistas de um ou dois elementos, onde realiza comparações diretas. Depois, combina os resultados escolhendo o menor e o maior entre os subproblemas.

O número total de comparações realizadas é aproximadamente **3n/2 - 2**, o que melhora a abordagem ingênua de **2n - 2** comparações.

### Complexidade Assintótica
A recorrência do algoritmo é dada por:
```math
T(n) = 2T(n/2) + O(1)
```

Aplicando o **Teorema Mestre**:
- **a = 2**, **b = 2**, **f(n) = O(1)**
- Calculamos **log_b(a) = log_2(2) = 1**
- Como f(n) = O(n^0) e p = 1, o caso 2 do Teorema Mestre se aplica, resultando em **O(n)**

Dessa forma, a complexidade do algoritmo é **O(n)**, garantindo eficiência em relação a métodos ingênuos.
