import os
import subprocess

# Generate a 6-second vertical 720x1280 video with animation and audio track
cmd = [
    "ffmpeg", "-y",
    "-f", "lavfi", "-i", "color=c=#0A0A0E:s=720x1280:d=6:r=30",
    "-f", "lavfi", "-i", "sine=f=440:b=4:d=6",
    "-filter_complex",
    "[0:v]format=yuv420p,"
    "drawbox=x=40:y=40:w=640:h=1200:color=#FF2B2B@0.4:t=2,"
    "drawbox=x=60:y=60:w=600:h=1160:color=#FFFFFF@0.05:t=1,"
    "drawtext=text='RADHIKA BAROT':fontsize=44:fontcolor=#F5F5F5:x=(w-text_w)/2:y=380:shadowcolor=#FF2B2B@0.5:shadowx=2:shadowy=2,"
    "drawtext=text='CODER • DIGITAL MARKETER • VIDEO EDITOR':fontsize=18:fontcolor=#A3A3A3:x=(w-text_w)/2:y=450,"
    "drawtext=text='I BUILD. I MARKET. I CREATE.':fontsize=26:fontcolor=#FF2B2B:x=(w-text_w)/2:y=540,"
    "drawtext=text='FEATURED PORTFOLIO SHOWREEL':fontsize=16:fontcolor=#FFFFFF@0.7:x=(w-text_w)/2:y=620,"
    "drawtext=text='[ REPLACE IN assets/video/radhika-intro.mp4 ]':fontsize=15:fontcolor=#FF2B2B:x=(w-text_w)/2:y=800,"
    "drawtext=text='%{pts\\:hms}':fontsize=20:fontcolor=#FFFFFF@0.4:x=(w-text_w)/2:y=1050[v];"
    "[1:a]volume=0.08[a]",
    "-map", "[v]",
    "-map", "[a]",
    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
    "assets/video/radhika-intro.mp4"
]

res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode != 0:
    print("Error:", res.stderr)
else:
    print("Video generated successfully!")
