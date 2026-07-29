<script setup lang="ts">
</script>

<template>
  <!-- Mirrors the delete button's shape, in green. Spacing is the parent's job. -->
  <button
    class="cursor-pointer rounded border border-green-200 bg-green-50 px-3 py-1 text-sm font-medium text-green-700 transition duration-100 ease-in-out hover:border-green-300 hover:bg-green-100"
  >
    <slot></slot>
  </button>
</template>
