$(document).ready(function(){
	$('.header>img').hover(function(event){ 
		var NeeWidth=parseInt($(this).css('width').replace('px',''))+50+'px'
		$(this).animate({width: NeeWidth}, 300); 
	}, function(event){ 
		var NeeWidth=parseInt($(this).css('width').replace('px',''))-50+'px' 
		$(this).animate({width: NeeWidth}, 300); 
	}); 
});