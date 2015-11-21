$(document).ready(function () {
	//Button for voting - phrasebook items
	$(".foreign").click(function (event) {
		event.preventDefault();

		$(this).siblings(".vote").fadeIn();

		$(this).next().children("button").click(function (event) {
			$(this).parent().fadeOut();
		});
	});	
});