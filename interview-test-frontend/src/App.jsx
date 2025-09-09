// src/App.jsx
import React from "react";

export default function App() {
  // Candidate receives this "const" object and will later replace it with fetched data
  const user = {
    id: 0,
    name: "Placeholder User",
    role: "N/A",
    skills: ["None"],
    experience: 0
  };

  return (
    <div style={{ display: "flex", justifyContent: "center", marginTop: 40 }}>
      <div style={{
        border: "1px solid #ccc",
        borderRadius: 10,
        padding: 20,
        width: 320,
        boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
      }}>
        <h2>{user.name}</h2>
        <p><strong>Role:</strong> {user.role}</p>
        <p><strong>Experience:</strong> {user.experience} years</p>
        <p><strong>Skills:</strong> {user.skills.join(", ")}</p>
      </div>
    </div>
  );
}
