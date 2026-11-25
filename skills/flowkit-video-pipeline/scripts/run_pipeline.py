import os
import sys
import json
import time
import argparse
import subprocess
import requests

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

def get_ffmpeg():
    winget_dir = os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\WinGet\Packages")
    for root, dirs, files in os.walk(winget_dir):
        if "ffmpeg.exe" in files:
            return os.path.join(root, "ffmpeg.exe")
    return "ffmpeg"

def get_ffprobe():
    winget_dir = os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\WinGet\Packages")
    for root, dirs, files in os.walk(winget_dir):
        if "ffprobe.exe" in files:
            return os.path.join(root, "ffprobe.exe")
    return "ffprobe"

def get_duration(file_path):
    ffprobe = get_ffprobe()
    cmd = [
        ffprobe, "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", file_path
    ]
    return float(subprocess.check_output(cmd, text=True).strip())

def main():
    parser = argparse.ArgumentParser(description="FlowKit + VieNeu-TTS Automated Video Pipeline")
    parser.add_argument("--config", required=True, help="Path to project config json")
    parser.add_argument("--output-dir", required=True, help="Directory to output video clips and final video")
    parser.add_argument("--flow-url", default="http://127.0.0.1:8100", help="FlowKit backend API URL")
    parser.add_argument("--voice", default="Minh Quân", help="VieNeu-TTS preset voice name")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    clips_dir = os.path.join(args.output_dir, "clips")
    audio_dir = os.path.join(args.output_dir, "audio")
    synced_dir = os.path.join(args.output_dir, "synced")
    os.makedirs(clips_dir, exist_ok=True)
    os.makedirs(audio_dir, exist_ok=True)
    os.makedirs(synced_dir, exist_ok=True)

    with open(args.config, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    # 1. Health check
    try:
        r = requests.get(f"{args.flow_url}/health", timeout=5).json()
        if not r.get("extension_connected"):
            print("ERROR: Extension is not connected to FlowKit backend.")
            sys.exit(1)
    except Exception as e:
        print("ERROR connecting to FlowKit backend:", e)
        sys.exit(1)

    print("=== Bước 1: Khởi tạo Project và Entities ===")
    project_payload = {
        "name": cfg["name"],
        "story": cfg.get("story", ""),
        "material": cfg.get("material", "realistic"),
        "flow_project_id": cfg["flow_project_id"],
        "video_model_family": cfg.get("video_model_family", "omni_flash"),
        "characters": cfg.get("characters", [])
    }
    proj_res = requests.post(f"{args.flow_url}/api/projects", json=project_payload).json()
    project_id = cfg["flow_project_id"]

    # Upload character image references if specified
    if cfg.get("characters"):
        chars = requests.get(f"{args.flow_url}/api/characters?project_id={project_id}").json()
        char_map = {c["name"]: c["id"] for c in chars}
        for c in cfg["characters"]:
            if c.get("reference_image") and os.path.exists(c["reference_image"]):
                print(f"Uploading reference image for {c['name']}...")
                up_res = requests.post(f"{args.flow_url}/api/flow/upload-image", json={
                    "file_path": c["reference_image"],
                    "project_id": project_id,
                    "file_name": os.path.basename(c["reference_image"])
                }).json()
                mid = up_res.get("media_id")
                if mid and c["name"] in char_map:
                    requests.patch(f"{args.flow_url}/api/characters/{char_map[c['name']]}", json={"media_id": mid})
                    print(f"Linked reference media_id {mid} to {c['name']}")

    # 2. Tạo video container và các scenes
    print("=== Bước 2: Tạo Video & Các phân cảnh ===")
    vid_res = requests.post(f"{args.flow_url}/api/videos", json={
        "project_id": project_id,
        "title": cfg["name"],
        "orientation": cfg.get("orientation", "HORIZONTAL"),
        "scene_count": len(cfg["scenes"])
    }).json()
    video_id = vid_res["id"]

    created_scenes = []
    for s in cfg["scenes"]:
        sc_res = requests.post(f"{args.flow_url}/api/scenes", json={
            "video_id": video_id,
            "display_order": s["scene_num"],
            "prompt": s["prompt"],
            "image_prompt": s["prompt"],
            "video_prompt": s.get("video_prompt", s["prompt"]),
            "character_names": s.get("character_names", []),
            "chain_type": "ROOT"
        }).json()
        requests.patch(f"{args.flow_url}/api/scenes/{sc_res['id']}", json={
            "narrator_text": s.get("narrator_text", "")
        })
        created_scenes.append(sc_res)

    # 3. Batch sinh ảnh
    print("=== Bước 3: Batch sinh hình ảnh phân cảnh ===")
    img_requests = [{
        "type": "GENERATE_IMAGE",
        "scene_id": s["id"],
        "project_id": project_id,
        "video_id": video_id,
        "orientation": cfg.get("orientation", "HORIZONTAL")
    } for s in created_scenes if not s.get("custom_video")]
    
    if img_requests:
        requests.post(f"{args.flow_url}/api/requests/batch", json={"requests": img_requests})
        while True:
            st = requests.get(f"{args.flow_url}/api/requests/batch-status?video_id={video_id}&type=GENERATE_IMAGE").json()
            print(f"Ảnh hoàn thành: {st['completed']}/{st['total']}")
            if st["done"]:
                break
            time.sleep(10)

    # 4. Batch sinh video
    print("=== Bước 4: Batch sinh video chuyển động ===")
    vid_requests = [{
        "type": "GENERATE_VIDEO",
        "scene_id": s["id"],
        "project_id": project_id,
        "video_id": video_id,
        "orientation": cfg.get("orientation", "HORIZONTAL")
    } for s in created_scenes if not s.get("custom_video")]

    if vid_requests:
        requests.post(f"{args.flow_url}/api/requests/batch", json={"requests": vid_requests})
        while True:
            st = requests.get(f"{args.flow_url}/api/requests/batch-status?video_id={video_id}&type=GENERATE_VIDEO").json()
            print(f"Video hoàn thành: {st['completed']}/{st['total']}")
            if st["done"]:
                break
            time.sleep(15)

    # 5. Tải video clips về máy
    print("=== Bước 5: Tải clips về máy ===")
    all_scenes = requests.get(f"{args.flow_url}/api/scenes?video_id={video_id}").json()
    scene_clip_files = {}
    for s in all_scenes:
        order = s["display_order"]
        url = s.get("horizontal_video_url") or s.get("vertical_video_url")
        out_clip = os.path.join(clips_dir, f"scene_{order}.mp4")
        if url:
            print(f"Downloading scene {order}...")
            r_clip = requests.get(url, stream=True)
            with open(out_clip, "wb") as f_out:
                for chunk in r_clip.iter_content(chunk_size=8192):
                    f_out.write(chunk)
            scene_clip_files[order] = out_clip

    # Xử lý các scene đặc biệt (interactive web hoặc custom video)
    for s in cfg["scenes"]:
        order = s["scene_num"]
        if s.get("custom_video") and os.path.exists(s["custom_video"]):
            scene_clip_files[order] = s["custom_video"]

    # 6. Sinh giọng VieNeu-TTS & Tự động đồng bộ
    print("=== Bước 6: Sinh giọng VieNeu-TTS & Đồng bộ khớp âm thanh ===")
    from vieneu import Vieneu
    tts = Vieneu("v3nano")
    ffmpeg = get_ffmpeg()
    synced_clips = []

    for s in cfg["scenes"]:
        order = s["scene_num"]
        text = s.get("narrator_text", "")
        input_clip = scene_clip_files.get(order)
        if not input_clip or not os.path.exists(input_clip):
            continue

        audio_path = os.path.join(audio_dir, f"voice_{order}.wav")
        synced_clip = os.path.join(synced_dir, f"synced_{order}.mp4")

        # Infer TTS
        audio_data = tts.infer(text=text, voice=args.voice)
        tts.save(audio_data, audio_path)
        speech_dur = get_duration(audio_path)
        target_dur = max(speech_dur + 0.8, 3.5)

        cmd = [
            ffmpeg, "-y",
            "-i", input_clip,
            "-i", audio_path,
            "-filter_complex",
            f"[0:v]tpad=stop_mode=clone:stop_duration=15,trim=duration={target_dur},setpts=PTS-STARTPTS,fps=24[v];[1:a]apad=pad_dur=0.8[a]",
            "-map", "[v]", "-map", "[a]",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-c:a", "aac", "-b:a", "192k",
            "-t", str(target_dur),
            synced_clip
        ]
        subprocess.run(cmd, check=True)
        synced_clips.append(synced_clip)
        print(f"Đã đồng bộ cảnh {order} ({target_dur:.2f}s)")

    # 7. Ghép video hoàn chỉnh
    print("=== Bước 7: Ghép video hoàn chỉnh ===")
    final_output = os.path.join(args.output_dir, f"{cfg.get('output_filename', 'final_video.mp4')}")
    concat_list = os.path.join(synced_dir, "filelist.txt")
    with open(concat_list, "w", encoding="ascii") as f:
        for c in synced_clips:
            f.write(f"file '{os.path.basename(c)}'\n")

    cmd_concat = [
        ffmpeg, "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_list,
        "-c", "copy",
        final_output
    ]
    subprocess.run(cmd_concat, check=True, cwd=synced_dir)
    print(f"\n✅ XUẤT VIDEO HOÀN CHỈNH THÀNH CÔNG TẠI: {final_output}")

if __name__ == "__main__":
    main()
