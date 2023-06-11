<template>
   <div class=" h-screen bg-gradient-to-r from-[#f7b1af] via-[#ecbac4]  to-[#d48399] ">
    <div>

        <!-- <nav class="flex flex-wrap items-center mx-24 justify-center my-10">
            <ul class="text-white ">
              <div class="flex text-2xl">
                <item name="Generate" path="/generate" />
                <item name="Validator" path="/validator" />
              </div>
            </ul>
          </nav> -->
    </div>
   </div>
</template>

<script>
import Item from "../components/Item.vue";
export default {
  name: "Header",
  components: {
    Item,
  },
};
</script>