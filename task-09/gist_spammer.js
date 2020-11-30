var message = "Spam Alert"; //spam message
var interval = 1000  ; // in milliseconds
var count = 10 ; //number of times to send
var i = 0 ;
var timer = setInterval(function(){
        document.getElementByID("new_comment_field").innerHTML = message;
        document.querySelector('#partial-new-comment-form-actions>.btn').click();
	i++;
	if(i==count)
	{clearInterval(timer);}
} , interval) ;
    