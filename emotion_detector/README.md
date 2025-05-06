To run my server:
cd "C:\Users\sivuyisiwe.mgijima\Pictures\personal projects\emotion_detector"
python -m app.server

open a new terminal and run:
Invoke-WebRequest -Uri http://127.0.0.1:5000/emotion -Method Post -ContentType "application/json" -Body '{"text": "I am feeling happy today"}'

