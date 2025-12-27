import { StatusBar, StyleSheet, Text, View } from "react-native";
import React from "react";
import Welcome from "../src/screens/welcome";
import { customFonts } from "../src/utils/fonts";
import { useFonts } from "expo-font";
import '../global.css'

const Index = () => {
  const [fontsLoaded] = useFonts(customFonts);
  if (!fontsLoaded) return null;
  return (
    <>
      {/* <StatusBar hidden /> */}
      <View
        style={{
          flex: 1,
          justifyContent: "center",
          alignItems: "center",
          padding: 20,
        }}
      >
        <Welcome />
      </View>
    </>
  );
};

export default Index;

const styles = StyleSheet.create({});
