import { defineStore } from "pinia";
import axios from "axios";

// const URL_API = "http://localhost:5000";

export const useApp = defineStore({
  id: "App",
  state: () => ({
      key: "",
      publicKey: "",
      privateKey: "",
  }),
  actions: {
    async generateKey() {
      const q = this.key;
      // console.log(q);
      
      try {
        const response = await axios.post('http://localhost:5000/api/data', { q });
        console.log(response.data.key); // Tanggapan dari server
        this.getData();
      } catch (error) {
        console.log(error);
      }
    },
    async getData() {
      console.log("halo ini get data")
      try {
        await axios.post('http://localhost:5000/api/data', {q: 'key'})
          .then(response => {
            this.publicKey = response.data.publicKey;
            this.privateKey = response.data.privateKey;
          })
           // Membuat file teks
          const publicKeyBlob = new Blob([this.publicKey], { type: 'text/plain' });
          const privateKeyBlob = new Blob([this.privateKey], { type: 'text/plain' });

          // Membuat URL objek blob
          const publicKeyURL = window.URL.createObjectURL(publicKeyBlob);
          const privateKeyURL = window.URL.createObjectURL(privateKeyBlob);

          // Membuat elemen anchor untuk mengunduh file
          const publicKeyLink = document.createElement('a');
          publicKeyLink.href = publicKeyURL;
          publicKeyLink.download = this.key + '.pub';

          const privateKeyLink = document.createElement('a');
          privateKeyLink.href = privateKeyURL;
          privateKeyLink.download = this.key + '.pri';

          // Menyembunyikan elemen anchor dan mengkliknya
          publicKeyLink.style.display = 'none';
          privateKeyLink.style.display = 'none';
          document.body.appendChild(publicKeyLink);
          document.body.appendChild(privateKeyLink);

          publicKeyLink.click();
          privateKeyLink.click();

          // Menghapus URL objek blob
          window.URL.revokeObjectURL(publicKeyURL);
          window.URL.revokeObjectURL(privateKeyURL);

          // console.log("Public Key:", this.publicKey);
          // console.log("Private Key:", this.privateKey);
      } catch (error) {
        console.log(error)
      }
    }
  }
})