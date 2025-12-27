import {
  Dimensions,
  Modal,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
  BackHandler,
} from "react-native";
import React, { useEffect, useState } from "react";
import LottieView from "lottie-react-native";
import { LinearGradient } from "expo-linear-gradient";
import scaleFontSize from "../utils/responsivefonts";
import { useNavigation } from "@react-navigation/native";

const animation = require("../assets/lottie/shopping girl.json");

const screenheight = Dimensions.get("window").height;
const screenwidth = Dimensions.get("window").width;

const Welcome = () => {
  const navigation = useNavigation();
  const [exitModalVisible, setExitModalVisible] = useState(false);

  useEffect(() => {
    const backAction = () => {
      setExitModalVisible(true);
      return true;
    };

    const backHandler = BackHandler.addEventListener(
      "hardwareBackPress",
      backAction
    );

    return () => backHandler.remove();
  }, []);

  return (
    <View
      style={{
        flex: 1,
        alignItems: "center",
        justifyContent: "space-evenly",
        marginBottom: 20,
      }}

      className="bg-background"
    >
      {/* Header + Lottie */}
      <View
        style={{
          flex: 1,
          alignItems: "center",
          justifyContent: "center",
          marginBottom: screenheight * 0.15,
        }}
      >
        <View
          style={{
            flexDirection: "row",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          <Text
            style={{
              color: "#e65100",
              fontSize: 50,
              fontFamily: "Quicksandbold",
            }}
          >
            D
          </Text>
          <Text
            style={{
              color: "black",
              fontSize: 50,
              fontFamily: "Quicksandbold",
            }}
          >
            afy
          </Text>
        </View>

        <LottieView
          style={{
            height: screenheight * 0.4,
            width: screenwidth * 0.7,
          }}
          source={animation}
          autoPlay
          loop
        />
      </View>

      {/* Welcome Text + Button */}
      <View style={{ gap: screenheight * 0.03 }}>
        <View style={{ width: screenwidth * 0.85, gap: screenheight * 0.02 }}>
          <Text
            style={{
              fontFamily: "Quicksandmedium",
              textAlign: "center",
              opacity: 0.7,
              fontSize: scaleFontSize(15),
              lineHeight: 22,
            }}
          >
            Welcome to Dafy — Your Trusted Marketplace for Second-Hand
            Treasures!
          </Text>

          <TouchableOpacity 
          onPress={() => navigation.navigate("Signup")}
          >
            <LinearGradient
              colors={["#f6aa1c", "#f86624"]}
              start={{ x: 0, y: 0 }}
              end={{ x: 1, y: 0 }}
              style={{
                width: screenwidth * 0.886,
                height: screenheight * 0.061,
                borderRadius: 10,
                justifyContent: "center",
                alignItems: "center",
                shadowColor: "#000",
                shadowOffset: { width: 0, height: 2 },
                shadowOpacity: 0.2,
                shadowRadius: 3,
                // elevation: 4,
              }}
            >
              <Text
                style={{
                  fontFamily: "QuicksandMedium",
                  color: "#ffffff",
                  fontSize: scaleFontSize(18),
                }}
              >
                Let's Begin
              </Text>
            </LinearGradient>
          </TouchableOpacity>
        </View>

        {/* Footer */}
        <View
          style={{
            flexDirection: "row",
            gap: 5,
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <TouchableOpacity>
            <Text style={{ fontFamily: "QuicksandSemiBold" }}>© Dafy.</Text>
          </TouchableOpacity>
          <Text style={{ fontFamily: "Quicksandlight" }}>
            All rights reserved.
          </Text>
        </View>
      </View>

      {/* Custom Exit Modal */}
      <Modal
        animationType="fade"
        transparent
        visible={exitModalVisible}
        onRequestClose={() => setExitModalVisible(false)}
      >
        <View
          style={{
            flex: 1,
            backgroundColor: "rgba(0,0,0,0.5)",
            justifyContent: "center",
            alignItems: "center",
          }}
        >
          <View
            style={{
              width: "80%",
              backgroundColor: "#fff",
              padding: 20,
              borderRadius: 12,
              alignItems: "center",
              elevation: 10,
            }}
          >
            <View style={{ alignItems: "center" }}>
              <Text
                style={{
                  fontSize: scaleFontSize(20),
                  fontFamily: "Quicksandbold",
                  marginBottom: screenheight * 0.01,
                }}
              >
                Exit App
              </Text>
              <Text
                style={{
                  fontSize: scaleFontSize(16),
                  fontFamily: "Quicksandmedium",
                  textAlign: "center",
                  marginBottom: screenheight * 0.04,
                }}
              >
                Do you really want to exit Dafy?
              </Text>
            </View>
            <View style={{ flexDirection: "row", gap: 15 }}>
              <TouchableOpacity
                onPress={() => setExitModalVisible(false)}
                style={{
                  paddingVertical: screenheight * 0.015,
                  paddingHorizontal: screenheight * 0.03,
                  backgroundColor: "#efefefff",
                  borderRadius: 8,
                  justifyContent: "center",
                  alignItems: "center",
                }}
              >
                <Text
                  style={{
                    fontFamily: "Quicksandmedium",
                    color: "#000000ff",
                  }}
                >
                  Cancel
                </Text>
              </TouchableOpacity>

              <TouchableOpacity
                onPress={() => BackHandler.exitApp()}
                style={{
                  paddingVertical: screenheight * 0.015,
                  paddingHorizontal: screenheight * 0.03,
                  backgroundColor: "#f86624",
                  borderRadius: 8,
                  justifyContent: "center",
                  alignItems: "center",
                }}
              >
                <Text
                  style={{
                    fontFamily: "Quicksandmedium",
                    color: "#fff",
                    fontSize: scaleFontSize(18),
                  }}
                >
                  Exit
                </Text>
              </TouchableOpacity>
            </View>
          </View>
        </View>
      </Modal>
    </View>
  );
};

export default Welcome;
