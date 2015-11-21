function updateMissionsForUser(id) {
	if (window.XMLHttpRequest) {
		xmlhttp=new XMLHttpRequest();
	} else { 
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange=function() {
		if (xmlhttp.readyState==4 && xmlhttp.status==200) {
			if (xmlhttp.responseText.length > 0){
				$("tr").remove();
				console.log(xmlhttp.responseText);
				$("div.user-mission-table").html(xmlhttp.responseText);
			}
		}
	}
	xmlhttp.open("GET","/refresh_missions/",true);
	xmlhttp.send();
}

function addMission(id) {
	var title = $("input[type='text']#title").val();
	var description = $("textarea#description").val();
	var start = $("input[type='text']#start").val();
	var goal = $("input[type='number']#goal").val();
	var units = $("input[type='text']#units").val();
	if(title.length <= 0 || description.length <= 0 ||
			start.length <= 0 || goal.length <= 0 ||
			units.length <=0 ){
		alert("All fields are required.");
		return;
	}
	if (window.XMLHttpRequest) {
		xmlhttp=new XMLHttpRequest();
	} else { 
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange=function() {
		if (xmlhttp.readyState==4 && xmlhttp.status==200) {
			if (xmlhttp.responseText.length > 0){
				if (xmlhttp.responseText == "true"){
					document.getElementById("mission-status").innerHTML = "Success!";
					document.getElementById("mission-message").innerHTML = "Mission Added Succesfully.";
					$("input[type='text']#title").val("");
					$("textarea#description").val("");
					$("input[type='number']#goal").val("");
					$("input[type='text']#units").val("");
					updateMissionsForUser(id);
				} else {
					document.getElementById("mission-status").innerHTML = "Error!";
					document.getElementById("mission-message").innerHTML = "Error adding mission. Try again.";
				}
			}
		}
	}
	xmlhttp.open("GET","/add_user_mission/?title="+title+"&description="+description+
			"&start="+start+"&goal="+goal+"&units="+units
			,true);
	xmlhttp.send();
}

function updateFavColor(){
	if (window.XMLHttpRequest) {
		xmlhttp=new XMLHttpRequest();
	} else { 
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	var color = $("input[type='hidden']#favcolor").val();
	xmlhttp.open("GET","/updatefavcolor/?color="+encodeURIComponent(color),true);
	xmlhttp.send();
}