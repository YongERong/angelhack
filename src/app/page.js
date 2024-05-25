"use client";
import Image from "next/image";
import styles from "./page.module.css";
import { Input, Select, Button, useColorMode } from "@chakra-ui/react";
import { useState } from "react";
import ReactPlayer from "react-player";
import axios from "axios";

export default function Home() {
  const [language, setLanguage] = useState("en");
  const [tooltips, setTooltips] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");
  const { colorMode, toggleColorMode } = useColorMode("dark");
  const [loading, setIsLoading] = useState(false);
  const [src, setSrc] = useState("");

  const sendQuery = async () => {
    console.log("sending query");
    setIsLoading(true);
    await axios.get(`http://127.0.0.1:5000?language=${language}&search_query=${searchQuery}`,{responseType: "blob"})
      .then((res) => {
        console.log("no u");
        console.log(res.data);
        setSrc(URL.createObjectURL(res.data));
        setIsLoading(false);
      })
      .catch((error) => {
        console.log("axios error:", error);
        setIsLoading(false);
      });
    
  };

  return (
    <main className={styles.main}>
      <Image src="/icon.png" width={10} height={10}/>
      <h1 className={styles.title}>To the Moon?</h1>
      <div className={styles.searchContainer}>
        <Select
          className={styles.selectDropdown}
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
          isLoading={loading}
          className={styles.searchbar}
          placeholder="Input your query here"
          onChange={(e) => setSearchQuery(e.target.value)}
        ></Input>
        <Button isLoading={loading} onClick={sendQuery}>Search</Button>
      </div>
      {!!src && <audio id="audio" controls src={src} />}
    </main>
  );
}
