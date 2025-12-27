import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import Ionicons from '@expo/vector-icons'
import Home from "../screens/home";
import Browse from "../screens/browse";
import Cart from "../screens/cart";
import Profile from "../screens/profile";
import Messages from "../screens/message";

const Tab = createBottomTabNavigator();

const MyTabs = () => {
  return (
    <Tab.Navigator
      initialRouteName="Home"
      screenOptions={{ 
        headerShown: false, 
        tabBarActiveTintColor: "#f86624",
    }}
    >
      <Tab.Screen name="Home" component={Home} 
    //   options={{tabBarIcon : ({name, size}) => (
    //     <Ionicons name='home-outline' size='24'/>
    //   )}}
      />
      <Tab.Screen name="Browse" component={Browse} />
      <Tab.Screen name="Cart" component={Cart} />
      <Tab.Screen name="Messages" component={Messages} />
      <Tab.Screen name="Profile" component={Profile} />
    </Tab.Navigator>
  );
};

export default MyTabs;
