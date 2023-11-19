<script setup>
  import { onMounted } from 'vue'
  import { useUserStore } from '@/stores/user'

  useHead({
    title: "MyTaskTracker",
    link: [
      {
        href: "https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css",
        rel: "stylesheet",
        integrity: "sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx",
        crossorigin: "anonymous"
      }
    ],
    script: [
      {
        src: "https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js",
        integrity: "sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa",
        crossorigin: "anonymous"
      }
    ]
  })
  const userStore = useUserStore()
  onMounted(() => {
    userStore.initStore()
  })
</script>


<template>
  <div>
    <NuxtLayout >

    </NuxtLayout>
  </div>
</template>


<style>
.putple-btn {
    --bs-btn-font-size: 1.5rem;
    background: rgb(101, 101, 194);
    --bs-btn-color: rgb(85, 85, 189);
}
.putple-btn:hover {
    background-color: rgb(85, 85, 189);
}
.putple-btn:active {
    --bs-btn-color: rgb(85, 85, 189);
}
</style>