$(document).ready(function(){
	$('.header>img').hover(function(event){ 
		var NeeWidth=parseInt($(this).css('width').replace('px',''))+30+'px'
		$(this).animate({width: NeeWidth}, 193); 
	}, function(event){ 
		var NeeWidth=parseInt($(this).css('width').replace('px',''))-30+'px' 
		$(this).animate({width: NeeWidth}, 193); 
	}); 
});