-- TODO: implament the cron job to send the reminders

CREATE TABLE users(
    phone VARCHAR(20) PRIMARY KEY
);

CREATE TABLE scheduled_messages(
  phone VARCHAR(20),
  scheduled_at DATETIME,
  content TEXT,
  FOREIGN KEY (phone) REFERENCES users(phone)
);
