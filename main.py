#Importar Bibliotecas
import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv("https://raw.githubusercontent.com/nadiduno/dataClient/main/cancelamentos.csv")
df=df.drop("CustomerID",axis=1)
#dropna para deletar valores vazios
df = df.dropna()

st.title('Dados de Cancelamentos dos cliente')
st.dataframe(df)

st.title('Gráfico')
st.plotly_chart(px.histogram(df),use_container_width=True)

# fig =px.line(df)
# st.dataframe(df.style.background_gradient(cmap='Blues'))


st.write('Porcentagem de cancelamentos sem análisis')
df2 = df.rename(columns={'cancelou': 'Cancelou 0/Não 1/Sim'})
st.dataframe(df2["Cancelou 0/Não 1/Sim"].value_counts(normalize=True).map("{:.2%}".format))

df = df[df["duracao_contrato"] != "Monthly"]
#Plotar todos os indicadores
# for coluna in tabela.columns:
#     grafico = px.histogram(tabela, x=coluna, color="cancelou")
#     grafico.show()
#Eliminando Ligacoes call center a partir de 5 
df2 = df2[df2["ligacoes_callcenter"]<5]
#EliminandoDias de atraso de 20 
df2 = df2[df2["dias_atraso"]<=20]
st.write('Reduzindo cancelamentos, seguindo os análises')
st.dataframe(df2["Cancelou 0/Não 1/Sim"].value_counts(normalize=True).map("{:.2%}".format))

