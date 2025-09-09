const http = require("http");
const { handleBooksRoute } = require("./routes/book.routes");
const { authMiddleware } = require("./middleware/auth.middleware");

const PORT = process.env.PORT || 4000;

const server = http.createServer(async (req, res) => {
  // ---- /books GET ----
  if (req.url === "/books" && req.method === "GET") {
    // TODO-2: Use JWT middleware
    const user = authMiddleware(req); // Candidate should implement authMiddleware logic
    if (!user) {
      res.writeHead(401, { "Content-Type": "application/json" });
      return res.end(JSON.stringify({ error: "Unauthorized" }));
    }

    return handleBooksRoute(req, res); // TODO-1: Return actual book list
  }

  // ---- 404 ----
  res.writeHead(404, { "Content-Type": "application/json" });
  res.end(JSON.stringify({ error: "Route not found" }));
});

server.listen(PORT, () => console.log(`Server running at http://localhost:${PORT}`));
