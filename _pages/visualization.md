---
permalink: visualization
title: Visualization
path: "assets/images/tiles"
---

<head>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css" integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ==" crossorigin=""/>
  <script src="https://unpkg.com/leaflet@1.6.0/dist/leaflet.js" integrity="sha512-gZwIG9x3wUXg2hdXF6+rVkLF/0Vi9U8D2Ntg4Ga5I5BZpVkVxlJWbSQtXPSiUTtC0TjtGOmxa1AJPuV0CPthew==" crossorigin=""></script>
  
  <style>
    .info {
      padding: 6px 8px;
      font: 14px/16px Arial, Helvetica, sans-serif;
      background: white;
      background: rgba(255,255,255,0.8);
      box-shadow: 0 0 15px rgba(0,0,0,0.2);
      border-radius: 5px;
    }
    .info h4 {
      margin: 0 0 5px;
      color: #777;
    }
    .legend {
      line-height: 18px;
      color: #555;
    }
    .legend i {
      width: 12px;
      height: 12px;
      float: left;
      margin-right: 8px;
      opacity: 0.7;
    }
    </style>
</head>

<div id="mapid" style="width: 600px; height: 400px;"></div>
<script>
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var myObj = JSON.parse(this.responseText);
      window.embedding = myObj;
      min_x = -30.5003;
      min_y = -29.6366
      max_x = 29.2283;
      max_y = 29.5328;
      resolution = 512;
      for (var key in myObj) {
        var x, y;
        [x, y] = myObj[key];
        myObj[key] = [(x - min_x) / (max_x - min_x) * resolution, ((y - min_y) / (max_y - min_y) - 1) * resolution];
      }
      console.log(window.embedding["Q5"]);
    }
  };
  xmlhttp.open("GET", '{{ "assets/json/entity2emb_top100k.json" | absolute_url }}', true);
  xmlhttp.send();
  
	var mymap = L.map('mapid', {crs: L.CRS.Simple, zoomSnap: 0}).setView([-256, 256], 0.5);

	L.tileLayer('{{ page.path | absolute_url }}/{z}_{x}_{y}.png', {
    minZoom: 0,
		maxZoom: 4,
		attribution: 'Wikidata5m | RotatE Embedding',
		id: 'mapbox/streets-v11',
		tileSize: 512,
		zoomOffset: 0
	}).addTo(mymap);
  
  var shelterMarkers = new L.FeatureGroup();
  
  var legend = L.control({position: 'bottomright'});
  legend.onAdd = function (map) {
    var div = L.DomUtil.create('div', 'info legend'),
        grades = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#d3d3d3'],
        labels = ['human', 'taxon', 'film', 'human settlement', 'album', 'else'];

    // loop through our density intervals and generate a label with a colored square for each interval
    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            '<div><i style="background:' + grades[i] + '"></i>' + labels[i] + '</div>';
    }

    return div;    
  }
  legend.addTo(mymap);
  
  var info = L.control();
  info.onAdd = function (map) {
      var div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
	  window.div = div;
      return div;
  };
  info.addTo(mymap);

  // shelterMarkers.addLayer(L.marker([-256.878041142838, 322.3327155313606]).addTo(mymap).bindTooltip("Bengio", {permanent: true}));  
  // shelterMarkers.addLayer(L.marker([-257.1287691787817, 323.6650758702294]).addTo(mymap).bindTooltip("LeCun", {permanent: true}));  
  // shelterMarkers.addLayer(L.marker([-257.0684177413557, 323.9724964773171]).addTo(mymap).bindTooltip("Hinton", {permanent: true}));  
  // shelterMarkers.addLayer(L.marker([-257.32842403922695, 323.2936450689255]).addTo(mymap).bindTooltip("Jordan (CS)", {permanent: true}));  
  // shelterMarkers.addLayer(L.marker([-262.1349886720287, 304.46255189957185]).addTo(mymap).bindTooltip("Jordan (Basketball)", {permanent: true}));  
  // shelterMarkers.addLayer(L.marker([-252.60821244990967, 246.43622765610672]).addTo(mymap).bindTooltip("Deep Learning", {permanent: true}));  
  // shelterMarkers.addLayer(L.marker([-250.56101801892993, 244.37838341377156]).addTo(mymap).bindTooltip("Machine Learning", {permanent: true}));  
  // shelterMarkers.addLayer(L.marker([-283.5808520767456, 247.5441610834172]).addTo(mymap).bindTooltip("Google", {permanent: true}));  
  // shelterMarkers.addLayer(L.marker([-377.24063606105085, 288.8077179085865]).addTo(mymap).bindTooltip("Facebook", {permanent: true}));  
  // shelterMarkers.addLayer(L.marker([-161.4393378596098, 218.10161184035312]).addTo(mymap).bindTooltip("Titanic", {permanent: true}));  
  // shelterMarkers.addLayer(L.marker([-157.8275670848086, 224.10973234544142]).addTo(mymap).bindTooltip("Frozen", {permanent: true}));  
  
  function GetNearestNeighbor(x, y) {
    var distance = Infinity, target;
    for (var key in window.embedding) {
      var tx, ty;
      [tx, ty] = window.embedding[key];
      var d = Math.pow(tx - x, 2) + Math.pow(ty - y, 2);
      if (d < distance) {
        distance = d;
        target = key;
      }
    }
    return [target, distance]
  }
  
  mymap.on('click', function(e) {
    var click_x, click_y, target, _;
    click_x = e.latlng.lng;
    click_y = e.latlng.lat;
    target = GetNearestNeighbor(click_x, click_y)[0];
    window.open(`https://www.wikidata.org/wiki/${target}`);
  } );
  
  mymap.on('mousemove', function(e) {
    var click_x, click_y, target, _;
    click_x = e.latlng.lng;
    click_y = e.latlng.lat;
    target = GetNearestNeighbor(click_x, click_y)[0];
	
    window.div.innerHTML = `(${click_x}, ${click_y})<br>` + `NN: ${target} ${window.embedding[target]}`;
  } );
  
  // mymap.on('zoomend', function() {
  //   if (mymap.getZoom() < 1){
  //           mymap.removeLayer(shelterMarkers);
  //   }
  //   else {
  //           mymap.addLayer(shelterMarkers);
  //       }
  // });

</script>