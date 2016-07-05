function checkInput(){
	var xmlhttp = new XMLHttpRequest();
	var url = "/getjson/2/Monday";

	xmlhttp.onreadystatechange = function() {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        var d = JSON.parse(xmlhttp.responseText);
        console.log(d[0]);
    }
};
xmlhttp.open("GET", url, true);
xmlhttp.send();
}