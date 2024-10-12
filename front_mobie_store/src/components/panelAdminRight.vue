<template>
    <div class="container_right">
        <a href="">داشبورد</a>
        <router-link to="/NoPayOrder"> سفارشات پرداخت نشده </router-link>
        <router-link to="/HistoryPanelAdmin"> تاریخچه سفارشات </router-link>
        <router-link to="/LikedPanelAdmin"> علاقه مندی ها </router-link>
        <router-link to="/CommentsPanelAdmin"> نظرات </router-link>
        <router-link to="/changePasswordPanelAdmin"> عملیات رمز عبور </router-link>
        <router-link to="/phoneNumberPanelAdmin">شماره ی شما</router-link>
    </div>
</template>

<script>
export default{
    name:"panelAdminRight",
}
</script>