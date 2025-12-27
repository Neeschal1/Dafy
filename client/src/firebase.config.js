import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import {getAuth, GoogleAuthProvider} from 'firebase/auth'

const firebaseConfig = {
  apiKey: "AIzaSyAj4UYZ5YvyKBJ8R5On6yxvhksjEdRx3CE",
  authDomain: "dafy-56c48.firebaseapp.com",
  projectId: "dafy-56c48",
  storageBucket: "dafy-56c48.firebasestorage.app",
  messagingSenderId: "673853603112",
  appId: "1:673853603112:web:e6d50bbd2d46f59d62241d",
};

const app = initializeApp(firebaseConfig);

const auth = getAuth(app)
const googleauth = new GoogleAuthProvider(app)

const analytics = getAnalytics(app);

export {auth, googleauth}