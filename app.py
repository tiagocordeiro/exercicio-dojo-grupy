nomes_descendencia = ["neto", "filho", "junior"]
nomes_ligacao = ["de", "da", "dos"]


def formata_autor(nome):
    if set(nomes_ligacao) & set(nome.split()):
        nome_partes = nome.split()
        nome_partes_ligacao = list(set(nomes_ligacao) & set(nome.split()))
        # print(nome_partes)
        # print(nome_partes_ligacao)
        # print(nome_partes[-1].upper())
        # print(nome_partes[:-1])
        sobrenome = nome_partes[-1].upper()
        nome_sem_sobrenome = nome_partes[:-1]
        print(nome_sem_sobrenome)
        resto_nome = ""
        for nome in nome_sem_sobrenome:
            if list(set(nomes_ligacao) & set(nome.split())):
                resto_nome = resto_nome + " " + nome.lower()
            else:
                resto_nome = resto_nome + " " + nome.capitalize()
        
        nome_tratado = sobrenome + "," + resto_nome

        return nome_tratado


    if nome.split()[-1] in nomes_descendencia:
        nome_partes = nome.split()
        sobrenome_descendencia = nome.split()[-2].upper() + " " + nome.split()[-1].upper()
        resto_nome = ""
        for nome in nome_partes[:-2]:
            resto_nome = resto_nome + " " + nome.capitalize()

        nome_tratado =  sobrenome_descendencia + "," + resto_nome
        return nome_tratado


    if len(nome.split()) >= 3:
        nome_partes = nome.split()
        sobrenome = nome_partes[-1].upper()
        resto_nome = ""
        for nome in nome_partes[:-1]:
            resto_nome = resto_nome + " " + nome.capitalize()

        nome_tratado =  sobrenome + "," + resto_nome
        return nome_tratado

    if len(nome.split()) == 2:
        nome_partes = nome.split()
        return nome_partes[1].upper() + ', ' + nome_partes[0].capitalize()
    
    if len(nome.split()) == 1:
        return nome.upper()

    return nome.upper()


if __name__ == "__main__":
    formata_autor("Valdik Soriano")
    