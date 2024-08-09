from repositories.internacao import countInternacao

def mostrarDadosInternacao(st, dadosUnidade):
    infoInternacao = countInternacao(dadosUnidade)

    st.header("Internacao:")
    st.write(f"Total: {infoInternacao["TotalInfoInternacao"]}")
    #st.write(f"Sequência vazia: {infoIdade["NumeroSequenciaVazia"]}")