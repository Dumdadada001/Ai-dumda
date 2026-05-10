1 import sys
2 import os
3 import time
4 from dotenv import load_dotenv
5
6 sys.path.append(os.path.join(os.getcwd(), ".agent", "tools"))
7
8 from veo_video_maker import generate_long_take
9
10 IMAGE_PATH = "pdrn_start.png"
11 BASE_PROMPT = "A cinematic high-end product commercial."
12 EXTEND_PROMPTS = ["A single drop falls.", "Close-up skin."]
13 OUTPUT_FILENAME = "pdrn_viral_video.mp4"
14
15 if __name__ == "__main__":
16     generate_long_take(IMAGE_PATH, BASE_PROMPT, EXTEND_PROMPTS, OUTPUT_FILENAME)
