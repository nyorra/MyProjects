window.addEventListener('scroll', function() {
    var video = document.getElementById('main-video');
    var videoPosition = video.getBoundingClientRect();
    
    if (videoPosition.top >= 0 && videoPosition.bottom <= window.innerHeight) {
      if (video.paused) {
        video.play();
      }
    } else {        video.pause();    }
  });

/*Slider Gallery*/

