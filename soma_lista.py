def soma_lista(numeros):
    """
    Calcula a soma de todos os números em uma lista.
    
    :param numeros: Lista de números.
    :return: Soma dos números na lista.
    """
    if not all(isinstance(num, (int, float)) for num in numeros):
        raise ValueError("A lista deve conter apenas números.")
    return sum(numeros)
