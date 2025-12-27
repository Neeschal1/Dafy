import {
  StyleSheet,
  Text,
  View,
  Image,
  ScrollView,
  TouchableOpacity,
} from "react-native";
import React, { useEffect, useState } from "react";
import { SafeAreaView } from "react-native-safe-area-context";
import ProductList from "../api/products";

const Home = () => {
  const [category, setCategory] = useState([]);

  const handleProducts = async () => {
    try {
      const prod = await ProductList();
      setCategory(prod);
      console.log("Products:", prod);
    } catch (err) {
      console.log("API Error:", err);
    }
  };

  useEffect(() => {
    handleProducts();
  }, []);

  return (
    <SafeAreaView className="flex flex-1 bg-background p-5">
      <ScrollView showsVerticalScrollIndicator={false}>
        <Text style={styles.sectionTitle}>Categories</Text>

        {/* HORIZONTAL LIST */}
        <ScrollView
          horizontal
          showsHorizontalScrollIndicator={false}
          contentContainerStyle={styles.scrollContent}
        >
          {category.map((item) => (
            <TouchableOpacity
              key={item.id}
              style={styles.categoryCard}
              activeOpacity={0.7}
            >
              <View style={styles.imageContainer}>
                <Image
                  source={{ uri: item.Prod_Image }}
                  style={styles.categoryImage}
                  resizeMode="cover"
                />
                <View style={styles.ratingBadge}>
                  <Text style={styles.ratingText}>⭐ {item.Prod_Rate}</Text>
                </View>
              </View>

              {/* TEXT BELOW IMAGE */}
              <Text style={styles.categoryName}>{item.Prod_Name}</Text>
            </TouchableOpacity>
          ))}
        </ScrollView>

        {/* GRID VIEW */}
        <Text style={[styles.sectionTitle, styles.gridTitle]}>
          Grid View
        </Text>

        <View style={styles.gridContainer}>
          {category.map((item) => (
            <TouchableOpacity
              key={item.id}
              style={styles.gridCard}
              activeOpacity={0.7}
            >
              <View style={styles.gridImageContainer}>
                <Image
                  source={{ uri: item.Prod_Image }}
                  style={styles.gridImage}
                  resizeMode="cover"
                />
                <View style={styles.gridRatingBadge}>
                  <Text style={styles.gridRatingText}>⭐ {item.Prod_Rate}</Text>
                </View>
              </View>

              {/* TEXT BELOW IMAGE */}
              <Text style={styles.gridCategoryName}>{item.Prod_Name}</Text>
            </TouchableOpacity>
          ))}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
};

export default Home;

const styles = StyleSheet.create({
  sectionTitle: {
    fontSize: 24,
    fontWeight: "bold",
    color: "#1F2937",
    marginBottom: 16,
  },
  scrollContent: {
    paddingRight: 20,
  },

  /* Horizontal Card */
  categoryCard: {
    marginRight: 16,
    width: 140,
  },
  imageContainer: {
    position: "relative",
    borderRadius: 16,
    overflow: "hidden",
    marginBottom: 8,
  },
  categoryImage: {
    width: 140,
    height: 140,
    backgroundColor: "#E5E7EB",
  },
  ratingBadge: {
    position: "absolute",
    top: 8,
    right: 8,
    backgroundColor: "rgba(255, 255, 255, 0.95)",
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 12,
  },
  ratingText: {
    fontSize: 12,
    fontWeight: "600",
    color: "#1F2937",
  },
  categoryName: {
    fontSize: 14,
    fontWeight: "600",
    color: "#000000",
    textAlign: "center",
  },

  /* Grid */
  gridTitle: {
    marginTop: 32,
  },
  gridContainer: {
    flexDirection: "row",
    flexWrap: "wrap",
    justifyContent: "space-between",
    gap: 12,
  },
  gridCard: {
    width: "48%",
    marginBottom: 16,
  },
  gridImageContainer: {
    position: "relative",
    borderRadius: 16,
    overflow: "hidden",
    marginBottom: 8,
  },
  gridImage: {
    width: "100%",
    height: 160,
    backgroundColor: "#E5E7EB",
  },
  gridRatingBadge: {
    position: "absolute",
    top: 8,
    right: 8,
    backgroundColor: "rgba(255, 255, 255, 0.95)",
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 12,
  },
  gridRatingText: {
    fontSize: 12,
    fontWeight: "600",
    color: "#1F2937",
  },
  gridCategoryName: {
    fontSize: 14,
    fontWeight: "600",
    color: "#374151",
  },
});
