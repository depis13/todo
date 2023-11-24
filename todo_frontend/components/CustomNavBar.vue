<template>
<nav class="navbar navbar-expand-lg bg-body-tertiary fixed-top">

<div class="navbar-container vh-10 container-fluid gap-2">
  <NuxtLink to="/" class="btn btn-hover main-btn" data-bs-toggle="button" style="--bs-btn-font-size: 1.4rem;">TaskTracker</NuxtLink>
  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon" style="--bs-navbar-active-color: #b6c2cf; --bs-navbar-brand-color: #b6c2cf;"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarText">
    <ul class="navbar-nav me-auto mb-2 mb-lg-0">

      <div v-if="userStore.user.isAuthenticated" class="d-flex flex-row">
        <NavbarLeftLogined></NavbarLeftLogined>
      </div>
      <div v-else>
        <NavbarLeftNotLogined></NavbarLeftNotLogined>
      </div>
    </ul>

  <div class="d-flex gap-2" style="margin-right: 40px;">

      <template v-if="userStore.user.isAuthenticated">
        <NavbarRightLogined :userEmail="userStore.user.email"></NavbarRightLogined>
      </template>
      <template v-else>
        <NavbarRightNotLogined></NavbarRightNotLogined>
      </template>

  </div>
  </div>
</div>
</nav>
</template>

<script setup>

import {useUserStore} from '@/stores/user.js'

const userStore = useUserStore()
</script>

<style>

</style>
