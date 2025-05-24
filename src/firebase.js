// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyA9zMV3EMoGRKygYXJApmCNIWyDfXDenWk",
  authDomain: "nutrilytics-55dbf.firebaseapp.com",
  projectId: "nutrilytics-55dbf",
  storageBucket: "nutrilytics-55dbf.firebasestorage.app",
  messagingSenderId: "412102134593",
  appId: "1:412102134593:web:c27e96d203bc3d79466fc0",
  measurementId: "G-8XQKJTR1G5"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// ✅ Export the auth object correctly
const auth = getAuth(app);
export { auth };