/*function showPassword() {
    
    var key_attr = $('#key').attr('type');
    
    if(key_attr != 'text') {
        
        $('.checkbox').addClass('show');
        $('#key').attr('type', 'text');
        
    } else {
        
        $('.checkbox').removeClass('show');
        $('#key').attr('type', 'password');
        
    }
    
}*/


/**function username_validation(mx,my) {
	var username = document.registration.getElementById('username');
	var username_len = username.value.length;
	if(username_len == 0 || username_len>=my || username_len< mx) {
		alert("User Id should not be empty / length be between "+mx+" to "+my);
		username.focus();
		return false;
	}
	
	return true;
}*/

function password_validation() {
	var password = document.getElementById('password');
	var cpassword=document.getElementById('cpassword');
	
	if(password!=cpassword){
		alert("Password mismatch");
		password.focus();
		return false;
	}
	else{
		return true;
	}
}

function checkPass() {
	var pass1 = document.getElementById('password');
	var pass2 = document.getElementById('cpassword');
	var goodColor = "#66cc66";
	var badColor = "#ff6666";	
	if(pass1.value == pass2.value) {
		pass2.style.backgroundColor = goodColor;
		message.style.color = goodColor;
		message.innerHTML = "Passwords Match!";
	}
	else
	{
		alert("password not matched");		
		pass2.style.backgroundColor = badColor;
		message.style.color = badColor;
		message.innerHTML = "Passwords Mismatch!"
	}
}
