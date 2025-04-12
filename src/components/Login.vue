<template>
    <div>
        <input type="text" v-model="username" placeholder="office@myground.org" />
        <input type="password" v-model="password"/>
        <button @click="login">Login</button> 
        <p>{{result}}</p>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const username = ref('office@myground.org')
const password = ref('dan')
const result = ref('')

const login = () => {

    fetch('http://127.0.0.1:5000/auth/dev-login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username.value,
            password: password.value
        })
    })
        .then(async data => {
            data = await data.json()
            console.log(data)
            if (data.status === 200) {
                result.value = 'Login successful'
            } else {
                result.value = 'Invalid username or password'
            }
        })
        .catch(error => {
            console.log(error)
        })
}

</script>
