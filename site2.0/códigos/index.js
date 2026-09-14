console.log("Testando o JS!");

const idnome = document.getElementById("idnome");
const idsenha = document.getElementById("idsenha");
const btnEnviar = document.getElementById("btnEnviar");
const ibid =

    //funcao anonima
    btnEnviar.onclick = function () {
        console.log("teste")
        console.log(idnome.value)
        console.log(idsenha.value)

        if (validate(idnome.value) && validate(idsenha.value)) {
            alert("sucesso!")
        }
        else {
            alert("ERRO!")
        }
    };

function validate(texto) {
    if (texto == "") {
        return false
    }
    return true
}
