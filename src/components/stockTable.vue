<template>
  <v-card>
    <v-card-title>
      <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="stocks"
      :search="search"
      class="elevation-1"
    >
      <template v-slot:[`item.logo`]="{ item }">
        <img :src="item.logo" style="width: 40px; height: 40px; margin: 10px" />
      </template>
    </v-data-table>
  </v-card>
</template>

<script>
import json from "../api/redditData.json";
import axios from "axios";

export default {
  data() {
    return {
      myJson: json,
      symbolsObject: {},
      comments: [],
      search: "",
      headers: [
        { text: "Logo", align: "start", value: "logo" },
        { text: "Symbol", value: "symbol" },
        { text: "Mentions", value: "mentions" },
      ],
      stocks: [],
    };
  },
  async mounted() {
    // Uses api to get all stock symbols, and then aranges them in an object with the symbol initialized to zero.
    await axios
      .get(
        "https://cloud.iexapis.com/stable/ref-data/symbols?token=pk_73b1f12f042b490c930419fee562da53&filter=symbol"
      )
      .then((response) => {
        for (let data2 in response.data) {
          this.symbolsObject[response.data[data2].symbol] = 0;
        }
      });

    // Takes every comment in the myJason object file, splits each comment into words, and pushes it into the comments array.
    for (let comment in this.myJson) {
      this.comments.push(this.myJson[comment][0].Comment.split(" "));
    }

    // Makes a new word array. takes the comments array, and checks if there are douplicate words in the comment. 
    // If there are it gets rid of the dupicate word.
    let wordArr = [];

    for (let words in this.comments) {
      wordArr[words] = [...new Set(this.comments[words])];
    }

    wordArr = wordArr.flat();
    let url = "";

    for (let symbol in this.symbolsObject) {
      if (wordArr.filter((e) => e === symbol.toUpperCase()).length > 0) {
        this.symbolsObject[symbol] = wordArr.filter((e) => e === symbol).length;
      }

      if (this.symbolsObject[symbol] > 5) {
        if (symbol === "ARE") {
          console.log();
        }
        await axios
          .get(
            `https://cloud.iexapis.com/stable/stock/${symbol}/logo?token=pk_73b1f12f042b490c930419fee562da53`
          )
          .then((response) => {
            url = response.data.url;
          });

        this.stocks.push({
          logo: url,
          symbol: symbol,
          mentions: this.symbolsObject[symbol],
        });
      }
    }
  },
};
</script>

<style></style>
