const express = require("express");
const SneaksAPI = require("sneaks-api");

const sneaks = new SneaksAPI();
const app = express();
const PORT = process.env.PORT || 5001;

app.use(express.json());
app.use(require("cors")()); // Allow CORS for Django requests

// Fetch popular sneakers from StockX
app.get("/stockx/popular", (req, res) => {
  sneaks.getMostPopular(10, (err, products) => {
    if (err) return res.status(500).json({ error: err.message });
    res.json(products);
  });
});

// Start Node.js microservice
app.listen(PORT, () => console.log(`StockX service running on port ${PORT}`));
