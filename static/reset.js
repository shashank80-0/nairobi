function validateForm(){

	var emailAddr = document.getElementById('emailInput');
	if(emailAddr.value==null || emailAddr.value==""){
		alert("Please enter email address");
		emailAddr.focus();
		return false;
	}

	var password = document.getElementById('userPasswordInput');
	if(password.value==null || password.value==""){
		alert("Please enter password");
		password.focus();
		return false;
	}

	var confirmPassword = document.getElementById('userConfirmasswordInput');
	if(confirmPassword.value==null || confirmPassword.value==""){
		alert("Please re-enter password");
		confirmPassword.focus();
		return false;
	}


	if(!(password.value==confirmPassword.value)){
		alert("Passwords do not match");
		password.focus();
		return false;
	}

}