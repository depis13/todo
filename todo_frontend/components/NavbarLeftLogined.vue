<template>
      <div class="d-flex flex-row">
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle btn btn-hover nav-btn" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Organisations
          </a>
          <ul class="dropdown-menu nav-dropdown-menu">
            <li><NuxtLink class="dropdown-item btn btn-hover nav-btn" to="/organisations">Your organisations</NuxtLink></li>
            <li><NuxtLink class="dropdown-item btn btn-hover nav-btn" to="/organisations/create">Create organisation</NuxtLink></li>
            <li><hr class="dropdown-divider"></li>
            <li><NuxtLink class="dropdown-item btn btn-hover nav-btn" to="/organisations/leave">Leave organisation</NuxtLink></li>
          </ul>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle btn-hover nav-btn btn" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Projects
          </a>
          <ul class="dropdown-menu nav-dropdown-menu">
            <li><NuxtLink class="dropdown-item btn btn-hover nav-btn" to="/projects">Your projects</NuxtLink></li>
            <li><NuxtLink class="dropdown-item btn btn-hover nav-btn" to="/projects/create">Create project</NuxtLink></li>
          </ul>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle btn-hover nav-btn btn" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Tasks
          </a>
          <ul class="dropdown-menu nav-dropdown-menu">
            <li><NuxtLink class="dropdown-item btn btn-hover nav-btn" to="/">1</NuxtLink></li>
            <li><NuxtLink class="dropdown-item btn btn-hover nav-btn" to="/">1</NuxtLink></li>
            <li><hr class="dropdown-divider"></li>
            <li><NuxtLink class="dropdown-item btn btn-hover nav-btn" to="/">1</NuxtLink></li>
          </ul>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle btn-hover nav-btn btn" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Desks
          </a>
          <ul class="dropdown-menu nav-dropdown-menu">
            <li><NuxtLink class="dropdown-item btn btn-hover nav-btn" to="/">3</NuxtLink></li>
            <li><NuxtLink class="dropdown-item btn btn-hover nav-btn" to="/">2</NuxtLink></li>
            <li><hr class="dropdown-divider"></li>

            <li><NuxtLink class="dropdown-item btn btn-hover nav-btn" to="/">1</NuxtLink></li>
          </ul>
        </li>
      </div>
</template>

<style>

</style>