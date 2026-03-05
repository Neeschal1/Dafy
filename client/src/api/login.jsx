import axios from "axios";
import React from "react";
import url from "../constants/url";

const LoginUserData = async (email, password, navigation, setLoading) => {
  const credentials = {
    Email: email,
    Password: password,
  };
  try {
    setLoading(true);
    const res = await axios.post(`${url}accounts/login/`, credentials, {
      headers: {
        "Content-Type": "application/json",
      },
    });
    const passworderror = res.data["Message"];
    const errormsg =
      "Invalid Credentials! Please check your password and then try again!";
    console.log(passworderror);
    if (passworderror == errormsg) {
      return errormsg;
    }
    setLoading(false);
  } catch (err) {
    const errormessage = err.response["data"]["Message"];
    console.log(errormessage);
    setLoading(false);
    return errormessage;
  } 
//   finally {
//     navigation("/home");
//   }
};

export default LoginUserData;
