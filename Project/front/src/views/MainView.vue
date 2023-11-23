<template>
  <div id="carousel-container" class="carousel slide carousel-dark" data-bs-ride="carousel">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <RouterLink :to="{ name: 'recommend' }">
            <img src="@/assets/carousel_sample_1.png" class="d-block w-100" alt="...">
          </RouterLink>
        </div>
        <div class="carousel-item">
          <RouterLink :to="{ name: 'map' }">
            <img src="@/assets/carousel_sample_2.png" class="d-block w-100" alt="...">
          </RouterLink>
        </div>
        <div class="carousel-item">
          <RouterLink :to="{ name: 'exchange' }">
            <img src="@/assets/carousel_sample_3.png" class="d-block w-100" alt="...">
          </RouterLink>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carousel-container" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carousel-container" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { useUserStore } from '@/stores/user'

const store = useUserStore()

</script>

<style scoped>
</style>