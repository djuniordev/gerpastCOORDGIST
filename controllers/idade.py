from repositories.idade import countIdade

def mostrarDadosIdade(st, dadosUnidade):
    infoIdade = countIdade(dadosUnidade)

    st.header("Idade:")
    st.write(f"Total: {infoIdade["TotalIdadeUnidade"]}")
    st.write(f"Sequência vazia: {infoIdade["NumeroSequenciaVazia"]}")
    st.write(f"Menos de 10 anos: {infoIdade["Total -10"]}")
    st.write(f"10 a 19 anos: {infoIdade["Total 10 a 19"]}")
    st.write(f"20 a 29 anos: {infoIdade["Total 20 a 29"]}")
    st.write(f"30 a 39 anos: {infoIdade["Total 30 a 39"]}")
    st.write(f"40 a 49 anos: {infoIdade["Total 40 a 49"]}")
    st.write(f"50 a 59 anos: {infoIdade["Total 50 a 59"]}")
    st.write(f"60 a 69 anos: {infoIdade["Total 60 a 69"]}")
    st.write(f"70 a 79 anos: {infoIdade["Total 70 a 79"]}")
    st.write(f"80 anos ou mais: {infoIdade["Total 80 ou +"]}")