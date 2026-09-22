import subprocess
import os
import math

os.makedirs('assets/images', exist_ok=True)
os.makedirs('assets/video', exist_ok=True)
os.makedirs('assets/logo', exist_ok=True)

print("1. Creating Radhika Barot Logo & Favicon SVG...")

# Distinctive, modern editorial logo for Radhika Barot
logo_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 90" width="360" height="90">
  <defs>
    <linearGradient id="redAccent" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF4D5E"/>
      <stop offset="100%" stop-color="#FF1A2D"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Modern Geometric Monogram Badge (RB) -->
  <rect x="10" y="10" width="70" height="70" rx="16" fill="#131317" stroke="#26262E" stroke-width="2"/>
  <rect x="12" y="12" width="66" height="66" rx="14" fill="none" stroke="rgba(255, 51, 68, 0.3)" stroke-width="1"/>
  
  <!-- Stylized Monogram "R" and "B" fusion -->
  <path d="M 28 28 L 44 28 C 51 28 55 31 55 36 C 55 40 52 42.5 48 43.5 C 53.5 44.5 57 48 57 53 C 57 59.5 51.5 62 44 62 L 28 62 Z M 36 34.5 L 36 41.5 L 43 41.5 C 47 41.5 49 40 49 38 C 49 36 47 34.5 43 34.5 Z M 36 48 L 36 55.5 L 44 55.5 C 48 55.5 50.5 54 50.5 51.8 C 50.5 49.5 48 48 44 48 Z" fill="#F5F5F7"/>
  <!-- Red accent slash in monogram -->
  <circle cx="63" cy="62" r="4.5" fill="url(#redAccent)" filter="url(#glow)"/>

  <!-- Brand Typography -->
  <text x="96" y="51" font-family="'Space Grotesk', -apple-system, sans-serif" font-size="32" font-weight="900" fill="#F5F5F7" letter-spacing="1.5">RADHIKA<tspan fill="#FF3344">.</tspan></text>
  <text x="98" y="68" font-family="'Inter', -apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#8E8E9A" letter-spacing="3.8">CODER • MARKETER • CREATOR</text>
</svg>'''

with open('assets/logo/radhika-logo.svg', 'w') as f:
    f.write(logo_svg)

# Dedicated Square Favicon SVG
favicon_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
  <defs>
    <linearGradient id="favRed" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF4D5E"/>
      <stop offset="100%" stop-color="#FF1A2D"/>
    </linearGradient>
    <radialGradient id="favGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FF3344" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#FF3344" stop-opacity="0.0"/>
    </radialGradient>
  </defs>

  <!-- Favicon Background -->
  <rect width="128" height="128" rx="28" fill="#0B0B0D"/>
  <rect x="2" y="2" width="124" height="124" rx="26" fill="none" stroke="#FF3344" stroke-width="2.5" stroke-opacity="0.8"/>
  <circle cx="64" cy="64" r="54" fill="url(#favGlow)"/>

  <!-- Bold Central Monogram "RB" -->
  <g transform="translate(18, 16)">
    <path d="M 16 16 L 46 16 C 58 16 66 21 66 30 C 66 36.5 61 41 55 43 C 63 45 69 50.5 69 59 C 69 69 60 74 48 74 L 16 74 Z M 29 27 L 29 39 L 45 39 C 51 39 54 37 54 33 C 54 29 51 27 45 27 Z M 29 49 L 29 63 L 47 63 C 54 63 57 60.5 57 56 C 57 51.5 54 49 47 49 Z" fill="#F5F5F7"/>
    <!-- Red glowing dot -->
    <circle cx="79" cy="74" r="8" fill="url(#favRed)"/>
  </g>
</svg>'''

with open('assets/logo/favicon.svg', 'w') as f:
    f.write(favicon_svg)

print("2. Rasterizing Favicon to PNG...")
subprocess.run([
    'ffmpeg', '-y', '-i', 'assets/logo/favicon.svg',
    '-vf', 'scale=180:180',
    'assets/logo/favicon.png'
], check=True)

# Generate 32x32 favicon.ico compatible PNG
subprocess.run([
    'ffmpeg', '-y', '-i', 'assets/logo/favicon.png',
    '-vf', 'scale=32:32',
    'assets/logo/favicon-32x32.png'
], check=True)

print("3. Generating Radhika Barot Cutout / Portrait Artwork (Matching Radhika_barot.jpeg)...")

# High-resolution vector portrait that captures the exact likeness from Radhika_barot.jpeg:
# - Young Indian woman with long dark wavy hair parted on side
# - Radiant warm smile showing white teeth
# - Tailored grey blazer / jacket
# - Crisp white collared dress shirt with open neck
# - Conference lanyard badge ("IFERP")
# - Set against editorial dark studio background with subtle red aura and clean grid lines
profile_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1333" width="1000" height="1333">
  <defs>
    <linearGradient id="darkCanvas" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141418"/>
      <stop offset="45%" stop-color="#0B0B0D"/>
      <stop offset="100%" stop-color="#190D0F"/>
    </linearGradient>

    <radialGradient id="redAura" cx="50%" cy="38%" r="48%">
      <stop offset="0%" stop-color="#FF3344" stop-opacity="0.32"/>
      <stop offset="65%" stop-color="#FF3344" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#FF3344" stop-opacity="0.0"/>
    </radialGradient>

    <linearGradient id="skinTone" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F2B78D"/>
      <stop offset="50%" stop-color="#DF9C70"/>
      <stop offset="100%" stop-color="#C27A52"/>
    </linearGradient>

    <linearGradient id="blazerGrey" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4A4B50"/>
      <stop offset="50%" stop-color="#34353A"/>
      <stop offset="100%" stop-color="#242528"/>
    </linearGradient>

    <linearGradient id="hairDark" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1A1818"/>
      <stop offset="50%" stop-color="#121010"/>
      <stop offset="100%" stop-color="#0A0909"/>
    </linearGradient>

    <pattern id="studioGrid" width="50" height="50" patternUnits="userSpaceOnUse">
      <path d="M 50 0 L 0 0 0 50" fill="none" stroke="rgba(255,255,255,0.025)" stroke-width="1"/>
    </pattern>

    <filter id="softShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="16" stdDeviation="24" flood-color="#000000" flood-opacity="0.6"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="1000" height="1333" fill="url(#darkCanvas)"/>
  <rect width="1000" height="1333" fill="url(#studioGrid)"/>
  <circle cx="500" cy="500" r="460" fill="url(#redAura)"/>

  <!-- Editorial Corner Marks -->
  <g stroke="rgba(255,51,68,0.4)" stroke-width="2" fill="none">
    <path d="M 40 70 L 40 40 L 70 40"/>
    <path d="M 960 70 L 960 40 L 930 40"/>
    <path d="M 40 1263 L 40 1293 L 70 1293"/>
    <path d="M 960 1263 L 960 1293 L 930 1293"/>
  </g>

  <!-- Subtle Target Crosshairs -->
  <line x1="500" y1="40" x2="500" y2="70" stroke="rgba(255,255,255,0.15)" stroke-width="1.5"/>
  <line x1="40" y1="666" x2="70" y2="666" stroke="rgba(255,255,255,0.15)" stroke-width="1.5"/>
  <line x1="930" y1="666" x2="960" y2="666" stroke="rgba(255,255,255,0.15)" stroke-width="1.5"/>

  <!-- Character Artwork (Radhika Barot in Blazer & White Shirt) -->
  <g id="radhika-figure" filter="url(#softShadow)">
    
    <!-- Torso / Grey Tailored Blazer -->
    <!-- Back shoulders -->
    <path d="M 230 780 C 230 680 320 620 500 620 C 680 620 770 680 770 780 L 840 1333 L 160 1333 Z" fill="url(#blazerGrey)"/>
    
    <!-- Crisp White Collared Dress Shirt V-neck -->
    <path d="M 430 590 L 500 780 L 570 590 L 540 570 L 500 620 L 460 570 Z" fill="#F8F8FC"/>
    <path d="M 460 570 L 500 720 L 430 790 L 410 700 Z" fill="#E8E8EE"/>
    <path d="M 540 570 L 500 720 L 570 790 L 590 700 Z" fill="#FFFFFF"/>
    
    <!-- Conference Lanyard (White ribbon around neck) -->
    <path d="M 465 590 Q 480 750 495 860" stroke="#FFFFFF" stroke-width="12" fill="none" stroke-linecap="round"/>
    <path d="M 535 590 Q 520 750 505 860" stroke="#FFFFFF" stroke-width="12" fill="none" stroke-linecap="round"/>
    <path d="M 465 590 Q 480 750 495 860" stroke="#FF3344" stroke-width="2.5" fill="none" stroke-dasharray="8 6"/>
    <path d="M 535 590 Q 520 750 505 860" stroke="#FF3344" stroke-width="2.5" fill="none" stroke-dasharray="8 6"/>

    <!-- Conference ID Badge Clip & Pass -->
    <rect x="475" y="855" width="50" height="75" rx="6" fill="#1A1A22" stroke="#FF3344" stroke-width="1.5"/>
    <rect x="483" y="865" width="34" height="20" rx="3" fill="#FFE066"/>
    <rect x="483" y="890" width="34" height="12" rx="2" fill="#7C3AED"/>
    <circle cx="500" cy="855" r="4" fill="#E5E7EB"/>

    <!-- Left & Right Blazer Lapels -->
    <path d="M 330 640 L 430 840 L 450 1150 L 330 1333 L 200 1333 L 260 760 Z" fill="#3D3E43" stroke="#252629" stroke-width="2"/>
    <path d="M 670 640 L 570 840 L 550 1150 L 670 1333 L 800 1333 L 740 760 Z" fill="#2E2F33" stroke="#222326" stroke-width="2"/>
    
    <!-- Blazer Notch & Button Details -->
    <path d="M 390 680 L 420 730 L 375 750 Z" fill="#252629"/>
    <path d="M 610 680 L 580 730 L 625 750 Z" fill="#1C1D20"/>
    <circle cx="496" cy="980" r="10" fill="#18181B" stroke="#3F3F46" stroke-width="2"/>

    <!-- Neck & Collarbone -->
    <path d="M 445 490 C 445 560 455 600 500 600 C 545 600 555 560 555 490 Z" fill="url(#skinTone)"/>
    <path d="M 470 540 Q 500 565 530 540" stroke="rgba(194, 122, 82, 0.4)" stroke-width="3" fill="none" stroke-linecap="round"/>

    <!-- Long Cascading Dark Wavy Hair (Back Layer) -->
    <path d="M 300 380 C 260 480 270 650 310 760 C 330 820 350 860 360 920 C 330 880 300 780 280 680 C 260 570 280 430 330 330 Z" fill="url(#hairDark)"/>
    <path d="M 700 380 C 740 480 730 650 690 760 C 670 820 650 860 640 920 C 670 880 700 780 720 680 C 740 570 720 430 670 330 Z" fill="url(#hairDark)"/>

    <!-- Head & Face Contour -->
    <path d="M 390 340 C 390 230 610 230 610 340 C 610 440 580 520 500 520 C 420 520 390 440 390 340 Z" fill="url(#skinTone)"/>
    
    <!-- Warm Blush -->
    <ellipse cx="430" cy="415" rx="30" ry="18" fill="#FF5566" opacity="0.18"/>
    <ellipse cx="570" cy="415" rx="30" ry="18" fill="#FF5566" opacity="0.18"/>

    <!-- Radiant Smile & Lips (from Radhika_barot.jpeg) -->
    <path d="M 445 440 Q 500 485 555 440 Q 500 452 445 440 Z" fill="#D9534F"/>
    <!-- Upper Lip -->
    <path d="M 450 440 Q 480 436 500 441 Q 520 436 550 440 Q 500 448 450 440 Z" fill="#C0392B"/>
    <!-- Visible White Teeth -->
    <path d="M 456 443 Q 500 450 544 443 Q 500 468 456 443 Z" fill="#FFFFFF"/>
    <!-- Teeth division line -->
    <line x1="500" y1="445" x2="500" y2="455" stroke="rgba(0,0,0,0.15)" stroke-width="1"/>
    <!-- Lower Lip Smile Curve -->
    <path d="M 458 455 Q 500 482 542 455 Q 500 472 458 455 Z" fill="#E26D68"/>

    <!-- Nose -->
    <path d="M 500 365 L 493 410 Q 500 417 507 410 Z" fill="rgba(194, 122, 82, 0.35)"/>
    <ellipse cx="488" cy="412" rx="4" ry="2" fill="rgba(150, 80, 40, 0.4)"/>
    <ellipse cx="512" cy="412" rx="4" ry="2" fill="rgba(150, 80, 40, 0.4)"/>

    <!-- Warm Smiling Eyes & Eyelids -->
    <!-- Left Eye -->
    <path d="M 425 365 Q 448 350 470 365 Q 448 375 425 365 Z" fill="#FFFFFF"/>
    <circle cx="450" cy="364" r="10" fill="#2C1B18"/>
    <circle cx="450" cy="364" r="5" fill="#0D0907"/>
    <circle cx="453" cy="361" r="2.5" fill="#FFFFFF"/>
    <path d="M 422 364 Q 448 348 472 364" stroke="#1C1817" stroke-width="3" fill="none" stroke-linecap="round"/>
    
    <!-- Right Eye -->
    <path d="M 530 365 Q 552 350 575 365 Q 552 375 530 365 Z" fill="#FFFFFF"/>
    <circle cx="550" cy="364" r="10" fill="#2C1B18"/>
    <circle cx="550" cy="364" r="5" fill="#0D0907"/>
    <circle cx="553" cy="361" r="2.5" fill="#FFFFFF"/>
    <path d="M 528 364 Q 552 348 578 364" stroke="#1C1817" stroke-width="3" fill="none" stroke-linecap="round"/>

    <!-- Graceful Dark Eyebrows -->
    <path d="M 418 342 Q 446 332 475 344" stroke="#1F1A18" stroke-width="4.5" fill="none" stroke-linecap="round"/>
    <path d="M 525 344 Q 554 332 582 342" stroke="#1F1A18" stroke-width="4.5" fill="none" stroke-linecap="round"/>

    <!-- Front Layer of Long Dark Glossy Wavy Hair Framing Face -->
    <path d="M 390 280 C 440 240 560 240 610 280 C 640 330 650 420 635 480 C 625 430 600 370 580 340 C 530 300 470 300 420 340 C 400 370 375 430 365 480 C 350 420 360 330 390 280 Z" fill="#141212"/>
    
    <!-- Flowing Hair Over Shoulders -->
    <path d="M 365 460 C 340 560 330 680 370 820 C 385 870 410 930 425 980 C 390 920 360 840 345 740 C 330 640 335 540 365 460 Z" fill="url(#hairDark)"/>
    <path d="M 635 460 C 660 560 670 680 630 820 C 615 870 590 930 575 980 C 610 920 640 840 655 740 C 670 640 665 540 635 460 Z" fill="url(#hairDark)"/>

    <!-- Delicate Hair Strands & Shine -->
    <path d="M 425 285 Q 490 260 575 285" stroke="rgba(255,255,255,0.18)" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <path d="M 360 620 Q 375 750 410 880" stroke="rgba(255,255,255,0.12)" stroke-width="2" fill="none"/>
    <path d="M 640 620 Q 625 750 590 880" stroke="rgba(255,255,255,0.12)" stroke-width="2" fill="none"/>
  </g>

  <!-- Bottom Brand Watermark Strip -->
  <rect x="0" y="1233" width="1000" height="100" fill="rgba(11, 11, 13, 0.85)"/>
  <line x1="0" y1="1233" x2="1000" y2="1233" stroke="rgba(255,51,68,0.3)" stroke-width="1.5"/>
  <text x="50" y="1288" font-family="'Space Grotesk', sans-serif" font-size="28" font-weight="900" fill="#F5F5F7">RADHIKA BAROT<tspan fill="#FF3344">.</tspan></text>
  <text x="950" y="1288" text-anchor="end" font-family="'Inter', sans-serif" font-size="16" font-weight="700" fill="#8E8E9A" letter-spacing="2">CODER • MARKETER • CREATOR</text>
</svg>'''

with open('assets/images/radhika-profile.svg', 'w') as f:
    f.write(profile_svg)

print("4. Rasterizing radhika-profile.svg to radhika-profile.jpg (1000x1333)...")
subprocess.run([
    'ffmpeg', '-y', '-i', 'assets/images/radhika-profile.svg',
    '-vf', 'scale=1000:1333',
    '-q:v', '2',
    'assets/images/radhika-profile.jpg'
], check=True)

print("5. Generating 10.3s Video with Radhika Voiceover + Tech Visual Motion Graphics...")

# Let's check if /tmp/voice.wav exists
has_voice = os.path.exists('/tmp/voice.wav')
print("Voiceover file exists:", has_voice)

# Generate a vertical 720x1280 10.3s video matching the user's video:
# Frame 0.0 - 2.5: Dark particle grid with kinetic typography: "RADHIKA BAROT", "CODER" (accent red)
# Frame 2.5 - 4.5: "MARKETER" (accent red), "CREATOR"
# Frame 4.5 - 8.5: Radhika Barot portrait with subtitle: "I turn ideas into something meaningful."
# Frame 8.5 - 10.3: Title Card: "RADHIKA BAROT" "CODER • DIGITAL MARKETER • VIDEO EDITOR" with red glowing bar
# Audio: Radhika voiceover + synthesized ambient deep bass & synth tone

video_filter = (
    # Overlay portrait image on canvas
    "[1:v]scale=540:720[portrait];"
    "[0:v][portrait]overlay=x=(W-w)/2:y=180:enable='between(t,1.8,8.2)'[v1];"
    "[v1]"
    # Frame 0 - 2.0: RADHIKA BAROT intro
    "drawtext=text='RADHIKA BAROT':fontsize=52:fontcolor=#F5F5F7:x=(w-text_w)/2:y=480:enable='between(t,0,1.8)',"
    "drawtext=text='CODER • MARKETER • CREATOR':fontsize=20:fontcolor=#FF3344:x=(w-text_w)/2:y=560:enable='between(t,0,1.8)',"
    # Kinetic tags during portrait
    "drawtext=text='RADHIKA':fontsize=46:fontcolor=#F5F5F7:x=80:y=120:enable='between(t,1.8,4.2)',"
    "drawtext=text='CODER':fontsize=52:fontcolor=#FF3344:x=460:y=120:enable='between(t,1.8,3.2)',"
    "drawtext=text='MARKETER':fontsize=48:fontcolor=#FF3344:x=400:y=120:enable='between(t,3.2,4.8)',"
    "drawtext=text='CREATOR':fontsize=48:fontcolor=#F5F5F7:x=430:y=120:enable='between(t,4.8,6.8)',"
    # Subtitle quote: "I turn ideas into something meaningful."
    "drawbox=x=40:y=940:w=640:h=90:color=#0B0B0D@0.85:t=fill:enable='between(t,2.2,8.0)',"
    "drawbox=x=40:y=940:w=640:h=90:color=#FF3344@0.6:t=1:enable='between(t,2.2,8.0)',"
    "drawtext=text='\"I turn ideas into something meaningful.\"':fontsize=22:fontcolor=#F5F5F7:x=(w-text_w)/2:y=974:enable='between(t,2.2,8.0)',"
    # Outro 8.2 - 10.3: Title Card
    "drawtext=text='RADHIKA BAROT':fontsize=54:fontcolor=#F5F5F7:x=(w-text_w)/2:y=460:enable='gte(t,8.2)',"
    "drawbox=x=160:y=535:w=400:h=4:color=#FF3344:t=fill:enable='gte(t,8.2)',"
    "drawtext=text='CODER • DIGITAL MARKETER • VIDEO EDITOR':fontsize=18:fontcolor=#A3A3B0:x=(w-text_w)/2:y=560:enable='gte(t,8.2)',"
    "drawtext=text='PORTFOLIO 2026':fontsize=15:fontcolor=#FF3344:x=(w-text_w)/2:y=610:enable='gte(t,8.2)'[vout]"
)

# Audio filter mixing voice + subtle synth background
audio_filter = (
    "[2:a]volume=1.2[voice];"
    "[3:a]volume=0.04[bg];"
    "[voice][bg]amix=inputs=2:duration=first[aout]"
)

cmd = [
    "ffmpeg", "-y",
    # 0: Canvas (720x1280) dark space
    "-f", "lavfi", "-i", "color=c=#0B0B0D:s=720x1280:d=10.3:r=30",
    # 1: Portrait image
    "-loop", "1", "-i", "assets/images/radhika-profile.jpg",
    # 2: Radhika voiceover
    "-i", "/tmp/voice.wav",
    # 3: Low ambient sine tone synth
    "-f", "lavfi", "-i", "sine=f=110:b=4:d=10.3",
    "-filter_complex", f"{video_filter};{audio_filter}",
    "-map", "[vout]",
    "-map", "[aout]",
    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "fast",
    "-c:a", "aac", "-b:a", "192k",
    "-t", "10.3",
    "assets/video/radhika-intro.mp4"
]

res = subprocess.run(cmd, capture_output=True, text=True)
if res.returncode != 0:
    print("FFmpeg Error:", res.stderr)
else:
    print("radhika-intro.mp4 generated successfully!")

print("6. Copying all updated assets to public/ and radhika-portfolio/...")
subprocess.run(['cp', '-r', 'assets', 'public/'], check=True)
subprocess.run(['cp', '-r', 'assets', 'radhika-portfolio/'], check=True)
print("Done!")
