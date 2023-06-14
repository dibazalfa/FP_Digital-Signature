<template>
  <div class="bg-[#EFEAEA] h-screen">
    <div
      class="w-full bg-cover bg-no-repeat bg-top h-96 sm:bg-cover"
      style="
        background-image: url(https://i.pinimg.com/564x/17/c4/3b/17c43b7d48bae5baab2cdcb798c8cf6c.jpg);
      "
    >
      <nav class="flex flex-wrap items-center mx-24 justify-center">
        <div class="flex my-12">
          <!-- <img
            class="w-full cursor-pointer"
            src="../assets/sora.png"
            alt="logo"
            @click="$router.push(`/`)"
          /> -->
        </div>
        <ul class="text-white">
          <div class="flex text-2xl gap-4">
            <item name="Home" path="/"  />
            <item name="Generate" path="/generate" />
            <item name="Validator" path="/validator" />
          </div>
        </ul>
      </nav>

    <!-- card -->
    <div class="my-10">
      <div
        class="max-w-4xl h-[500px] px-8 py-10 mx-auto bg-white rounded-lg shadow-md"
        style="cursor: auto"
      >
        <div class="font-bold justify-center flex items-center text-3xl">
          <svg
            width="35"
            height="35"
            viewBox="0 0 16 19"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M2 6.33337H9.64583C10.9069 6.33337 11.5374 6.33337 12.0414 6.51993C12.8623 6.8238 13.5096 7.47105 13.8134 8.29195C14 8.79595 14 9.42648 14 10.6875C14 11.9486 14 12.5791 13.8134 13.0831C13.5096 13.904 12.8623 14.5513 12.0414 14.8551C11.5374 15.0417 10.9069 15.0417 9.64583 15.0417H6.8C5.11984 15.0417 4.27976 15.0417 3.63803 14.7147C3.07354 14.4271 2.6146 13.9682 2.32698 13.4037C2 12.7619 2 11.9219 2 10.2417V6.33337Z"
              fill="#222222"
            />
            <path
              d="M2 6.33337C2 5.98502 2 5.81085 2.02165 5.66491C2.15091 4.7935 2.83513 4.10928 3.70654 3.98002C3.85247 3.95837 4.02665 3.95837 4.375 3.95837H5.18493C5.72539 3.95837 5.99562 3.95837 6.24647 4.02456C6.47586 4.08509 6.69265 4.18595 6.8867 4.32242C7.09891 4.47166 7.27298 4.67837 7.62111 5.09177L8.66667 6.33337H2Z"
              fill="#222222"
            />
          </svg>

          FILE DIGITAL SIGN
        </div>
        <div class="my-10">
          <div class="grid justify-center">
            <div class="flex">
              <label
                for="default-input"
                class="mx-10 text-xl font-medium text-gray-900"
                >File Input</label
              >
                <label class="block mx-5">
                  <span class="sr-only">Choose File</span>
                  <input
                  type="file" ref="fileInput" @change="App.inputFile($event.target.files[0])"
                    class="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-rose-50 file:text-rose-700 hover:file:bg-rose-100"
                  />
                </label>
            </div>
            <div class="my-5 flex">
              <label
                for="default-input"
                class="mx-10 text-xl font-medium text-gray-900"
                >Private Key</label
              >
              <label class="block mx-1">
                  <span class="sr-only">Choose File</span>
                  <input
                  type="file" ref="privateKeyInput" @change="App.inputPrivateKey($event.target.files[0])"
                    class="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-rose-50 file:text-rose-700 hover:file:bg-rose-100"
                  />
                </label>
            </div>
            <button
            @click="App.submit"
              class="my-10 mx-auto bg-rose-400 hover:bg-rose-500 text-white py-2 px-12 justify-center rounded-full text-lg hover:text-slate-100 items-center"
            >
              Sign File
            </button>
          </div>
              <!-- img -->
              <img src="../assets/pentol.gif" alt="hi" class="w-2/6 block -my-32 -mx-5">
        </div>
      </div>
    </div>
    </div>
  </div>
</template>

<script>
import Item from "../components/Item.vue";
import { useApp } from '../stores/index';

export default {
  name: "Header",
  components: {
    Item,
  },
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
