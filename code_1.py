#Importar Bibliotecas
import pandas as pd
import plotly.express as px
#Importar Dados
#DataFrame
tabela = pd.read_csv("https://raw.githubusercontent.com/nadiduno/dataClient/main/cancelamentos.csv")
#Axis = 0 para Linha
#Axis = 1 para Coluna
tabela=tabela.drop("CustomerID",axis=1)
#Tratamento de erros
#dropna para deletar valores vazios
tabela = tabela.dropna()
print('Dados de Cancelamentos dos cliente')




#Análise inicial (cancelamento)
print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format))
#Análise inicial (Duração Contrato)
print(tabela["duracao_contrato"].value_counts())
print(tabela["duracao_contrato"].value_counts(normalize=True).map("{:.2%}".format))
#Estudar cancelamentos por duração de contrato (Calculando media MEAN)
print(tabela.groupby("duracao_contrato").mean())
#Plotar indicador contratos
grafico = px.histogram(tabela, x="duracao_contrato", color="cancelou")
grafico = px.histogram(tabela, x="duracao_contrato", color="cancelou")
grafico.show()
#Eliminando os contratos mensal 
tabela = tabela[tabela["duracao_contrato"] != "Monthly"]
print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format))
#Plotar todos os indicadores
for coluna in tabela.columns:
     grafico = px.histogram(tabela, x=coluna, color="cancelou")
     grafico.show()
#Eliminando Ligacoes call center a partir de 5 
tabela = tabela[tabela["ligacoes_callcenter"]<5]
#Eliminando Dias de atraso de 20 
tabela = tabela[tabela["dias_atraso"]<=20]
print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format))