# hello_world.al - Simple AgentLang demo

# Load any text - it becomes a semantic object
text = load_file("README.md")

# Extract properties using LLM
title = text.title
summary = text.summary

# Print results
print("=== Hello from AgentLang! ===")
print(f"Document title: {title}")
print(f"Summary: {summary}")