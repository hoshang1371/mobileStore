<template>
    <div>
        <div class="content">
            <panelAdminRight/>

            <div class="container_left">

            </div>
        </div>
    </div>
</template>

<script>
import panelAdminRight from '@/components/panelAdminRight.vue'

export default{
    name:"HistoryPanelAdmin",
    components:{
        panelAdminRight,    
    },
}
</script>