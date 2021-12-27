<template>
  <v-app>
    <v-main>
      <Navbar />
      <v-container>
<StockTable />
<NewStockTable />
      </v-container>
      
    </v-main>
  </v-app>
</template>

<script>
import Navbar from "./components/navbar";
import StockTable from "./components/stockTable";
import NewStockTable from "./components/newStockTable";

export default {
  name: "App",

  components: {
    Navbar,
    StockTable,
    NewStockTable
  },

  data: () => ({
    //
  }),
};
</script>
