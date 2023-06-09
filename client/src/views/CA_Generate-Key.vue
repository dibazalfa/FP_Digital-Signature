<template>
  <div>
    <div>
      <h1>Generate Key</h1>
    </div>
    <div>
      <h2>RSA Key Generate</h2>
      <label>Nama File Output</label>
      <input type="text" v-model="App.key">
      <!-- <button @click="App.generateKey()">Generate Key</button> -->
      <button @click="App.sendDataToServer()">Generate Key</button>
    </div>
  </div>
</template>

<script>
import { useApp } from "../stores/index";
export default {
  setup() {
    const App = useApp();
    return {
      App,
    };
  },
};
</script>
  