import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 허용할 API 스코프 지정 (YouTube 동영상 업로드 및 관리 권한)
SCOPES = ["https://www.googleapis.com/auth/youtube.upload", "https://www.googleapis.com/auth/youtube.readonly"]

def get_authenticated_service():
    """
    OAuth 2.0을 통해 인증을 수행하고 YouTube API 서비스 객체를 반환합니다.
    token.json이 있으면 재사용하고, 없거나 만료되었으면 새로 인증을 진행합니다.
    """
    creds = None
    # token.json 파일은 사용자 액세스 및 새로고침 토큰을 저장합니다.
    # 최초 로그인 완료 시 자동으로 생성됩니다.
    token_file = "token.json"
    
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
        
    # 유효한 자격 증명이 없는 경우 사용자 로그인 진행
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # client_secrets.json 파일 경로를 환경변수 또는 기본값에서 가져옵니다.
            client_secrets_file = os.getenv("YOUTUBE_CLIENT_SECRETS_FILE", "client_secrets.json")
            if not os.path.exists(client_secrets_file):
                raise FileNotFoundError(f"{client_secrets_file} 파일이 없습니다. Google Cloud Console에서 다운로드하여 작업 디렉토리에 넣어주세요.")
            
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                client_secrets_file, SCOPES
            )
            # 로컬 서버를 띄워 브라우저를 통한 인증을 진행합니다.
            creds = flow.run_local_server(port=0)
            
        # 인증 성공 후 토큰을 파일로 저장하여 다음 실행 시 재사용합니다.
        with open(token_file, "w") as token:
            token.write(creds.to_json())

    # YouTube API 서비스 객체 생성 및 반환
    return googleapiclient.discovery.build("youtube", "v3", credentials=creds)

def test_connection():
    """
    유튜브 채널 정보 조회를 통해 인증 상태를 테스트합니다.
    """
    print("유튜브 API 인증을 시작합니다...")
    try:
        youtube = get_authenticated_service()
        
        # 내 채널 정보 조회
        request = youtube.channels().list(
            part="snippet,contentDetails,statistics",
            mine=True
        )
        response = request.execute()
        
        if response.get("items"):
            channel = response["items"][0]
            print("\n[SUCCESS] 유튜브 API 연결 성공!")
            print(f"- 채널명: {channel['snippet']['title']}")
            print(f"- 채널 ID: {channel['id']}")
            print(f"- 구독자 수: {channel['statistics']['subscriberCount']}명")
        else:
            print("\n[ERROR] 채널 정보를 찾을 수 없습니다. (채널이 존재하지 않을 수 있습니다.)")
            
    except Exception as e:
        print(f"\n[ERROR] 인증 또는 API 호출 중 오류가 발생했습니다: {e}")

def upload_video(file_path, title, description, tags, category_id="22", privacy_status="private"):
    """
    비디오를 유튜브에 업로드하는 함수 뼈대입니다.
    """
    # TODO: 추후 구현할 영상 업로드 로직
    pass

if __name__ == "__main__":
    # 단독 실행 시 연결 테스트를 수행합니다.
    test_connection()
