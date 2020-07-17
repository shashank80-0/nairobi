function validateForm(){

	var emailAddr = document.getElementById('emailInput');
	if(emailAddr.value==null || emailAddr.value==""){
		alert("Please enter email address");
		emailAddr.focus();
		return false;
	}

}