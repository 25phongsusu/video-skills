# video-skills

Bộ sưu tập các **AI Agent Skills** phục vụ sản xuất và dựng video tự động (Remotion, AI Avatar, FlowKit, VieNeu-TTS / Edge-TTS).

## Danh sách Skills

| Skill | Mô tả |
|---|---|
| `ai-avatar-video` | Quy trình sản xuất video ngắn TikTok/Reels/Shorts phong cách AI Avatar (Talking Head / 2D Vector Presenter) kết hợp Remotion, VieNeu-TTS / Audio Sync, phụ đề SRT và Motion Graphic. |
| `flowkit-video-pipeline` | Pipeline tự động tạo video AI kết hợp Google Flow (Veo/Omni Flash qua FlowKit), VieNeu-TTS và FFmpeg/Playwright. |
| `modern-talking-head-editor` | Dựng video talking-head dọc bằng Remotion theo phong cách hiện đại (Montserrat, kinetic phrases, outline overlays, masked behind-subject text, SFX). |
| `remotion-cuongit-video` | Tạo video ngắn 9:16 tự động bằng Remotion + Edge TTS theo 2 chế độ: Chia sẻ kiến thức (Tech Explainer) và Tiếp thị / Bán hàng. |

> Xem thêm skill dựng hoạt hình 2D vẽ bằng code: **[boldline-explainer](https://github.com/25phongsusu/boldline-explainer)**

## Cài đặt nhanh

Clone repo và link skill bạn muốn dùng vào thư mục skills của agent:

```powershell
git clone https://github.com/25phongsusu/video-skills
cd video-skills

# Antigravity (Windows) - ví dụ link cả 4 skill
foreach ($s in @("ai-avatar-video","flowkit-video-pipeline","modern-talking-head-editor","remotion-cuongit-video")) {
    New-Item -ItemType Junction -Path "$env:USERPROFILE\.gemini\config\skills\$s" -Target "$PWD\skills\$s"
}
```
