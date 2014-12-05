$( window ).load(function() {
	$("a.reference").fluidbox({stackIndexDelta: 1000});
	var scrollAnchor = function(href) {
		href = typeof(href) == "string" ? href : $(this).attr("href");
		if(!href) 
			return;
		var fromTop = 75;
		if(href.charAt(0) == "#") {
			var $target = $(href);
			if($target.length) {
				$('html, body').animate({ scrollTop: $target.offset().top - fromTop });
			}
		}
	}    
	scrollAnchor(window.location.hash);
	$("body").on("click", "a", scrollAnchor);
});
