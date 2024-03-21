function konsentrasi() {
    var konsentrasi = document.getElementById("konsentrasi").value
    var option = document.getElementById("konsentrasi-option")
    if (Number(konsentrasi) > 2) {
        option.disabled = false
    } else {
        option.disabled = true
    }
}