
(function( $ ){
	$.fn.grtmobile = function () {
		if ($(window).width() < 768) {
			$('.grt-mobile-button').on('click', function(){
				$(this).toggleClass("grt-mobile-button-open");
				$("ul.grt-menu").toggleClass("open-grt-menu ");
				$("html, body").toggleClass("body-overflow");
			});
			$('li.grt-dropdown').on('click', function(e){
				$(this).toggleClass("active-dropdown");
			});
		}
	}
})( jQuery );

$.fn.grtmobile();

var resizeTimeout;
$(window).resize(function(){
  if(!!resizeTimeout){ clearTimeout(resizeTimeout); }
  resizeTimeout = setTimeout(function(){
    $.fn.grtmobile();
  },200);
});

$(window).scroll(function(e){
	if ($(window).scrollTop() < 60) {
   	console.log("scrolled");
      $('header').removeAttr('style');
      $("#nu").css("display","block")
    }

   if ($(window).scrollTop() > 60) {
   	console.log("scrolled");
      $('header').css("position", "fixed");
      $('header').css("position", "fixed");
      $("#nu").css("display","none")
    }
});

$('li.grt-dropdown > a').on('click', function(e){
	e.preventDefault();
});