<script setup lang="ts">
</script>

<template>
  <button class="text-sm font-medium border rounded px-3 py-1 m-4 float-right border-green-300 hover:border-green-400 hover:bg-green-100 bg-green-50 text-green-700 cursor-pointer" @click="$emit('register')">
    <slot></slot>
  </button>
</template>
