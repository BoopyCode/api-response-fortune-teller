#!/usr/bin/env python3
"""
API Response Fortune Teller - Because APIs are the modern crystal ball.
Predicts what your API will return before it inevitably disappoints you.
"""

import json
import random
from datetime import datetime

class APIFortuneTeller:
    """
    Reads the mystical tea leaves of API responses.
    More accurate than your API documentation (probably).
    """
    
    def __init__(self):
        self.fortunes = [
            "The API returns 200 but the data is null. Classic.",
            "Unexpected field 'foo' appears! It will vanish in next version.",
            "Rate limit exceeded. Please wait 5... 4... 3... just kidding, 429 forever.",
            "Authentication works on Postman but not in code. It's a you problem.",
            "The response schema changed. Documentation? We don't do that here.",
            "Everything works! (This fortune appears 0.1% of the time)",
            "CORS error from the API gateway. The frontend devs are crying.",
            "Pagination works until page 3, then returns cats. Just cats.",
            "The 'status' field contains Shakespeare quotes. For reasons.",
            "Deprecated endpoint still works but mocks you in response headers."
        ]
    
    def analyze_response(self, response_text):
        """
        Performs deep mystical analysis on API response.
        Accuracy: ±100% (which is statistically impressive).
        """
        try:
            data = json.loads(response_text)
            complexity = len(str(data))
            
            # Deep analysis algorithm (patent pending)
            if isinstance(data, dict) and 'error' in data:
                fortune = "API admits error! This is progress."
            elif complexity > 1000:
                fortune = "Response so large, parsing will timeout. Good luck!"
            elif not data:
                fortune = "Empty response. Either genius or laziness."
            else:
                fortune = random.choice(self.fortunes)
                
            return {
                "fortune": fortune,
                "confidence": random.randint(42, 99),  # Never 100%, that's hubris
                "timestamp": datetime.now().isoformat(),
                "recommendation": self._get_recommendation()
            }
            
        except json.JSONDecodeError:
            return {
                "fortune": "Not JSON. Is this even an API or just a sad text file?",
                "confidence": 95,
                "timestamp": datetime.now().isoformat(),
                "recommendation": "Check if API is actually returning HTML error page"
            }
    
    def _get_recommendation(self):
        """Returns sage advice. Mostly involves caffeine."""
        recommendations = [
            "Add more try-catch blocks. All the blocks.",
            "Blame the backend team, then apologize tomorrow.",
            "Implement exponential backoff and hope.",
            "Check Stack Overflow for someone with same problem (2018).",
            "Write a strongly worded comment in the code."
        ]
        return random.choice(recommendations)


def main():
    """Main function - because every script needs one."""
    teller = APIFortuneTeller()
    
    print("🔮 API Fortune Teller 🔮")
    print("Paste your API response (JSON or otherwise). Press Ctrl+D when done:\n")
    
    try:
        lines = []
        while True:
            lines.append(input())
    except EOFError:
        response_text = '\n'.join(lines)
    
    if not response_text.strip():
        response_text = '{"error": "User too lazy to paste response"}'
    
    result = teller.analyze_response(response_text)
    
    print("\n=== YOUR API FORTUNE ===")
    print(f"🔮 {result['fortune']}")
    print(f"📊 Confidence: {result['confidence']}%")
    print(f"💡 Recommendation: {result['recommendation']}")
    print(f"⏰ Timestamp: {result['timestamp']}")

if __name__ == "__main__":
    main()
