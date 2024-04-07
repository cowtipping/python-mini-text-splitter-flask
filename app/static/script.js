function copyToClipboard(elementId, buttonId) {
  let text = document.getElementById(elementId).innerText;
  let button = document.getElementById('copy-button-' + buttonId);
  navigator.clipboard.writeText(text).then(function () {
    button.innerHTML = 'Copied to clipboard!';
    setTimeout(function () {
      button.innerHTML = 'Copy';
    }, 2000);
  }).catch(function (err) {
    console.error('Error in copying text: ', err);
  });
}

function togglePopoutTextarea() {
  let overlay = document.getElementById('popout-overlay');
  let textarea = document.getElementById('text');
  let button = document.getElementById('toggle-button');
  let isOverlayVisible = overlay.classList.contains('visible');

  if (!isOverlayVisible) {
    overlay.appendChild(textarea);
    overlay.appendChild(button);
    textarea.classList.add('fullscreen-textarea');
    button.textContent = 'Close';
  } else {
    let textareaGroup = document.getElementById('textarea-group');
    textareaGroup.appendChild(textarea);
    textareaGroup.appendChild(button);
    textarea.classList.remove('fullscreen-textarea');
    textarea.style.height = '';
    button.textContent = 'Pop-out';
  }

  overlay.classList.toggle('visible');
}

// Close the overlay when clicking outside the textarea.
window.addEventListener('click', function (event) {
  let overlay = document.getElementById('popout-overlay');
  if (event.target === overlay) {
    togglePopoutTextarea();
  }
});
