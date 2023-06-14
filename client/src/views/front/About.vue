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
      </div>
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
