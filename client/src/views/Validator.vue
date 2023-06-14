<template>
  <div>
    <div>
      <h1>Digital Signature Verification</h1>
    </div>
    <div>
      <h2>Sign Verification</h2>

      <!-- untuk upload file .pdf -->
      <label>File Input</label>
      <input type="file" ref="fileInput" @change="App.inputFile($event.target.files[0])" />
      <!-- <input type="file" ref="fileInput" @change="App.handleFileChange"> -->
      <!-- <button @click="App.uploadFile()">Unggah</button>  -->

      <br />
      <label>File Key</label>
      <input type="file" ref="privateKeyInput" @change="App.inputPublicKey($event.target.files[0])" />
      <br />
      <label>File Sign</label>
      <input type="file" ref="privateKeyInput" @change="App.inputSign($event.target.files[0])" />
    </div>
    <button @click="App.submitvalidator">Submit</button>
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
  mounted() {},
};
</script>
