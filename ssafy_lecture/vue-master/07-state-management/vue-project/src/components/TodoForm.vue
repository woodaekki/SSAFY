<template>
  <!-- Q. store.addTodo(todoText) 이렇게 써도 된다? O -->
  <!-- <form @submit.prevent="store.addTodo(todoText)"> -->
    <!-- 써도 되는데, 나는 별도의 함수를 따로 정의해서 작성할것이다. -->
  <form @submit.prevent="onAddTodo">
    <!-- 양방향 바인딩으로, 사용자가 입력한 값을 사용하자. -->
    <input type="text" v-model="todoText">
    <button>CREATE</button>
  </form>
</template>

<script setup>
  import { ref } from 'vue'
  import { useCounterStore } from '@/stores/counter.js'
  const store = useCounterStore()

  const todoText = ref('')
  const onAddTodo = function () {
    // 추가 로직 작성하려고...
    // 이 컴포넌트를 위한 함수로써 기능하도록
    store.addTodo(todoText.value)
    todoText.value = ''
  }
</script>

<style scoped>

</style>