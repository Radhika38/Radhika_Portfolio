import os
import subprocess
import shutil

def run(cmd):
    print("Running:", " ".join(cmd[:6]) + "...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("Error:", res.stderr)
        raise RuntimeError(res.stderr)
    print("Done!")

os.makedirs("assets/video", exist_ok=True)
os.makedirs("public/assets/video", exist_ok=True)
os.makedirs("assets/images", exist_ok=True)
os.makedirs("public/assets/images", exist_ok=True)

src_video = "assets/video/Create_a_premium_cinematic_per (online-video-cutter.com).mp4"
font = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

# ==========================================
# 1. Reel 1: Brand Identity Hook (720x1280)
# ==========================================
print("=== Generating Reel 1: Brand Identity Hook ===")
reel1_cmd = [
    "ffmpeg", "-y",
    "-i", src_video,
    "-filter_complex",
    "[0:v]crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=720:1280,eq=contrast=1.1:saturation=1.1,"
    f"drawbox=x=30:y=60:w=260:h=44:color=#FF2B2B@0.9:t=fill,"
    f"drawtext=fontfile='{font}':text='SHORT-FORM REELS':fontsize=18:fontcolor=white:x=45:y=73,"
    f"drawbox=x=30:y=970:w=660:h=240:color=#0A0A0E@0.85:t=fill,"
    f"drawbox=x=30:y=970:w=660:h=240:color=#FF2B2B@0.5:t=2,"
    f"drawtext=fontfile='{font}':text='RADHIKA BAROT':fontsize=34:fontcolor=#FFFFFF:x=60:y=1000,"
    f"drawtext=fontfile='{font}':text='BRAND IDENTITY HOOK':fontsize=24:fontcolor=#FF2B2B:x=60:y=1050,"
    f"drawtext=fontfile='{font}':text='Dynamic typography pacing & beat-synced cuts':fontsize=18:fontcolor=#D0D0D0:x=60:y=1095,"
    f"drawtext=fontfile='{font}':text='0.3s ATTENTION HOOK  |  MAX RETENTION':fontsize=15:fontcolor=#FF2B2B:x=60:y=1140[v]",
    "-map", "[v]",
    "-map", "0:a?",
    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
    "-t", "10",
    "assets/video/reel-brand-hook.mp4"
]
run(reel1_cmd)
run(["ffmpeg", "-y", "-ss", "00:00:03", "-i", "assets/video/reel-brand-hook.mp4", "-vframes", "1", "assets/images/reel-poster-1.jpg"])


# ==========================================
# 2. Reel 2: Product Explainer (Motion & Tech)
# ==========================================
print("=== Generating Reel 2: Product Explainer ===")
reel2_cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-t", "5", "-i", "assets/images/project-socialhub.jpg",
    "-loop", "1", "-t", "5", "-i", "assets/images/project-aicruit.jpg",
    "-i", src_video,
    "-filter_complex",
    "[0:v]scale=1280:720,zoompan=z='min(zoom+0.0015,1.25)':d=150:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=720x1280[v0];"
    "[1:v]scale=1280:720,zoompan=z='min(zoom+0.0018,1.3)':d=150:x='iw/2-(iw/zoom/2)+10':y='ih/2-(ih/zoom/2)+10':s=720x1280[v1];"
    "[v0][v1]concat=n=2:v=1:a=0,"
    f"drawbox=x=30:y=60:w=260:h=44:color=#FF2B2B@0.9:t=fill,"
    f"drawtext=fontfile='{font}':text='MOTION & TECH':fontsize=18:fontcolor=white:x=60:y=73,"
    f"drawbox=x=40:y=480:w=440:h=50:color=#0A0A0E@0.85:t=fill,"
    f"drawbox=x=40:y=480:w=440:h=50:color=#FF2B2B@0.6:t=2,"
    f"drawtext=fontfile='{font}':text='[ UI WALKTHROUGH & ARCHITECTURE ]':fontsize=17:fontcolor=#FFFFFF:x=55:y=496,"
    f"drawbox=x=30:y=970:w=660:h=240:color=#0A0A0E@0.85:t=fill,"
    f"drawbox=x=30:y=970:w=660:h=240:color=#FF2B2B@0.5:t=2,"
    f"drawtext=fontfile='{font}':text='PRODUCT EXPLAINER':fontsize=34:fontcolor=#FFFFFF:x=60:y=1000,"
    f"drawtext=fontfile='{font}':text='KINETIC UI & CALLOUTS':fontsize=24:fontcolor=#FF2B2B:x=60:y=1050,"
    f"drawtext=fontfile='{font}':text='Clean UI walkthroughs  |  Micro-motion callouts':fontsize=18:fontcolor=#D0D0D0:x=60:y=1095,"
    f"drawtext=fontfile='{font}':text='FEATURE HIGHLIGHT  |  SPEED OPTIMIZED':fontsize=15:fontcolor=#FF2B2B:x=60:y=1140[v];"
    "[2:a]volume=0.9[a]",
    "-map", "[v]",
    "-map", "[a]",
    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
    "-t", "10",
    "assets/video/reel-product-explainer.mp4"
]
run(reel2_cmd)
run(["ffmpeg", "-y", "-ss", "00:00:02", "-i", "assets/video/reel-product-explainer.mp4", "-vframes", "1", "assets/images/reel-poster-2.jpg"])


# ==========================================
# 3. Reel 3: Engagement Cut (Storytelling)
# ==========================================
print("=== Generating Reel 3: Engagement Cut ===")
reel3_cmd = [
    "ffmpeg", "-y",
    "-i", src_video,
    "-filter_complex",
    "[0:v]crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=720:1280,eq=contrast=1.15:saturation=1.15,"
    f"drawbox=x=30:y=60:w=260:h=44:color=#FF2B2B@0.9:t=fill,"
    f"drawtext=fontfile='{font}':text='STORYTELLING':fontsize=18:fontcolor=white:x=65:y=73,"
    f"drawbox=x=410:y=220:w=280:h=100:color=#0A0A0E@0.9:t=fill,"
    f"drawbox=x=410:y=220:w=280:h=100:color=#FF2B2B@0.6:t=2,"
    f"drawtext=fontfile='{font}':text='+340 PERCENT REACH':fontsize=22:fontcolor=#FF2B2B:x=430:y=245,"
    f"drawtext=fontfile='{font}':text='Audience Retention Boost':fontsize=14:fontcolor=#A3A3A3:x=430:y=285,"
    f"drawbox=x=30:y=970:w=660:h=240:color=#0A0A0E@0.85:t=fill,"
    f"drawbox=x=30:y=970:w=660:h=240:color=#FF2B2B@0.5:t=2,"
    f"drawtext=fontfile='{font}':text='ENGAGEMENT CUT':fontsize=34:fontcolor=#FFFFFF:x=60:y=1000,"
    f"drawtext=fontfile='{font}':text='HIGH RETENTION EDITING':fontsize=24:fontcolor=#FF2B2B:x=60:y=1050,"
    f"drawtext=fontfile='{font}':text='Pattern interrupts  |  Sound design  |  Pacing':fontsize=18:fontcolor=#D0D0D0:x=60:y=1095,"
    f"drawtext=fontfile='{font}':text='HOOK  |  HOLD  |  REWARD  |  ACTION':fontsize=15:fontcolor=#FF2B2B:x=60:y=1140[v]",
    "-map", "[v]",
    "-map", "0:a?",
    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
    "-t", "10",
    "assets/video/reel-engagement-cut.mp4"
]
run(reel3_cmd)
run(["ffmpeg", "-y", "-ss", "00:00:04", "-i", "assets/video/reel-engagement-cut.mp4", "-vframes", "1", "assets/images/reel-poster-3.jpg"])

# Copy to public/
for f in ["reel-brand-hook.mp4", "reel-product-explainer.mp4", "reel-engagement-cut.mp4"]:
    shutil.copy(f"assets/video/{f}", f"public/assets/video/{f}")
for p in ["reel-poster-1.jpg", "reel-poster-2.jpg", "reel-poster-3.jpg"]:
    shutil.copy(f"assets/images/{p}", f"public/assets/images/{p}")

shutil.copy(src_video, "public/assets/video/Create_a_premium_cinematic_per (online-video-cutter.com).mp4")
print("Updated all reels and posters successfully without missing glyphs!")
