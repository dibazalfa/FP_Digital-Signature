<template>
  <div>
    <div>
      <h1>Digital Signature Verification</h1>
    </div>
    <div>
      <h2>Sign Verification</h2>

      <!-- untuk upload file .pdf -->
      <label>File Input</label>
      <input type="text">
      <button>Browse</button>
      <!-- <input type="file" ref="fileInput" @change="App.handleFileChange"> -->
      <!-- <button @click="App.uploadFile()">Unggah</button>  -->
      
      <br>
      <label>File Key</label>
      <input type="text">
      <button>Browse</button> 
      <br>
      <label>File Sign</label>
      <input type="text">
      <button>Browse</button> 
      
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
  mounted() {
    
  }
};
</script>
