import { defineStore } from 'pinia';
import axios from 'axios';

// const URL_API = "http://localhost:5000";

export const useApp = defineStore({
  id: 'App',
  state: () => ({
    key: '',
    publicKey: '',
    privateKey: '',
    file: null,
    privatekey: null,
    isSubmitted: false,
  }),
  actions: {
    async generateKey() {
      const q = this.key;
      try {
        const response = await axios.post('http://localhost:5000/api/data', { q });
        console.log(response.data.key);
        this.getData();
      } catch (error) {
        console.log(error);
      }
    },
    async getData() {
      console.log('halo ini get data');
      try {
        await axios.post('http://localhost:5000/api/data', { q: 'key' }).then((response) => {
          this.publicKey = response.data.publicKey;
          this.privateKey = response.data.privateKey;
        });

        const publicKeyBlob = new Blob([this.publicKey], { type: 'text/plain' });
        const privateKeyBlob = new Blob([this.privateKey], { type: 'text/plain' });

        const publicKeyURL = window.URL.createObjectURL(publicKeyBlob);
        const privateKeyURL = window.URL.createObjectURL(privateKeyBlob);

        const publicKeyLink = document.createElement('a');
        publicKeyLink.href = publicKeyURL;
        publicKeyLink.download = this.key + '.pub';

        const privateKeyLink = document.createElement('a');
        privateKeyLink.href = privateKeyURL;
        privateKeyLink.download = this.key + '.pri';

        publicKeyLink.style.display = 'none';
        privateKeyLink.style.display = 'none';

        document.body.appendChild(publicKeyLink);
        document.body.appendChild(privateKeyLink);

        publicKeyLink.click();
        privateKeyLink.click();

        window.URL.revokeObjectURL(publicKeyURL);
        window.URL.revokeObjectURL(privateKeyURL);
      } catch (error) {
        console.log(error);
      }
    },
    inputFile(file) {
      if (file) {
        console.log('File dipilih:', file.name);
        this.file = file;
      }
    },
    browseFile() {
      const fileInput = document.querySelector('input[type="file"]');
      fileInput.click();
    },
    inputPrivateKey(privatekey) {
      if (privatekey) {
        console.log('Private key dipilih:', privatekey.name);
        this.privatekey = privatekey;
      }
    },
    browsePrivateKey() {
      const privateKeyInput = document.querySelectorAll('input[type="file"]')[1];
      privateKeyInput.click();
    },
    async submit() {
      try {
        const formData = new FormData();
        formData.append('filename', this.file);
        formData.append('privatekey', this.privatekey);
        console.log(this.file);
        console.log(this.privatekey);

        const response = await axios.post('http://localhost:5000/api/sign', formData);
        const { message, signed_filename } = response.data;
        console.log(signed_filename);
        if (signed_filename) {
          alert(message);
          this.isSubmitted = true;
        } else {
          console.log('Gagal menandatangani file:', message);
        }
      } catch (error) {
        console.log(error);
      }
    },
  },
});
