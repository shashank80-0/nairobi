$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})


function isNumberKey(evt){
	var charCode = (evt.which) ? evt.which : evt.keyCode;
	if(charCode > 31 && (charCode <48 || charCode >57)){
		return false;
	}
	else{
		return true;
	}
}

var today = new Date();
var dd = today.getDate();
var mm = today.getMonth()+1;  //January is 0
var yyyy = today.getFullYear();
dd = (dd<10) ? "0"+dd : dd;
mm = (mm<10) ? "0"+mm : mm;
today = yyyy+'-'+mm+'-'+dd;
document.getElementById("exampleInputDateOfBirth").setAttribute("max",today);


function validatForm(){

			const nameRegex = (/^[a-zA-Z]+$/);

			const dateRegex = (/^([0-9]{4})-([0-9]{2})-([0-9]{2})$/);

			const emailRegex = (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/);

			const passwordRegex = (/^[A-Za-z0-9@$_]*$/);

			
			var firstName = document.getElementById("exampleInputFirstname");
				if(firstName.value==null || firstName.value==""){
					alert("First name cannot be blank");
					firstName.focus();
					return false;
			}

				if(!nameRegex.test(firstName.value)){
					alert("First name cannot contain numbers, space or special characters");
					firstName.focus();
					return false;
			}


			var lastName = document.getElementById("exampleInputLastname");
				if(lastName.value==null || lastName.value==""){
					alert("Last name cannot be empty");
					lastName.focus();
					return false;
			}

				if(!nameRegex.test(lastName.value)){
					alert("Last name cannot contain numbers, space or special characters");
					lastName.focus();
					return false;
			}
			
			var phone = document.getElementById("exampleInputPhone");
				if(phone.value==null || phone.value=="" || phone.value=="+91-"){
					alert("Phone number cannot be empty");
					phone.focus();
					return false;
				}

				if(phone.value.length!=10){
					alert("Phone number must have 10 digits");
					return false;
				}

			var dob = document.getElementById("exampleInputDateOfBirth");
				if(dob.value==null || dob.value==""){
					alert("Date of birth cannot be empty");
					dob.focus();
					return false;
				}

				if(!dateRegex.test(dob.value)){
					alert("Invalid Date of birth");
					dob.focus();
					return false;
				}

			var email = document.getElementById("exampleInputEmail");
				if(email.value==null || email.value==""){
					alert("Email cannot be empty");
					email.focus();
					return false;
				} 

 				if (!emailRegex.test(email.value)){
    				alert("Invalid email address");
    				email.focus();
    				return false;
				}


			var password = document.getElementById("exampleInputPassword");
				if(password.value==null || password.value==""){
					alert("Password cannot be empty");
					password.focus();
					return false;
				}

				if(password.value.length<8){
					alert("Password must have more than 8 characters");
					return false;
				}

				if(password.value.length>20){
					alert("Password must have less than 20 characters");
					return false;
				}

				if(!passwordRegex.test(password.value)){
					alert("Password cannot contain spaces, special characters, or emoji");
					return false;
				}

			var confirmPassword = document.getElementById("exampleInputConfirmPassword");
				if(confirmPassword.value==null || confirmPassword.value==""){
					alert("Please confirm password");
					confirmPassword.focus();
					return false;
				}

				if(!(password.value==confirmPassword.value)){
					alert("Passwords do not match");
					password.focus();
					return false;
				}

			

		}	
