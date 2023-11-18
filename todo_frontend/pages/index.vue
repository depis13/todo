<template>
<div class="container-fluid vh-100 d-flex align-items-center justify-content-center">
  <div class="my-full-height-div text-center align-self-center">
    <div>
      <h1>TaskTracker</h1>
      <h2>Effective app to set up work flows.</h2>
    </div>
    <div class="login-text">
      <h3>Start using your time efficiently.</h3>
      <div class="d-flex align-items-center justify-content-center btn-container">
        <div class="d-flex gap-3">
          <NuxtLink to="/signup" class="btn btn-hover purple-btn big-purple-btn" data-bs-toggle="button">Sign up</NuxtLink>
          <NuxtLink to="/login" class="btn btn-hover purple-btn big-purple-btn" data-bs-toggle="button">Log in</NuxtLink>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<style>

body {
  background-color: #292d33;
  color: #b3bdc9;

}
h1 {
    font-size: 4.5rem ;
}
h2 {
    font-size: 2rem;
}
h3 {
    margin-bottom: 3vh;
}
.btn {
    border: none;
    color: #fff;

}
.big-purple-btn {
    --bs-btn-font-size: 1.5rem;
    background: rgb(101, 101, 194);
    --bs-btn-color: rgb(85, 85, 189);
}
.big-purple-btn:hover {
    background-color: rgb(85, 85, 189);
}
.big-purple-btn:active {
    --bs-btn-color: rgb(85, 85, 189);
}

.login-text {
    margin-top: 6vh;
}
</style>
