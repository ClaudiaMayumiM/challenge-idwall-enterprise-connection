# critérios - senha, ajuda da senha, telefone, nome, email, data do vazamento 

senha = 'senha'
ajuda_da_senha = 'ajuda da senha'
telefone = 'telefone'
nome = 'nome'
email = 'email'

# LISTA COM 41 EMPRESAS

listas = [ ['DELL EMC', 'telefone', 'nome', 'email', 202203],
['SAP LABS LATIN AMERICA', 'senha', 'ajuda da senha', 'telefone', 'nome', 'email', 202106],
['SAP BRASIL', 'telefone', 'nome', 'email', 201806],
['CI&T', 'senha', 'ajuda da senha', 201310],
['VIVO', 'telefone', 'nome', 202010],
['ORACLE DO BRASIL', 'telefone', 'nome', 202008],
['LOGICALIS', 'ajuda da senha', 'telefone', 'nome', 202109],
['INTELBRAS', 'telefone', 'email', 201904],
['MERCADO LIVRE', 'nome', 'email', 201705],
['GETNET', 'nome', 'email', 200211],
['ALGAR TELECOM', 'ajuda da senha', 'nome', 'email', 200905],
['IBM BRASIL', 'nome', 'email', 202201],
['CLEAR SALE', 'telefone', 'nome', 'email', 201208],
['CIELO', 'ajuda da senha', 'telefone', 'email', 201410],
['COGNIZANT BRASIL', 'senha', 'ajuda da senha', 'telefone', 'nome', 'email', 201508],
['NEXTEL', 'telefone', 'email', 201411],
['ATENTO BRASIL', 'ajuda da senha', 200504],
['ALGAR TECH', 'telefone', 'nome', 'email', 201406],
['TELEPERFORMANCE', 'senha', 'ajuda da senha', 'telefone', 'email', 201806],
['SENIOR SISTEMAS', 'telefone', 202002],
['ADOBE', 'senha', 'ajuda da senha', 'telefone', 'nome', 'email', 201207],
['HURB', 'nome', 'email', 201910],
['CANVAS', 'email', 201707],
['SONY', 'telefone', 200709],
['EBAY', 'senha', 'telefone', 'nome', 'email', 200305],
['GOOGLE', 'senha', 'ajuda da senha', 'telefone', 201308],
['YAHOO', 'ajuda da senha', 'nome', 200107],
['COMPANY', 'email', 201509],
['CONECTA', 'ajuda da senha', 'nome', 200001],
['NINTENDO', 'ajuda da senha', 'telefone', 'nome', 'email', 200710],
['APPLE', 'email', 202111],
['MICROSOFT', 'ajuda da senha', 'telefone', 'nome', 201112],
['META', 'senha', 'ajuda da senha', 'telefone', 201807],
['ALPHABET', 'senha', 'ajuda da senha', 'telefone', 'nome', 'email', 201604],
['AMAZON', 'senha', 'nome', 'telefone', 201305],
['TENCENT', 'ajuda da senha', 'telefone', 'email', 201812],
['ALIBABA GROUP', 'ajuda da senha', 'telefone', 202001],
['TSMC', 'telefone', 'email', 'nome', 202010],
['NVIDIA', 'telefone', 'nome', 200906],
['SAMSUNG', 'ajuda da senha', 'telefone', 'nome', 201411],
['CISCO', 'senha', 'ajuda da senha', 201108]
]


listas = sorted(listas, key=lambda x: x[-1], reverse=True) # organiza pela data
  
ranking_senha = []
ranking_ajuda_senha = []
ranking_telefone = []
ranking_nome = []
ranking_email = []

def verifica_criterios (listas):

  for lista in listas:
    if senha in lista:
      ranking_senha.append(lista)
    elif ajuda_da_senha in lista:
      ranking_ajuda_senha.append(lista)
    elif telefone in lista:
      ranking_telefone.append(lista)
    elif nome in lista:
      ranking_nome.append(lista)
    elif email in lista:
      ranking_email.append(lista)
  
  return ranking_senha, ranking_ajuda_senha, ranking_telefone, ranking_nome, ranking_email

verifica_criterios(listas)

ranking_final = []

def ranking_geral (ranking_senha, ranking_ajuda_senha, ranking_telefone, ranking_nome, ranking_email, ranking_final):

  for lista in ranking_senha:
    if lista not in ranking_final:
      ranking_final.append(lista)
  
  for lista in ranking_ajuda_senha:
    if lista not in ranking_final:
      ranking_final.append(lista)

  for lista in ranking_telefone:
    if lista not in ranking_final:
      ranking_final.append(lista)
  
  for lista in ranking_nome:
    if lista not in ranking_final:
      ranking_final.append(lista)

  for lista in ranking_email:
    if lista not in ranking_final:
      ranking_final.append(lista)

  return ranking_final

ranking_geral(ranking_senha, ranking_ajuda_senha, ranking_telefone, ranking_nome, ranking_email, ranking_final)

def imprime_ranking(ranking_final):

  i = 0 

  while i < len(ranking_final):
    print(f'{i+1}ª empresa do ranking - dados vazados e data de vazamento (ano e mês) - {ranking_final[i]}')
    i+=1

imprime_ranking(ranking_final)


# Lógica utilizada:
# Filtramos a lista de listas de empresas, armazenando as empresas que vazaram o primeiro critério (senha) em uma variável e rankeamos essa lista de acordo com a data (mais recentes primeiro);
# Fizemos isso para todos os critérios seguintes.. Filtramos as empresas que vazaram o segundo critério (ajuda da senha) e rankeamos de acordo com a data (mais recentes primeiro) e assim por diante, com os demais critérios;
# Portanto, na lista de ranking_final, primeiro se encontram as empresas que vazaram a senha mais recentemente, seguidas pelas empresas que vazaram o dado "ajuda da senha" mais recentemente, seguidas pelas empresas que vazaram o dado "telefone" mais recentemente e por aí vai... 

## formato da data (elemento armazenado no último index da lista de cada empresa) - anoMês