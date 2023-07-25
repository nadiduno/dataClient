#Importar Bibliotecas
import pandas as pd
import plotly.express as px
#Importar Dados
#DataFrame
tabela = pd.read_csv("cancelamentos.csv")
print(tabela)
#Axis = 0 para Linha
#Axis = 1 para Coluna
tabela=tabela.drop("CustomerID",axis=1)
#Visualizar
print(tabela)
#Tratamento de erros
print(tabela.info())
#dropna para deletar valores vazios
tabela = tabela.dropna()
print(tabela.info())
#Análise inicial (cancelamento)
print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format))
#Análise inicial (Duração Contrato)
print(tabela["duracao_contrato"].value_counts())
print(tabela["duracao_contrato"].value_counts(normalize=True).map("{:.2%}".format))
#Eliminando os contratos mensal 
tabela = tabela[tabela["duracao_contrato"] != "Monthly"]
print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format))
#Eliminando Ligacoes call center a partir de 5 
tabela = tabela[tabela["ligacoes_callcenter"]<5]
#EliminandoDias de atraso de 20 
tabela = tabela[tabela["dias_atraso"]<=20]
print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format))
