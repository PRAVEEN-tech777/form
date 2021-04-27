import os
from django.http import HttpResponse

  
def sample(request):
    return HttpResponse("this is praveen")

def htmlsample(request):
    data1=""" <!DOCTYPE html>
<html>
<head>
	<title>Form</title>
</head>
<body>

	<form action="#" method="GET" nonvalidate>
		<label>FIRST NAME:</label>
		<input type="text" name="fn"  placeholder="Enter Your First Name" size="25"/>
		<br><br>
		<label>LAST NAME:</label>
		<input type="text" name="fn"  placeholder="Enter you Last name" maxlength="25"/>

		<br>

		<input type="password" name="pass" placeholder="Enter your password" />

		<br><br>
		<textarea rows="5" cols="20">Comment on the class: </textarea>

		<br><BR>
		<select name="dropdown">
			<option value="Maths">Maths</option>
			<option value="Maths">Maths</option>
			<option value="Maths">Maths</option>
		</select>
<BR>
		<br>
		<input type="radio" name="gender" value="male">Male

		<input type="radio" name="gender" value="Female">Female

		<input type="radio" name="gender" value="others">others
		<BR>

		<input type="checkbox" name="java" value="Java">Java

		<input type="checkbox" name="javASCRIPT" value="javASCRIPT" checked>JavasCRIPT
		<input type="checkbox" name="j2EE" value="J2EE">J2EE
		<input type="checkbox" name="ANGULAR" value="ANGULAR">ANGULAR
		<input type="checkbox" name="REACT" value="REACT">REACT

		

		<input type="file" name="fileupload" accept="image/*"><br><br>
		<input type="submit" value="submit">
		<input type="reset" value="reset">

		<BR><BR>

		<button>Login</button> """
    return HttpResponse(data1)

























