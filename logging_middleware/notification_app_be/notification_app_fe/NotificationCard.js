import React from "react";
import { Card, CardContent, Typography, Chip } from "@mui/material";

const NotificationCard = ({ notification }) => {
  return (
    <Card sx={{ marginBottom: 2 }}>
      <CardContent>
        <Typography variant="h6">
          {notification.title}
        </Typography>

        <Chip
          label={notification.type}
          sx={{ marginRight: 1 }}
        />

        <Chip
          label={notification.viewed ? "Viewed" : "New"}
          color={notification.viewed ? "default" : "primary"}
        />
      </CardContent>
    </Card>
  );
};

export default NotificationCard;