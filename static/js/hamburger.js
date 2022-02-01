$(function () {
  $('.navbar_toggle').on('click', function () {
    $(this).toggleClass('open');
    $('.menu').toggleClass('open');
  });
});