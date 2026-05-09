# Campus-Notification-Priority-Inbox

## Project Description

The Campus Notification Priority Inbox is a Python-based application developed to organize and prioritize campus notifications efficiently.
Students usually receive many updates related to placements, results, and events. This project ensures that the most important notifications appear first based on priority and time.

The system fetches notifications from an API, assigns priority scores, and displays the **Top 10 most relevant notifications**.

---

## Objectives

* Fetch notifications from a notification service API
* Classify notifications based on importance
* Rank notifications using priority logic
* Display only high-priority notifications to users

---

## Features

* API-based notification fetching
* Priority scoring using notification type and timestamp
* Efficient Top-N selection using Min Heap
* Handles API errors gracefully using sample data
* Simple command-line output

---

## Priority Logic

Notifications are ranked using:

**1. Notification Type**

* Placement → Highest priority
* Result → Medium priority
* Event → Normal priority

**2. Recency**

* Recent notifications receive higher preference.

Final priority is calculated by combining type weight and timestamp.

---

## Project Structure

```
23481A1299/
└── logging_middleware/
    ├── notification_app_be/
    ├── priority_inbox.py
    ├── notification_system_design.md
    ├── README.md
    └── requirements.txt
```

---

## Technologies Used

* Python 3
* Requests Library
* Heap Queue (heapq)
* REST API

---

## Setup Instructions

### Clone Repository

```
git clone <repository-link>
cd 23481A1299/logging_middleware
```

### Install Dependencies

```
pip install -r requirements.txt
```

### Run Application

```
python priority_inbox.py
```

---

## Sample Output

```
===== PRIORITY INBOX (TOP 10) =====

1. [Placement] Google Hiring Drive
2. [Result] Mid-Sem Results Published
3. [Event] Hackathon Registration Open
```

---

## Design Approach

The system calculates a priority score for each notification and maintains only the Top 10 notifications using a Min Heap data structure.
This improves performance and avoids sorting large datasets entirely.

---
