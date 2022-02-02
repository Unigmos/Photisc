$(function () {
  $('.navbar_toggle').on('click', function () {
    $(this).toggleClass('open');
    $('.menu').toggleClass('open');
    $('.to-template-button a').fadeToggle(320);
    $('.main_container').toggleClass('white');
  });
});