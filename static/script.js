function copyToClipboard(elementId, buttonId) {
  var text = document.getElementById(elementId).innerText;
  var button = document.getElementById('copy-button-' + buttonId);
  navigator.clipboard.writeText(text).then(function () {
    button.innerHTML = 'Copied to clipboard!';
    setTimeout(function () {
      button.innerHTML = 'Copy';
    }, 2000);
  }).catch(function (err) {
    console.error('Error in copying text: ', err);
  });
}
