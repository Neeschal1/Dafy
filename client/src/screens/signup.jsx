import {
  Dimensions,
  StyleSheet,
  Text,
  View,
  TextInput,
  TouchableOpacity,
  ScrollView,
  Alert,
  KeyboardAvoidingView,
  Platform,
} from "react-native";
import React, { useState } from "react";
import { SafeAreaView } from "react-native-safe-area-context";
import { LinearGradient } from "expo-linear-gradient";
import scaleFontSize from "../utils/responsivefonts";
import { useNavigation } from "@react-navigation/native";
import Signup_an_account from "../api/signupauth";

const screenheight = Dimensions.get("window").height;
const screenwidth = Dimensions.get("window").width;

const Signup = ({navigation}) => {

  const [username, setUsername] = useState("");
  const [firstname, setFirstname] = useState("");
  const [lastname, setLastname] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSignup = async () => {
    try {
      const new_user_account = await Signup_an_account(
        username,
        firstname,
        lastname,
        email,
        password
      );
      Alert.alert("Success", "Account Created!");
      navigation.navigate("Login");
    } catch (err) {
      console.log("SIGNUP ERROR", err);
      const message =
        err.email?.[0] || err.username?.[0] || err.error || "Signup failed";

      Alert.alert("Issue Occurred", message);
    }
  };

  return (
    <SafeAreaView className="bg-background flex-1">
      <KeyboardAvoidingView
        behavior={Platform.OS === "ios" ? "padding" : "height"}
        className="flex-1"
      >
        <ScrollView
          contentContainerStyle={{ flexGrow: 1 }}
          showsVerticalScrollIndicator={false}
          className="flex-1"
        >
          <View
            style={{
              paddingHorizontal: screenwidth * 0.07,
              paddingTop: screenheight * 0.04,
              paddingBottom: screenheight * 0.02,
            }}
            className="flex-1 justify-between"
          >
            {/* Header */}
            <View>
              <View className="flex-row items-center justify-center mb-2">
                <Text
                  style={{
                    fontSize: 40,
                    fontFamily: "Quicksandbold",
                  }}
                  className="text-[#e65100]"
                >
                  D
                </Text>
                <Text
                  style={{
                    fontSize: 40,
                    fontFamily: "Quicksandbold",
                  }}
                  className="text-black"
                >
                  afy
                </Text>
              </View>

              <View style={{ marginBottom: screenheight * 0.04 }}>
                <Text
                  style={{
                    fontFamily: "Quicksandbold",
                    fontSize: scaleFontSize(28),
                  }}
                  className="text-center mb-2"
                >
                  Create Account
                </Text>
                <Text
                  style={{
                    fontFamily: "Quicksandmedium",
                    fontSize: scaleFontSize(15),
                  }}
                  className="text-center opacity-70"
                >
                  Sign up to start buying and selling
                </Text>
              </View>

              {/* Form Fields */}
              <View style={{ gap: screenheight * 0.02 }}>
                <View>
                  <Text
                    style={{
                      fontFamily: "QuicksandSemiBold",
                      fontSize: scaleFontSize(14),
                      marginBottom: screenheight * 0.008,
                    }}
                    className="opacity-80"
                  >
                    Username
                  </Text>
                  <TextInput
                    style={{
                      paddingHorizontal: screenwidth * 0.04,
                      paddingVertical: screenheight * 0.015,
                      fontFamily: "Quicksandmedium",
                      fontSize: scaleFontSize(15),
                    }}
                    className="bg-white border border-gray-300 rounded-lg"
                    placeholder="Enter your username"
                    placeholderTextColor="#999"
                    value={username}
                    onChangeText={setUsername}
                  />
                </View>
                <View>
                  <Text
                    style={{
                      fontFamily: "QuicksandSemiBold",
                      fontSize: scaleFontSize(14),
                      marginBottom: screenheight * 0.008,
                    }}
                    className="opacity-80"
                  >
                    First Name
                  </Text>
                  <TextInput
                    style={{
                      paddingHorizontal: screenwidth * 0.04,
                      paddingVertical: screenheight * 0.015,
                      fontFamily: "Quicksandmedium",
                      fontSize: scaleFontSize(15),
                    }}
                    className="bg-white border border-gray-300 rounded-lg"
                    placeholder="Enter your First Name"
                    placeholderTextColor="#999"
                    value={firstname}
                    onChangeText={setFirstname}
                  />
                </View>
                <View>
                  <Text
                    style={{
                      fontFamily: "QuicksandSemiBold",
                      fontSize: scaleFontSize(14),
                      marginBottom: screenheight * 0.008,
                    }}
                    className="opacity-80"
                  >
                    Last Name
                  </Text>
                  <TextInput
                    style={{
                      paddingHorizontal: screenwidth * 0.04,
                      paddingVertical: screenheight * 0.015,
                      fontFamily: "Quicksandmedium",
                      fontSize: scaleFontSize(15),
                    }}
                    className="bg-white border border-gray-300 rounded-lg"
                    placeholder="Enter your Last Name"
                    placeholderTextColor="#999"
                    value={lastname}
                    onChangeText={setLastname}
                  />
                </View>

                <View>
                  <Text
                    style={{
                      fontFamily: "QuicksandSemiBold",
                      fontSize: scaleFontSize(14),
                      marginBottom: screenheight * 0.008,
                    }}
                    className="opacity-80"
                  >
                    Email
                  </Text>
                  <TextInput
                    style={{
                      paddingHorizontal: screenwidth * 0.04,
                      paddingVertical: screenheight * 0.015,
                      fontFamily: "Quicksandmedium",
                      fontSize: scaleFontSize(15),
                    }}
                    className="bg-white border border-gray-300 rounded-lg"
                    placeholder="Enter your email"
                    placeholderTextColor="#999"
                    value={email}
                    onChangeText={setEmail}
                    keyboardType="email-address"
                    autoCapitalize="none"
                  />
                </View>

                <View>
                  <Text
                    style={{
                      fontFamily: "QuicksandSemiBold",
                      fontSize: scaleFontSize(14),
                      marginBottom: screenheight * 0.008,
                    }}
                    className="opacity-80"
                  >
                    Password
                  </Text>
                  <TextInput
                    style={{
                      paddingHorizontal: screenwidth * 0.04,
                      paddingVertical: screenheight * 0.015,
                      fontFamily: "Quicksandmedium",
                      fontSize: scaleFontSize(15),
                    }}
                    className="bg-white border border-gray-300 rounded-lg"
                    placeholder="Create a password"
                    placeholderTextColor="#999"
                    value={password}
                    onChangeText={setPassword}
                    secureTextEntry
                  />
                </View>
              </View>

              {/* Sign Up Button */}
              <TouchableOpacity
                // onPress={handleSignup}
                onPress={()=>{navigation.navigate("Products")}}
                style={{ marginTop: screenheight * 0.03 }}
              >
                <LinearGradient
                  colors={["#f6aa1c", "#f86624"]}
                  start={{ x: 0, y: 0 }}
                  end={{ x: 1, y: 0 }}
                  style={{
                    height: screenheight * 0.061,
                    borderRadius: 10,
                    shadowColor: "#000",
                    shadowOffset: { width: 0, height: 2 },
                    shadowOpacity: 0.2,
                    shadowRadius: 3,
                  }}
                  className="justify-center items-center"
                >
                  <Text
                    style={{
                      fontFamily: "QuicksandMedium",
                      fontSize: scaleFontSize(18),
                    }}
                    className="text-white"
                  >
                    Create Account
                  </Text>
                </LinearGradient>
              </TouchableOpacity>
            </View>

            {/* Footer */}
            <View className="flex-row items-center justify-center gap-1 mt-4">
              <Text style={{ fontFamily: "Quicksandmedium" }}>
                Already have an account?
              </Text>
              <TouchableOpacity onPress={() => navigation.navigate("Login")}>
                <Text
                  style={{ fontFamily: "QuicksandSemiBold" }}
                  className="text-[#f86624]"
                >
                  Log In
                </Text>
              </TouchableOpacity>
            </View>
          </View>
        </ScrollView>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
};

export default Signup;

const styles = StyleSheet.create({});
