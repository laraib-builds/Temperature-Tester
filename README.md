## Week 1 Day 5 — Temperature Tester

A Python tool that simulates how temperature affects LLM output 
by running the same prompt three times with different instructions 
(conservative, balanced, creative) using a local Ollama model.

## Setup
1. Install Ollama from ollama.com
2. Run: ollama pull phi3
3. Run: python temp_tester.py

## What I Learned
Temperature controls how the model samples from its probability 
distribution. Low temperature picks the highest probability token 
(predictable). High temperature flattens the distribution, giving 
unlikely tokens a chance (creative but less reliable).
