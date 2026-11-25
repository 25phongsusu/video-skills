---
name: flowkit-video-pipeline
description: "Pipeline tự động tạo video AI chuyên nghiệp kết hợp Google Flow (Veo/Omni Flash qua FlowKit), VieNeu-TTS (giọng đọc tiếng Việt tự nhiên chuẩn xác) và FFmpeg/Playwright (quay màn hình tương tác web và auto-sync audio)."
---

# FlowKit AI Video Pipeline (Google Flow + VieNeu-TTS + Playwright + FFmpeg)

Skill này cung cấp quy trình khép kín tự động hóa việc tạo video tiếp thị, video tổng quan website, giới thiệu sản phẩm và portfolio thương hiệu cá nhân với các công nghệ hàng đầu:
1. **Google Flow (qua FlowKit):** Sinh hình ảnh & video điện ảnh (Omni Flash / Veo 3.1) độ phân giải cao 16:9 hoặc 9:16.
2. **Entity Consistency:** Giữ khuôn mặt nhân vật đồng nhất 100% bằng cách tải ảnh chân dung thật làm reference (`imageInputs`).
3. **VieNeu-TTS:** Tạo giọng đọc tiếng Việt on-device (không cần token trả phí, không lo giới hạn) bằng mô hình `v3nano` (`Minh Quân`, `Ái Hân`, `Hữu Quân`, `Mai Anh`,...).
4. **Interactive Web Recording (Playwright):** Quay trực tiếp thao tác thực tế trên trang web thật (hover, click CTA, lướt dashboard) thay cho ảnh tĩnh.
5. **Auto Audio-Video Synchronization (FFmpeg):** Tự động đo độ dài từng câu thoại và kéo dãn/cắt ngắn video clip tương ứng khớp khít với âm thanh.

---

## 1. Điều kiện tiên quyết (Prerequisites)

* **FFmpeg:** Đã có trong máy (hoặc cài bằng `winget install Gyan.FFmpeg`).
* **Python Libraries:** `pip install fastapi uvicorn websockets pydantic vieneu onnxruntime playwright requests pillow`
* **FlowKit Backend:**
  * Thư mục backend: `c:\Users\phong\Downloads\video port\flowkit`
  * Khởi động server (WebSocket port 9225 để không trùng với CDP trình duyệt):
    ```powershell
    $env:FLOW_PROJECT_ID="<YOUR_FLOW_PROJECT_UUID>"; python -m agent.main
    ```
* **Trình duyệt (Brave / Chrome):**
  * Load unpacked extension tại `flowkit/extension`.
  * Mở 1 tab `https://flow.google.com/project/<YOUR_FLOW_PROJECT_UUID>` luôn hoạt động.

---

## 2. Cấu trúc File Cấu hình Video (`project_config.json`)

Tạo một file JSON định nghĩa dự án của bạn theo cấu trúc mẫu:

```json
{
  "name": "Tên Dự Án Video",
  "flow_project_id": "6a19b5ec-9c7f-47c0-9b56-fc91194bdd14",
  "orientation": "HORIZONTAL",
  "material": "realistic",
  "video_model_family": "omni_flash",
  "output_filename": "video_result.mp4",
  "characters": [
    {
      "name": "TenNhanVat",
      "entity_type": "character",
      "reference_image": "C:\\path\\to\\portrait.png",
      "description": "Mô tả nhân vật chi tiết khớp với ảnh gốc"
    }
  ],
  "scenes": [
    {
      "scene_num": 1,
      "prompt": "Prompt sinh ảnh và video cảnh 1...",
      "video_prompt": "Prompt chuyển động camera cảnh 1...",
      "character_names": [],
      "narrator_text": "Lời thuyết minh tiếng Việt cho cảnh 1 (viết chữ thay vì số và viết từ tiếng Việt để đọc mượt)."
    },
    {
      "scene_num": 2,
      "prompt": "Prompt cảnh 2...",
      "video_prompt": "Prompt camera cảnh 2...",
      "character_names": ["TenNhanVat"],
      "narrator_text": "Lời thuyết minh cảnh 2."
    },
    {
      "scene_num": 3,
      "custom_video": "C:\\path\\to\\interactive_web_clip.mp4",
      "narrator_text": "Lời thuyết minh cảnh cuối tương tác thực tế trên web."
    }
  ]
}
```

---

## 3. Cách chạy Pipeline Tự Động Hóa

Chạy script thực thi toàn bộ pipeline tự động:

```powershell
python "C:\Users\phong\.gemini\config\skills\flowkit-video-pipeline\scripts\run_pipeline.py" --config "path\to\project_config.json" --output-dir "path\to\output_folder" --voice "Minh Quân"
```

### Các bước script tự động thực hiện:
1. Kiểm tra kết nối với FlowKit và Google Flow extension.
2. Upload ảnh chân dung thật lên Flow để lấy `media_id` gán cho nhân vật.
3. Tạo video project và khởi tạo toàn bộ scenes.
4. Gửi yêu cầu sinh ảnh hàng loạt (`GENERATE_IMAGE`).
5. Gửi yêu cầu sinh video hàng loạt (`GENERATE_VIDEO`).
6. Tải các file video clip MP4 về máy.
7. Dùng **VieNeu-TTS** đọc toàn bộ kịch bản thuyết minh tiếng Việt.
8. Đo đạc độ dài từng câu thoại và dùng **FFmpeg** tự động cắt/ghép video clip khớp từng giây nói.
9. Nối (concat) các phân cảnh thành 1 file video hoàn chỉnh sẵn sàng phát hành.
