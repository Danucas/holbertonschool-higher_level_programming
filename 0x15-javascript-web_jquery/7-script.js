$(window).on('load', function () {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  $.ajax({
    url:url,
    success: function (data) {
      $('DIV#character').text(data.name);
    }
  });
});
