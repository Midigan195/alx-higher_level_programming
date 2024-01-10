$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi.co/api/people/5/?format=json',
    success: function (data) {
      $('div#character').text(data.name);
    }
  });
});
