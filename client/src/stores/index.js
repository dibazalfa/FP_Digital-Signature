import { defineStore } from 'pinia';
import axios from 'axios';
import Swal from 'sweetalert2';

// const URL_API = "http://localhost:5000";

export const useApp = defineStore({
  id: 'App',
  state: () => ({
    key: '',
    publicKey: '',
    privateKey: '',
    file: null,
    privatekey: null,
    publicKey: null,
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
          // alert(message);
          Swal.fire({
            icon:  'success',
            title: message,
          })
          this.isSubmitted = true;
        } else {
          // console.log('Signed file not falid');
          Swal.fire({
            icon:  'error',
            title:  'Gagal Menandatangani File'
          })
        }
      } catch (error) {
        console.log(error);
      }
    },
    async submitvalidator() {
      try {
        const formData = new FormData();
        formData.append('filename', this.file);
        formData.append('publicKey', this.publicKey);
        formData.append('Sign', this.Sign);
        console.log(this.file);
        console.log(this.publicKey);
        console.log(this.Sign);

        const response = await axios.post('http://localhost:5000/api/validation', formData);
        const { message, error } = response.data;

        if (error) {
          alert(error);
        } else {
          // alert(message);
          Swal.fire({
            title:  message,
          })
          this.isSubmitted = true;
        }
      } catch (error) {
        console.log(error);
      }
    },

    inputPublicKey(publicKey) {
      if (publicKey) {
        console.log('publicKey key dipilih:', publicKey.name);
        this.publicKey = publicKey;
      }
    },
    browsePublicKey() {
      const publicKeyInput = document.querySelectorAll('input[type="file"]')[1];
      publicKeyInput.click();
    },
    inputSign(Sign) {
      if (Sign) {
        console.log('Sign key dipilih:', Sign.name);
        this.Sign = Sign;
      }
    },
    browseSign() {
      const inputSign = document.querySelectorAll('input[type="file"]')[1];
      inputSign.click();
    },
  },
});
