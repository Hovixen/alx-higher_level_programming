const $ = window.$;
$(document).ready(function () {
  function fetchTranslation () {
    const languageCode = $('INPUT#language_code').val();

    $.getJSON('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode }, function (data) {
      $('DIV#hello').text(data.hello);
    }).fail(function () {
      console.error('Failed to fetch translation from the API!');
    });
  }

  $('INPUT#btn_translate').click(fetchTranslation);

  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});
