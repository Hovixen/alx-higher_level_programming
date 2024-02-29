const $ = window.$;
$.getJSON('https://swapi-api.alx-tools.com/api/films/?', function (data) {
  $('UL#list_movies').text(data.title);
});
