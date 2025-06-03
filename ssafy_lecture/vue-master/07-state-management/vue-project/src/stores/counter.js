import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  // 얘는 return 해야 할까?
  let id = 0
  // 사용자가 값을 CUD 할 때 반응할 수 있도록 반응형으로 작성
  const todos = ref([
    // todo 객체 들을 만든다.
    // input:checkbox에 쓰일 id도 필요하고, v-for로 순회할때 쓸 key도 필요하다.
    // 더미 데이터니까 1, 2, 3 할 수도 있는데,,, 나중에 값이 추가됐을때도 처리!
    { id: id++, text: 'vue 공부', isDone: false },
    { id: id++, text: 'JS 공부', isDone: false },
    { id: id++, text: 'django 공부', isDone: true },
  ])

  const addTodo = function (todoText) {
    todos.value.push({
      id: id++,
      isDone: false,
      text: todoText
    })
  }

  const deleteTodo = function (selectedId) {
    // 넘겨받은 id 값을 기준으로, 
    // 내가 가진 todos를 전체 순회하면서, 각각의 todo 객체가 가진 id와 비교한다.
    // 그리고, 비교한 결과가 true인 값을 반환할때의 todo들만 모아서 새로운 배열을 만든다.
    todos.value = todos.value.filter(todo => todo.id != selectedId)
  }

  const updateTodo = function (selectedId) {
    todos.value = todos.value.map((todo) => {
      if (todo.id === selectedId) {
        todo.isDone = !todo.isDone
      }
      return todo
    })
  }

  return { 
      // 값 선언 했으면, 바로바로 까먹지 않도록 return 해주자.
      todos,
      addTodo, deleteTodo, updateTodo
   }
}, { persist: true })
