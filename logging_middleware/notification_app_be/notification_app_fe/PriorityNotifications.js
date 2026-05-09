import React, { useState } from "react";
import notifications from "../data/notifications";
import NotificationCard from "../components/NotificationCard";
import {
  Container,
  Typography,
  Select,
  MenuItem,
} from "@mui/material";

const PriorityNotifications = () => {
  const [type, setType] = useState("All");

  const filtered = notifications
    .filter((n) => n.priority === 1)
    .filter((n) => (type === "All" ? true : n.type === type));

  return (
    <Container>
      <Typography variant="h4" sx={{ marginBottom: 3 }}>
        Priority Notifications
      </Typography>

      <Select
        value={type}
        onChange={(e) => setType(e.target.value)}
        sx={{ marginBottom: 3 }}
      >
        <MenuItem value="All">All</MenuItem>
        <MenuItem value="Academic">Academic</MenuItem>
        <MenuItem value="Placement">Placement</MenuItem>
        <MenuItem value="General">General</MenuItem>
        <MenuItem value="Event">Event</MenuItem>
      </Select>

      {filtered.map((n) => (
        <NotificationCard key={n.id} notification={n} />
      ))}
    </Container>
  );
};

export default PriorityNotifications;