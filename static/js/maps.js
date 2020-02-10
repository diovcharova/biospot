function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 17,
        center: {
            lat: 42.497144,
            lng: 27.474846
        }
    });

    var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    var locations = [
        { lat: 42.497035, lng: 27.474890 },
    ];

    var markers = locations.map(function(location, i) {
        return new google.maps.Marker({
            position: location,
        });
    });

    var markerCluster = new MarkerClusterer(map, markers, { imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m' });
}