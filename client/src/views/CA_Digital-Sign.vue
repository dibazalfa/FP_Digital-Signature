<template>
  <div>
    <div>
      <h1>Digital Sign</h1>
    </div>
    <div>
      <h2>File Digital Sign</h2>

      <!-- untuk upload file .pdf -->
      <label>File Input</label>
      <input type="file" ref="fileInput" @change="App.inputFile($event.target.files[0])" />
      <br />
      <label>Private Key</label>
      <input type="file" ref="privateKeyInput" @change="App.inputPrivateKey($event.target.files[0])" />
    </div>
    <button @click="App.submit">Submit</button>
  </div>
</template>

<script>
import { useApp } from '../stores/index';

export default {
  setup() {
    const App = useApp();

    return {
      App,
    };
  },
  mounted() {
    // this.App.getData();
  },
};
</script>
