import sys
import os
import time
from dotenv import load_dotenv

sys.path.append(os.path.join(os.getcwd(), ".agent", "tools"))

from veo_video_maker import generate_long_take

IMAGE_PATH = "pdrn_start.png"
BASE_PROMPT = "A cinematic high-end product commercial."
EXTEND_PROMPTS = ["A single drop falls.", "Close-up skin."]
OUTPUT_FILENAME = "pdrn_viral_video.mp4"

if __name__ == "__main__":
    generate_long_take(IMAGE_PATH, BASE_PROMPT, EXTEND_PROMPTS, OUTPUT_FILENAME)
