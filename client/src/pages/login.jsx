import React, { useState } from "react";
import LoginUserData from "../api/login";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [seePassword, setSeePassword] = useState(false);
  const [pswrd, setPswrd] = useState("password");
  const [loading, setLoading] = useState(false);
  const [ermsg, setErmsg] = useState(null);

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const navigation = useNavigate();

  const handleLogin = () => {
    console.log("Email: ", email);
    console.log("Password: ", password);
    const api = LoginUserData(email, password, navigation, setLoading);
    if (api) {
      setErmsg(api);
    }
  };

  const handleSeePassword = () => {
    if (seePassword == false) {
      setPswrd("password");
      setSeePassword(true);
    } else {
      setSeePassword(false);
      setPswrd("text");
    }
  };

  return (
    <div className="border py-30 px-20 rounded-2xl">
      <h1 className="text-6xl font-bold">Login with Dafy</h1>
      <div className="flex gap-10 flex-col mt-10">
        <div className="flex flex-col gap-5">
          <div className="flex gap-2 flex-col">
            <h1 className="text-2xl">Email</h1>
            <input
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="Enter your email"
              className="flex items-center w-full border border-white/30 rounded-xl px-4 py-3 bg-white/5 focus-within:border-white transition duration-200"
              type="email"
            />
          </div>
          <div className="flex flex-col gap-2 w-full">
            <h1 className="text-lg font-semibold text-white">Password</h1>

            <div className="flex items-center w-full border border-white/30 rounded-xl px-4 py-3 bg-white/5 focus-within:border-white transition duration-200">
              <input
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                type={`${pswrd}`}
                placeholder="Enter your password"
                className="flex-1 bg-transparent outline-none text-white placeholder-white/50"
              />
              
              <button
                onClick={handleSeePassword}
                type="button"
                className="text-sm text-blue-400 hover:text-blue-300 transition duration-200"
              >
                {seePassword ? "Show" : "Hide"}
              </button>
            </div>
          </div>
        </div>
        <h1>{ermsg}</h1>
        <button
          onClick={handleLogin}
          className="w-full h-15 rounded-l justify-center items-center bg-[#FF6600] hover:bg-[#cc5302] duration-400 cursor-pointer text-back text-2xl"
        >
          {loading ? "Loading..." : "Next"}
        </button>
      </div>
      <div className="flex gap-10 mt-10 items-center flex-col">
        <h3 className="">Or</h3>
        <div className="flex-row flex gap-3">
          <h2 className="text-xl">Don't have an account?</h2>
          <a className="text-xl" href="http://localhost:5173/signup">
            Signup
          </a>
        </div>
      </div>
    </div>
  );
};

export default Login;
