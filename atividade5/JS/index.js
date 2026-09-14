const tabelaCorpo = document.getElementById("tabela-corpo")

let dados = [
{ID_Aplicativo: 1,Nome: "Roblox",Descrição: " Plataforma de jogos " },
{ID_Aplicativo: 2,Nome: "FNF",Descrição: " Jogo de ritmo"},
{ID_Aplicativo: 3,Nome: "Gacha Life",Descrição: " Jogo de RPG "},
{ID_Aplicativo: 4,Nome: "Free Fire",Descrição: " Jogo de tiro imersivo"},
]

let linhasProcessadas = dados.map(n => `
        <tr class="linhas">
            <td>${n.ID_Aplicativo}</td>
            <td>${n.Nome}</td>
            <td>${n.Descrição}</td>
        </tr>
    `).join("")

tabelaCorpo.innerHTML += linhasProcessadas