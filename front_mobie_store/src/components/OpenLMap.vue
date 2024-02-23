<template>
    <div ref="map-root" style="width: 100%; height: 100%">
    </div>
  </template>
    
  <script>
  import View from 'ol/View'
  import Map from 'ol/Map'
  import TileLayer from 'ol/layer/Tile'
  import OSM from 'ol/source/OSM'
  
  // importing the OpenLayers stylesheet is required for having
  // good looking buttons!
  import 'ol/ol.css'
  
  
  import Feature from 'ol/Feature.js';
  import Point from 'ol/geom/Point.js';
  import { Circle, Fill, Icon, Stroke, Style, Text } from 'ol/style.js';
  import {Vector as VectorSource} from 'ol/source.js';
  import { Vector as VectorLayer} from 'ol/layer.js';
  
  export default {
    name: 'OpenLMap',
    components: {},
    props: {},
    mounted() {
      const iconFeature = new Feature({
        geometry: new Point([6591900.0, 3879800.0]),
        name: 'Null Island',
        population: 4000,
        rainfall: 500,
      });
  
      const iconStyle = new Style({
        image: new Icon({
          anchor: [0.5, 46],
          anchorXUnits: 'fraction',
          anchorYUnits: 'pixels', 
          // src: './assets/loc.png',
          src: require('../assets/icons/loc.png'),
        }),
      });
      iconFeature.setStyle(iconStyle);
  
      const vectorSource = new VectorSource({
        features: [iconFeature],
      });
  
      const vectorLayer = new VectorLayer({
        source: vectorSource,
      });
  
      // this is where we create the OpenLayers map
      new Map({
        // the map will be created using the 'map-root' ref
        target: this.$refs['map-root'],
        layers: [
          // adding a background tiled layer
          new TileLayer({
            source: new OSM() // tiles are served by OpenStreetMap
          }),
          vectorLayer
        ],
  
        // the map view will initially show the whole world
        view: new View({
          zoom: 17,
          center: [6591900.0, 3879700.0],
          constrainResolution: true
        }),
      })
    },
  }
  </script>