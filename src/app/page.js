"use client";
import Image from "next/image";
import styles from "./page.module.css";
import { Input, Select, Button, useColorMode } from "@chakra-ui/react";
import { useState } from "react";

export default function Home() {
  const [language, setLanguage] = useState("en");
  const [tooltips, setTooltips] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");
  const { colorMode, toggleColorMode } = useColorMode("dark");

  const sendQuery = async (query) => {
    const response = await fetch(
      `http://localhost:5000`,
      { method: "POST" , body: JSON.stringify({language: language, search_query: searchQuery})}

    );
    const data = await response.json();
    console.log(data);
    setTooltips(data);
  };

  return (
    <main className={styles.main}>
      <h1 className={styles.title}>discere</h1>
      <div className={styles.searchContainer}>
        <Select className={styles.selectDropdown}
          defaultValue={"en"}
          onChange={(e) => setLanguage(e.target.value)}
        >
          <option value="en">English</option>
          <option value="cn">Chinese</option>
          {/* <option value="ml">Malay</option>
        <option value="tm">Tamil</option> */}
        </Select>
      </div>

      <div className={styles.searchContainer}>
        <Input
          className={styles.searchbar}
          placeholder="Input your query here"
          onChange={(e) => setSearchQuery(e.target.value)}
        ></Input>
        <Button onClick={()=>sendQuery}>Search</Button>
      </div>
    </main>
  );
}
