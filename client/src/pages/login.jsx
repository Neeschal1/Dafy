import React from "react";

const Login = () => {
  return (
    <div>
      <h1 className="text-6xl font-bold">Login with Dafy</h1>
      <div className="flex gap-10 flex-col mt-10">
        <div className="flex gap-2 flex-col">
          <h1 className="text-2xl">Email</h1>
          <input
          placeholder="Enter your email"
            className="border border-white/40 w-full h-15 pl-5 rounded-l text-2xl"
            type="email"
          />
        </div>
        <button className="w-full h-15 rounded-l justify-center items-center bg-[#FF6600] hover:bg-[#cc5302] duration-400 cursor-pointer text-back">
          Next
        </button>
      </div>
      <div className="flex gap-10 mt-10 items-center flex-col">
        <h3 className="">Or</h3>
        <div className="flex-row flex gap-3">
          <h2 className="text-xl">Don't have an account?</h2>
          <a className="text-xl" href="http://localhost:5173/signup">Signup</a>
        </div>
      </div>
    </div>
  );
};

export default Login;
