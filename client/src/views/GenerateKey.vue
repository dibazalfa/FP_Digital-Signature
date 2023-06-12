<template>
  <div
    class="h-screen bg-gradient-to-r from-[#f7b1af] via-[#ecbac4] to-[#d48399]"
  >
    <div class="w-full flex items-center sm:items-center">
      <div class="flex my-10 mx-12">
        <a
          href="/"
          class="flex bg-red-400 hover:bg-rose-500 text-white py-2 p-5 justify-center rounded-full text-2xl hover:text-slate-100 items-center"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="w-6 h-6 mr-2"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25"
            />
          </svg>

          Home
        </a>
      </div>
      <nav class="flex items-center sm:mx-24 lg:mx-[420px] md:mx-56">
        <ul class="text-white">
          <div class="flex text-2xl">
            <item name="Generate" path="/generate" />
            <item name="Validator" path="/validator" />
          </div>
        </ul>
      </nav>
    </div>

    <!-- card -->
    <div class="my-5">
      <div
        class="max-w-4xl h-[500px] px-8 py-10 mx-auto bg-white rounded-lg shadow-md"
        style="cursor: auto"
      >
        <div class="font-bold justify-center flex items-center text-3xl">
          <svg
            width="35"
            height="35"
            viewBox="0 0 38 38"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <circle
              cx="12.6667"
              cy="23.75"
              r="4.75"
              fill="#222222"
              stroke="#222222"
              stroke-width="2"
            />
            <path
              d="M28.4154 9.41548C28.806 9.02496 28.806 8.39179 28.4154 8.00127C28.0249 7.61074 27.3917 7.61074 27.0012 8.00127L28.4154 9.41548ZM29.3762 14.9571L30.0833 15.6643L31.4975 14.25L30.7904 13.5429L29.3762 14.9571ZM26.2096 14.9571L26.9167 15.6643L28.3309 14.25L27.6238 13.5429L26.2096 14.9571ZM15.1262 19.8763C14.7357 20.2668 14.7357 20.9 15.1262 21.2905C15.5167 21.681 16.1499 21.681 16.5404 21.2905L15.1262 19.8763ZM22.9583 13.4584L22.2512 12.7513L22.2512 12.7513L22.9583 13.4584ZM25.4179 17.3321L26.125 18.0393L27.5392 16.625L26.8321 15.9179L25.4179 17.3321ZM26.8321 10.9988L28.4154 9.41548L27.0012 8.00127L25.4179 9.5846L26.8321 10.9988ZM25.4179 10.9988L29.3762 14.9571L30.7904 13.5429L26.8321 9.5846L25.4179 10.9988ZM25.2488 12.5821L26.8321 10.9988L25.4179 9.5846L23.8346 11.1679L25.2488 12.5821ZM23.8346 12.5821L26.2096 14.9571L27.6238 13.5429L25.2488 11.1679L23.8346 12.5821ZM16.5404 21.2905L23.6654 14.1655L22.2512 12.7513L15.1262 19.8763L16.5404 21.2905ZM23.6654 14.1655L25.2488 12.5821L23.8346 11.1679L22.2512 12.7513L23.6654 14.1655ZM22.2512 14.1655L25.4179 17.3321L26.8321 15.9179L23.6654 12.7513L22.2512 14.1655Z"
              fill="#222222"
            />
          </svg>
          RSA KEY GENERATE
        </div>
        <div class="my-10">
          <label
            for="default-input"
            class="block my-3 text-xl font-medium text-gray-900"
            >File Name Output</label
          >
          <div class="flex">
            <input
              type="text"
              id="default-input"
              class="bg-white border border-gray-500 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-4/6 p-2.5"
            />
            <button
              class="mx-auto bg-rose-400 hover:bg-rose-500 text-white py-2 px-12 justify-center rounded-full text-lg hover:text-slate-100 items-center"
            >
              Generate Key
            </button>
          </div>
          <label for="sign" class="block mt-5 text-xl font-medium text-gray-900"
            >Next Step</label
          >
          <router-link to="/ds" >
            <button
              class="mx-auto mt-3 bg-[#fca49c] hover:bg-[#d68f9f] text-white py-2 px-10 justify-center rounded-full text-lg hover:text-slate-100 items-center"
            >
              <div class="flex items-center">
                <svg
                  width="30"
                  height="30"
                  viewBox="0 0 14 17"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M1.66803 5.44446H7.93317C8.62369 5.44446 8.96895 5.44446 9.25615 5.50104C10.4505 5.73637 11.3843 6.67014 11.6196 7.86454C11.6762 8.15174 11.6762 8.497 11.6762 9.18751V9.18751C11.6762 9.87803 11.6762 10.2233 11.6196 10.5105C11.3843 11.7049 10.4505 12.6387 9.25615 12.874C8.96895 12.9306 8.62369 12.9306 7.93317 12.9306H6.46803C4.78787 12.9306 3.94779 12.9306 3.30606 12.6036C2.74157 12.316 2.28263 11.857 1.99501 11.2925C1.66803 10.6508 1.66803 9.81073 1.66803 8.13057V5.44446Z"
                    fill="white"
                  />
                  <path
                    d="M1.66803 5.44444C1.66803 5.40575 1.66803 5.38641 1.6683 5.37005C1.68595 4.2911 2.55636 3.42069 3.63531 3.40304C3.65167 3.40277 3.67101 3.40277 3.7097 3.40277H4.30795C4.60493 3.40277 4.75342 3.40277 4.89394 3.42282C5.29453 3.47997 5.66835 3.65728 5.96605 3.93134C6.07048 4.02747 6.16443 4.14246 6.35233 4.37245L7.22814 5.44444H1.66803V5.44444Z"
                    fill="white"
                  />
                </svg>
                <span class="px-2">Digital Sign</span>
              </div>
            </button >
          </router-link>
          <!-- img -->
          <img src="../assets/hi.gif" alt="hi" class="mx-96 block -my-20">
        </div>
      </div>
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
