import React from 'react';

import My_Map from '../../components/map/map.component';

import './mappage.styles.scss';
import 'leaflet/dist/leaflet.css';

const MapPage = () => (
  <div className='mappage'>
    <My_Map />
  </div>
);

export default MapPage;
