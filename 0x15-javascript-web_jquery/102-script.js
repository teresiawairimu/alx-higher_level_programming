$(document).ready(function () {
  $('#btn_translate').click(function () {
    const langCode = $('#language_code').val();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`;
    $.get(url)
      .done(function (data) {
        $('#hello').text(data.hello);
      })
      .fail(function () {
        $('#hello').text('Error: Unable to fetch translation');
      });
  });
});
