import Vue from 'vue'
import Router from 'vue-router'
import { createRouter, createWebHashHistory } from 'vue-router'
import HomeVue from '../components/Home/Home.vue'
import LoginVue from '../components/Login/Login.vue'

const routes = []

export const router = createRouter({
  // Provide the history implementation to use. We are using the hash history for simplicity here.
  history: createWebHashHistory(),
  routes, // short for `routes: routes`
})