import { StatusBar, StyleSheet, Text, View } from "react-native";
import React from "react";
import Stacknavigation from '../src/constants/stacknavigation'
import { customFonts } from "../src/utils/fonts";
import { useFonts } from "expo-font";
import '../global.css'
import { useNavigation } from "expo-router";

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
        <Stacknavigation />
      </View>
    </>
  );
};

export default Index;

const styles = StyleSheet.create({});
