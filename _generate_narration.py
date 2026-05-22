"""
20개 슬라이드 핵심 키워드 내레이션 생성.
Gemini TTS (Kore 음성, ko-KR) → WAV → ffmpeg로 MP3 변환.
"""
import os
import subprocess
import sys
import time
import wave
from pathlib import Path

from google import genai
from google.genai import types

THROTTLE_SECONDS = 7  # 10 req/min limit, leave headroom

NARRATIONS = {
    1: "포용적인 학습자료. 설계 단계부터.",
    2: "19세기 교실, 20세기 교사, 21세기 학생.",
    3: "자기 주도와 산만함. 두 얼굴의 양면성.",
    4: "포용성과 몰입감. 학습자료가 갖춰야 할 두 축.",
    5: "콘텐츠 기획자, 그리고 환경 설계자. 교사의 두 역할.",
    6: "키보드 대신 말로. 자연어 한 문장으로. 결정적 변화.",
    7: "오늘의 질문. 우리가 만드는 학습자료는 포용적인가.",
    8: "유 디 엘. 표상, 행동과 표현, 참여. 세 가지 원칙.",
    9: "여러 감각, 여러 진입로. 멀티모달 설계.",
    10: "첫 프롬프트에 단 한 줄. 설계 단계부터 접근성 내장.",
    11: "사례 하나. 워드 봄. 영영풀이를 박진감으로. 공강 30분에 완성.",
    12: "래프 해프닝. 에이아이의 실수가 만든 즐거운 교실.",
    13: "사례 둘. 스토리 디텍티브. 교과서 본문을 추리 서사로.",
    14: "사례 셋. 그래머 포션 랩. 문법을 마법의 물약으로.",
    15: "교훈. 교육 데이터의 엄밀함은 아직 사람의 몫.",
    16: "사례 넷. 픽 미. 한 줄 프롬프트로 화려함과 접근성을 동시에.",
    17: "학생 평가 하나. 만족도, 집중도, 학습 도움. 신명중 1학년 130명.",
    18: "학생 평가 둘. 줄였으면 0명. 활용 희망 94.6 퍼센트. 재미가 1위.",
    19: "학생의 자유 의견. 마물 맑은물. 오기가 생긴다.",
    20: "학습용 앱 개발의 핵심 가치. 접근성과 포용성은 선택이 아닌 필수 조건.",
}

VOICE = "Kore"
MODEL = "gemini-3.1-flash-tts-preview"


def gemini_tts_to_wav(client, text, wav_path):
    response = client.models.generate_content(
        model=MODEL,
        contents=text,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name=VOICE
                    )
                ),
                language_code="ko-KR",
            ),
        ),
    )
    pcm = response.candidates[0].content.parts[0].inline_data.data
    with wave.open(str(wav_path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(pcm)


def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        sys.exit("GEMINI_API_KEY env var not set")

    client = genai.Client(api_key=api_key)
    out_dir = Path("narration")
    out_dir.mkdir(exist_ok=True)

    for slide_num, text in NARRATIONS.items():
        name = f"slide-{slide_num:02d}"
        wav_path = out_dir / f"{name}.wav"
        mp3_path = out_dir / f"{name}.mp3"

        if mp3_path.exists():
            print(f"[{slide_num:02d}] skip (exists)")
            continue

        print(f"[{slide_num:02d}] generating: {text}")
        gemini_tts_to_wav(client, text, wav_path)
        time.sleep(THROTTLE_SECONDS)

        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-i",
                str(wav_path),
                "-codec:a",
                "libmp3lame",
                "-b:a",
                "96k",
                "-ar",
                "24000",
                str(mp3_path),
            ],
            check=True,
            capture_output=True,
        )
        wav_path.unlink()

    print("Done.")


if __name__ == "__main__":
    main()
