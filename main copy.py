#Importar Bibliotecas
import pandas as pd
import plotly.express as px
import streamlit as st
import pygwalker as pyg
#Importar Dados
#DataFrame
tabela = pd.read_csv("https://raw.githubusercontent.com/nadiduno/dataClient/main/cancelamentos.csv")
#Axis = 0 para Linha
#Axis = 1 para Coluna
tabela=tabela.drop("CustomerID",axis=1)
#Tratamento de erros
#dropna para deletar valores vazios
tabela = tabela.dropna()
st.title('Dados de Cancelamentos dos cliente')
# st.write(tabela.info())
# st.dataframe(tabela)
st.dataframe(tabela.style.background_gradient(cmap='Blues'))
df = pd.read_csv('./bike_sharing_dc.csv', parse_dates=['date'])
walker = pyg.walk(df)
# fig = px.histogram(tabela, x="date", y=, title=)
# fig.update_layout( xaxis_title='Data', yaxis_title='', title = 'Cancelamentos dos cliente')

#st.line_chart(tabela)

#st.plotly_chart

#Análise inicial (cancelamento)
# print(tabela["cancelou"].value_counts())
# print(tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format))
#Análise inicial (Duração Contrato)
# print(tabela["duracao_contrato"].value_counts())
# print(tabela["duracao_contrato"].value_counts(normalize=True).map("{:.2%}".format))
#Estudar cancelamentos por duração de contrato (Calculando media MEAN)
# print(tabela.groupby("duracao_contrato").mean())
#Plotar indicador contratos
# grafico = px.histogram(tabela, x="duracao_contrato", color="cancelou")
# grafico = px.histogram(tabela, x="duracao_contrato", color="cancelou")
# grafico.show()
#Eliminando os contratos mensal 
tabela = tabela[tabela["duracao_contrato"] != "Monthly"]
# print(tabela["cancelou"].value_counts())
# print(tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format))
#Plotar todos os indicadores
# for coluna in tabela.columns:
#     grafico = px.histogram(tabela, x=coluna, color="cancelou")
#     grafico.show()
#Eliminando Ligacoes call center a partir de 5 
tabela = tabela[tabela["ligacoes_callcenter"]<5]
#EliminandoDias de atraso de 20 
tabela = tabela[tabela["dias_atraso"]<=20]
st.write(tabela["cancelou"].value_counts())
st.write(tabela["cancelou"].value_counts(normalize=True).map("{:.2%}".format))