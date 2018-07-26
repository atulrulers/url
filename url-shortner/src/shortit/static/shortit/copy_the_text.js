$(document).ready(function(){

	$("#copy").on('click', function(){
		var shorted_url = $("#shorted_url");
		// select the text to be copied
		$(shorted_url).select();
		// copy the selected text
		document.execCommand("copy");
	});
});
