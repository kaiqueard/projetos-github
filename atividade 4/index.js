const inptValor1 = document.getElementById("inptValor1")
const inptValor2 = document.getElementById("inptValor2")
const lblResultado = document.getElementById("lblResultado")
const btnMaior = document.getElementById("btnMaior")
const btnCalc = document.getElementById("btnCalc")
const btnLimpar = document.getElementById("btnLimpar")

btnMaior.onclick = function () {
    let v1 = Number(inptValor1.value)
    let v2 = Number(inptValor2.value)

    if (v1 > v2) {
        lblResultado.innerHTML = "O maior é: " + v1
        lblResultado.style.color = "lightgreen"
    }
    else if (v2 > v1) {
        lblResultado.innerHTML = "O maior é: " + v2
        lblResultado.style.color = "lightgreen"
    }
    else {
        lblResultado.innerHTML = "Os valores são iguais"
        lblResultado.style.color = "orange"
    }
};

btnCalc.onclick = function () {
    let v1 = Number(inptValor1.value)
    let v2 = Number(inptValor2.value)

    alert("Soma: " + (v1 + v2))
    alert("Subtração: " + (v1 - v2))
    alert("Multiplicação: " + (v1 * v2))
    alert("Divisão: " + (v1 / v2))
};

btnLimpar.onclick = function () {
    inptValor1.value = ""
    inptValor2.value = ""
    lblResultado.innerHTML = "Aguardando ação..."
    lblResultado.style.color = "white"
};