#Importar Bibliotecas
import pandas as pd
import plotly.express as px
import streamlit as st

import plotly.graph_objs as go
import plotly.offline as pyo

st.set_page_config(page_title='Contas/Clientes', layout='wide')

df = pd.read_csv('https://raw.githubusercontent.com/nadiduno/dataClient/main/cancelamentos.csv')

df=df.drop({'CustomerID','idade','sexo'},axis=1)
df = df.dropna()

st.title('Dados de Cancelamentos dos cliente')
st.dataframe(df)
st.title('Gráficos')
# fig = px.histogram(df, x="duracao_contrato",color="cancelou")
# st.plotly_chart(fig)
for coluna in df.columns:
    fig = px.histogram(df, x=coluna,color="cancelou")
    st.plotly_chart(fig)


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
st.write('Seguindo os análises')
st.dataframe(df2["Cancelou 0/Não 1/Sim"].value_counts(normalize=True).map("{:.2%}".format))

st.title('Reduziremos cancelamentos de 56.71% a 18.40%')
st.caption('Seguindo as recomendações:')
st.caption('- Tirar a forma de pagamento mensal o colocar um valor menor.')
st.caption('- Evitar que o cliente chegue a 20 dias de atraso no pagamento, porque cancela.')
st.caption('- Evitar que o cliente ligue al call center mais de 5 (resolver seu problema antes)')

st.write('Dados disponíveis em https://github.com/nadiduno/dataClient')
st.markdown('Um aplicativo feito com <💜 /> [Nadi Duno](https://www.linkedin.com/in/nadiduno/) © Julho 2023')