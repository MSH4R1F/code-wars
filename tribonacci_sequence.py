def tribonacci(signature, n):
    if n == 0:
        return []
    if n < 3:
        return [signature[x] for x in range(n)]
    for i in range(3,n):
        signature.append(signature[i-3]+signature[i-2]+signature[i-1])
    return signature
