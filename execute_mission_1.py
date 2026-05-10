import sys
import os
import time
from dotenv import load_dotenv

# 도구 경로 설정
sys.path.append(os.path.join(os.getcwd(), ".agent", "tools"))

from veo_video_maker import generate_long_take

# 미션 설정
IMAGE_PATH = "pdrn_start.png"
BASE_PROMPT = "A cinematic high-end product commercial for a luxury skin ampoule."
EXTEND_PROMPTS = [
    "A single drop falls in slow motion.",
    "Close-up of radiant skin.",
    "Premium packaging on marble."
]
OUTPUT_FILENAME = "pdrn_viral_video.mp4"

if __name__ == "__main__":
    print("--- 영상 생성을 시작합니다.")
    generate_long_take(IMAGE_PATH, BASE_PROMPT, EXTEND_PROMPTS, OUTPUT_FILENAME)
