#Função para determinar o tipo do input (mantida igual)
def determinar_tipo(valor):
    try:
        return int(valor)
    except ValueError:
        try:
            return float(valor)
        except ValueError:
            if valor.lower() in ['true', 'false']:
                return valor.lower() == 'true'
            else:
                return valor

#Parte 1 e 2: Input único e mostrar tipo
entrada = input("Digite algo: ")
convertido = determinar_tipo(entrada)
print(f"\nVocê digitou: {convertido}, Tipo: {type(convertido).__name__}\n")

#Parte 3: Lista de inputs com sublistas
print("Digite elementos para a lista (use 'lista' para criar sublista, 'fim' para encerrá-la, 'sair' para terminar):")
lista_principal = []
sublista_atual = None

while True:
    elemento = input("> ").strip()
    if elemento.lower() == 'sair':
        break
    elif elemento.lower() == 'lista':
        sublista_atual = []
    elif elemento.lower() == 'fim':
        if sublista_atual is not None:
            lista_principal.append(sublista_atual)
            sublista_atual = None
    else:
        item_convertido = determinar_tipo(elemento)
        if sublista_atual is not None:
            sublista_atual.append(item_convertido)
        else:
            lista_principal.append(item_convertido)

print("\nLista criada:", lista_principal)

#Parte 4: Codificação ajustada (sem vírgula no float)
def codificar(lista, is_sublist=False):
    elementos = []
    for item in lista:
        tipo = type(item).__name__
        if tipo == 'str':
            parte = f"str: '{item}'"
        elif tipo == 'int':
            parte = f"int: {item}"
        elif tipo == 'float':
            parte = f"float: {item}"
        elif tipo == 'bool':
            parte = f"bool: {item}"
        elif tipo == 'list':
            sub = codificar(item, is_sublist=True)
            parte = f"list({sub}]"
        else:
            parte = str(item)
        
        if not is_sublist and tipo != 'list':
            parte = f"({parte})"
        
        elementos.append(parte)
    
    return ", ".join(elementos)

#Parte 5: Decodificação ajustada (incorpora elementos da sublista)
def decodificar(string, is_sublist=False):
    import re
    lista = []
    
    if is_sublist:
        padrao = re.compile(r"\s*(int|float|str|bool):\s*((?:'[^']*'|[^,]+))")
    else:
        padrao = re.compile(r"\s*(?:\((int|float|str|bool):\s*((?:'[^']*'|[^)]+))\)|list\((.*?)\])")
    
    pos = 0
    while pos < len(string):
        match = padrao.match(string, pos)
        if not match:
            pos += 1
            continue
        
        if is_sublist:
            tipo, valor = match.groups()
            sublista = None
        else:
            tipo_main, valor_main, sublista = match.groups()
            tipo = tipo_main if tipo_main else None
            valor = valor_main if valor_main else None
        
        if sublista:
            elementos_sublista = decodificar(sublista, is_sublist=True)
            lista.extend(elementos_sublista) 
            pos = match.end()
        elif tipo:
            if tipo == 'str':
                lista.append(valor.strip("'"))
            elif tipo == 'int':
                lista.append(int(valor))
            elif tipo == 'float':
                lista.append(float(valor))
            elif tipo == 'bool':
                lista.append(valor == 'True')
            pos = match.end()
        else:
            pos += 1
    
    return lista

codificado = codificar(lista_principal)
print("\nString codificada:\n", codificado)

decodificado = decodificar(codificado)
print("\nLista decodificada:\n", decodificado)