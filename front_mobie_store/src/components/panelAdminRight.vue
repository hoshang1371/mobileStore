<template>
    <div class="container_right">
        <a href="">داشبورد</a>
        <a href="">سفارشات پرداخت نشده</a>
        <a href="">تاریخچه سفارشات</a>
        <a href="">علاقه مندی ها</a>
        <a href="">نظرات</a>
        <router-link to="/changePasswordPanelAdmin"> عملیات رمز عبور </router-link>
        <router-link to="/phoneNumberPanelAdmin">شماره ی شما</router-link>
    </div>
</template>

<script>
export default{
    name:"panelAdminRight",
}
</script>