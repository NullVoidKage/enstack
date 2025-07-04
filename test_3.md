Hypothetically, we are building an app that collects accelerometer data from thin clients (sensors with limited processing capacity)

A. Assuming that the device is sending continuously at 16000Hz for the X,Y, and Z acceleration measurements, what would your strategy be in handling and processing the data? How would you design the server infrastructure? Please enumerate the steps, software, algorithms, and services that you would use to ensure that the servers can handle the incoming data from our users. Diagrams can be really helpful for this.

B. If the sensors were upgraded to modern mobile devices, how would you change your architecture from A?


Problem: Each sensor sends 48,000 numbers per second (16k samples × 3 axes). That's a lot.
Thin Client Approach
Step 1: Don't send everything immediately

Buffer 100-200 samples on the device first
Send in chunks every few milliseconds
Use UDP if you can lose some packets, TCP if you can't

Step 2: Server setup

Put a message queue in front (RabbitMQ or Kafka)
Use multiple worker processes to handle incoming data
Store in a time-series database like InfluxDB

Step 3: Processing
def handle_sensor_data(device_id, samples):
    if len(samples) > expected_size:
        return "too much data"
    
    database.insert(device_id, samples, timestamp)
    
    if max(samples) > threshold:
        send_alert(device_id)
Infrastructure you'll need:

Load balancer
Several app servers
Message queue
Time-series database
Monitoring system

Mobile Device Approach
Big difference: Phones are smart, so use that.
What changes:

Let the phone calculate averages, detect movement patterns
Only send summaries or when something interesting happens
Use regular HTTP REST calls instead of streaming
Store in regular PostgreSQL

Much simpler setup:
Phone does the work → sends summary → your API → database
The mobile version is way easier because you're not drowning in raw data anymore.