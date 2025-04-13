<template>
  <form @submit.prevent="saveMovie" enctype="multipart/form-data">
    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input v-model="title" type="text" name="title" class="form-control" />
    </div>

    <div class="form-group mb-3">
      <label for="description" class="form-label">Description</label>
      <textarea v-model="description" name="description" class="form-control"></textarea>
    </div>

    <div class="form-group mb-3">
      <label for="poster" class="form-label">Movie Poster</label>
      <input @change="handleFileUpload" type="file" name="poster" class="form-control" />
    </div>

    <button type="submit" class="btn btn-primary">Add Movie</button>

    <div v-if="message" class="alert alert-success mt-3">{{ message }}</div>
    <ul v-if="errors.length" class="alert alert-danger mt-3">
      <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
    </ul>
  </form>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const title = ref('')
const description = ref('')
const poster = ref(null)
const message = ref('')
const errors = ref([])
const csrf_token = ref('')

// Fetch the CSRF token from the backend
function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then(response => response.json())
    .then(data => {
      csrf_token.value = data.csrf_token
    })
}

onMounted(() => {
  getCsrfToken()
})

// Handle file upload
function handleFileUpload(event) {
  poster.value = event.target.files[0]
}

// Submit movie form data
function saveMovie() {
  const formData = new FormData()
  formData.append('title', title.value)
  formData.append('description', description.value)
  formData.append('poster', poster.value)

  fetch('/api/v1/movies', {
    method: 'POST',
    body: formData,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  })
    .then(response => response.json())
    .then(data => {
      if (data.errors) {
        errors.value = data.errors
        message.value = ''
      } else {
        message.value = data.message
        errors.value = []
        title.value = ''
        description.value = ''
        poster.value = null
      }
    })
    .catch(error => {
      console.log(error)
      errors.value = ['An error occurred while submitting the form.']
    })
}
</script>
