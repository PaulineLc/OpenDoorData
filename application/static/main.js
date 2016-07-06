function checkInput(){
	var xmlhttp = new XMLHttpRequest();
	var url = "/getjson/2/Monday";

	xmlhttp.onreadystatechange = function() {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        var data = JSON.parse(xmlhttp.responseText);
        console.log(data);
    }
};
xmlhttp.open("GET", url, true);
xmlhttp.send();
}