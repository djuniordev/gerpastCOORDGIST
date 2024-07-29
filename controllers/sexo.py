from repositories.sexo import countSexo

def mostrarDadosSexo(st, dadosUnidade):

    infoSexo = countSexo(dadosUnidade)

    st.header("Sexo:")
    st.write(f"Total: {infoSexo["TotalSexoUnidade"]}")
    st.write(f"Sequência vazia: {infoSexo["NumeroSequenciaVazia"]}")
    st.write(f"Masculino: {infoSexo["TotalMasculino"]}")
    st.write(f"Feminino: {infoSexo["TotalFeminino"]}")

