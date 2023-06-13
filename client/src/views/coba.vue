<template>
    <div>
      <button @click="getData">Get Data</button>
      <div>{{ response }}</div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        response: '',
      };
    },
    methods: {
      async getData() {
        try {
          const response = await axios.get('http://localhost:5000/api/data');
          this.response = response.data.message;
        } catch (error) {
          console.log(error);
        }
      },
    },
  };
  </script>
  