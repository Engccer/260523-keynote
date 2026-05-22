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
    1: "우리가 만드는 학습자료는 포용적인가",
    2: "지금 우리의 교실은?",
    3: "21세기 학생의 특성",
    4: "포용성과 몰입감",
    5: "교사의 두 역할",
    6: "수업 도구 확장. 학습지가 학습 앱으로",
    7: "우리가 만드는 학습자료는 포용적인가?",
    8: "유 디 엘 3대 원칙",
    9: "다중 감각, 다중 접근",
    10: "설계 단계부터 접근성을 내장하라",
    11: "워드 봄. 영영풀이를 박진감 넘치는 게임으로",
    12: "래프 해프닝. 에이아이의 어처구니없는 실수",
    13: "스토리 디텍티브. 교과서 본문을 추리 서사로",
    14: "그래머 포션 랩. 문법을 마법의 물약으로",
    15: "에이아이의 한계. 최종 검수는 아직 사람의 몫",
    16: "픽 미. 소소한 학생 추첨 도구",
    17: "학생들의 미니게임 앱 만족도",
    18: "학생들이 뽑은 강점",
    19: "학생들의 평가 한마디",
    20: "학습용 앱 개발의 핵심 가치",
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
