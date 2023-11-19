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
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle btn-hover btn" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Organisations
          </a>
          <ul class="dropdown-menu">
            <li><NuxtLink class="dropdown-item btn btn-hover" to="/organisations">Your organisations</NuxtLink></li>
            <li><NuxtLink class="dropdown-item btn btn-hover" to="/organisations/create">Create organisation</NuxtLink></li>
            <li><hr class="dropdown-divider"></li>
            <li><NuxtLink class="dropdown-item btn btn-hover" to="/organisations/leave">Leave organisation</NuxtLink></li>
          </ul>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle btn-hover btn" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Projects
          </a>
          <ul class="dropdown-menu">
            <li><NuxtLink class="dropdown-item btn btn-hover" to="/projects">Your projects</NuxtLink></li>
            <li><NuxtLink class="dropdown-item btn btn-hover" to="/projects/create">Create project</NuxtLink></li>
          </ul>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle btn-hover btn" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Tasks
          </a>
          <ul class="dropdown-menu">
            <li><NuxtLink class="dropdown-item btn btn-hover" to="/">1</NuxtLink></li>
            <li><NuxtLink class="dropdown-item btn btn-hover" to="/">1</NuxtLink></li>
            <li><hr class="dropdown-divider"></li>
            <li><NuxtLink class="dropdown-item btn btn-hover" to="/">1</NuxtLink></li>
          </ul>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle btn-hover btn" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Desks
          </a>
          <ul class="dropdown-menu">
            <li><NuxtLink class="dropdown-item btn btn-hover" to="/">3</NuxtLink></li>
            <li><NuxtLink class="dropdown-item btn btn-hover" to="/">2</NuxtLink></li>
            <li><hr class="dropdown-divider"></li>

            <li><NuxtLink class="dropdown-item btn btn-hover" to="/">1</NuxtLink></li>
          </ul>
        </li>
      </div>
      <div v-else>
        <li class="nav-item">
          <NuxtLink to="/features" class="btn btn-hover" data-bs-toggle="button">features</NuxtLink>
        </li>
      </div>
    </ul>

  <div class="d-flex gap-2">

      <template v-if="userStore.user.isAuthenticated">
        <!-- <NuxtLink to="/profile" class="btn btn-hover" data-bs-toggle="button">{{userStore.user.email}}</NuxtLink> -->
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle btn-hover btn" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            {{userStore.user.email}}
          </a>
          <ul class="dropdown-menu">
            <li><NuxtLink class="dropdown-item btn btn-hover" to="/organisations">Profile</NuxtLink></li>
            <li><hr class="dropdown-divider"></li>
            <li><NuxtLink class="dropdown-item btn btn-hover" to="/organisations">Your organisations</NuxtLink></li>
            <li><NuxtLink class="dropdown-item btn btn-hover" to="/organisations/create">Create organisation</NuxtLink></li>
          </ul>
        </li>
      </template>
      <template v-else>
        <NuxtLink to="/login" class="btn btn-hover" data-bs-toggle="button">Log in</NuxtLink>
        <NuxtLink to="/signup" class="btn btn-hover" data-bs-toggle="button">Sign up</NuxtLink>
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

<style scoped>
.nav-item.dropdown ul.dropdown-menu li {
    list-style-type: none;
}
.navbar{
    background-color: #1d2125;

}
.nav-link {
  color: #b6c2cf;
}
.nav-link:hover {
  --bs-btn-font-size: 1.rem;
  border: none;
}
.btn {
    color: #b6c2cf;
}
.dropdown-item{
  color: #b6c2cf;
}
.dropdown-menu {
  background-color: #1d2125;
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
