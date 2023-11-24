<template>
    <li class="nav-item dropdown list-unstyled">
        <a class="nav-link dropdown-toggle btn btn-hover nav-btn" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
        {{userEmail}}
        </a>
        <ul class="dropdown-menu nav-dropdown-menu">
            <li><NuxtLink class="dropdown-item btn btn-hover nav-btn" to="/profile">Profile</NuxtLink></li>
            <li><hr class="dropdown-divider"></li>
            <li><NuxtLink class="dropdown-item btn btn-hover nav-btn" to="/organisations/create">Create organisation</NuxtLink></li>
            <li><NuxtLink class="dropdown-item btn btn-hover nav-btn" to="/organisations/change">Your organisations</NuxtLink></li>
        </ul>
    </li>
</template>


<script>
export default {
  props: {
    userEmail: {
      type: String,
      required: true,
    },
  },
};
</script>