import React from "react";
import { useNavigate } from "react-router-dom";

const Landing = () => {
  const navigation = useNavigate();

  const handleLogin = () => {
    navigation("/login")
  };

  const handleSignup = () => {
    navigation("/signup")
  };

  return (
    <div className="flex w-full h-full justify-center items-center flex-col gap-30">
      <h1>Landing</h1>
      <div className="flex gap-10 flex-col">
        <button onClick={handleLogin} className="bg-black hover:bg-amber-400 cursor-pointer text-white hover:text-black py-7 px-10 rounded-2xl">
          Login
        </button>
        <button onClick={handleSignup} className="bg-black hover:bg-amber-400 cursor-pointer text-white hover:text-black py-7 px-10 rounded-2xl">
          Signup
        </button>
      </div>
    </div>
  );
};

export default Landing;
