<script setup>
import { RouterLink, RouterView } from 'vue-router'
import ParticipationStorageService from './services/ParticipationStorageService';
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light header">
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown"
      aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <div class="nav-link">
            <RouterLink to="/">Home</RouterLink>

          </div>
        </li>
        <li class="nav-item">
          <div class="nav-link">
            <RouterLink to="/NewQuizPage">Quiz</RouterLink>
          </div>
        </li>
      </ul>
      <ul class="collapse navbar-collapse justify-content-end">
        <li class="nav-item">
          <div class="nav-link" v-if="logged == false" :key="logged">
            <RouterLink to="/Login">Login</RouterLink>
          </div>
          <div class="nav-link" v-else>
            <RouterLink to="/Adminparam">Gestion Admin </RouterLink>
          </div>
        </li>
      </ul>
    </div>
  </nav>


  <RouterView />
</template>

<script>
import participationStorageService from "@/services/ParticipationStorageService";
export default {
  data() {
    return { logged: false };
  },

  async created() {
    if (participationStorageService.getToken() != null) {
      this.logged = true;
    }
  },

}
</script>

<style scoped>
nav {
  padding-top: 0px;
  position: fixed;
  width: 100%;
  top: 0;
  left: 0;
  z-index: 9999;
  margin-bottom: 20px;
}
</style>
