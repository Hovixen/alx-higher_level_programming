const $ = window.$;
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const url = 'https://www.fourtonfish.com/hellosalut/hello/';
    const langRet = $('INPUT#language_code').val();
    $.getJSON(url, { lang: langRet }, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
