
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    }
}
function showPosition(position) {

    $.get("http://maps.googleapis.com/maps/api/geocode/json?latlng=" +position.coords.latitude + "," + position.coords.longitude + "&sensor=true,callback",
        function(results){
            if(results.results.length > 0){
                console.log(results);
                address = results.results[0].address_components[0]['long_name'];
                console.log(address);
                s = 'Jak podoba Ci się ' + address + ' ?';
                $('#text').text(s);
            } else {
                console.log('unnamed address');
            }
        }
    );
}



