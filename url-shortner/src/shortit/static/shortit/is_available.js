$(document).ready(function(){
	// This is to check on runtime whether custom url is present or not
	$("#id_shortcode").on('input', function(){
		var shortcode     = this.value ;
		var csrf 		  = $("[name='csrfmiddlewaretoken']").val();
		var toshow_error  = $("#is_available");
		var shortcode_len = shortcode.length;

		$.ajax({
			type : 'POST',
			url  : '/shortcode/is_available/'	,

			data : {
				'shortcode' 			: shortcode,
				'csrfmiddlewaretoken'	: csrf,
			},

			success : function(data){
				// console.log(data);
				if(!data['is_available']){
					$(toshow_error).text('This custom url is already taken');
				}else{
					$(toshow_error).empty();
				}
			},

			error : function(data){
				console.log("Failing")
			},

		});

	});
});

// tool tip 
$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();   
});


// check link count tooltip

$(document).ready(function(){
	$("#checkCount").tooltip();
});


