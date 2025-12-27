import axios from "axios";
import { View } from "react-native-web";

const login_url = 'http://10.0.2.2:8000/'

const Login_an_account = async (email, password) => {
    try{
        const login = await axios.post(`${login_url}accounts/login`, {email, password})
        return login.data

    } catch (err) {
        return (<View><Text>Login Failed!</Text></View>)
    }
}

export default Login_an_account