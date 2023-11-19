<script setup>
const router = useRouter()
let email = ref('')
let password1 = ref('')
let password2 = ref('')
let errors = ref([])

async function submitForm() {
    console.log('submitForm')
    errors.value = []
    await $fetch('http://127.0.0.1:8000/api/v1/users/', {
        method: 'POST',
        body: {
            username: email.value,
            password: password1.value
        }
    }).then(response => {
        console.log('response', response)
        router.push({path: '/login'})
    }).catch(error => {
        console.log(`test`, error)
        // console.log(response)
        if (error.response) {
            for (const property in error.response._data) {
                errors.value.push(`${property}: ${error.response._data[property]}`)
            }
            console.log(JSON.stringify(error.response))
            if (error.password) {
                errors.push(error.password)
            }
            if (error.username) {
                errors.push(error.username)
            }
            // if (response._data.username){
            //     errors.push(response._data.username)
            // }
            // if (response._data.password){
            //     error.push(response._data.password)
            // }
        } else {
            errors.value.push('Something went wrong')
            // console.log(JSON.stringify(error))
        }
        // else {
        //     console.log(error.username)
        // }
    })
    console.log(JSON.stringify(errors))
}
</script>


<template>
    <div class="container-fluid vh-100 d-flex align-items-center justify-content-center">
        <div class="my-full-height-div text-center align-self-center">
            <form v-on:submit.prevent="submitForm" class="row g-3">
            <div class="col-12">
                <label for="inputEmail4" class="form-label">Email</label>
                <input v-model="email" type="email" class="form-control" id="inputEmail4">
            </div>
            <div class="col-12">
                <label for="inputPassword4" class="form-label">Password</label>
                <input v-model="password1" type="password" class="form-control" id="inputPassword4">
            </div>
            <div class="col-12">
                <label for="inputPassword4" class="form-label">Password again</label>
                <input v-model="password2" type="password" class="form-control" id="inputPassword4">
            </div>
            <div v-if="errors.length" class="col-12 error-block">
                <div v-if="errors" class="alert alert-danger">
                    {{ errors[0] }}
                </div>
                <div v-else class="alert alert-danger" role="alert">
                    Something went wrong. Please try again.
                </div>
            </div>
            <div class="col-12">
                <button type="submit" class="btn btn-primary mid-purple-btn">Sign up</button>
            </div>
            </form>
        </div>
    </div>
</template>


<style>
.mid-purple-btn {
    --bs-btn-font-size: 1.2rem;
    background: rgb(101, 101, 194);
    --bs-btn-color: rgb(85, 85, 189);
}
.mid-purple-btn:hover {
    background-color: rgb(85, 85, 189);
}
.mid-purple-btn:active {
    --bs-btn-color: rgb(85, 85, 189);
}
</style>