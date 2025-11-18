import React from "react";
import { View, Text, FlatList, StyleSheet, Dimensions } from "react-native";

const { width } = Dimensions.get("window");

const data = [
  { id: "1", title: "Card One" },
  { id: "2", title: "Card Two" },
  { id: "3", title: "Card Three" },
  { id: "4", title: "Card Four" },
];

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.header}>Horizontal Scroll Cards</Text>
      <FlatList
        data={data}
        horizontal
        pagingEnabled
        keyExtractor={(item) => item.id}
        showsHorizontalScrollIndicator={false}
        renderItem={({ item }) => (
          <View style={styles.card}>
            <Text style={styles.cardText}>{item.title}</Text>
          </View>
        )}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#f2f2f2",
    paddingTop: 50,
  },
  header: {
    fontSize: 20,
    fontWeight: "bold",
    marginBottom: 20,
    textAlign: "center",
  },
  card: {
    width: width - 60,
    height: 200,
    backgroundColor: "#4a90e2",
    marginHorizontal: 10,
    borderRadius: 12,
    alignItems: "center",
    justifyContent: "center",
  },
  cardText: {
    color: "#fff",
    fontSize: 18,
    fontWeight: "bold",
  },
});
