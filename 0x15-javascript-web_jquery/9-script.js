$(window).on('load', function () {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.ajax({
    url:url,
    success: function (salut) {
	$('DIV#hello').text(salut.hello);
    }
  });
});
