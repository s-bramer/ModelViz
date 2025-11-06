// Declare the GeoJSON layer variables
var polygonLayer;
var markerLayer;
var polylineLayer;

// Initialize the Leaflet map
var mymap = L.map('map').setView([53.957, -0.385], 10);

// Add a basic tile layer to the map
var baseLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
}).addTo(mymap);

// Create a layer control object
var layerControl = L.control.layers(null, null, { collapsed: true }).addTo(mymap);

// Style and event handling for Polygon layer
function stylePolygon(feature) {
    return {
        fillColor: '#92b6f0',
        weight: 1,
        opacity: 1,
        color: '#797c82',
        fillOpacity: 0.4
    };
}

function onPolygonFeature(feature, layer) {
    layer.bindTooltip(feature.properties.EA_WB_ID, { // Tooltip displays the 'name' property
        permanent: false, // Tooltip only shows on hover
        direction: 'auto'
    });
    layer.on({
        mouseover: function(e) {
            var layer = e.target;
            layer.setStyle({
                weight: 2,
                color: '#0074D9',
                fillOpacity: 0.7
            });
            layer.bringToFront();
        },
        mouseout: function(e) {
            polygonLayer.resetStyle(e.target);
        },
        click: function(e) {
            var catchmentName = feature.properties.EA_WB_ID;  // Replace with actual property name
            console.log("Catchment clicked:", catchmentName);
            // polygonLayer.resetStyle(e.target);
            onCatchmentClick(catchmentName);
        }
    });
}

// Style and event handling for Marker layer
function markerIcon(feature) {
    return L.icon({
        iconUrl: 'apps/static/assets/images/dot.png',  // Replace with actual icon path
        iconSize: [30, 30], // Size of the icon
        iconAnchor: [15, 15], // Anchor point of the icon
        popupAnchor: [1, -34], // Popup anchor
        // shadowUrl: 'apps/static/assets/images/dot.png',  // Shadow icon path
        // shadowSize: [41, 41] // Size of the shadow
    });
}

function onMarkerFeature(feature, layer) {
    layer.setIcon(markerIcon(feature));
    layer.bindTooltip(feature.properties.EYCModelID, { // Tooltip displays the 'name' property
        permanent: false, // Tooltip only shows on hover
        direction: 'top'
    });
    layer.on({
        mouseover: function(e) {
            var layer = e.target;
            var highlightIcon = L.icon({
                iconUrl: 'apps/static/assets/images/dot_highlighted.png',  // Replace with actual highlighted icon path
                iconSize: [30, 30], // Size of the icon
                iconAnchor: [15, 15], // Anchor point of the icon
                popupAnchor: [1, -34], // Popup anchor
                // shadowUrl: 'apps/static/assets/images/dot_highlighted.png',  // Shadow icon path
                // shadowSize: [41, 41] // Size of the shadow
            });
            layer.setIcon(highlightIcon);
        },
        mouseout: function(e) {
            var layer = e.target;
            var originalIcon = markerIcon(layer.feature);
            layer.setIcon(originalIcon);
        },
        click: function(e) {
            var featureName = e.target.feature.properties.name;  // Replace with actual property name
            console.log("Marker clicked:", featureName);
        }
    });
}

// Style and event handling for Polyline layer
function stylePolyline(feature) {
    return {
        color: '#1f6eed',
        weight: 1,
        opacity: 0.7
    };
}

//Polyline interactions
// function onPolylineFeature(feature, layer) {
//     layer.bindTooltip(feature.properties.name, { // Tooltip displays the 'name' property
//         permanent: false, // Tooltip only shows on hover
//         direction: 'auto'
//     });
//     layer.on({
//         mouseover: function(e) {
//             var layer = e.target;
//             layer.setStyle({
//                 color: '#FF851B',
//                 weight: 2,
//                 opacity: 1
//             });
//         },
//         mouseout: function(e) {
//             polylineLayer.resetStyle(e.target);
//         },
//         click: function(e) {
//             var featureName = e.target.feature.properties.name;  // Replace with actual property name
//             console.log("Polyline clicked:", featureName);
//         }
//     });
// }

// Function to load GeoJSON and add it to the map
function loadGeoJSON(url, styleFunc, onEachFeatureFunc, layerVarName, layerName) {
    $.getJSON(url, function(data) {
        console.log(layerVarName + " GeoJSON data fetched successfully.");

        var geojsonLayer = L.geoJson(data, {
            style: styleFunc,
            onEachFeature: onEachFeatureFunc
        }).addTo(mymap);

        console.log(layerVarName + " GeoJSON layer added to the map.");

        // Assign to the correct layer variable
        if (layerVarName === 'polygonLayer') {
            polygonLayer = geojsonLayer;
        } else if (layerVarName === 'markerLayer') {
            markerLayer = geojsonLayer;
        } else if (layerVarName === 'polylineLayer') {
            polylineLayer = geojsonLayer;
        }

        // Add the layer to the unified layer control
        layerControl.addOverlay(geojsonLayer, layerVarName);
    }).fail(function() {
        console.error("Failed to fetch " + layerVarName + " GeoJSON data.");
    });
}

// Load the GeoJSON layers
loadGeoJSON('/get_geojson/Catchments_WGS84', stylePolygon, onPolygonFeature, 'polygonLayer'); //onPolygonFeature
loadGeoJSON('/get_geojson/Modelled_GWAbs_PWS_WGS84', null, onMarkerFeature, 'markerLayer');  // No style function needed for markers
loadGeoJSON('/get_geojson/Rivers_WGS84', stylePolyline, null, 'polylineLayer'); //onPolylineFeature

// Function to handle click events on all features
function onCatchmentClick(catchmentName) {
    console.log("Executing onCatchmentClick with:", catchmentName);

    $.ajax({
        type: 'POST',
        url: '/plot',
        contentType: 'application/json',
        data: JSON.stringify({ catchment: catchmentName }),
        success: function(response) {
            // console.log("Plot data received:", response);

            var plotData = JSON.parse(response);
            Plotly.newPlot('plot', plotData.data, plotData.layout);
        },
        error: function(error) {
            console.error("Error in onCatchmentClick AJAX request:", error);
        }
    });
}
