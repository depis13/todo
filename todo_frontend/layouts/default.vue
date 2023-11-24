<template>
  <div>
    <CustomNavBar />
    <NuxtPage/>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
const userStore = useUserStore()
console.log(userStore)
onMounted(() => {
  userStore.initStore()
})
</script>


<style scoped>
.navbar{
    background-color: #1d2125;

}
.nav-dropdown-menu {
  background-color: #1d2125;
}
.nav-btn {
  --bs-btn-font-size: 1.rem;
  border: none;
  color: #b6c2cf;
}
.nav-btn:hover {
  background-color: #272d33;
  color: #fff;
  border: none;
  --bs-btn-font-size: 1.rem;
}

.nav-dropdown-menu {
  background-color: #1d2125;
}

/* .btn {
    color: #b6c2cf;
}
/* .dropdown-item{
  color: #b6c2cf;
} */


/* .nav-item.dropdown ul.dropdown-menu li {
    list-style-type: none;
} */
/* .dropdown-divider {
  --bs-dropdown-divider-bg: #b6c2cf;
} */
/* .navbar{
    background-color: #1d2125;

} */
/* .nav-link {
  color: #b6c2cf;
} */
/* .nav-link:hover {
  --bs-btn-font-size: 1.rem;
  border: none;
} */
/* .btn {
    color: #b6c2cf;
} */
/* .dropdown-item{
  color: #b6c2cf;
} */
/* .btn-hover nav-btn {
  --bs-btn-font-size: 1.rem;
  border: none;
} */

/*
.btn-hover {
  --bs-btn-font-size: 1.rem;
  border: none;
}
.btn-hover:hover {
  background-color: #272d33;
  color: #fff;
  border: none;
} */


</style>