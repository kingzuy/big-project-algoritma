async function getdata() {
  const response = await fetch('/data');
  console.log(response);
}

function konsentrasi() {
    var konsentrasi = document.getElementById("konsentrasi").value
    var option = document.getElementById("konsentrasi-option")
    if (Number(konsentrasi) > 2) {
        option.disabled = false
    } else {
        option.disabled = true
    }
}

getdata()