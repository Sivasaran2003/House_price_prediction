function onPageLoad() {
    console.log("document loaded")
    var url = "http://127.0.0.1:5000/get_location_names";
    $.get(url,function(data,status)) {
        console.log("got response for get_locations_names request...");
        if(data) {
            var locs = data.locations;
            var locations = documnet.querySelector()
        }
    }
}