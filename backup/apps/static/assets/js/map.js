console.log("Starting map initialization...");

// Initialize the Leaflet map
var mymap = L.map('map').setView([53.957, -0.385], 10);

if (mymap) {
    console.log("Map object created successfully.");
} else {
    console.error("Map object creation failed.");
}

// Add a basic tile layer to the map
var baseLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
}).addTo(mymap);

console.log("Tile layer added to the map.");

// Define style and highlight functions
function style(feature) {
    return {
        fillColor: '#92b6f0',
        weight: 1,
        opacity: 1,
        color: '#797c82',
        // dashArray: '3',
        fillOpacity: 0.2
    };
}

function highlightFeature(e) {
    var layer = e.target;

    layer.setStyle({
        weight: 2,
        color: '#797c82',
        dashArray: '',
        fillOpacity: 0.5
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
}

function resetHighlight(e) {
    geojsonLayer.resetStyle(e.target);
}

function onEachFeature(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
        click: function () {
            var catchmentName = feature.properties.EA_WB_ID;
            console.log("Catchment clicked:", catchmentName);
            onCatchmentClick(catchmentName);
        }
    });
}

// Load and add the GeoJSON layer with the defined styles and events
var geojsonLayer;

function loadGeoJSON() {
    $.getJSON('/get_geojson', function(data) {
        console.log("GeoJSON data fetched successfully.");

        geojsonLayer = L.geoJson(data, {
            style: style,
            onEachFeature: onEachFeature
        }).addTo(mymap);

        console.log("GeoJSON layer added to the map.");

        // Add layer control for toggling the GeoJSON layer
        var overlayMaps = {
            "Catchments": geojsonLayer
        };
        L.control.layers(null, overlayMaps).addTo(mymap);
    }).fail(function() {
        console.error("Failed to fetch GeoJSON data.");
    });
}

loadGeoJSON();  // Load the GeoJSON layer when the page loads

// Function to handle click events on catchments
function onCatchmentClick(catchmentName) {
    console.log("Executing onCatchmentClick with:", catchmentName);

    $.ajax({
        type: 'POST',
        url: '/plot',
        contentType: 'application/json',
        data: JSON.stringify({ catchment: catchmentName }),
        success: function(response) {
            console.log("Plot data received:", response);

            var plotData = JSON.parse(response);
            Plotly.newPlot('plot', plotData.data, plotData.layout);
        },
        error: function(error) {
            console.error("Error in onCatchmentClick AJAX request:", error);
        }
    });
}
