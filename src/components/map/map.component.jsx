import React from 'react'
import { render } from 'react-dom'
import { Map, Marker, Popup, TileLayer } from 'react-leaflet'
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import { LatLng } from 'leaflet';

import './map.styles.scss';


delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
    iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
    iconUrl: require('leaflet/dist/images/marker-icon.png'),
    shadowUrl: require('leaflet/dist/images/marker-shadow.png')
});

const position = [60.1660,24.9400];

const redMarker = new L.Icon({
  iconUrl: require('../../assets/marker-icon-2x-red.png'),
  iconRetinaUrl: require('../../assets/marker-icon-2x-red.png'),
  shadowUrl: require('../../assets/marker-shadow.png'),
	shadowSize: [41, 41],
  shadowAnchor: null,
  iconSize: new L.Point(60, 75),
  className: 'leaflet-div-icon',
  iconSize: [25, 41],
	iconAnchor: [12, 41],
  popupAnchor: [1, -34]
});

export { redMarker };


var json = [];


class My_Map extends React.Component {

  constructor() {
    super();
    const windowUrl = window.location.search;
    const params = new URLSearchParams(windowUrl);
    var arr = params.get("ids").split(",");
    console.log(arr);
    
    var eans_array = [];

    for(let i=0;i<arr.length;i++) {
      eans_array.push({"ean": eans_array[i]});
    }


      fetch('http://127.0.0.1:8000/api/optimise_market_food_waste', {
        method: 'post',
        body: JSON.stringify({"items":[{"ean":eans_array}], "user_lat":60.1618222, "user_lon":24.737745, "max_time":10})})
       .then((response) => response.json())
       .then((responseJson) => {
          console.log(responseJson);
          json = responseJson;
          for(let i=0;i<responseJson["best_ranked_markets"].length;i++) {
            const {markers} = this.state;
            markers.push(new LatLng(responseJson["best_ranked_markets"][i]["Coordinate"]["Latitude"], responseJson["best_ranked_markets"][i]["Coordinate"]["Longitude"]));
            this.setState({markers});
          }
      })
       .catch((error) => {
         console.error(error);
       })

    this.state = {
      markers: []
    };
  }


  render() {
    
    return(
      <Map center={position} zoom={10} style={{ width: '100%', height: '100%' }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution="&copy; <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
      />
      <Marker
        position={position}
        icon={ redMarker }
        >
      </Marker>

      {this.state.markers.map((position, idx) => 
          <Marker key={`marker-${idx}`} position={position}>
          <Popup>
              <span>{json["best_ranked_markets"][idx] ? json["best_ranked_markets"][idx]["Name"] : ""}</span>
              <br></br>
              <a target="_blank" href={json["best_ranked_markets"][idx] ? json["best_ranked_markets"][idx]["gmapsLink"] : ""}>Directions</a>
          </Popup>
        </Marker>
      )}
    </Map>
    );
  }
}

export default My_Map;