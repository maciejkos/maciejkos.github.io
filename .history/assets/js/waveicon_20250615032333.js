// Wave icon audio and animation
// Requires Howler.js

(function() {
  document.addEventListener('DOMContentLoaded', function() {
    var button = document.getElementById('wave-button');
    if (!button) return;

    // Replace with the correct path to your audio files
    var sound = new Howl({
      src: [
        '/assets/audio/name.mp3',
        '/assets/audio/name.ogg'
      ],
      html5: true
    });

    var isPlaying = false;

    button.addEventListener('click', function() {
      if (isPlaying) {
        sound.stop();
      } else {
        sound.play();
      }
    });

    sound.on('play', function() {
      isPlaying = true;
      button.classList.add('playing');
    });

    function clear() {
      isPlaying = false;
      button.classList.remove('playing');
    }

    sound.on('end', clear);
    sound.on('stop', clear);
  });
})(); 