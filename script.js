const fileInput = document.getElementById("fileInput");
const previewImg = document.getElementById("previewImg");
const placeholder = document.getElementById("placeholder");
const uploadBtn = document.getElementById("uploadBtn");
const analyzeBtn = document.getElementById("analyzeBtn");
const resultBox = document.getElementById("resultBox");
const cameraBtn = document.getElementById("cameraBtn");
const cameraBox = document.getElementById("cameraBox");
const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const captureBtn = document.getElementById("captureBtn");
const stopBtn = document.getElementById("stopBtn");
const openBreedDB = document.getElementById("openBreedDB");
const closeBreedDB = document.getElementById("closeBreedDB");
const breedDB = document.getElementById("breedDB");
let stream;

// Upload
uploadBtn.onclick = () => fileInput.click();
fileInput.onchange = (e) => {
  const file = e.target.files[0];
  if (!file) return;
  const url = URL.createObjectURL(file);
  previewImg.src = url;
  previewImg.classList.remove("hidden");
  placeholder.classList.add("hidden");
  resultBox.textContent = "Image ready — click Analyze.";
};

// Analyze
analyzeBtn.onclick = () => {
  if (previewImg.src) {
    resultBox.innerHTML = `
      <div class="p-3 border rounded-lg bg-green-50">
        Best Match: <b>Murrah</b> (92%)<br>Type: Buffalo
      </div>`;
  } else {
    resultBox.textContent = "Please upload or capture an image first.";
  }
};

// Camera
cameraBtn.onclick = async () => {
  stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } });
  video.srcObject = stream;
  video.play();
  cameraBox.classList.remove("hidden");
};

captureBtn.onclick = () => {
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  canvas.getContext("2d").drawImage(video, 0, 0);
  canvas.toBlob((blob) => {
    const url = URL.createObjectURL(blob);
    previewImg.src = url;
    previewImg.classList.remove("hidden");
    placeholder.classList.add("hidden");
    resultBox.textContent = "Captured — click Analyze.";
  });
};

stopBtn.onclick = () => {
  stream.getTracks().forEach((t) => t.stop());
  cameraBox.classList.add("hidden");
};

// Modal
openBreedDB.onclick = () => breedDB.classList.remove("hidden");
closeBreedDB.onclick = () => breedDB.classList.add("hidden");
