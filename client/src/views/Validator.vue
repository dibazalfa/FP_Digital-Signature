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
            <item name="Home" path="/" />
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
              viewBox="0 0 21 18"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M18.9229 5.5864C19.489 4.85379 19.3979 3.77982 18.6867 3.16373C17.9411 2.51783 16.8356 2.64785 16.2439 3.41365L10.9521 10.2619L8.75556 8.40132C8.00218 7.76317 6.89848 7.90739 6.31574 8.67867C5.75805 9.41679 5.85923 10.49 6.57789 11.0987L9.57249 13.6353C10.6227 14.5249 12.1589 14.3399 12.9915 13.2623L18.9229 5.5864Z"
                stroke="#222222"
                stroke-width="2"
                stroke-linecap="round"
              />
              <mask
                id="path-2-outside-1_110_106"
                maskUnits="userSpaceOnUse"
                x="0.416626"
                y="1.5"
                width="16"
                height="14"
                fill="black"
              >
                <rect
                  fill="white"
                  x="0.416626"
                  y="1.5"
                  width="16"
                  height="14"
                />
                <path
                  fill-rule="evenodd"
                  clip-rule="evenodd"
                  d="M6.52583 13.2861L4.6426 11.6245C3.99507 11.0531 3.60923 10.2956 3.49453 9.50298C3.17446 9.47828 2.84822 9.60784 2.63355 9.87817C2.2901 10.3107 2.36228 10.9397 2.79478 11.2832L4.83456 12.903C5.33019 13.2966 5.9542 13.417 6.52583 13.2861ZM9.6533 6.71031L11.8337 3.8886C12.1714 3.45159 12.7994 3.37107 13.2364 3.70876C13.3562 3.8013 13.4492 3.91563 13.5141 4.04186L10.7229 7.65405L9.6533 6.71031Z"
                />
              </mask>
              <path
                d="M6.52583 13.2861L6.97209 15.2357L10.7723 14.3658L7.84907 11.7864L6.52583 13.2861ZM4.6426 11.6245L3.31936 13.1241H3.31936L4.6426 11.6245ZM3.49453 9.50298L5.47392 9.21655L5.24463 7.63212L3.64845 7.50891L3.49453 9.50298ZM2.63355 9.87817L4.19978 11.1219L4.19978 11.1219L2.63355 9.87817ZM2.79478 11.2832L4.03855 9.71694L4.03855 9.71694L2.79478 11.2832ZM4.83456 12.903L3.59079 14.4692H3.59079L4.83456 12.903ZM9.6533 6.71031L8.07073 5.48741L6.92496 6.97018L8.33006 8.20998L9.6533 6.71031ZM11.8337 3.8886L13.4163 5.1115L13.4163 5.11149L11.8337 3.8886ZM13.2364 3.70876L12.0136 5.29133L12.0136 5.29133L13.2364 3.70876ZM13.5141 4.04186L15.0967 5.26476L15.8746 4.25811L15.2926 3.12689L13.5141 4.04186ZM10.7229 7.65405L9.39964 9.15373L11.0003 10.566L12.3055 8.87695L10.7229 7.65405ZM7.84907 11.7864L5.96585 10.1248L3.31936 13.1241L5.20258 14.7858L7.84907 11.7864ZM5.96585 10.1248C5.68713 9.87885 5.52324 9.55736 5.47392 9.21655L1.51515 9.78942C1.69522 11.0337 2.30301 12.2273 3.31936 13.1241L5.96585 10.1248ZM4.19978 11.1219C3.98395 11.3937 3.65468 11.5213 3.34062 11.4971L3.64845 7.50891C2.69423 7.43526 1.7125 7.82197 1.06733 8.6344L4.19978 11.1219ZM4.03855 9.71694C4.47105 10.0604 4.54323 10.6894 4.19978 11.1219L1.06733 8.6344C0.0369635 9.9319 0.253518 11.819 1.55102 12.8494L4.03855 9.71694ZM6.07832 11.3368L4.03855 9.71694L1.55102 12.8494L3.59079 14.4692L6.07832 11.3368ZM6.07956 11.3365C6.07728 11.3371 6.07587 11.3367 6.07673 11.3369C6.07748 11.3371 6.07862 11.3374 6.07976 11.338C6.08109 11.3386 6.08067 11.3386 6.07832 11.3368L3.59079 14.4692C4.58274 15.2569 5.83407 15.4962 6.97209 15.2357L6.07956 11.3365ZM11.2359 7.9332L13.4163 5.1115L10.2511 2.66571L8.07073 5.48741L11.2359 7.9332ZM13.4163 5.11149C13.0786 5.54851 12.4506 5.62903 12.0136 5.29133L14.4593 2.12619C13.1483 1.11311 11.2642 1.35466 10.2511 2.66571L13.4163 5.11149ZM12.0136 5.29133C11.8967 5.20104 11.802 5.08574 11.7357 4.95684L15.2926 3.12689C15.0963 2.74552 14.8157 2.40156 14.4593 2.12619L12.0136 5.29133ZM12.3055 8.87695L15.0967 5.26476L11.9316 2.81897L9.14032 6.43116L12.3055 8.87695ZM8.33006 8.20998L9.39964 9.15373L12.0461 6.15438L10.9765 5.21063L8.33006 8.20998Z"
                fill="#222222"
                mask="url(#path-2-outside-1_110_106)"
              />
            </svg>

            DIGITAL SIGNATURE VERIFICATION
          </div>
          <div class="my-10">
            <div class="grid justify-center gap-4">
              <div class="flex max-w-xl">
                <label
                  for="default-input"
                  class="mr-auto text-xl font-medium text-gray-900"
                  >File Input</label
                >
                <label class="block px-5">
                  <span class="sr-only">Choose File</span>
                  <input
                    type="file"
                    ref="fileInput"
                    @change="App.inputFile($event.target.files[0])"
                    class="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-rose-50 file:text-rose-700 hover:file:bg-rose-100"
                  />
                </label>
              </div>
              <div class="flex">
                <label
                  for="default-input"
                  class="mr-auto text-xl font-medium text-gray-900"
                  >File Key</label
                >
                <label class="block px-5">
                  <span class="sr-only">Choose File</span>
                  <input
                    type="file"
                    ref="privateKeyInput"
                    @change="App.inputPublicKey($event.target.files[0])"
                    class="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-rose-50 file:text-rose-700 hover:file:bg-rose-100"
                  />
                </label>
              </div>
              <div class="flex">
                <label
                  for="default-input"
                  class="mr-auto text-xl font-medium text-gray-900"
                  >File Sign</label
                >
                <label class="block px-5">
                  <span class="sr-only">Choose File</span>
                  <input
                    type="file"
                    ref="privateKeyInput"
                    @change="App.inputSign($event.target.files[0])"
                    class="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-rose-50 file:text-rose-700 hover:file:bg-rose-100"
                  />
                </label>
              </div>
              <button
                @click="App.submitvalidator"
                class="my-10 mx-auto bg-rose-400 hover:bg-rose-500 text-white py-2 px-12 justify-center rounded-full text-lg hover:text-slate-100 items-center"
              >
                Check File
              </button>
            </div>
            <!-- img -->
            <img
              src="../assets/ok.gif"
              alt="hi"
              class="w-2/6 mx-[530px] block -my-48"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Item from "../components/Item.vue";
import { useApp } from "../stores/index";
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
  mounted() {},
};
</script>
