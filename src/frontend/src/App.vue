<template>
  <div class="page-loader" v-if="!isLoaded">
    <div style="background-color: #8cc271" class="cube first"></div>
    <div style="background-color: #69beeb" class="cube"></div>
    <div style="background-color: #f5aa39" class="cube"></div>
    <div style="background-color: #e9643b" class="cube last"></div>
  </div>
  <div id="head">
      <p style="cursor: pointer;">BÁCH KHOA TP.HCM - TẠO MÀU CHO ẢNH XÁM <a target="_blank" style="color: yellow;" href="https://github.com/dee-ex/EE3151_SEM202_PROJECT/">[Github]</a></p>
      <img id="logo" src="./assets/hcmut.png">
  </div>

  <div id="up">
      <button id="button" onclick="document.getElementById('inputfile').click()">CHỌN ẢNH</button>
      <input type='file' id="inputfile" style="display:none" @change="onFileChange">
      <button id="process" @click="onProcess">TẠO MÀU</button>
  </div>

  <div id="down">
      <div id="left">
        <img v-if="url" :src="url" alt="Ảnh xám">
      </div>
      <div id="right">
        <img v-if="outurl" :src="outurl" alt="Ảnh sau khi tạo màu">
      </div>
  </div>
  <footer><p>© Nguyễn Thành Trung - 1814515 (trung.nguyendx@hcmut.edu.vn)</p></footer>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      isLoaded: false,
      file: null,
      url: null,
      outurl: null,
      fd: null,
    }
  },
  mounted() {
    document.onreadystatechange = () => {
      if (document.readyState == "complete") {
        this.isLoaded = true;
      }
    }
  },
  methods: {
    onFileChange(e) {
      this.file = e.target.files[0];
      this.url = URL.createObjectURL(this.file);
    },

    onProcess() {
      this.isLoaded = false;

      this.fd = new FormData();

      this.fd.append("image", this.file);

      fetch("http://localhost:8000/main/", {method: "POST", body: this.fd})
      .then(response => response.blob())
      .then(blob => {
        this.outurl = URL.createObjectURL(blob);
        this.isLoaded = true;
      });
    },
  },
}
</script>

<style>

@keyframes left {
  40% {
    transform: translateX(-60px);
  }

  50% {
    transform: translateX(0);
  }
}

@keyframes right {
  40% {
    transform: translateX(60px);
  }

  50% {
    transform: translateX(0);
  }
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  padding-left: 10%;
  padding-right: 10%;
}

div {
  border-radius: 12px;
}

.page-loader {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(3, 3, 3, .3);
  z-index: 999;
}

.cube {
  width: 40px;
  height: 40px;
  margin-right: 10px;
}

.first {
  animation: left 1s infinite;
}

.last {
  animation: right 1s infinite .5s;
}

#head {
    padding: 10px;
    text-align: center;
    background-color: #074B80;
    font-size: 30px;
    font-weight: bold;
    color: white;
    margin: 1%;
}

#up {
    padding: 10px 10px;
    margin: 1%;
    padding-left: 39%;
}

#logo {
    width: 5%;
    height: 5%;
    cursor: pointer;
}

#button {
    display: block;
    background-color: white;
    border: 2px solid #074B80;
    color: black;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    border-radius: 12px;
    margin-right: 10px;
}

#process {
    display: block;
    background-color: white;
    border: 2px solid #4CAF50;
    color: black;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    border-radius: 12px;
}

#button:hover {
    background-color: #074B80;
    color: white;
    cursor: pointer;
}

#process:hover {
    background-color: #4CAF50;
    color: white;
    cursor: pointer;
}

#left {
    float: left;
    background: gray;
    width: 48%;
    height: 500px;
    margin: 1%;
    display: flex;
    align-items: center;
    justify-content: center;
}

#right {
    float: right;
    background: gray;
    width: 48%;
    height: 500px;
    margin: 1%;
    display: flex;
    align-items: center;
    justify-content: center;
}

footer {
    margin: 1%;
    text-align: center;
    color: #074B80;
    font-size: 20px;
    margin-top: 38%;
}
</style>
