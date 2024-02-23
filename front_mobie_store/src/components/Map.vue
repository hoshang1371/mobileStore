<template>
    <h1 style="
    font-weight: 500;
    font-size: 1.8rem;
    font-family: KalamehWeb_Bold;
    margin-bottom: 1rem;
    ">نقشه</h1>
    <div id='map' ref="mapRef"> </div>
</template>
 
<script>
import { onMounted, ref } from 'vue'
export default
    {
        name: 'Map',
        setup() {
            const mapRef = ref(null);
            onMounted(() => {
                const tt = window.tt;


                var map = tt.map({
                    key: 'WFnpaG4CsM4uGDHdiw9BWSPGu2AikmO3',
                    container: mapRef.value,
                    style: 'tomtom://vector/1/basic-main',
                });

                map.addControl(new tt.FullscreenControl());
                map.addControl(new tt.NavigationControl());
                addMarker(map);
            });

            function addMarker(map) {
                const tt = window.tt;
                var location = [59.311996, 32.877231,];
                var popupOffsets = {
                    top: [0, 0],
                    bottom: [0, -30],
                    'bottom-right': [0, -30],
                    'bottom-left': [0, -30],
                    left: [25, -35],
                    right: [-25, -35]
                }
                
                var marker = new tt.Marker().setLngLat(location).addTo(map);
                // var zoom = new tt.Marker().zoom
                var popup = new tt.Popup({ offset: popupOffsets }).setHTML("Your address!");
                marker.setPopup(popup).togglePopup();
                
            }

            return {
                mapRef,
            }
        }
    }
</script>

<style>
#map {
    height: 50vh;
    width: 50vw;
    margin-left: 50px;
}
</style>
