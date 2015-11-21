window.addEventListener('load', getCountryName, false );
var lat;
var lon;

function getCountryName(){
    $.ajax( $SCRIPT_ROOT + "/get_country" + "lat?=" + lat + "lon?=" + lon,{ // Nie wiem czy tak powinien wygladac ten url
        success: function (responseText, statusText, jqXHR){
            print(responseText);
        }
    });
}

function getLocalization() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        //x.innerHTML = "Brak obsługi geolokalizacji.";
    }
}

function showPosition(position) {
    lat = position.coords.latitude;
    lon = position.coords.longitude;
}
