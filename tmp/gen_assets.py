import subprocess
import os

os.makedirs('/tmp/assets_gen', exist_ok=True)

# 1. Logo SVG
logo_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 80" width="320" height="80">
  <defs>
    <linearGradient id="rbGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF2B2B"/>
      <stop offset="100%" stop-color="#B30000"/>
    </linearGradient>
  </defs>
  <!-- Monogram RB Emblem -->
  <rect x="5" y="10" width="60" height="60" rx="12" fill="#151515" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
  <path d="M 22 25 L 36 25 C 43 25 47 28 47 33 C 47 37 44 39 40 40 C 45 41 49 44 49 49 C 49 55 44 57 37 57 L 22 57 Z M 30 31 L 30 38 L 35 38 C 39 38 41 36 41 34.5 C 41 32.5 39 31 35 31 Z M 30 44 L 30 51 L 36 51 C 41 51 43 49 43 47 C 43 45 41 44 36 44 Z" fill="#F5F5F5"/>
  <circle cx="55" cy="58" r="4" fill="#FF2B2B"/>
  <!-- Brand text -->
  <text x="82" y="47" font-family="'Space Grotesk', 'Inter', -apple-system, sans-serif" font-size="28" font-weight="800" fill="#F5F5F5" letter-spacing="1">RADHIKA<tspan fill="#FF2B2B">.</tspan></text>
  <text x="83" y="62" font-family="'Inter', sans-serif" font-size="9" font-weight="600" fill="#A3A3A3" letter-spacing="3.5">TECH • MARKETING • CREATIVE</text>
</svg>'''

with open('/tmp/assets_gen/radhika-logo.svg', 'w') as f:
    f.write(logo_svg)

# 2. Profile Photo Placeholder SVG (high-res 800x1000)
profile_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 1000" width="800" height="1000">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141414"/>
      <stop offset="50%" stop-color="#090909"/>
      <stop offset="100%" stop-color="#180a0a"/>
    </linearGradient>
    <radialGradient id="redGlow" cx="50%" cy="40%" r="50%">
      <stop offset="0%" stop-color="#FF2B2B" stop-opacity="0.35"/>
      <stop offset="70%" stop-color="#FF2B2B" stop-opacity="0.0"/>
    </radialGradient>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255,255,255,0.03)" stroke-width="1"/>
    </pattern>
  </defs>
  
  <rect width="800" height="1000" fill="url(#bgGrad)"/>
  <rect width="800" height="1000" fill="url(#grid)"/>
  <circle cx="400" cy="420" r="320" fill="url(#redGlow)"/>

  <!-- Border & Crosshairs -->
  <rect x="25" y="25" width="750" height="950" rx="20" fill="none" stroke="rgba(255,43,43,0.3)" stroke-width="1.5"/>
  <circle cx="25" cy="25" r="4" fill="#FF2B2B"/>
  <circle cx="775" cy="25" r="4" fill="#FF2B2B"/>
  <circle cx="25" cy="975" r="4" fill="#FF2B2B"/>
  <circle cx="775" cy="975" r="4" fill="#FF2B2B"/>

  <!-- Avatar Silhouette Silhouette Graphic -->
  <g transform="translate(400, 420)">
    <!-- Aura Ring -->
    <circle cx="0" cy="0" r="180" fill="none" stroke="rgba(255,43,43,0.25)" stroke-width="2" stroke-dasharray="8 6"/>
    <!-- Head -->
    <circle cx="0" cy="-60" r="85" fill="#1C1C1C" stroke="#FF2B2B" stroke-width="2"/>
    <!-- Sleek Minimalist Face Contour -->
    <path d="M -50 -50 Q 0 -10 50 -50" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="2"/>
    <!-- Torso -->
    <path d="M -130 150 C -120 40 -80 15 -30 15 L 30 15 C 80 15 120 40 130 150 Z" fill="#181818" stroke="rgba(255,255,255,0.15)" stroke-width="1.5"/>
  </g>

  <!-- Tag Pill -->
  <rect x="280" y="670" width="240" height="38" rx="19" fill="#151515" stroke="rgba(255,43,43,0.5)" stroke-width="1.5"/>
  <text x="400" y="694" font-family="'Space Grotesk', sans-serif" font-size="13" font-weight="700" fill="#FF2B2B" text-anchor="middle" letter-spacing="2">RADHIKA BAROT</text>

  <!-- Meta details -->
  <text x="400" y="745" font-family="'Space Grotesk', sans-serif" font-size="28" font-weight="800" fill="#F5F5F5" text-anchor="middle" letter-spacing="1">RADHIKA BAROT</text>
  <text x="400" y="780" font-family="'Inter', sans-serif" font-size="14" font-weight="600" fill="#A3A3A3" text-anchor="middle" letter-spacing="3">CODER • DIGITAL MARKETER • VIDEO EDITOR</text>
  
  <rect x="200" y="830" width="400" height="60" rx="12" fill="rgba(255,43,43,0.08)" stroke="rgba(255,43,43,0.3)" stroke-width="1"/>
  <text x="400" y="855" font-family="'Inter', sans-serif" font-size="12" font-weight="600" fill="#F5F5F5" text-anchor="middle">REPLACE WITH YOUR PHOTO IN</text>
  <text x="400" y="875" font-family="'Space Grotesk', monospace" font-size="13" font-weight="700" fill="#FF2B2B" text-anchor="middle">assets/images/radhika-profile.jpg</text>
</svg>'''

with open('/tmp/assets_gen/radhika-profile.svg', 'w') as f:
    f.write(profile_svg)

# 3. Project 01: E-Commerce
p1_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="1200" height="800">
  <defs>
    <linearGradient id="p1bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0E0E0E"/>
      <stop offset="100%" stop-color="#190F0F"/>
    </linearGradient>
    <radialGradient id="p1glow" cx="80%" cy="20%" r="60%">
      <stop offset="0%" stop-color="#FF2B2B" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="1200" height="800" fill="url(#p1bg)"/>
  <rect width="1200" height="800" fill="url(#p1glow)"/>

  <!-- Browser Frame -->
  <rect x="60" y="60" width="1080" height="680" rx="18" fill="#121212" stroke="rgba(255,255,255,0.1)" stroke-width="1.5"/>
  <!-- Browser Header -->
  <rect x="60" y="60" width="1080" height="50" rx="18" fill="#181818"/>
  <circle cx="95" cy="85" r="6" fill="#FF5F56"/>
  <circle cx="115" cy="85" r="6" fill="#FFBD2E"/>
  <circle cx="135" cy="85" r="6" fill="#27C93F"/>
  <rect x="340" y="72" width="520" height="26" rx="6" fill="#222" stroke="rgba(255,255,255,0.06)"/>
  <text x="600" y="89" font-family="'Space Grotesk', sans-serif" font-size="11" fill="#A3A3A3" text-anchor="middle">store.radhikabarot.preview / shop / premium-collection</text>

  <!-- Content Layout -->
  <!-- Hero banner inside mockup -->
  <rect x="100" y="140" width="1000" height="240" rx="12" fill="#171717" stroke="rgba(255,43,43,0.2)"/>
  <text x="140" y="210" font-family="'Space Grotesk', sans-serif" font-size="34" font-weight="800" fill="#F5F5F5">MINIMALIST APPAREL &amp; TECH</text>
  <text x="140" y="250" font-family="'Inter', sans-serif" font-size="16" fill="#A3A3A3">Responsive front-end shopping layout with sleek product filtering</text>
  <rect x="140" y="280" width="160" height="44" rx="8" fill="#FF2B2B"/>
  <text x="220" y="307" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" fill="#FFFFFF" text-anchor="middle">EXPLORE NOW ↗</text>

  <!-- Product Cards Grid -->
  <g transform="translate(100, 410)">
    <!-- Card 1 -->
    <rect x="0" y="0" width="310" height="290" rx="12" fill="#161616" stroke="rgba(255,255,255,0.08)"/>
    <rect x="20" y="20" width="270" height="150" rx="8" fill="#202020"/>
    <circle cx="155" cy="95" r="45" fill="#292929" stroke="#FF2B2B" stroke-width="1.5"/>
    <text x="20" y="205" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="700" fill="#F5F5F5">Cyber Hoodie Matte</text>
    <text x="20" y="230" font-family="'Inter', sans-serif" font-size="13" fill="#A3A3A3">Pure Cotton • Edition 01</text>
    <text x="20" y="260" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="800" fill="#FF2B2B">$89.00</text>
    <rect x="220" y="240" width="70" height="30" rx="6" fill="#262626"/>
    <text x="255" y="260" font-family="'Inter', sans-serif" font-size="11" font-weight="600" fill="#FFF" text-anchor="middle">ADD +</text>

    <!-- Card 2 -->
    <rect x="345" y="0" width="310" height="290" rx="12" fill="#161616" stroke="rgba(255,43,43,0.3)"/>
    <rect x="365" y="20" width="270" height="150" rx="8" fill="#202020"/>
    <rect x="440" y="55" width="120" height="80" rx="8" fill="#292929" stroke="rgba(255,255,255,0.1)"/>
    <text x="365" y="205" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="700" fill="#F5F5F5">Ergonomic Desk Mat</text>
    <text x="365" y="230" font-family="'Inter', sans-serif" font-size="13" fill="#A3A3A3">Waterproof Microfiber</text>
    <text x="365" y="260" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="800" fill="#FF2B2B">$45.00</text>
    <rect x="565" y="240" width="70" height="30" rx="6" fill="#FF2B2B"/>
    <text x="600" y="260" font-family="'Inter', sans-serif" font-size="11" font-weight="600" fill="#FFF" text-anchor="middle">ADD +</text>

    <!-- Card 3 -->
    <rect x="690" y="0" width="310" height="290" rx="12" fill="#161616" stroke="rgba(255,255,255,0.08)"/>
    <rect x="710" y="20" width="270" height="150" rx="8" fill="#202020"/>
    <polygon points="845,60 885,130 805,130" fill="#292929" stroke="#FF2B2B" stroke-width="1.5"/>
    <text x="710" y="205" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="700" fill="#F5F5F5">Mechanical Keycap Set</text>
    <text x="710" y="230" font-family="'Inter', sans-serif" font-size="13" fill="#A3A3A3">PBT Dye-Sub Crimson</text>
    <text x="710" y="260" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="800" fill="#FF2B2B">$65.00</text>
    <rect x="910" y="240" width="70" height="30" rx="6" fill="#262626"/>
    <text x="945" y="260" font-family="'Inter', sans-serif" font-size="11" font-weight="600" fill="#FFF" text-anchor="middle">ADD +</text>
  </g>
</svg>'''

with open('/tmp/assets_gen/project-ecommerce.svg', 'w') as f:
    f.write(p1_svg)

# 4. Project 02: Airline Booking
p2_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="1200" height="800">
  <defs>
    <linearGradient id="p2bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#080B12"/>
      <stop offset="100%" stop-color="#140909"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="800" fill="url(#p2bg)"/>

  <!-- Browser Frame -->
  <rect x="60" y="60" width="1080" height="680" rx="18" fill="#101319" stroke="rgba(255,255,255,0.1)" stroke-width="1.5"/>
  <rect x="60" y="60" width="1080" height="50" rx="18" fill="#151922"/>
  <circle cx="95" cy="85" r="6" fill="#FF5F56"/>
  <circle cx="115" cy="85" r="6" fill="#FFBD2E"/>
  <circle cx="135" cy="85" r="6" fill="#27C93F"/>
  <text x="600" y="89" font-family="'Space Grotesk', sans-serif" font-size="11" fill="#A3A3A3" text-anchor="middle">flyhorizon.portal / booking-engine / routes</text>

  <!-- Flight Search Banner -->
  <rect x="100" y="140" width="1000" height="150" rx="14" fill="#161B26" stroke="rgba(255,43,43,0.3)"/>
  <text x="140" y="180" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" fill="#FF2B2B" letter-spacing="2">AIRLINE RESERVATION SYSTEM</text>
  
  <rect x="140" y="205" width="220" height="55" rx="8" fill="#202636"/>
  <text x="160" y="228" font-family="'Inter', sans-serif" font-size="11" fill="#8892B0">ORIGIN</text>
  <text x="160" y="248" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="700" fill="#FFF">BOM • MUMBAI</text>

  <circle cx="390" cy="232" r="18" fill="#FF2B2B"/>
  <path d="M 383 232 L 397 232 M 392 227 L 397 232 L 392 237" stroke="#FFF" stroke-width="2" fill="none"/>

  <rect x="420" y="205" width="220" height="55" rx="8" fill="#202636"/>
  <text x="440" y="228" font-family="'Inter', sans-serif" font-size="11" fill="#8892B0">DESTINATION</text>
  <text x="440" y="248" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="700" fill="#FFF">DXB • DUBAI</text>

  <rect x="670" y="205" width="180" height="55" rx="8" fill="#202636"/>
  <text x="690" y="228" font-family="'Inter', sans-serif" font-size="11" fill="#8892B0">TRAVEL DATE</text>
  <text x="690" y="248" font-family="'Space Grotesk', sans-serif" font-size="15" font-weight="700" fill="#FFF">28 OCT 2026</text>

  <rect x="880" y="205" width="180" height="55" rx="8" fill="#FF2B2B"/>
  <text x="970" y="238" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" fill="#FFF" text-anchor="middle">SEARCH FLIGHTS ↗</text>

  <!-- Flight Result Cards -->
  <g transform="translate(100, 320)">
    <!-- Flight Card 1 -->
    <rect x="0" y="0" width="1000" height="120" rx="12" fill="#141822" stroke="rgba(255,255,255,0.08)"/>
    <text x="40" y="45" font-family="'Space Grotesk', sans-serif" font-size="20" font-weight="800" fill="#FFF">AIR HORIZON</text>
    <text x="40" y="70" font-family="'Inter', sans-serif" font-size="12" fill="#8892B0">Flight HZ-842 • Boeing 787-9</text>
    <rect x="40" y="82" width="70" height="22" rx="4" fill="#222A3A"/>
    <text x="75" y="97" font-family="'Space Grotesk', sans-serif" font-size="10" font-weight="700" fill="#FF2B2B" text-anchor="middle">NON-STOP</text>

    <text x="320" y="55" font-family="'Space Grotesk', sans-serif" font-size="24" font-weight="800" fill="#FFF">06:40</text>
    <text x="320" y="75" font-family="'Inter', sans-serif" font-size="12" fill="#8892B0">BOM</text>

    <!-- Path -->
    <line x1="420" y1="58" x2="580" y2="58" stroke="rgba(255,43,43,0.6)" stroke-width="2" stroke-dasharray="6 4"/>
    <circle cx="500" cy="58" r="10" fill="#FF2B2B"/>
    <text x="500" y="45" font-family="'Inter', sans-serif" font-size="11" fill="#A3A3A3" text-anchor="middle">3h 30m</text>

    <text x="630" y="55" font-family="'Space Grotesk', sans-serif" font-size="24" font-weight="800" fill="#FFF">10:10</text>
    <text x="630" y="75" font-family="'Inter', sans-serif" font-size="12" fill="#8892B0">DXB</text>

    <text x="820" y="55" font-family="'Space Grotesk', sans-serif" font-size="24" font-weight="800" fill="#FF2B2B">$340</text>
    <rect x="800" y="70" width="160" height="36" rx="6" fill="#FF2B2B"/>
    <text x="880" y="93" font-family="'Space Grotesk', sans-serif" font-size="12" font-weight="700" fill="#FFF" text-anchor="middle">RESERVE SEAT ↗</text>

    <!-- Flight Card 2 -->
    <rect x="0" y="145" width="1000" height="120" rx="12" fill="#141822" stroke="rgba(255,255,255,0.08)"/>
    <text x="40" y="190" font-family="'Space Grotesk', sans-serif" font-size="20" font-weight="800" fill="#FFF">EMIRATES CONNECT</text>
    <text x="40" y="215" font-family="'Inter', sans-serif" font-size="12" fill="#8892B0">Flight EC-209 • Airbus A350</text>
    
    <text x="320" y="200" font-family="'Space Grotesk', sans-serif" font-size="24" font-weight="800" fill="#FFF">14:15</text>
    <text x="320" y="220" font-family="'Inter', sans-serif" font-size="12" fill="#8892B0">BOM</text>

    <line x1="420" y1="203" x2="580" y2="203" stroke="rgba(255,43,43,0.6)" stroke-width="2" stroke-dasharray="6 4"/>
    <circle cx="500" cy="203" r="10" fill="#FF2B2B"/>
    <text x="500" y="190" font-family="'Inter', sans-serif" font-size="11" fill="#A3A3A3" text-anchor="middle">3h 40m</text>

    <text x="630" y="200" font-family="'Space Grotesk', sans-serif" font-size="24" font-weight="800" fill="#FFF">17:55</text>
    <text x="630" y="220" font-family="'Inter', sans-serif" font-size="12" fill="#8892B0">DXB</text>

    <text x="820" y="200" font-family="'Space Grotesk', sans-serif" font-size="24" font-weight="800" fill="#FF2B2B">$385</text>
    <rect x="800" y="215" width="160" height="36" rx="6" fill="#222A3A" stroke="rgba(255,255,255,0.1)"/>
    <text x="880" y="238" font-family="'Space Grotesk', sans-serif" font-size="12" font-weight="700" fill="#FFF" text-anchor="middle">RESERVE SEAT ↗</text>
  </g>
</svg>'''

with open('/tmp/assets_gen/project-airline.svg', 'w') as f:
    f.write(p2_svg)

# 5. Project 03: Gym Management
p3_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="1200" height="800">
  <defs>
    <linearGradient id="p3bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0D0D0E"/>
      <stop offset="100%" stop-color="#190A0A"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="800" fill="url(#p3bg)"/>

  <!-- Browser Frame -->
  <rect x="60" y="60" width="1080" height="680" rx="18" fill="#131315" stroke="rgba(255,255,255,0.1)" stroke-width="1.5"/>
  <rect x="60" y="60" width="1080" height="50" rx="18" fill="#1A1A1D"/>
  <circle cx="95" cy="85" r="6" fill="#FF5F56"/>
  <circle cx="115" cy="85" r="6" fill="#FFBD2E"/>
  <circle cx="135" cy="85" r="6" fill="#27C93F"/>
  <text x="600" y="89" font-family="'Space Grotesk', sans-serif" font-size="11" fill="#A3A3A3" text-anchor="middle">apexfitness.crm / admin / dashboard / operations</text>

  <!-- Sidebar -->
  <rect x="60" y="110" width="220" height="630" fill="#111113"/>
  <text x="90" y="160" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="800" fill="#FF2B2B">APEX GYM</text>
  <rect x="80" y="190" width="180" height="40" rx="8" fill="#FF2B2B"/>
  <text x="100" y="215" font-family="'Inter', sans-serif" font-size="13" font-weight="600" fill="#FFF">Dashboard</text>
  <text x="100" y="260" font-family="'Inter', sans-serif" font-size="13" fill="#888">Members Roster</text>
  <text x="100" y="300" font-family="'Inter', sans-serif" font-size="13" fill="#888">Subscriptions</text>
  <text x="100" y="340" font-family="'Inter', sans-serif" font-size="13" fill="#888">Trainer Schedule</text>
  <text x="100" y="380" font-family="'Inter', sans-serif" font-size="13" fill="#888">Access Control</text>

  <!-- Main Dashboard Content -->
  <!-- Stat Tiles -->
  <g transform="translate(310, 140)">
    <rect x="0" y="0" width="230" height="110" rx="10" fill="#18181C" stroke="rgba(255,43,43,0.3)"/>
    <text x="25" y="35" font-family="'Inter', sans-serif" font-size="12" fill="#A3A3A3">ACTIVE MEMBERS</text>
    <text x="25" y="75" font-family="'Space Grotesk', sans-serif" font-size="30" font-weight="800" fill="#FFF">842</text>
    <text x="25" y="95" font-family="'Inter', sans-serif" font-size="11" fill="#27C93F">✓ Fully Synced</text>

    <rect x="260" y="0" width="230" height="110" rx="10" fill="#18181C" stroke="rgba(255,255,255,0.08)"/>
    <text x="285" y="35" font-family="'Inter', sans-serif" font-size="12" fill="#A3A3A3">DAILY CHECK-INS</text>
    <text x="285" y="75" font-family="'Space Grotesk', sans-serif" font-size="30" font-weight="800" fill="#FF2B2B">194</text>
    <text x="285" y="95" font-family="'Inter', sans-serif" font-size="11" fill="#A3A3A3">Peak hours: 6-9 PM</text>

    <rect x="520" y="0" width="230" height="110" rx="10" fill="#18181C" stroke="rgba(255,255,255,0.08)"/>
    <text x="545" y="35" font-family="'Inter', sans-serif" font-size="12" fill="#A3A3A3">TRAINER SESSIONS</text>
    <text x="545" y="75" font-family="'Space Grotesk', sans-serif" font-size="30" font-weight="800" fill="#FFF">38</text>
    <text x="545" y="95" font-family="'Inter', sans-serif" font-size="11" fill="#FF2B2B">12 scheduled today</text>
  </g>

  <!-- Member Table preview -->
  <g transform="translate(310, 280)">
    <rect x="0" y="0" width="750" height="410" rx="12" fill="#16161A" stroke="rgba(255,255,255,0.06)"/>
    <text x="30" y="40" font-family="'Space Grotesk', sans-serif" font-size="18" font-weight="800" fill="#FFF">Recent Member Check-ins</text>
    
    <!-- Table Header -->
    <rect x="20" y="60" width="710" height="35" rx="6" fill="#1D1D22"/>
    <text x="40" y="82" font-family="'Inter', sans-serif" font-size="12" font-weight="600" fill="#A3A3A3">MEMBER NAME</text>
    <text x="260" y="82" font-family="'Inter', sans-serif" font-size="12" font-weight="600" fill="#A3A3A3">PLAN</text>
    <text x="440" y="82" font-family="'Inter', sans-serif" font-size="12" font-weight="600" fill="#A3A3A3">STATUS</text>
    <text x="610" y="82" font-family="'Inter', sans-serif" font-size="12" font-weight="600" fill="#A3A3A3">CHECK-IN</text>

    <!-- Row 1 -->
    <text x="40" y="130" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" fill="#FFF">Alex Martinez</text>
    <text x="260" y="130" font-family="'Inter', sans-serif" font-size="13" fill="#A3A3A3">Annual VIP Pro</text>
    <rect x="440" y="113" width="75" height="24" rx="4" fill="rgba(39,201,63,0.15)"/>
    <text x="477" y="129" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#27C93F" text-anchor="middle">ACTIVE</text>
    <text x="610" y="130" font-family="'Inter', sans-serif" font-size="13" fill="#A3A3A3">10:42 AM</text>
    <line x1="20" y1="155" x2="730" y2="155" stroke="rgba(255,255,255,0.05)"/>

    <!-- Row 2 -->
    <text x="40" y="195" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" fill="#FFF">Sophia Vance</text>
    <text x="260" y="195" font-family="'Inter', sans-serif" font-size="13" fill="#A3A3A3">Quarterly Access</text>
    <rect x="440" y="178" width="75" height="24" rx="4" fill="rgba(39,201,63,0.15)"/>
    <text x="477" y="194" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#27C93F" text-anchor="middle">ACTIVE</text>
    <text x="610" y="195" font-family="'Inter', sans-serif" font-size="13" fill="#A3A3A3">10:15 AM</text>
    <line x1="20" y1="220" x2="730" y2="220" stroke="rgba(255,255,255,0.05)"/>

    <!-- Row 3 -->
    <text x="40" y="260" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" fill="#FFF">David Chen</text>
    <text x="260" y="260" font-family="'Inter', sans-serif" font-size="13" fill="#A3A3A3">Monthly Starter</text>
    <rect x="440" y="243" width="90" height="24" rx="4" fill="rgba(255,43,43,0.15)"/>
    <text x="485" y="259" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#FF2B2B" text-anchor="middle">RENEWAL DUE</text>
    <text x="610" y="260" font-family="'Inter', sans-serif" font-size="13" fill="#A3A3A3">09:50 AM</text>
  </g>
</svg>'''

with open('/tmp/assets_gen/project-gym.svg', 'w') as f:
    f.write(p3_svg)

# 6. Project 04: Social Media Auto Posting
p4_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="1200" height="800">
  <defs>
    <linearGradient id="p4bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#090B10"/>
      <stop offset="100%" stop-color="#1A0D0D"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="800" fill="url(#p4bg)"/>

  <!-- Browser Frame -->
  <rect x="60" y="60" width="1080" height="680" rx="18" fill="#12141A" stroke="rgba(255,255,255,0.1)" stroke-width="1.5"/>
  <rect x="60" y="60" width="1080" height="50" rx="18" fill="#171A22"/>
  <circle cx="95" cy="85" r="6" fill="#FF5F56"/>
  <circle cx="115" cy="85" r="6" fill="#FFBD2E"/>
  <circle cx="135" cy="85" r="6" fill="#27C93F"/>
  <text x="600" y="89" font-family="'Space Grotesk', sans-serif" font-size="11" fill="#A3A3A3" text-anchor="middle">socialhub.automation / pipeline / publisher / scheduler</text>

  <!-- Flow Visualizer -->
  <g transform="translate(100, 140)">
    <!-- Header -->
    <text x="0" y="30" font-family="'Space Grotesk', sans-serif" font-size="22" font-weight="800" fill="#FFF">AUTOMATED PUBLISHING PIPELINE</text>
    <text x="0" y="55" font-family="'Inter', sans-serif" font-size="13" fill="#A3A3A3">Django REST API + Webhook Queue + Multi-Channel Dispatcher</text>

    <!-- Source Node -->
    <rect x="0" y="100" width="260" height="180" rx="12" fill="#181B24" stroke="rgba(255,43,43,0.3)"/>
    <circle cx="35" cy="135" r="14" fill="#FF2B2B"/>
    <text x="65" y="140" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="700" fill="#FFF">Content Ingestion</text>
    <text x="25" y="180" font-family="'Inter', sans-serif" font-size="12" fill="#A3A3A3">• Markdown parser</text>
    <text x="25" y="205" font-family="'Inter', sans-serif" font-size="12" fill="#A3A3A3">• Media asset compressor</text>
    <text x="25" y="230" font-family="'Inter', sans-serif" font-size="12" fill="#A3A3A3">• Metadata validator</text>
    <rect x="25" y="245" width="90" height="22" rx="4" fill="rgba(39,201,63,0.15)"/>
    <text x="70" y="260" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#27C93F" text-anchor="middle">QUEUE OK</text>

    <!-- Connecting Arrow 1 -->
    <line x1="260" y1="190" x2="360" y2="190" stroke="#FF2B2B" stroke-width="2" stroke-dasharray="6 4"/>
    <polygon points="360,190 350,185 350,195" fill="#FF2B2B"/>

    <!-- Processing Node -->
    <rect x="360" y="100" width="280" height="180" rx="12" fill="#181B24" stroke="rgba(255,255,255,0.1)"/>
    <circle cx="395" cy="135" r="14" fill="#222"/>
    <text x="425" y="140" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="700" fill="#FFF">Django Scheduler</text>
    <text x="385" y="180" font-family="'Inter', sans-serif" font-size="12" fill="#A3A3A3">• Celery + Redis beat</text>
    <text x="385" y="205" font-family="'Inter', sans-serif" font-size="12" fill="#A3A3A3">• Timezone synchronizer</text>
    <text x="385" y="230" font-family="'Inter', sans-serif" font-size="12" fill="#A3A3A3">• Rate limit governor</text>
    <rect x="385" y="245" width="100" height="22" rx="4" fill="rgba(255,43,43,0.15)"/>
    <text x="435" y="260" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#FF2B2B" text-anchor="middle">SYNC ACTIVE</text>

    <!-- Connecting Arrow 2 -->
    <line x1="640" y1="190" x2="740" y2="190" stroke="#FF2B2B" stroke-width="2" stroke-dasharray="6 4"/>
    <polygon points="740,190 730,185 730,195" fill="#FF2B2B"/>

    <!-- Target Dispatcher -->
    <rect x="740" y="100" width="260" height="180" rx="12" fill="#181B24" stroke="rgba(255,43,43,0.3)"/>
    <circle cx="775" cy="135" r="14" fill="#FF2B2B"/>
    <text x="805" y="140" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="700" fill="#FFF">API Dispatcher</text>
    <text x="765" y="180" font-family="'Inter', sans-serif" font-size="12" fill="#A3A3A3">• Meta Graph API</text>
    <text x="765" y="205" font-family="'Inter', sans-serif" font-size="12" fill="#A3A3A3">• LinkedIn API</text>
    <text x="765" y="230" font-family="'Inter', sans-serif" font-size="12" fill="#A3A3A3">• X / Twitter API v2</text>
    <rect x="765" y="245" width="100" height="22" rx="4" fill="rgba(39,201,63,0.15)"/>
    <text x="815" y="260" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#27C93F" text-anchor="middle">CONNECTED</text>

    <!-- Schedule log table -->
    <rect x="0" y="320" width="1000" height="220" rx="12" fill="#15171F" stroke="rgba(255,255,255,0.06)"/>
    <text x="25" y="355" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="700" fill="#FFF">Scheduled Queue Logs</text>

    <rect x="25" y="375" width="950" height="40" rx="6" fill="#1A1E29"/>
    <text x="45" y="400" font-family="'Inter', sans-serif" font-size="12" fill="#A3A3A3">POST: "Weekly Product Launch Recap" → Meta Page, LinkedIn</text>
    <text x="750" y="400" font-family="'Space Grotesk', sans-serif" font-size="12" fill="#FF2B2B">TODAY, 18:00</text>
    <rect x="860" y="383" width="95" height="24" rx="4" fill="rgba(39,201,63,0.15)"/>
    <text x="907" y="399" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#27C93F" text-anchor="middle">DISPATCHED</text>

    <rect x="25" y="430" width="950" height="40" rx="6" fill="#1A1E29"/>
    <text x="45" y="455" font-family="'Inter', sans-serif" font-size="12" fill="#A3A3A3">POST: "Marketing Trends Infographic Q4" → Instagram Graph</text>
    <text x="750" y="455" font-family="'Space Grotesk', sans-serif" font-size="12" fill="#FF2B2B">TOMORROW, 10:30</text>
    <rect x="860" y="438" width="95" height="24" rx="4" fill="rgba(255,189,46,0.15)"/>
    <text x="907" y="454" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#FFBD2E" text-anchor="middle">QUEUED</text>
  </g>
</svg>'''

with open('/tmp/assets_gen/project-socialhub.svg', 'w') as f:
    f.write(p4_svg)

# 7. Project 05: Aicruit
p5_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="1200" height="800">
  <defs>
    <linearGradient id="p5bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#08080C"/>
      <stop offset="100%" stop-color="#1B0909"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="800" fill="url(#p5bg)"/>

  <!-- Phone Frame & App Mockup -->
  <!-- Left Side: Conceptual Architecture & Radar -->
  <g transform="translate(100, 100)">
    <text x="0" y="50" font-family="'Space Grotesk', sans-serif" font-size="36" font-weight="800" fill="#FFF">AICRUIT</text>
    <text x="0" y="85" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" fill="#FF2B2B" letter-spacing="2">AI JOB MATCHING &amp; RESUME EXTRACTOR</text>
    <text x="0" y="125" font-family="'Inter', sans-serif" font-size="15" fill="#A3A3A3">Kotlin Android client backed by Firebase &amp; AI-driven candidate match score.</text>

    <!-- Radar / Match Graphic -->
    <rect x="0" y="170" width="480" height="420" rx="14" fill="#141418" stroke="rgba(255,43,43,0.3)"/>
    <text x="30" y="210" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="700" fill="#FFF">Candidate Skill Compatibility</text>
    
    <circle cx="240" cy="380" r="140" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
    <circle cx="240" cy="380" r="90" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
    <circle cx="240" cy="380" r="40" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

    <!-- Radar Polygon -->
    <polygon points="240,260 350,330 320,460 160,450 140,320" fill="rgba(255,43,43,0.25)" stroke="#FF2B2B" stroke-width="2"/>
    <circle cx="240" cy="260" r="5" fill="#FF2B2B"/>
    <circle cx="350" cy="330" r="5" fill="#FF2B2B"/>
    <circle cx="320" cy="460" r="5" fill="#FF2B2B"/>
    <circle cx="160" cy="450" r="5" fill="#FF2B2B"/>
    <circle cx="140" cy="320" r="5" fill="#FF2B2B"/>

    <text x="240" y="245" font-family="'Inter', sans-serif" font-size="11" fill="#FFF" text-anchor="middle">Python/ML (95%)</text>
    <text x="370" y="335" font-family="'Inter', sans-serif" font-size="11" fill="#FFF">Systems (82%)</text>
    <text x="340" y="480" font-family="'Inter', sans-serif" font-size="11" fill="#FFF">DevOps (75%)</text>
    <text x="140" y="470" font-family="'Inter', sans-serif" font-size="11" fill="#FFF">APIs (88%)</text>
    <text x="110" y="315" font-family="'Inter', sans-serif" font-size="11" fill="#FFF">Frontend (78%)</text>
  </g>

  <!-- Right Side: Android Phone Frame -->
  <g transform="translate(680, 80)">
    <rect x="0" y="0" width="380" height="660" rx="36" fill="#121215" stroke="rgba(255,255,255,0.15)" stroke-width="3"/>
    <!-- Speaker notch -->
    <rect x="130" y="15" width="120" height="20" rx="10" fill="#090909"/>
    <circle cx="230" cy="25" r="4" fill="#222"/>

    <!-- Screen Content -->
    <g transform="translate(20, 50)">
      <text x="20" y="35" font-family="'Space Grotesk', sans-serif" font-size="18" font-weight="800" fill="#FFF">Job Discovery</text>
      <circle cx="300" cy="28" r="16" fill="#202020"/>
      <text x="300" y="33" font-family="'Inter', sans-serif" font-size="12" fill="#FF2B2B" text-anchor="middle">98%</text>

      <!-- Match Card -->
      <rect x="10" y="60" width="320" height="240" rx="16" fill="#1B1B22" stroke="rgba(255,43,43,0.35)"/>
      <rect x="25" y="75" width="60" height="60" rx="10" fill="#FF2B2B"/>
      <text x="55" y="112" font-family="'Space Grotesk', sans-serif" font-size="20" font-weight="800" fill="#FFF" text-anchor="middle">AI</text>

      <text x="100" y="95" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="700" fill="#FFF">Sr. Full-Stack Dev</text>
      <text x="100" y="118" font-family="'Inter', sans-serif" font-size="12" fill="#A3A3A3">Remote • Global AI Labs</text>

      <rect x="25" y="150" width="100" height="26" rx="6" fill="#272733"/>
      <text x="75" y="167" font-family="'Inter', sans-serif" font-size="11" fill="#FFF" text-anchor="middle">Kotlin / Python</text>

      <rect x="135" y="150" width="80" height="26" rx="6" fill="#272733"/>
      <text x="175" y="167" font-family="'Inter', sans-serif" font-size="11" fill="#FFF" text-anchor="middle">FastAPI</text>

      <text x="25" y="215" font-family="'Inter', sans-serif" font-size="12" fill="#A3A3A3">Resume Match Score: 94%</text>
      <rect x="25" y="235" width="290" height="42" rx="8" fill="#FF2B2B"/>
      <text x="170" y="261" font-family="'Space Grotesk', sans-serif" font-size="13" font-weight="700" fill="#FFF" text-anchor="middle">APPLY WITH ONE TAP ↗</text>

      <!-- Secondary Card -->
      <rect x="10" y="320" width="320" height="150" rx="16" fill="#1B1B22" stroke="rgba(255,255,255,0.08)"/>
      <text x="25" y="355" font-family="'Space Grotesk', sans-serif" font-size="15" font-weight="700" fill="#FFF">AI Data Engineer</text>
      <text x="25" y="378" font-family="'Inter', sans-serif" font-size="12" fill="#A3A3A3">Hybrid • Cloud Neural Systems</text>
      <rect x="25" y="400" width="290" height="36" rx="8" fill="#272733"/>
      <text x="170" y="423" font-family="'Space Grotesk', sans-serif" font-size="12" font-weight="600" fill="#FFF" text-anchor="middle">VIEW DETAILS</text>
    </g>
  </g>
</svg>'''

with open('/tmp/assets_gen/project-aicruit.svg', 'w') as f:
    f.write(p5_svg)

# 8. Project Placeholder SVG
placeholder_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="1200" height="800">
  <rect width="1200" height="800" fill="#101010"/>
  <rect x="50" y="50" width="1100" height="700" rx="16" fill="#141414" stroke="rgba(255,43,43,0.2)" stroke-width="2"/>
  <circle cx="600" cy="350" r="80" fill="#1B1B1B" stroke="#FF2B2B" stroke-width="2"/>
  <path d="M 580 350 L 620 350 M 600 330 L 600 370" stroke="#FF2B2B" stroke-width="3"/>
  <text x="600" y="490" font-family="'Space Grotesk', sans-serif" font-size="24" font-weight="800" fill="#F5F5F5" text-anchor="middle">PROJECT SHOWCASE MOCKUP</text>
  <text x="600" y="530" font-family="'Inter', sans-serif" font-size="15" fill="#A3A3A3" text-anchor="middle">Designed Visual Representation • Radhika Barot Portfolio</text>
</svg>'''

with open('/tmp/assets_gen/project-placeholder.svg', 'w') as f:
    f.write(placeholder_svg)

print("SVG templates generated successfully!")
