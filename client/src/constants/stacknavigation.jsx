import { StyleSheet, Text, View } from "react-native";
import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import Signup from '../screens/signup'
import Welcome from '../screens/welcome'
import Login from '../screens/login'
import MyTabs from './bottomtabbar' 
import { createNativeStackNavigator } from "@react-navigation/native-stack";

const Stack = createNativeStackNavigator();

const Stacknavigation = () => {
  return (
    
      <Stack.Navigator initialRouteName="Login">
        <Stack.Screen name="Welcome" component={Welcome} options={{
          headerShown: false,
          title: " "
        }}/>
        <Stack.Screen name="Signup" component={Signup} 
        options={{
          headerShown: true,
          title: " ",
          headerTransparent: true,
          headerStyle: {
            backgroundColor: "transparent"
          }
        }}
        />
        <Stack.Screen name="Login" component={Login} 
        options={{
          headerShown: true,
          title: " ",
          headerTransparent: true,
          headerStyle: {
            backgroundColor: "transparent"
          }
        }}
        />
        <Stack.Screen name="MyTabs" component={MyTabs} 
        options={{
          headerShown: false,
          title: " ",
          headerTransparent: true,
          headerStyle: {
            backgroundColor: "transparent"
          }
        }}
        />
      </Stack.Navigator>
    
  );
};

export default Stacknavigation;

const styles = StyleSheet.create({});
