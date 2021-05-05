<template>
  <v-app>
    <v-main>
      <Navbar />
      <v-container>
<StockTable />
      </v-container>
      
    </v-main>
  </v-app>
</template>

<script>
import Navbar from "./components/navbar";
import StockTable from "./components/stockTable";

export default {
  name: "App",

  components: {
    Navbar,
    StockTable
  },

  data: () => ({
    //
  }),
};
</script>
