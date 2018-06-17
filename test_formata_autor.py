from app import formata_autor

def test_maiuscula():
    assert formata_autor("a") == "A"
    assert formata_autor("d") == "D"
    assert formata_autor("k") == "K"
    assert formata_autor("Valdik") == "VALDIK"
    assert formata_autor("noronha") == "NORONHA"
    assert formata_autor("robertinha") == "ROBERTINHA"


def teste_nome_duplo():
    assert formata_autor("valdick soriano") == "SORIANO, Valdick"
    assert formata_autor("ReginAldo rossi") == "ROSSI, Reginaldo"
    assert formata_autor("roberto müller") == "MÜLLER, Roberto"
    assert formata_autor("wando") == "WANDO"
    assert formata_autor("diana") == "DIANA"

def test_nome_triplo_ou_mais():
    assert formata_autor("carlos josé oliveira santos") == "SANTOS, Carlos José Oliveira"
    assert formata_autor("antoniNo dantas silveira")  == "SILVEIRA, Antonino Dantas"
    assert formata_autor("roberta cristina ponzio binati") == "BINATI, Roberta Cristina Ponzio"
    

def test_nome_descendencia():
    assert formata_autor("joão ubaldo ribeiro neto") == "RIBEIRO NETO, João Ubaldo"
    assert formata_autor("carlos augusto miranda filho") == "MIRANDA FILHO, Carlos Augusto"
    assert formata_autor("antonio goulard junior") == "GOULARD JUNIOR, Antonio"


def test_nome_ligacao():
    assert formata_autor("Manoel augusto de nobraga") == "NOBREGA, Manoel Augusto de"