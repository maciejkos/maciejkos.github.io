// Wave icon audio and animation
// Requires Howler.js

(function() {
  document.addEventListener('DOMContentLoaded', function() {
    var button = document.getElementById('wave-button');
    if (!button) return;

    // Provide your own audio clip in /assets/audio/
    // Supported formats: MP3 (modern browsers) + optional OGG for legacy Linux/Firefox
    var sound = new Howl({
      src: [
        '/assets/audio/name.mp3',
        '/assets/audio/name.ogg'
      ],
      html5: true
    });

    // Basic diagnostics
    sound.on('load', function() {
      console.log('[waveicon] Audio sprite loaded. Duration:', sound.duration(), 's');
    });

    sound.on('loaderror', function(id, err) {
      console.error('[waveicon] Failed to load audio (id=' + id + '):', err);
    });

    sound.on('playerror', function(id, err) {
      console.error('[waveicon] Failed to play audio (id=' + id + '):', err);
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