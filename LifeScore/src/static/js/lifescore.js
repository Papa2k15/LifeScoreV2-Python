
function addMission() {
	var title = $("input[type='text']#title").val();
	var description = $("textarea#description").val();
	var start = $("input[type='text']#start").val();
	var goal = $("input[type='number']#goal").val();
	var units = $("input[type='text']#units").val();
//	alert(title);
//	alert(description);
//	alert(start);
//	alert(goal);
//	aler(units);
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
					$("div.mission-message").show();
				} else {
					$("div.mission-message").hide();
				}
			}
		}
	}
	xmlhttp.open("GET","/add_user_mission/?title="+title+"&description="+description+
			"&start="+start+"&goal="+goal+"&units="+units
			,true);
	xmlhttp.send();
}