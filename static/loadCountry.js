window.addEventListener('load', getCountryName, false );
var lat;
var lon;

function getCountryName(){
    getLocalization();
    console.info(lat);
    console.info(lon);

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
    console.info(lat);
    console.info(lon);
    $.ajax( document.URL.substring(0, document.URL.length - 11) + "get_country?" + "lat?=" + lat + "&" + "lon?=" + lon,{ // Nie wiem czy tak powinien wygladac ten url
        success: function (responseText, statusText, jqXHR){
            print(responseText);
        }
    });
}
