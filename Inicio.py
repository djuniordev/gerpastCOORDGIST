import streamlit as st
from pages import configPage

def inicioPage():
    configPage()
    
    st.title("Sistema de análise de dados da GERPAST")
    st.markdown("Sistema implementado para análise de dados de casos de :blue[**internações**] e :blue[**sinistros**] de trânsito importados do :blue[**Done**].")
    st.divider()
    st.markdown("Para começar, há três páginas de análise de dados:")
    st.markdown("""
    - Acidentes
    - Acidentes e Tratamento
    - Tratamento
""")
    st.divider()
    st.header("Passo 1:")
    st.markdown("Selecione a página que você deseja e que está com necessidade.")
    st.header("Passo 2:")
    st.markdown("Para continuar, na lateral esquerda na :blue[**barra de navegação**], importe a planilha correspondente a página.")
    st.header("Passo 3:")
    st.markdown("Após importar a planilha, o programa irá carregar e você conseguirá fazer os filtros que desejar na :blue[**barra de navegação**].")
   

inicioPage()