const $ = window.$;
$.getJSON('https://swapi-api.alx-tools.com/api/films/?', function (data) {
  $.each(data.results, function (index, movie) {
    $('UL#list_movies').append('<li>' + movie.title + '</li>');
  });
});
