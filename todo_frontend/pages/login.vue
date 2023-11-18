<template>
    <div class="container-fluid vh-100 d-flex align-items-center justify-content-center">
        <div class="my-full-height-div text-center align-self-center">
            <form class="row g-3">
            <div class="col-12">
                <label for="inputEmail4" class="form-label">Email</label>
                <input type="email" class="form-control" id="inputEmail4">
            </div>
            <div class="col-12">
                <label for="inputPassword4" class="form-label">Password</label>
                <input type="password" class="form-control" id="inputPassword4">
            </div>
            <div class="col-12">
                <button type="submit" class="btn btn-primary mid-purple-btn">Sign in</button>
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