---
name: ai-avatar-video
description: "Quy trình chuẩn sản xuất video ngắn TikTok/Reels/Shorts phong cách AI Avatar (Talking Head / 2D Vector Presenter) kết hợp đồ họa Remotion, VieNeu-TTS / Audio Sync, phụ đề SRT chống ngắt sớm và hiệu ứng Motion Graphic / Vox Explainer tỷ lệ vàng."
---

# AI Avatar Video - Professional Short Video Creation Skill

Skill chuyên biệt dùng để tự động sản xuất video ngắn định dạng dọc 9:16 (1080x1920 @ 30fps) phong cách **AI Avatar / 2D Vector Studio Presenter** kết hợp đồ họa chuyển động **Remotion**, giọng đọc tự nhiên **VieNeu-TTS**, phụ đề **SRT đồng bộ giọng nói chống ngắt sớm (Zero Dead Gap)** và hệ thống đồ họa **Vox Explainer / Motion Graphics** kích thước lớn tối ưu cho mobile.

---

## 1. Định Vị Phong Cách Hybrid: "2D Vector Presenter + Vox Explainer"

Hệ thống kết hợp 2 trạng thái chuyển cảnh nhịp nhàng (Dual-Mode Architecture):

### A. State 1: "2D Vector Studio Presenter" (Dẫn Chuyện & Tương Tác Trực Quan)
- **Hình ảnh nhân vật:** 
  - Nhân vật 2D Vector phẳng phong cách hiện đại (áo vest xanh navy, kính cận, nụ cười chuyên nghiệp).
  - **Tạo hình Clean Puppet:** Không sử dụng cánh tay vẽ tĩnh để tránh đơ cứng; đặt **Laptop** ở chính giữa thân (in nhãn nhận diện thương hiệu, ví dụ `@phongphammarketing`); ly cà phê bốc khói nhẹ cạnh bàn; mặt bàn gỗ kéo dài thân xuống tận đáy màn hình che kín viền, không để lộ cạnh cắt lơ lửng.
- **Hệ thống Khẩu hình (Lip-Sync Visemes):**
  - Sử dụng bộ 5 visemes SVG chuẩn hóa:
    - `rest`: Miệng ngậm mỉm cười nhẹ (dùng khi im lặng / ngắt câu).
    - `ae`: Mở miệng phát âm A, E, O (nói chính).
    - `ou`: Miệng tròn nhỏ phát âm U, O.
    - `wide`: Miệng bè rộng phát âm I, E cao.
    - `mbp`: Mím môi phát âm M, B, P.
- **Đồng bộ nhịp nói tự nhiên (Audio Reactivity & Cadence):**
  - **Bắt buộc trích xuất `speechActivityArray`** từ file âm thanh `.wav` (chu kỳ 30fps): Mảng boolean xác định frame nào có giọng nói và frame nào là khoảng lặng (silence / pause).
  - **Lưu ý kiểm tra điều kiện Lip-Sync:** Luôn dùng `Boolean(speechActivityArray[frame])` thay vì so sánh cứng `=== 1` để tránh lỗi sai kiểu dữ liệu giữa boolean và number.
  - Khi giọng nói tạm dừng (`isActive === false`): Miệng **lập tức chuyển về `rest`**, tránh tình trạng puppet vẫn nhép miệng dù audio đã ngắt.
  - Khi đang nói (`isActive === true`): Luân chuyển mượt mà với nhịp 2 frame/viseme (`Math.floor(frame / 2) % visemes.length`), tạo cảm giác phát âm sống động, không bị giật cục.
- **Nhịp thở & Chớp mắt tự nhiên:**
  - Breathing dao động nhẹ (`Math.sin(frame / 15) * 4px`).
  - Chớp mắt tự động mỗi 90-120 frames.
- **Top Motion Graphic Stage (Minh họa ngay từ giây 0 phía trên nhân vật):**
  - **Tuyệt đối không để cảnh Avatar chỉ có text tĩnh kéo dài tới 10-15s gây nhàm chán.**
  - Ngay từ **Scene 1 (Hook) và Scene 2 (Pain Point)**, vùng không gian phía trên đầu nhân vật (Y: 150 -> 480) **phải có Motion Graphic minh họa chuyển động**:
    + Thẻ so sánh động nảy số (Dynamic Comparison Cards với hiệu ứng `spring()`).
    + Thanh đo tiến trình / chỉ số phần trăm chạy (Progress & Metric Bars).
    + Biểu đồ mini, sơ đồ phân nhánh não bộ (Brain Mechanism) hoặc icon cảnh báo nhấp nháy.
  - Thiết kế nằm gọn trong bảng trình chiếu studio trên đầu nhân vật, không che khuất mặt và không đè lên thanh phụ đề phía dưới.

### B. State 2: "Vox / Deep-Dive Explainer" (Giải Thích Chuyên Môn & Đồ Họa Số Liệu)
- **Kích thước Đồ họa Tối Ưu Mobile (Scale Up 20-25%):**
  - Tuyệt đối không để motion graphics quá nhỏ lọt thỏm giữa màn hình.
  - **Funnel Flow Diagram / Sơ đồ phễu:** Chiều rộng từ `960px` đến `1000px`, font chữ `text-2xl font-black`, padding rộng rãi, lấp đầy 85-90% chiều ngang màn hình.
  - **Vox Explainer Board / Bảng số liệu:** Kích thước `w-[1000px] min-h-[1100px]`, tiêu đề lớn `text-6xl font-black`, số liệu nổi bật `text-7xl font-black`.
- **Nguyên tắc Safe Zone & Xếp Lớp (Layer Stacking):**
  - Ở các phân cảnh hiển thị bảng biểu toàn màn hình, **không chèn Mini Presenter ở góc dưới** nếu nó đè lên hoặc thu hẹp diện tích của thanh Subtitle.

---

## 2. Tiêu Chuẩn Giọng Đọc (VieNeu-TTS Engine)

Tuyệt đối **không dùng giọng Edge TTS máy móc thô cứng**. Ưu tiên dùng **VieNeu-TTS** để có giọng đọc tiếng Việt tự nhiên, có ngắt nghỉ và ngữ điệu chân thực:

- **Model khuyến nghị:** `v3nano`
- **Voice:**
  - Giọng nam: `Minh Quân` (Trầm ấm, đĩnh đạc, dứt khoát).
  - Giọng nữ: `Thu Ngân` (Thanh thoát, truyền cảm hứng, tự nhiên).
- **Script tạo Voice:** `scripts/generate-vieneu-tts.py`
  - Đầu ra: File `.wav` từng scene lưu tại `public/audio/<ProjectName>/scene_{i}.wav`.
  - Đo độ dài chính xác bằng thư viện `wave` hoặc `pydub`, tự động tính tổng số frame (`durationInFrames = ceil(seconds * 30)`).
  - Trích xuất `speechActivity.json` phục vụ lip-sync tự nhiên.

---

## 3. Tiêu Chuẩn Phụ Đề SRT Chống Ngắt Sớm (Zero Dead Gap)

### A. Vấn đề thực tế và Giải pháp:
- **Lỗi thường gặp:** Chia vụn phụ đề thành các cụm 2-3 từ quá ngắn và để khoảng trống thời gian giữa các cue khiến phụ đề **biến mất trước khi dứt câu** hoặc chớp nháy liên tục gây ức chế cho người xem.
- **Tiêu chuẩn chuẩn hóa:**
  1. **Mệnh đề hoàn chỉnh (8 đến 14 từ):** Mỗi cue là một câu hoặc vế câu trọn vẹn ý nghĩa, cho phép tự động xuống dòng 2 hàng cân đối.
  2. **Quy tắc Zero Dead Gap:** `endFrame` của cue hiện tại phải **kéo dài chạm sát mốc `startFrame` của cue tiếp theo** (hoặc thời điểm dứt giọng thực tế của audio + 5 frames). Không để hở khoảng trống khiến phụ đề bị ngắt lửng.
  3. **Thời lượng hiển thị hợp lý:** Mỗi cue hiển thị tối thiểu từ **2.0 giây đến 4.0 giây** để người xem đọc kịp.

### B. Logic Highlight Ngữ Nghĩa (Semantic Asterisk Syntax)
- Trong file phụ đề / config, bọc từ khóa cốt lõi bằng dấu sao `*từ khóa*`:
  ```srt
  1
  00:00:00,000 --> 00:00:03,200
  Bạn đổ *hàng trăm triệu* vào quảng cáo nhưng *đơn hàng* vẫn lẹt đẹt?
  ```
- **Quy tắc chọn từ khóa:**
  - Chỉ highlight: Con số giật mình, nỗi đau cốt lõi, khái niệm chuyên ngành, phương pháp đột phá.
  - Không highlight đại từ, liên từ hay từ đệm.

### C. Giao Diện Thanh Phụ Đề Chuẩn (`SrtSubtitleOverlay.tsx`)
- Container rộng thoáng: `max-w-[980px]` căn giữa đáy màn hình (`bottom: 240px` đến `280px`).
- Kiểu dáng: Bo góc mềm mại `rounded-3xl border-2 border-cyan-400/60 bg-slate-950/95 px-8 py-4 backdrop-blur-2xl shadow-[0_10px_40px_rgba(0,0,0,0.8)]`.
- Font chữ động:
  - <= 8 từ: `text-4xl leading-snug`.
  - > 8 từ: `text-3xl leading-relaxed`.
- Màu sắc:
  - Từ khóa highlight: `text-amber-300 drop-shadow-[0_0_15px_rgba(252,211,77,0.85)] font-black`.
  - Chữ thường: `text-slate-100 font-extrabold`.

---

## 4. Script Trích Xuất Speech Activity Phục Vụ Lip-Sync

Khi có các file `.wav` giọng đọc, chạy script Python để phân tích mức năng lượng sóng âm và xuất ra mảng boolean 30fps:

```python
import wave
import numpy as np
import json

def analyze_speech_activity(wav_path, fps=30, threshold=500):
    with wave.open(wav_path, 'rb') as wf:
        n_channels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        framerate = wf.getframerate()
        n_frames = wf.getnframes()
        data = wf.readframes(n_frames)
        
    audio = np.frombuffer(data, dtype=np.int16)
    if n_channels > 1:
        audio = audio[::n_channels]
        
    samples_per_video_frame = framerate // fps
    total_video_frames = int(np.ceil(len(audio) / samples_per_video_frame))
    
    activity = []
    for f in range(total_video_frames):
        chunk = audio[f * samples_per_video_frame : (f + 1) * samples_per_video_frame]
        if len(chunk) == 0:
            activity.append(False)
            continue
        rms = np.sqrt(np.mean(chunk.astype(float)**2))
        activity.append(bool(rms > threshold))
        
    return activity
```

---

## 5. Quy Trình Sản Xuất Video Từ A Đến Z

Khi người dùng yêu cầu làm video mới:

### Bước 1: Soạn kịch bản (6 Cảnh Chuẩn Mobile)
1. **Scene 1 (Hook - 0s - 4.5s):** Câu hỏi bất ngờ / Nghịch lý gây tò mò.
2. **Scene 2 (Pain Point - 4.5s - 11.5s):** Bóc tách nguyên nhân sai lầm cốt lõi.
3. **Scene 3 (Concept / Solution - 11.5s - 20.5s):** Sơ đồ phễu / Giải pháp trực quan (Funnel Diagram).
4. **Scene 4 (Deep Dive Case Study - 20.5s - 32.5s):** Bảng so sánh / Số liệu minh chứng (Vox Board).
5. **Scene 5 (Key Takeaway - 32.5s - 40.5s):** Bài học thực chiến cô đọng.
6. **Scene 6 (Outro & CTA - 40.5s - 45s):** Avatar mời gọi follow / tương tác.

### Bước 2: Sinh Giọng VieNeu-TTS & Phân Tích Âm Thanh
- Sinh âm thanh từng scene ra `public/audio/<ProjectName>/scene_{i}.wav`.
- Trích xuất `speechActivity.json` và lưu thời lượng frame vào `manifest.json`.

### Bước 3: Chuẩn Bị Puppet & Subtitle Cấu Hình
- Nhúng `AvatarCleanPuppet.tsx` (laptop ở giữa, không cánh tay, bàn gỗ kéo dài).
- Viết phụ đề theo quy tắc **Zero Dead Gap**, thời gian hiển thị 2.5s - 4.0s/câu.

### Bước 4: Lắp Ghép Composition Remotion
- **Bắt buộc tích hợp Top Motion Graphic ngay từ đầu (Scene 1 & Scene 2):**
  - Truyền prop `topGraphic={<CustomMotionGraphic />}` vào `AvatarCleanStudioScene`.
  - Hiển thị các thẻ so sánh trực quan, thanh chỉ số phần trăm chạy (progress meter), hoặc sơ đồ phân nhánh ngay phía trên đầu nhân vật (Y 150 -> 480) từ giây 0.
  - Tuyệt đối không để 10-15s đầu chỉ có avatar nói với text tĩnh gây nhàm chán.
- **Scene 3 & 4 (Deep Dive):**
  - Chuyển tiếp mượt mà sang giao diện Vox Explainer / Documentary Stage toàn màn hình (`w-[1000px]`).
- **Đảm bảo Subtitle:**
  - Vị trí `bottom: 240px` đến `280px`, không bị che khuất bởi bất kỳ layer nào.

### Bước 5: Render Kiểm Tra & Xuất Video
- Lệnh render trên Windows:
  ```powershell
  npx.cmd remotion render <CompositionId> out/<TargetFolder>/<VideoName>.mp4 --overwrite
  ```
- Kiểm tra tính toàn vẹn của file video và cung cấp link cho người dùng.

---

## 6. Thư Viện Motion Graphics Chuẩn Hóa (`src/components/motion/`)

Hệ thống tích hợp sẵn kho component chuyển động phong cách Magic UI, Aceternity UI, Johnny Harris & Vox Explainer:
- **`NumberTicker`:** Số nhảy tăng dần tự động (tỷ lệ %, doanh thu, lượt view).
- **`BorderBeam`:** Viền laser xoay tròn phát sáng bao quanh các thẻ card/bảng số liệu.
- **`AnimatedBeam`:** Tia năng lượng nối đường cong Bezier giữa 2 điểm/icon (biểu diễn dòng tiền, luồng dữ liệu).
- **`RadarScan`:** Vòng tròn radar quét 360° phát hiện insight, mục tiêu hoặc nỗi đau khách hàng.
- **`BalanceScale`:** Cán cân so sánh nghiêng bập bênh động (Giá bán vs Giá trị, Mất mát vs Lợi ích).
- **`HighlighterPen`:** Vệt bút dạ quang quét ngang gạch chân từ khóa chốt hạ.
- **`DonutProgress`:** Vòng tròn phần trăm tiến trình SVG xoay động.
- **`SparklesCore`:** Bụi sáng công nghệ bay lơ lửng nền Vox Documentary.
- **`CameraShake`:** Rung lắc camera Perlin Noise (`@remotion/noise`) tạo hiệu ứng giật gân, chấn động.
- **`MorphingShape`:** Biến hình SVG mượt mà giữa các hình học (`@remotion/shapes` & `@remotion/paths`).
- **`ConfettiBlast`:** Pháo giấy ăn mừng khi đạt kết quả, doanh số đột phá.
- **`LottieAnimation`:** Nhúng Lottie JSON animation frame-by-frame (`@remotion/lottie`).

---

## 7. Lưu Ý Kỹ Thuật Bắt Buộc Trên Windows
- Luôn gọi lệnh bằng `npm.cmd` và `npx.cmd`.
- Mọi script Python in text tiếng Việt ra console phải có:
  ```python
  import sys
  if hasattr(sys.stdout, "reconfigure"):
      sys.stdout.reconfigure(encoding="utf-8")
  ```

