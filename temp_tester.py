import requests
import json

def ask_ollama(prompt, style, instruction):
    full_prompt = f"{instruction}\n\nComplete this: {prompt}"
    
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3",
            "prompt": full_prompt,
            "stream": False
        }
    )
    
    result = response.json()
    return result["response"]

def run_temperature_test(prompt):
    styles = [
        {
            "style": "CONSERVATIVE (Low Temp)",
            "instruction": "Respond in the most predictable, common, and safe way possible. No creativity."
        },
        {
            "style": "BALANCED (Medium Temp)",
            "instruction": "Respond naturally and clearly."
        },
        {
            "style": "CREATIVE (High Temp)",
            "instruction": "Respond in the most unexpected, creative, surprising way possible. Avoid obvious answers."
        }
    ]
    
    print("\n" + "="*50)
    print(f"PROMPT: {prompt}")
    print("="*50)
    
    results = []
    
    for s in styles:
        print(f"\n[{s['style']}]")
        print("Thinking...")
        response = ask_ollama(prompt, s["style"], s["instruction"])
        print(response)
        results.append(f"[{s['style']}]\n{response}\n")
    
    return results

def save_results(prompt, results):
    filename = "temperature_results.txt"
    
    with open(filename, "w") as f:
        f.write(f"TEMPERATURE TESTER RESULTS\n")
        f.write(f"PROMPT: {prompt}\n")
        f.write("="*50 + "\n\n")
        for r in results:
            f.write(r + "\n")
    
    print(f"\n✓ Results saved to {filename}")

# Main
prompt = input("\nEnter your prompt: ")
results = run_temperature_test(prompt)
save_results(prompt, results)