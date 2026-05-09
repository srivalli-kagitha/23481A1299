import React from "react";
import notifications from "../data/notifications";
import NotificationCard from "../components/NotificationCard";
import { Container, Typography } from "@mui/material";

const AllNotifications = () => {
  return (
    <Container>
      <Typography variant="h4" sx={{ marginBottom: 3 }}>
        All Notifications
      </Typography>

      {notifications.map((n) => (
        <NotificationCard key={n.id} notification={n} />
      ))}
    </Container>
  );
};

export default AllNotifications;