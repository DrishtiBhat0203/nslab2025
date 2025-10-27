import hashlib
import time
import random

SHARED_KEY = "mysecret123"

def server_generate_challenge():
    challenge = str(random.randint(10000, 99999))
    issued_time = int(time.time())
    return challenge, issued_time
  
def client_generate_response(challenge, secret):
    text = challenge + secret
    return hashlib.sha256(text.encode()).hexdigest()

reused_challenges = set()

def server_verify(challenge, response, challenge_time):
    if challenge in reused_challenges:
        return f"Replay Attack Detected!\n(Challenge issued at {challenge_time})"
    expected = client_generate_response(challenge, SHARED_KEY)
    if response == expected:
        reused_challenges.add(challenge)
        return f"Authentication Successful (Challenge issued at {challenge_time})"
    return "Authentication Failed"

challenge, timestamp = server_generate_challenge()
print(f"\nServer Challenge: {challenge} (Issued at: {time.ctime(timestamp)} 2025)")

user_key = input("Enter your secret key: ")

client_response = client_generate_response(challenge, user_key)
print("Client Response:", client_response)

print("Server Verification:", server_verify(challenge, client_response, timestamp))

print("\n--- Replay Attack Simulation ---")
time.sleep(3)
print(f"Replay Attempt at {time.ctime()} 2025 -> {server_verify(challenge, client_response, timestamp)}")
