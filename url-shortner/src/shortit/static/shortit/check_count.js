$(document).ready(function(){
	$("#count_click").on('click', function(){

		var shorted_url 	= $("#short_url").val();
		var shortcode 		= "";
		var csrf 		  	=	$("[name='csrfmiddlewaretoken']").val();

		// to be changed in production
		var l = shorted_url.length;
		shortcode = shorted_url.slice(22);

		if( shortcode === "" ) {
			alert("Not a valid url.");
		}
		else {

			$.ajax({

				type : "POST",
				url  : "/shortcode/click_count/",

				data : {
					'shortcode' 			: shortcode,
					'csrfmiddlewaretoken'	: csrf,
				},

				success : function(data){
					// console.log(data)

					if(data['is_available']){

						$("#counter1").empty();
						$("#counter").empty();
						$("#counter1").text("This url does not exist");

					}else{

						$("#counter1").empty();
						$("#counter").empty();
						$("#counter").text("Total click : " + data['total_click'] );
					}
				},

				error : function(data) {
					console.log("Something went wrong...!");
				},

			});

		}

	});
});