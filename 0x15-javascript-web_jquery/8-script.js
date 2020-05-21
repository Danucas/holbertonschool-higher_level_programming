$(window).on('load', function () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.ajax({
    url:url,
    success: function (movies) {
      for (movie of movies.results) {
        const li = '<li>' + movie.title + '</li>';
        $('UL#list_movies').append($(li));
      }
    }
  });
});
