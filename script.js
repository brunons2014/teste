async function carregarDados() {
    try {
        const resposta = await fetch('http://127.0.0.1:8000/clima');
        const dados = await resposta.json();

        if (dados.length > 0) {
            const maisRecente = dados[0]; // O FastAPI já devolve ordenado

            // Atualiza o Card Principal
            document.getElementById('temp-atual').innerText = `${maisRecente.temperatura}°C`;
            document.getElementById('desc-atual').innerText = maisRecente.descricao.toUpperCase();
            document.getElementById('data-atual').innerText = new Date(maisRecente.data_hora).toLocaleString();

            // Preenche a Tabela
            const tbody = document.querySelector('#history-table tbody');
            tbody.innerHTML = ''; // Limpa a tabela antes de preencher

            dados.forEach(registro => {
                const linha = `
                    <tr>
                        <td>${new Date(registro.data_hora).toLocaleString()}</td>
                        <td>${registro.temperatura}°C</td>
                        <td>${registro.descricao}</td>
                    </tr>
                `;
                tbody.innerHTML += linha;
            });

            document.getElementById('loading').style.display = 'none';
            document.getElementById('current-weather').style.display = 'block';
        }
    } catch (erro) {
        console.error("Erro ao buscar dados da API:", erro);
        document.getElementById('loading').innerText = "Erro ao conectar com a API. Verifique se o Uvicorn está rodando!";
    }
}

// Carrega os dados ao abrir a página
carregarDados();