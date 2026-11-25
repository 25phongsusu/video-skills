---
name: remotion-cuongit-video
description: "Tạo video ngắn 9:16 (TikTok, Reels, Shorts) tự động bằng Remotion + Edge TTS dựa trên template Cường IT. Hỗ trợ 2 chế độ: Video Chia sẻ kiến thức (Tech Explainer) và Video Tiếp thị / Bán hàng (Marketing & Product Showcase)."
---

# Remotion Cường IT Video Skill (Tech Explainer & Marketing Video)

Skill này hướng dẫn và điều khiển việc tự động tạo video ngắn định dạng dọc (9:16, 1080x1920 @ 30fps) hoàn chỉnh bằng **Remotion**, **Tailwind CSS**, và giọng đọc AI **Edge TTS** (`edge-tts-universal`), dựa trên kiến trúc của template `remotion-cuongit-template`.

Template hỗ trợ 2 chế độ chính:
1. **Chế độ Tech / Topic Explainer:** Video giải thích thuật ngữ, công nghệ, kiến thức chuyên sâu.
2. **Chế độ Marketing / Product Showcase:** Video tiếp thị sản phẩm, SaaS, khóa học, bán hàng, dịch vụ theo công thức chuyển đổi cao (PAS / AIDA).

---

## 1. Lưu ý quan trọng trên Windows & Môi trường

1. **Lệnh thực thi:**
   - Khi chạy lệnh trên Windows PowerShell, luôn dùng `npm.cmd` và `npx.cmd` thay vì `npm` / `npx` trần để tránh lỗi Execution Policy (`PSSecurityException`).
2. **Cài đặt dependencies:**
   ```powershell
   npm.cmd install
   ```
3. **Cấu hình file `.env`:**
   Đảm bảo file `.env` đã có các biến:
   ```env
   EDGE_TTS_VOICE=vi-VN-HoaiMyNeural    # hoặc vi-VN-NamMinhNeural, en-US-ChristopherNeural
   EDGE_TTS_RATE=+10%                   # +10% đến +15% giúp nhịp điệu nhanh, dồn dập
   EDGE_TTS_PITCH=+0Hz
   EDGE_TTS_VOLUME=+0%
   EDGE_TTS_OUTPUT_DIR=public/audio
   CHANNEL_NAME="CƯỜNG IT"              # Hoặc tên Brand / Shop của bạn
   ```

---

## 2. So sánh 2 Chế độ Video

| Tiêu chí | Chế độ Tech Explainer | Chế độ Marketing / Product Showcase |
| :--- | :--- | :--- |
| **Mục tiêu** | Trao giá trị, giải thích khái niệm, xây dựng uy tín | Kích thích nhu cầu, giải quyết nỗi đau, chốt đơn / lead |
| **Cấu trúc 6 cảnh** | Hook -> Problem -> Concept 1 -> Concept 2 -> Impact -> Outro | Hook -> Pain Point -> Solution (Sản phẩm) -> 3 USP/Features -> Offer/Bảo chứng -> Call to Action |
| **Visual Elements** | Glassmorphism card, SVG Diagram, Code snippet, Flow | Product Mockup, Ảnh sản phẩm thực tế (`<Img />`), Rating 5★, Badge Sale, Testimonials |
| **CTA** | Follow kênh, thả tim, lưu video | Mua ngay tại giỏ hàng, Điền form, Inbox nhận ưu đãi |
| **Âm thanh** | Voiceover rõ ràng | Voiceover dứt khoát + Nhạc nền BGM cuốn hút + SFX Whoosh/Ding |

---

## 3. Cấu trúc Kịch bản Marketing Chuẩn (50-60 giây)

Một video marketing đạt tỷ lệ chuyển đổi cao tuân theo mô hình **AIDA / PAS**:

```
[Scene 1: Hook (0s-5s)]       -> Dừng ngón tay lướt với câu hỏi trúng tim đen / Số liệu giật mình
[Scene 2: Pain Point (5s-12s)] -> Khoét sâu nỗi đau: Mất thời gian, tốn tiền, bực bội vì cách làm cũ
[Scene 3: Solution (12s-20s)]  -> Giới thiệu sản phẩm/tính năng giải quyết triệt để vấn đề
[Scene 4: USP / Proof (20s-32s)]-> 3 lý do vì sao sản phẩm vượt trội + Đánh giá 5 sao từ khách hàng
[Scene 5: Offer (32s-42s)]     -> Ưu đãi có hạn (Giảm giá, Quà tặng, Dùng thử miễn phí)
[Scene 6: CTA (42s-50s)]       -> Chỉ dẫn hành động rõ ràng: "Click link bên dưới / Nhắn tin ngay"
```

---

## 4. Quy trình Tự động tạo Video từng bước

Khi người dùng yêu cầu: *"Tạo video về [Chủ đề / Sản phẩm X]"*:

### Bước 1: Soạn kịch bản (Scripting)
1. Xác định chế độ: `Tech Explainer` hay `Marketing`.
2. Tạo 6 phân cảnh với câu từ súc tích, ngắt nhịp tự nhiên, từ 15-30 từ mỗi cảnh.

### Bước 2: Sinh giọng đọc Voiceover (TTS)
1. Tạo script TTS hoặc gọi engine `scripts/generate-tts.ts` để sinh audio MP3 và file `manifest.json`.
2. Lấy thời lượng thực tế của từng phân cảnh (`durationInFrames`).

### Bước 3: Thiết kế Scene Components
Trong thư mục `src/<TênProject>/`:
- Căn giữa toàn bộ nội dung chính (Centered Layout).
- Giữ Brand Header cố định ở `top: 150px` (tránh bị che bởi UI TikTok/Reels).
- Watermark nhận diện thương hiệu đặt dưới Header hoặc góc an toàn.
- Sử dụng Subtitle dạng `.srt` đồng bộ âm thanh chuẩn xác:
  - Chia nhỏ 3-6 từ/cụm để chống tràn màn hình dọc 9:16 trên điện thoại (`flex flex-wrap`, bỏ `whitespace-nowrap`).
  - Highlight từ khóa ngữ nghĩa có ý thức bằng dấu `*từ khóa*` trong `.srt` (chỉ bôi vàng những trọng tâm marketing/punchline thực sự quan trọng).
- Hỗ trợ giọng đọc AI: **VieNeu-TTS** (chuẩn cảm xúc tự nhiên tiếng Việt, mô hình `v3nano`, giọng `Minh Quân`) hoặc **Edge TTS**.
- Áp dụng `spring()` với `damping: 12`, `stiffness: 100` cho mọi chuyển động xuất hiện.
- Khoảng đệm giữa các cảnh (buffer): `durationInFrames + 3` (chuyển cảnh dồn dập, không để khoảng lặng).

### Bước 4: Đăng ký Composition vào `src/Root.tsx`
Thêm `<Composition>` mới với kích thước chuẩn mobile 1080x1920 @ 30fps.

### Bước 5: Kiểm tra và Render
- Mở Remotion Studio để xem trước:
  ```powershell
  npm.cmd run dev
  ```
- Xuất video MP4:
  ```powershell
  npx.cmd remotion render <TênComposition> out/<TênComposition>.mp4
  ```
