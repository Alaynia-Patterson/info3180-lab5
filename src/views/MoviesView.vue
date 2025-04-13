<template>
  <div class="container mt-4">
    <h2 class="mb-4">All Movies</h2>
    <div class="row">
      <div
        v-for="movie in movies"
        :key="movie.id"
        class="col-md-4 mb-4"
      >
        <div class="card h-100 shadow">
          <img :src="movie.poster" class="card-img-top" :alt="movie.title" />
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
            <p class="card-text">{{ movie.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);

function fetchMovies() {
  fetch("/api/v1/movies")
    .then((res) => res.json())
    .then((data) => {
      movies.value = data.movies;
    })
    .catch((err) => {
      console.error("Failed to load movies:", err);
    });
}

onMounted(() => {
  fetchMovies();
});
</script>

