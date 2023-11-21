<template>
  <div>
    <CustomNavBar />
    <NuxtPage/>
  </div>
</template>

<script setup>

import {useUserStore} from '@/stores/user.js'

const userStore = useUserStore()
</script>

<style scoped>
.navbar{
    background-color: #1d2125;

}

.btn {
    color: #b6c2cf;
}
.btn-hover {
  --bs-btn-font-size: 1.rem;
  border: none;
}
.btn-hover:hover {
  background-color: #272d33; /* Adjust the color for hover effect */
  color: #fff; /* Adjust text color on hover */
  border: none;
}

</style>