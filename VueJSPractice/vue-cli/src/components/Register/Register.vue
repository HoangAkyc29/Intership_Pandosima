<!-- eslint-disable vue/multi-word-component-names -->
<script setup lang="ts">
import './Register.css';
// import loginImg from "../../assets/login.svg";
import { ref } from 'vue';

const username = ref('');
const password = ref('');
const handelRegister = () => {

};
</script>
<template>
    <div class="base-container" ref={this.props.containerRef}>
        <div class="header">Register</div>
        <div class="content">
            <div class="image">
                <!-- <img :src='loginImg' /> -->
            </div>
            <div class="form">
                <div class="form-group">
                    <!-- eslint-disable vuejs-accessibility/label-has-for -->
                    <label htmlFor="username">
                        Username
                    </label>
                    <input type="text" name="username" placeholder="username" v-model="username" />
                </div>
                <div class="form-group">
                    <label htmlFor="email">Email</label>
                    <input type="text" name="email" placeholder="email" />
                </div>
                <div class="form-group">
                    <label htmlFor="password">Password</label>
                    <input type="text" name="password" placeholder="password" v-model="password"/>
                </div>
            </div>
        </div>
        <div class="footer">
            <button type="button" class="btn" @click="handelRegister">
                Register
            </button>
        </div>
    </div>
</template>
