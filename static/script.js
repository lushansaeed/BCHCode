document.getElementById('encodeButton').addEventListener('click', function() {
    sendData('encode');
});

document.getElementById('decodeButton').addEventListener('click', function() {
    sendData('decode');
});

function sendData(action) {
    var inputNumber = document.getElementById('inputNumber').value;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/' + action, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
        if (xhr.status === 200) {
            document.getElementById('result').innerText = xhr.responseText;
        } else {
            document.getElementById('result').innerText = 'Error: ' + xhr.responseText;
        }
    };
    xhr.send(JSON.stringify({ number: inputNumber }));
}
