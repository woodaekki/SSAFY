<template>
  <div>
    {{ count }}
  </div>
</template>

<script setup>
import {ref} form 'vue'

const count = ref(0)

const increment = function() {
  count.value++
}
</script>

<style lang="scss" scoped>

</style>