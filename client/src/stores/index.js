import { defineStore } from "pinia";
import axios from "axios";

const URL_API = "http://localhost:5000";

export const useApp = defineStore({
  id: "App",
  state: () => ({
      key: "",
  }),
  actions: {
      // generateKey() {
      //   const q = this.key;
      //   console.log(this.key);
      //   fetch(`http://localhost:3000/api/key?q=${q}`)
      //     .then((response) => response.json())
      //     .then((data) => {

      //     })
      //     .catch((error) => {
      //       console.error(error)
      //     })
      // }

      async generateKey() {
        const q = this.key
        try {
          const { data } = 
            await axios.post(URL_API + `/api/key?q=${q}`, 
            { headers: { 'Content-Type': 'application/json' } }
          );
        } catch (error) {
          console.log(error);
        }
      },

      sendDataToServer() {
        const data = {
          // Data yang ingin dikirim ke server
          halo: "halo"
        };
    
        axios.post('http://localhost:5000/api/data', data)
          .then(response => {
            // Tanggapan dari server jika diperlukan
          })
          .catch(error => {
            // Tangani kesalahan jika ada
          });
      }

      // async generateKey() {
      //   const q = this.key;
      //   try {
      //     const { data } = await axios.post(
      //       URL_API + '/api/key',
      //       { q },
      //       { headers: { 'Content-Type': 'application/json' } }
      //     );
      
      //     // Tangani respons dari server
      //     const public_key_content = data.public_key;
      //     const private_key_content = data.private_key;
      
      //     // Inisiasi unduhan file .pub
      //     const pubBlob = new Blob([public_key_content], { type: 'text/plain' });
      //     const pubLink = document.createElement('a');
      //     pubLink.href = URL.createObjectURL(pubBlob);
      //     pubLink.download = 'public_key.pub';
      //     pubLink.click();
      
      //     // Inisiasi unduhan file .pri (jika diperlukan)
      //     if (private_key_content) {
      //       const priBlob = new Blob([private_key_content], { type: 'text/plain' });
      //       const priLink = document.createElement('a');
      //       priLink.href = URL.createObjectURL(priBlob);
      //       priLink.download = 'private_key.pri';
      //       priLink.click();
      //     }
      //   } catch (error) {
      //     console.log(error);
      //   }
      // }
      

  }
})