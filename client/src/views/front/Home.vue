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
        <ul class="text-white ">
          <div class="flex text-2xl">
            <item name="Home" path="/" />
            <item name="About" path="/about" />
          </div>
        </ul>
      </nav>
      <!-- card -->
      <div class="my-32">
        <div
          class="max-w-4xl px-8 py-4 mx-auto bg-white rounded-lg shadow-md "
          style="cursor: auto"
        >
          <div class="flex justify-center">
            <img
              src="https://stackdiary.com/140x100.png"
              alt="Author Photo"
              class="hidden object-cover w-24 h-24 mx-4 -mt-20 rounded-full sm:block"
            />
            <img
              src="https://stackdiary.com/140x100.png"
              alt="Author Photo"
              class="hidden object-cover w-24 h-24 mx-4 -mt-20 rounded-full sm:block"
            />
            <img
              src="https://stackdiary.com/140x100.png"
              alt="Author Photo"
              class="hidden object-cover w-24 h-24 mx-4 -mt-20 rounded-full sm:block"
            />
            <img
              src="https://stackdiary.com/140x100.png"
              alt="Author Photo"
              class="hidden object-cover w-24 h-24 mx-4 -mt-20 rounded-full sm:block"
            />
          </div>
          <div class="flex items-center justify-center my-5">
            <span class="text-3xl font-bold text-gray-950"
              >DIGITAL SIGNATURE</span
            >
        </div>
        <div class="flex justify-center mt-6">
            <a href="/generate"
              class="bg-[#b67998] hover:bg-[#c08c9f] text-white font-bold py-4 px-32 rounded-full text-2xl"
            >
              Let's Started
            </a>

        </div>
          <div class="mt-2">
            <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-300">
            <p class="mt-2 text-gray-600 ">
                A digital signature is the result of a digital signing process that verifies and authenticates the integrity, authenticity, and non-repudiation of a document or message. Therefore, let's verify the authenticity of your signature or document.
            </p>
          </div>
          <div class="flex items-center justify-between mt-4">
            <a href="#" class="text-blue-600 dark:text-blue-400 hover:underline"
              >Read more ⟶</a
            >
          </div>
        </div>
      </div>
    </div>
    <!-- img -->
    <img src="../../assets/love.gif" alt="hi" class="w-64 block my-[100px] ml-[1200px] ">
    
  </div>
</template>

<script>
import Item from "../../components/Item.vue";
export default {
  name: "Header",
  components: {
    Item,
  },
};
</script>
