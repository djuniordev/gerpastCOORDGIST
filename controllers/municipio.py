from repositories.municipio import countMunicipio

def mostrarDadosMunicipio(st, dadosUnidade):

        infoMunicipio = countMunicipio(dadosUnidade)

        st.header("Município:")
        st.write(f"Total: {infoMunicipio["TotalMunicipioAcidente"]}")
        st.write(f"Sequência vazia: {infoMunicipio["NumeroSequenciaVazia"]}")
        for municipio in infoMunicipio["ContagemMunicipio"]:
                st.write(f"{municipio}: {infoMunicipio["ContagemMunicipio"][municipio]}")
