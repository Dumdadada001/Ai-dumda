import sys
import os
import time
from dotenv import load_dotenv

# .agent/tools 경로를 시스템 경로에 추가하여 모듈 임포트 가능하게 설정
sys.path.append(os.path.join(os.getcwd(), ".agent", "tools"))

from veo_video_maker import generate_long_take

# 미션 1: PDRN 리프팅 앰플 영상 생성 설정
IMAGE_PATH = "pdrn_start.png"
BASE_PROMPT = (
    "A cinematic high-end product commercial for a luxury skin ampoule. "
    "The camera slowly pans around the golden glass bottle labeled 'PDRN CORE'. "
    "Elegant laboratory lighting, soft focus background, high-tech vibes."
)
EXTEND_PROMPTS = [
    "A single drop of thick, viscous golden liquid falls from the glass dropper in slow motion, hitting a pool of serum.",
    "Extreme close-up of the serum spreading smoothly across a person's glowing, radiant skin.",
    "The camera pulls back to show the premium packaging of 'PDRN CORE' sitting on a marble surface, with a final cinematic gleam."
]
OUTPUT_FILENAME = "pdrn_viral_video.mp4"

if __name__ == "__main__":
    print("--- 영식이가 미션 1: PDRN 바이럴 영상 생성을 시작합니다.")
    generate_long_take(IMAGE_PATH, BASE_PROMPT, EXTEND_PROMPTS, OUTPUT_FILENAME)
    print(f"\n--- 영상 생성 완료! 결과물: {OUTPUT_FILENAME}")
