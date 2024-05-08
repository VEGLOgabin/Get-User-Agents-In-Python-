# pip install fake-useragent

from fake_useragent import UserAgent

# Instantiate the UserAgent object
ua = UserAgent()

# Get a random user agent
random_user_agent = ua.random

# Get a list of all user agents
all_user_agents = ua.data_browsers

print("Random User Agent:", random_user_agent)
print("\nAll User Agents:", all_user_agents)
