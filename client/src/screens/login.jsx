import {
  Dimensions,
  StyleSheet,
  Text,
  View,
  TextInput,
  TouchableOpacity,
  ScrollView,
  KeyboardAvoidingView,
  Platform,
  Alert,
} from "react-native";
import React, { useState } from "react";
import { SafeAreaView } from "react-native-safe-area-context";
import { LinearGradient } from "expo-linear-gradient";
import scaleFontSize from "../utils/responsivefonts";
import Login_an_account from '../api/loginuserverify'

const screenheight = Dimensions.get("window").height;
const screenwidth = Dimensions.get("window").width;

const Login = ({navigation}) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    try{
        const res = await Login_an_account(email, password)
        Alert.alert('Welcome', res.Message)
        navigation.navigate('MyTabs')
    } catch (err) {

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
              paddingTop: screenheight * 0.08,
              paddingBottom: screenheight * 0.02,
            }}
            className="flex-1 justify-between"
          >
            {/* Header */}
            <View>
              <View className="flex-row items-center justify-center mb-3">
                <Text
                  style={{
                    fontSize: 45,
                    fontFamily: "Quicksandbold",
                  }}
                  className="text-[#e65100]"
                >
                  D
                </Text>
                <Text
                  style={{
                    fontSize: 45,
                    fontFamily: "Quicksandbold",
                  }}
                  className="text-black"
                >
                  afy
                </Text>
              </View>

              <View style={{ marginBottom: screenheight * 0.06 }}>
                <Text
                  style={{
                    fontFamily: "Quicksandbold",
                    fontSize: scaleFontSize(32),
                  }}
                  className="text-center mb-2"
                >
                  Welcome Back
                </Text>
                <Text
                  style={{
                    fontFamily: "Quicksandmedium",
                    fontSize: scaleFontSize(15),
                    lineHeight: 22,
                  }}
                  className="text-center opacity-70"
                >
                  Log in to continue your shopping journey
                </Text>
              </View>

              {/* Form Fields */}
              <View style={{ gap: screenheight * 0.025 }}>
                <View>
                  <Text
                    style={{
                      fontFamily: "QuicksandSemiBold",
                      fontSize: scaleFontSize(14),
                      marginBottom: screenheight * 0.01,
                    }}
                    className="opacity-80"
                  >
                    Email
                  </Text>
                  <TextInput
                    style={{
                      paddingHorizontal: screenwidth * 0.04,
                      paddingVertical: screenheight * 0.018,
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
                  <View className="flex-row items-center justify-between mb-2">
                    <Text
                      style={{
                        fontFamily: "QuicksandSemiBold",
                        fontSize: scaleFontSize(14),
                      }}
                      className="opacity-80"
                    >
                      Password
                    </Text>
                    <TouchableOpacity>
                      <Text
                        style={{
                          fontFamily: "QuicksandSemiBold",
                          fontSize: scaleFontSize(13),
                        }}
                        className="text-[#f86624]"
                      >
                        Forgot?
                      </Text>
                    </TouchableOpacity>
                  </View>
                  <TextInput
                    style={{
                      paddingHorizontal: screenwidth * 0.04,
                      paddingVertical: screenheight * 0.018,
                      fontFamily: "Quicksandmedium",
                      fontSize: scaleFontSize(15),
                    }}
                    className="bg-white border border-gray-300 rounded-lg"
                    placeholder="Enter your password"
                    placeholderTextColor="#999"
                    value={password}
                    onChangeText={setPassword}
                    secureTextEntry
                  />
                </View>
              </View>

              {/* Login Button */}
              <TouchableOpacity
                onPress={handleLogin}
                style={{ marginTop: screenheight * 0.04 }}
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
                    Log In
                  </Text>
                </LinearGradient>
              </TouchableOpacity>

              {/* Divider */}
              <View
                className="flex-row items-center justify-center"
                style={{ marginTop: screenheight * 0.04 }}
              >
                <View className="flex-1 h-[1px] bg-gray-300" />
                <Text
                  style={{
                    fontFamily: "Quicksandmedium",
                    paddingHorizontal: 15,
                    fontSize: scaleFontSize(14),
                  }}
                  className="opacity-60"
                >
                  OR
                </Text>
                <View className="flex-1 h-[1px] bg-gray-300" />
              </View>

              {/* Social Login Buttons */}
              <View style={{ gap: screenheight * 0.015, marginTop: screenheight * 0.03 }}>
                <TouchableOpacity
                  style={{
                    paddingVertical: screenheight * 0.015,
                    borderWidth: 1,
                  }}
                  className="bg-white border-gray-300 rounded-lg flex-row items-center justify-center"
                >
                  <Text
                    style={{
                      fontFamily: "QuicksandSemiBold",
                      fontSize: scaleFontSize(15),
                    }}
                  >
                    Continue with Google
                  </Text>
                </TouchableOpacity>

                <TouchableOpacity
                  style={{
                    paddingVertical: screenheight * 0.015,
                    borderWidth: 1,
                  }}
                  className="bg-white border-gray-300 rounded-lg flex-row items-center justify-center"
                >
                  <Text
                    style={{
                      fontFamily: "QuicksandSemiBold",
                      fontSize: scaleFontSize(15),
                    }}
                  >
                    Continue with Apple
                  </Text>
                </TouchableOpacity>
              </View>
            </View>

            {/* Footer */}
            <View style={{ marginTop: screenheight * 0.04 }}>
              <View className="flex-row items-center justify-center gap-1">
                <Text style={{ fontFamily: "Quicksandmedium" }}>
                  Don't have an account?
                </Text>
                <TouchableOpacity onPress={() => navigation.navigate("Signup")}>
                  <Text
                    style={{ fontFamily: "QuicksandSemiBold" }}
                    className="text-[#f86624]"
                  >
                    Sign Up
                  </Text>
                </TouchableOpacity>
              </View>

              {/* Copyright Footer */}
              <View
                className="flex-row items-center justify-center gap-1"
                style={{ marginTop: screenheight * 0.02 }}
              >
                <TouchableOpacity>
                  <Text style={{ fontFamily: "QuicksandSemiBold" }}>© Dafy.</Text>
                </TouchableOpacity>
                <Text style={{ fontFamily: "Quicksandlight" }}>
                  All rights reserved.
                </Text>
              </View>
            </View>
          </View>
        </ScrollView>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
};

export default Login;

const styles = StyleSheet.create({});