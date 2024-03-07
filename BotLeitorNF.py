import pandas as pd # import do modulo para manipulção de dados
import xmltodict as xml # import do modulo para mexer com xml
import os # import do modulo para mexer com arquivos
import json # para formatar a estrutura das nf

# função para procurar e abrir a nf
def pegarinf(nomearq, valores):
#   mostra se pegou e da onde as informações foram tiradas
    print(f"Pegou as informações de {nomearq}")

#   abre a pasta e extrai o arquivo
    with open(f"E:/XMLs/{nomearq}", "rb") as arqXML:

#       vai "traduzir" o formato XML para Python atraves do .parse
        dicionario = xml.parse(arqXML)
        # print(json.dumps(dicionario, indent=4)) # aqui vai ser printado a nf inteira formatada como um "código python"

#       agora a adição da filtragem de informações
        try: #para tratamento de erros
            if "NFe" in dicionario: # para o tratamento de eventuais erros com chaves
                infNF = dicionario["NFe"]["infNFe"]
            else:# aqui no caso as chaves das NFs não eram as mesmas
                infNF = dicionario["nfeProc"]["NFe"]["infNFe"]
            numNF = infNF["@Id"]                            # daqui serão apenas exemplos práticos de uma NF
            empEmissora = infNF["emit"]["xNome"]            # todos os dados de filtragem podem ser alterados
            nomeClient = infNF["dest"]["xNome"]             # e outras coisas podem ser separadas
            enderClient = infNF["dest"]["enderDest"]        # assim como informações de outros tipos de NFs
            produto = infNF["det"]["prod"]["xProd"]
            valor = infNF["pag"]["detPag"]["vPag"]
            imposto = infNF["total"]["ICMSTot"]["vTotTrib"]
            print(f"Número: {numNF}", f"Empresa Emissora: {empEmissora}", f"Nome do Cliente: {nomeClient}, "
            f"Endereço do Cliente: {enderClient}", f"Produto/Serviço: {produto}", f"Valor: {valor}", f"Valor do Imposto no Total: {imposto}", sep="\n")
#           acrescenta os valores em uma lista
            valores.append([numNF, empEmissora,nomeClient, enderClient, produto, valor, imposto])

        except Exception as e:
            print(e)
            print(json.dumps(dicionario, indent=4))


lista_arquivos = os.listdir("E:/XMLs") # assim como lá em cima o "E:/XMLs" é apenas o caminho do arquivo que procuro
                                       # e pode ser mudado para qualquer outroi lugar do computador

coluna = ["numNF", "empEmissora", "nomeClient", "enderClient", "produto", "valor", "imposto"] # aqui são as listas de armazenagem das informações tiradas da NF
valores = []

for arquivo in lista_arquivos: # aqui sera feito o mesmo processo para cada NF na pasta
    pegarinf(arquivo, valores)

tabela = pd.DataFrame(columns=coluna, data=valores)
tabela.to_excel("E:/XMLs/NotasFiscais.xlsx", index=False) # aqui é para mandar as informações para um Excel
# e para essa ultima linha funcionar deve-se install openpyxl