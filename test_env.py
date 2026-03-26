from env import EmailEnv

env = EmailEnv()

# reset environment
state = env.reset()
print("Initial State:")
print(state)

# try an action
action = "reply"
next_state, reward, done = env.step(action)

print("\nAfter Action:")
print("Action taken:", action)
print("Reward:", reward)
print("Done:", done)