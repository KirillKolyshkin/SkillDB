var bgImgs = [
    '{% static 'img/red.jpg' %}'
  , '{% static 'img/blue.jpg' %}'
];

$(function () {
  if (bgImgs.length > 1) {
    var bgImage = $('#bgImage')
      , index = 0
      , interval = 5000
      , slideshow = $('#slider');

    setInterval(function () {
      slideshow.css('background-image', 'url(' + bgImage.attr('src') + ')');
      bgImage.fadeOut(function () {
        index = index < bgImgs.length - 1 ? index + 1 : 0;
        bgImage.attr('src', bgImgs[index]);
        bgImage.fadeIn('slow');
      });
    }, interval);
  }
});