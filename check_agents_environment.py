import os
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()

print("=============================================")
print("🤖 에이전트 시스템 환경 점검 스크립트를 시작합니다.")
print("=============================================\n")

def check_api_credentials():
    """1. API 키 및 Secret 파일 존재 여부를 확인합니다."""
    print("--- 1/3 API 자격 증명(Credentials) 검사 ---")
    if os.getenv("GEMINI_API_KEY"):
        print("   - [SUCCESS] Gemini API Key가 .env에 로드되었습니다.")
    else:
        print("   - [FAILURE] GEMINI_API_KEY를 찾을 수 없습니다. .env 파일을 확인해주세요.")

    if os.path.exists("client_secrets.json"):
        print("   - [SUCCESS] YouTube Client Secrets 파일이 존재합니다.")
    else:
        print("   - [FAILURE] client_secrets.json 파일을 찾을 수 없습니다.")
    print("-", "-" * 28, "-")

def check_dependencies():
    """2. 필수 라이브러리 의존성(Dependencies)을 확인합니다."""
    print("--- 2/3 필수 Python 라이브러리 의존성 검사 ---")
    try:
        import google.genai
        import google_auth_oauthlib
        print("   - [SUCCESS] Google GenAI 및 OAuth 라이브러리가 성공적으로 임포트되었습니다.")
    except ImportError as e:
        print(f"   - [FAILURE] 필수 라이브러리 누락 또는 버전 문제: {e}")

def check_local_files():
    """3. 핵심 프로젝트 파일의 존재 유무를 확인합니다."""
    print("--- 3/3 로컬 자산(Asset) 및 설정 파일 검사 ---")
    required_assets = ["pdrn_start.png", "requirements.txt"]
    all_found = True
    for asset in required_assets:
        if os.path.exists(asset):
            print(f"   - [SUCCESS] {asset} 파일이 존재합니다.")
        else:
            print(f"   - [FAILURE] 필수 자산 '{asset}' 파일을 찾을 수 없습니다.")
            all_found = False
    return all_found

if __name__ == "__main__":
    check_api_credentials()
    check_dependencies()
    local_files_ok = check_local_files()
    print("-", "-" * 28, "-")
    if local_files_ok:
        print("\n=== 환경 검사 완료! ===\n모든 파일과 라이브러리는 로컬에서 준비된 상태입니다.")
    else:
        print("\n🚨 경고: 일부 필수 자산이 누락되었습니다. 작업을 진행하기 전에 파일을 확인해주세요.")