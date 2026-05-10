import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def test_imagen():
    print("Imagen 4.0 이미지 생성을 테스트합니다...")
    try:
        # Imagen 4.0 모델을 사용하여 이미지 생성 시도
        response = client.models.generate_images(
            model='imagen-3.0-generate-001', # 일단 3.0으로 시도 (안전빵)
            prompt='A high-end luxury skincare bottle on a marble pedestal, cinematic lighting.',
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio='16:9'
            )
        )
        for i, img in enumerate(response.generated_images):
            with open(f"test_image_{i}.png", "wb") as f:
                f.write(img.image_bytes)
        print("✅ 이미지 생성 및 저장 성공!")
    except Exception as e:
        print(f"❌ 오류 발생: {e}")

if __name__ == "__main__":
    test_imagen()
