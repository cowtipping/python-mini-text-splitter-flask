function togglePopoutTextarea() {
  var overlay = document.getElementById('popout-overlay');
  var textarea = document.getElementById('text');
  var button = document.getElementById('toggle-button');
  var isOverlayVisible = overlay.classList.contains('visible');

  if (!isOverlayVisible) {
    // When opening the overlay
    overlay.appendChild(textarea);
    overlay.appendChild(button);
    textarea.classList.add('fullscreen-textarea');
    button.textContent = 'Close';
  } else {
    // When closing the overlay
    var textareaGroup = document.getElementById('textarea-group');
    textareaGroup.appendChild(textarea);
    textareaGroup.appendChild(button);
    textarea.classList.remove('fullscreen-textarea');
    textarea.style.height = '';
    button.textContent = 'Pop-out';
  }

  overlay.classList.toggle('visible');
}

// Close the overlay when clicking outside the textarea
window.addEventListener('click', function (event) {
  var overlay = document.getElementById('popout-overlay');
  if (event.target === overlay) {
    togglePopoutTextarea();
  }
});
