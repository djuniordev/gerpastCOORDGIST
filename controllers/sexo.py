from repositories.sexo import countSexo
import plotly.express as px

def mostrarDadosSexo(st, dadosUnidade):

    infoSexo = countSexo(dadosUnidade)

    # Dados
    sexo_counts = dadosUnidade["SEXO"].value_counts().reset_index()
    sexo_counts.columns = ['Sexo', 'Total']

    # Criar gráfico com plotly
    fig = px.pie(sexo_counts, names='Sexo', values='Total', color='Sexo', hole=0.6, title="Distribuição por Sexo",
                 color_discrete_map={"Masculino": "#40E0D0", "Feminino": "#FF007F", "Outros": "#90EE90"})

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig)

    # st.metric(label="Total Sexo", value=infoSexo["TotalSexoUnidade"])
    #st.header("Sexo:")
    #st.write(f"Total: {infoSexo["TotalSexoUnidade"]}")
    #st.write(f"Sequência vazia: {infoSexo["NumeroSequenciaVazia"]}")
    #st.write(f"Masculino: {infoSexo["TotalMasculino"]}")
    #st.write(f"Feminino: {infoSexo["TotalFeminino"]}")
def sexoDetalhado(st, dadosUnidade):
    infoSexo = countSexo(dadosUnidade)
    st.header("Sexo:")
    st.write(f"Total: {infoSexo["TotalSexoUnidade"]}")
    st.write(f"Sequência vazia: {infoSexo['NumeroSequenciaVazia']}")
    st.write(f"Masculino: {infoSexo["TotalMasculino"]}")
    st.write(f"Feminino: {infoSexo["TotalFeminino"]}")




