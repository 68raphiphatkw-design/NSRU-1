import sys

path = r'd:\โฟลเดอร์ใหม่ (4)\index.html'

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

insert_segment = """            width: 8px; height: 8px;
            background: #ef4444; border-radius: 50%;
            display: none;
            border: 2px solid white;
            box-shadow: 0 2px 6px rgba(239, 68, 68, 0.4);
        }
        .dark .nav-badge-dot { border-color: #1c1c1e; }
        
        /* --- Dynamic Weather Themes --- */
        .weather-theme-sunny {
            background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 30%, rgba(56, 189, 248, 0.1) 100%) !important;
        }
        .dark .weather-theme-sunny {
            background: linear-gradient(135deg, #321c08 0%, #0a0a09 100%) !important;
        }

        .weather-theme-rainy {
            background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 50%, #b1bb9d 100%) !important;
        }
        .dark .weather-theme-rainy {
            background: linear-gradient(135deg, #082f49 0%, #030712 100%) !important;
        }

        .weather-theme-cloudy {
            background: linear-gradient(135deg, #f1f5f9 0%, #cbd5e1 50%, #e2e8f0 100%) !important;
        }
        .dark .weather-theme-cloudy {
            background: linear-gradient(135deg, #0f172a 0%, #020617 100%) !important;
        }

        /* Particle Overlay Animations */
        .rain-drop {
            position: absolute;
            width: 1.5px;
            height: 15px;
            background: linear-gradient(to bottom, rgba(255,255,255,0), rgba(125,211,252,0.8));
            opacity: 0.8;
            animation: rainFall linear infinite;
        }
        .dark .rain-drop {
            background: linear-gradient(to bottom, rgba(255,255,255,0), rgba(56,189,248,0.5));
        }
        @keyframes rainFall {
            0% { transform: translateY(-20px) rotate(12deg); }
            100% { transform: translateY(100vh) rotate(12deg); }
        }

        .sun-ray {
            position: absolute;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(253,224,71,0.2) 0%, rgba(252,211,77,0) 75%);
            animation: floatGlow 8s ease-in-out infinite alternate;
        }
        @keyframes floatGlow {
            0% { transform: translate(0, 0) scale(1); opacity: 0.4; }
            100% { transform: translate(50px, -30px) scale(1.3); opacity: 0.7; }
        }

        body.modal-open { overflow: hidden; }
        html { visibility: hidden; }
        html.loaded { visibility: visible; }

        /* --- AI Modern Overhaul --- */
        .ai-window-expanded {
            width: calc(100vw - 40px) !important;
            height: calc(100vh - 120px) !important;
            max-width: 600px !important;
            bottom: 100px !important;
        }
        @media (max-width: 768px) {
            .ai-window-expanded {
                width: 100dvw !important;
                height: 100dvh !important;
                bottom: 0 !important;
                right: 0 !important;
                border-radius: 0 !important;
                max-width: none !important;
            }
        }
        .ai-glow-bg {
            background: radial-gradient(circle at 70% 30%, rgba(151, 8, 204, 0.08), transparent 50%),
                        radial-gradient(circle at 30% 70%, rgba(67, 203, 255, 0.08), transparent 50%);
        }
        .ai-bubble-user {
            background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.15), inset 0 1px 0 rgba(255, 255, 255, 0.2);
            color: white;
            border-bottom-right-radius: 4px;
        }
        .ai-bubble-bot {
            background: rgba(255, 255, 255, 0.9);\n"""

with open(path, 'w', encoding='utf-8') as f:
    for i, line in enumerate(lines):
        if i == 318: # index of 'background: rgba(255, 255, 255, 0.9);'
            f.write(insert_segment)
        f.write(line)

print("Insertion success!")
