let totalPessoas = 0;
const limiteMaximo = 50;
const nomes = ["Carlos Silva", "Ana Souza", "Marcos Oliveira", "Juliana Lima", "Bruno Santos", "Mariana Costa", "Gabriel Almeida", "Fernanda Rocha", "Lucas Mendes", "Beatriz Ribeiro"];

function gerarSubordinado() {
    if (totalPessoas >= limiteMaximo) return;

    totalPessoas++;
    let nomeSorteado = nomes[Math.floor(Math.random() * nomes.length)];
    let idValido = "ID" + Math.floor(100000 + Math.random() * 900000);
    
    document.getElementById("total-subordinados").innerText = totalPessoas;

    let lista = document.getElementById("lista-pessoas");
    let item = document.createElement("li");
    item.innerHTML = `<span>${nomeSorteado}</span> <small style="color: #00ff88;">${idValidu = idValido}</small>`;
    lista.prepend(item);

    if (totalPessoas >= limiteMaximo) {
        let btn = document.getElementById("btn-gerar");
        btn.disabled = true;
        btn.innerText = "Limite Atingido (50/50)";
    }
}
