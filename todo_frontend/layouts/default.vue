<script>

</script>

<template>
  <div>
    <p>
      <nav class="navbar navbar-expand-lg bg-body-tertiary fixed-top">

      <div class="navbar-container vh-10 container-fluid gap-2">
        <NuxtLink to="/" class="btn btn-hover main-btn" data-bs-toggle="button" style="--bs-btn-font-size: 1.4rem;">TaskTracker</NuxtLink>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon" style="--bs-navbar-active-color: #b6c2cf; --bs-navbar-brand-color: #b6c2cf;"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarText">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
                <NuxtLink to="/features" class="btn btn-hover" data-bs-toggle="button">features</NuxtLink>
            </li>
          </ul>
        <div class="d-flex gap-2">
            <NuxtLink to="/login" class="btn btn-hover" data-bs-toggle="button">Log in</NuxtLink>
            <NuxtLink to="/signup" class="btn btn-hover" data-bs-toggle="button">Sign up</NuxtLink>
        </div>
        </div>
      </div>
      </nav>
    </p>
    <slot />
  </div>
</template>



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