def max_min_select(arr):
    def recursive_max_min(arr, left, right):
        if left == right: 
            return arr[left], arr[left]
        elif right - left == 1: 
            return (arr[left], arr[right]) if arr[left] < arr[right] else (arr[right], arr[left])
        
        mid = (left + right) // 2  
        min1, max1 = recursive_max_min(arr, left, mid)
        min2, max2 = recursive_max_min(arr, mid + 1, right)
        
        return min(min1, min2), max(max1, max2) 
    
    return recursive_max_min(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    try:
        arr = list(map(int, input("Digite os numeros separados por espaco: ").split()))
        if not arr:
            raise ValueError("A lista não pode ser vazia")
        min_val, max_val = max_min_select(arr)
        print(f"Menor elemento: {min_val}, Maior elemento: {max_val}")
    except ValueError as e:
        print(f"Erro: {e}")
