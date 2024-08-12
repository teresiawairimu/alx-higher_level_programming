$(document).ready(function () {
  function fetchTranslation () {
    const langCode = $('#language_code').val();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`;

    $.get(url)
      .done(function (data) {
        $('#hello').text(data.hello);
      })
      .fail(function () {
        $('#hello').text('Error: Unable to fetch translation');
      });
  }

  $('#btn_translate').click(function () {
    fetchTranslation();
  });

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});
