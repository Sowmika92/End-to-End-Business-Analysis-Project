# Data dictionary

users
- user_id: string, primary key
- signup_date: timestamp
- country: string
- age_group: string
- gender: string
- acquisition_channel: string

payments
- user_id
- subscription_start: timestamp
- subscription_end: timestamp (nullable)
- plan_type: enum (monthly, annual, trial)
- price: decimal

events
- user_id
- event_time: timestamp
- event_type: string (app_open, workout_start, workout_complete, video_play)
- duration_minutes: numeric
- content_id: string
