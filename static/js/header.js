$(window).resize(function() {
    var WindowWidth = $(window).width();
    if(WindowWidth < 768){
        $('hamburger-menu').show();
        $('navi_menu').hide();
    }else{
        $('hamburger-menu').hide();
        $('navi_menu').show();
    }
});
