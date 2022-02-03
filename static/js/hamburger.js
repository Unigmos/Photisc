$(function () {
  var z_index_flag = false;
  $('.navbar_toggle').on('click', function () {
    $(this).toggleClass('open');
    $('.menu').toggleClass('open');
    $('.main_container').toggleClass('white');
    if(z_index_flag == false){
      $('.to-template-button a').css('z-index','0');
      z_index_flag = true;
    }else{
      $('.to-template-button a').css('z-index','30');
      z_index_flag = false;
    }
  });
});