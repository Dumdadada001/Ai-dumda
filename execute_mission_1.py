import sys
import os
import time
from dotenv import load_dotenv

# Set tool path
sys.path.append(os.path.join(os.getcwd(), ".agent", "tools"))

from veo_video_maker import generate_long_take

# Mission Settings
IMAGE_PATH = "pdrn_start.png"
BASE_PROMPT = "A cinematic high-end product commercial for a luxury skin ampoule."
EXTEND_PROMPTS = [
    "A single drop falls in slow motion.",
    "Close-up of radiant skin.",
    "Premium packaging on marble."
]
OUTPUT_FILENAME = "pdrn_viral_video.mp4"

if __name__ == "__main__":
    print("--- Starting Video Generation ---")
    generate_long_take(IMAGE_PATH, BASE_PROMPT, EXTEND_PROMPTS, OUTPUT_FILENAME)
