function togglePopoutTextarea() {
  var overlay = document.getElementById('popout-overlay');
  var button = document.getElementById('toggle-button');
  var isOverlayVisible = overlay.classList.contains('visible');

  if (!isOverlayVisible) {
    // When opening the overlay
    overlay.appendChild(document.getElementById('text'));
    overlay.appendChild(button);
    button.textContent = 'Close';
  } else {
    // When closing the overlay
    var formGroup = document.getElementById('textarea-group');
    formGroup.appendChild(document.getElementById('text'));
    formGroup.appendChild(button);
    button.textContent = 'Pop-out';
  }

  overlay.classList.toggle('visible');
}

// Adjusted event listener for closing the overlay on outside click
window.addEventListener('click', function (event) {
  var overlay = document.getElementById('popout-overlay');
  if (event.target === overlay) {
    togglePopoutTextarea();
  }
});
