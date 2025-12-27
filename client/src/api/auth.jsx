import axios from "axios";
import AsyncStorage from "@react-native-async-storage/async-storage";
import { Alert } from "react-native";

const root_api = "http://10.0.2.2:8000/";

const Signup_an_account = async (
  username,
  first_name,
  last_name,
  email,
  password
) => {
  try {
    const new_account = await axios.post(`${root_api}signup/`, {
      username,
      first_name,
      last_name,
      email,
      password,
    });
    return new_account.data;
  } catch (err) {
    throw err.response?.data ?? { error: err.message };
  }
};

export default Signup_an_account