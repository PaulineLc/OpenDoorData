var map;
function initialize() {
	var mapProp = {
		center: new google.maps.LatLng(53.3075343,-6.2215082),
		zoom: 16,
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

google.maps.event.addDomListener(window, 'load', initialize);


