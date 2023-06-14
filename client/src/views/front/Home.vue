<template>
  <div class="bg-[#EFEAEA] h-screen">
    <div
      class="w-full bg-cover bg-no-repeat bg-top h-96 sm:bg-cover"
      style="
        background-image: url(https://i.pinimg.com/564x/17/c4/3b/17c43b7d48bae5baab2cdcb798c8cf6c.jpg);
      "
    >
    <nav class="flex flex-wrap items-center mx-24 justify-center">
      <div class=" my-12">
<!--         
        <div class="flex">
          <img
                  class="w-20  cursor-pointer"
                  src="../../assets/logo.png"
                  alt="logo"
                  @click="$router.push(`/`)"
                />
    
        </div> -->
        </div>
        <ul class="text-white">
          <div class="flex text-2xl gap-4">
            <item name="Home" path="/" />
            <item name="Tools" path="/generate" />
          </div>
        </ul>
      </nav>
      <!-- card -->
      <div class="my-32">
        <div
          class="max-w-4xl px-8 py-4 mx-auto bg-white rounded-lg shadow-md"
          style="cursor: auto"
        >
          <div class="flex justify-center">
            <button @click="profil(1)">
              <img
                src="../../assets/diba.jpg"
                alt="Adiba"
                class="hidden object-cover w-24 h-24 mx-4 -mt-20 rounded-full sm:block"
              />
            </button>
            <button @click="profil(2)">
              <img
                src="../../assets/nara.jpg"
                alt="Brigitta"
                class="hidden object-cover w-24 h-24 mx-4 -mt-20 rounded-full sm:block"
              />
            </button>
            <button @click="profil(3)">
              <img
                src="../../assets/della.jpg"
                alt="Della S"
                class="hidden object-cover w-24 h-24 mx-4 -mt-20 rounded-full sm:block"
              />
            </button>
            <button @click="profil(4)">
              <img
                src="../../assets/keiza.jpg"
                alt="Fina Keiza"
                class="hidden object-cover w-24 h-24 mx-4 -mt-20 rounded-full sm:block"
              />
            </button>

            <div
              v-show="isOpen"
              class="absolute inset-0 flex items-center justify-center bg-gray-700 bg-opacity-50"
            id="diba"
              >
              <div class="max-w-2xl p-6 bg-white rounded-md shadow-xl">
                <div class="flex items-center justify-between">
                  <h3 class="text-2xl mx-2">{{nama}}</h3>
                  <svg
                    @click="isOpen = false"
                    xmlns="http://www.w3.org/2000/svg"
                    class="w-8 h-8 text-red-900 cursor-pointer"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
                    />
                  </svg>
                </div>
                <div class="mt-4">
                  <p class="mb-4 mx-2 text-sm">
                    {{ output }}
                  </p>
                </div>
              </div>
            </div>

            

          </div>
          <div class="flex items-center justify-center my-5">
            <span class="text-3xl font-bold text-gray-950"
              >DIGITAL SIGNATURE</span
            >
          </div>
          <div class="flex justify-center mt-6">
            <a
              href="/generate"
              class="bg-[#b67998] hover:bg-[#c08c9f] text-white font-bold py-4 px-32 rounded-full text-2xl"
            >
              Let's Started
            </a>
          </div>
          <div class="mt-2">
            <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-300" />
            <p class="mt-2 text-gray-600">
              A digital signature is the result of a digital signing process
              that verifies and authenticates the integrity, authenticity, and
              non-repudiation of a document or message. Therefore, let's verify
              the authenticity of your signature or document.
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
    <img
      src="../../assets/love.gif"
      alt="hi"
      class="w-64 block my-[100px] ml-[1200px]"
    />
  </div>
</template>

<script>
import Item from "../../components/Item.vue";
export default {
  data() {
    return {
      isOpen: false,
      output: "",
      nama: "",
      bagian: "",
    };
  },
  methods: {
    profil(buttonNumber) {
      this.isOpen = true;
      if (buttonNumber === 1) {
        this.nama = 'Adiba Zalfa Camilla';
        this.output = '5027211060';
      } else if (buttonNumber === 2) {
        this.nama = 'Brigitta Naraduhita P. P.';
        this.output = '5027211055';
      } else if (buttonNumber === 3) {
        this.nama = 'Della Setyowati';
        this.output = '5027211044';
      } else if (buttonNumber === 4) {
        this.nama = 'Fina Keiza Arismana';
        this.output = '5027211028';
      } 
    }
  },
  name: "Header",
  components: {
    Item,
  },
};
</script>
