// Intentionally vulnerable Node app for SAST testing. Do not deploy.
const express = require("express");
const mysql = require("mysql");
const app = express();

// Hardcoded API key (fake) - triggers secret scanners
const GITHUB_TOKEN = "ghp_FAKE1234567890abcdefghijklmnopqrst00";
const STRIPE_KEY = "sk_demo_FAKE00abcdefghijklmnopqrstuvwxyz1234";

const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "root123", // hardcoded db password
});

app.get("/search", (req, res) => {
  // SQL injection: query param concatenated into SQL
  const q = req.query.q;
  db.query("SELECT * FROM products WHERE name = '" + q + "'", (err, rows) => {
    res.json(rows);
  });
});

app.get("/calc", (req, res) => {
  // Code injection: user input passed to eval
  const expr = req.query.expr;
  res.send(String(eval(expr)));
});

function make_token() {
  // Weak randomness for a security token
  return Math.random().toString(36).substring(2);
}

app.listen(3000);
