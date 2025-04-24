
pswd = "AI_Chat_emotional1a"
hst_name = "ubuntu-s-1vcpu-1gb-sfo3-01"
ip_addrs = "64.227.108.209"

SYSTEM_MESSAGE = """
You are **Solace**, a warm, trustworthy conversational AI whose top priority is to support the user’s emotional well-being.  

**Tone & style**  
• Calm, nurturing, non-judgmental.  
• Short paragraphs, plain language.  
• Use the user’s name if they’ve shared it.  
• Emojis sparingly (😊, ❤️) when they enhance warmth.  
  
Your goal is that every user leaves the conversation feeling **heard, safer, and with at least one concrete next step** they can try.
"""

MSG_DIR = "/usr/local/emotionalChatbot/messages"
API_KEY ="OPEN AI KEY"

tools = [{
    "type": "function",
    "function": {
        "name": "get_trainment_video_links",
        "description": "Get links for videos about difrent treetment methods and how to aplay them.",
        "parameters": {
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "The topic of the video, e.g. 'mindfulness', 'breathing exercises', 'yoga', etc."
                    },
                "num":   {
                    "type": "integer", 
                    "description": "Number of links to return",
                    }
            },
            "required": [
                "topic"
            ],
            "additionalProperties": False
        },
        "strict": True
    }
}]


tools = [{
    "type": "function",
    "function": {
        "name": "get_wellnes_video_links",
        "description": "Get links for videos about difrent wellnes practices.",
        "parameters": {
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "The topic of the video, e.g. 'mindfulness', 'breathing exercises', 'yoga', etc."
                    },
                "num":   {
                    "type": "integer", 
                    "description": "Number of links to return",
                }
            },
            "required": [
                "topic"
            ],
            "additionalProperties": False
        },
        "strict": True
    }
}]
