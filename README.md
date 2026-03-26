<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>Santosh Adhikari | 9D Cyber Nexus</title>
    <!-- Google Fonts & Font Awesome -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Fira+Code:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <!-- Three.js Core -->
    <script type="importmap">
        {
            "imports": {
                "three": "https://unpkg.com/three@0.128.0/build/three.module.js"
            }
        }
    </script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background-color: #010101;
            font-family: 'Inter', 'Fira Code', monospace;
            overflow-x: hidden;
            color: #e0e0e0;
            scroll-behavior: smooth;
        }

        /* 9D Glow & Matrix Core */
        .glow-text {
            text-shadow: 0 0 5px #00ff9d, 0 0 10px #00ff9d, 0 0 20px #00ff9d, 0 0 40px #00cc77;
        }

        .neon-border {
            border: 1px solid rgba(0, 255, 157, 0.5);
            box-shadow: 0 0 15px rgba(0, 255, 157, 0.3), inset 0 0 10px rgba(0, 255, 157, 0.2);
            transition: all 0.3s ease;
        }

        .neon-border:hover {
            border-color: #00ff9d;
            box-shadow: 0 0 25px #00ff9d, inset 0 0 15px #00ff9d;
        }

        /* Animated Background Canvas */
        #bg-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -2;
            pointer-events: none;
        }

        .matrix-rain-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            opacity: 0.2;
            pointer-events: none;
            background: repeating-linear-gradient(0deg, #00ff9d20 0px, #00ff9d20 2px, transparent 2px, transparent 6px);
        }

        /* Glassmorphic 9D Cards */
        .glass-card {
            background: rgba(5, 10, 20, 0.55);
            backdrop-filter: blur(12px);
            border-radius: 2rem;
            border: 1px solid rgba(0, 255, 157, 0.4);
            box-shadow: 0 20px 40px rgba(0,0,0,0.4), 0 0 20px rgba(0,255,157,0.2);
            transition: transform 0.4s cubic-bezier(0.2, 0.9, 0.4, 1.1), box-shadow 0.4s;
        }

        .glass-card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 30px 50px rgba(0,0,0,0.5), 0 0 35px #00ff9d;
        }

        /* 3D Flip Container */
        .flip-3d {
            perspective: 1500px;
        }
        .flip-inner {
            transition: transform 0.8s;
            transform-style: preserve-3d;
        }
        .flip-3d:hover .flip-inner {
            transform: rotateY(180deg);
        }
        .flip-front, .flip-back {
            backface-visibility: hidden;
            border-radius: 1.5rem;
        }
        .flip-back {
            transform: rotateY(180deg);
            background: rgba(0,0,0,0.85);
            backdrop-filter: blur(8px);
        }

        /* Animated skill bars */
        .skill-bar {
            background: #0a0f1f;
            border-radius: 1rem;
            overflow: hidden;
        }
        .skill-fill {
            background: linear-gradient(90deg, #00ff9d, #00cc77);
            width: 0%;
            transition: width 1.5s cubic-bezier(0.22, 0.97, 0.36, 1.02);
            box-shadow: 0 0 8px #00ff9d;
        }

        /* Infinite marquee tech icons */
        @keyframes scrollIcons {
            0% { transform: translateX(0); }
            100% { transform: translateX(-50%); }
        }
        .tech-marquee {
            display: flex;
            animation: scrollIcons 20s linear infinite;
            width: max-content;
        }
        .tech-marquee img {
            margin: 0 20px;
            filter: drop-shadow(0 0 6px #00ff9d);
        }

        /* custom scrollbar */
        ::-webkit-scrollbar {
            width: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #0a0f1f;
        }
        ::-webkit-scrollbar-thumb {
            background: #00ff9d;
            border-radius: 10px;
        }
        a {
            text-decoration: none;
            color: inherit;
        }
        .hover-lift {
            transition: all 0.3s ease;
        }
        .hover-lift:hover {
            transform: translateY(-5px);
            filter: drop-shadow(0 0 12px #00ff9d);
        }
    </style>
</head>
<body>

    <!-- 3D Background Canvas (9D Orbital Core) -->
    <canvas id="bg-canvas"></canvas>
    <div class="matrix-rain-bg"></div>

    <!-- Main Container -->
    <div class="container" style="max-width: 1400px; margin: 0 auto; padding: 20px; position: relative; z-index: 2;">
        
        <!-- Header Snake / Matrix Banner (SVG) -->
        <div align="center" style="margin-bottom: 2rem;">
            <img src="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake-dark.svg" width="100%" style="border-radius: 30px; opacity: 0.9;">
        </div>

        <!-- Typing SVG with Hologram Effect -->
        <div align="center" style="margin: 20px 0 20px;">
            <a href="https://git.io/typing-svg">
                <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=800&size=38&duration=2800&pause=600&color=00FF9D&center=true&vCenter=true&width=1100&height=130&lines=%3E+SYSTEM_BOOT_SEQUENCE:9D_ACTIVATED;%3E+USER:SANTOSH_ADHIKARI;%3E+ROOT_ACCESS:GRANTED;%3E+CEO_@_SMAIT_TECHNOLOGY;%3E+CYBER_SHADOW_MODE:ON" alt="9D Matrix Typing" />
            </a>
        </div>

        <!-- Stats Badges Animated -->
        <p align="center">
            <img src="https://komarev.com/ghpvc/?username=codersantoshadhikari&label=⚡PROFILE+VIEWS&color=00ff9d&style=for-the-badge" />
            <img src="https://img.shields.io/badge/🚀_WAKATIME-2500+_HOURS-00ff9d?style=for-the-badge&logo=wakatime" />
            <img src="https://img.shields.io/github/followers/codersantoshadhikari?label=👾_FOLLOWERS&style=for-the-badge&color=00ff9d" />
        </p>

        <!-- Personal Website Hologram Banner -->
        <div align="center" class="glass-card" style="width: fit-content; margin: 20px auto; padding: 12px 25px;">
            <a href="https://santoshadhikari.com.np" target="_blank">
                <i class="fas fa-globe" style="color:#00ff9d; margin-right: 12px;"></i>
                <span style="font-weight: bold; letter-spacing: 1px;">🌐 OFFICIAL NEXUS: SANTOSHADHIKARI.COM.NP</span>
                <i class="fas fa-arrow-right" style="margin-left: 12px;"></i>
            </a>
        </div>

        <!-- Main Title with 3D Rotation effect -->
        <h1 align="center" style="font-size: 4rem; font-weight: 900; margin: 20px 0;">
            <span style="background: linear-gradient(135deg, #00ff9d, #00ccff, #aa00ff); -webkit-background-clip: text; background-clip: text; color: transparent; text-shadow: 0 0 20px #00ff9d;">
                SANTOSH ADHIKARI
            </span>
            <span style="display: inline-block; animation: pulse-glow 2s infinite;">⚡</span>
        </h1>
        <h3 align="center">
            <code style="background: #000000aa; padding: 12px 20px; border-radius: 60px; border: 1px solid #00ff9d; backdrop-filter: blur(8px); font-weight: bold;">
                [ SENIOR ARCHITECT | CEO @ SMAIT | CYBER PHANTOM ]
            </code>
        </h3>

        <!-- 9D Coding Animation Hologram -->
        <div align="center" style="margin: 40px 0;">
            <div class="glass-card" style="display: inline-block; padding: 10px; border-radius: 50px;">
                <img src="https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif" width="520" style="border-radius: 40px; border: 2px solid #00ff9d; box-shadow: 0 0 35px #00ff9d;" alt="Coding Matrix"/>
            </div>
        </div>

        <!-- Bio Glassmorphism System Specs -->
        <div align="center">
            <div class="glass-card" style="padding: 30px; width: 95%; margin: 20px auto;">
                <h2 style="color:#00ff9d;"><i class="fas fa-microchip"></i> SYSTEM OVERRIDE <i class="fas fa-database"></i></h2>
                <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 35px; margin-top: 25px;">
                    <div><i class="fas fa-briefcase"></i> <b>6+ Years</b> Full-Cycle</div>
                    <div><i class="fas fa-rocket"></i> <b>60+</b> Applications</div>
                    <div><i class="fas fa-chart-line"></i> <b>1M+</b> Global Users</div>
                    <div><i class="fas fa-crown"></i> <b>CEO</b> @ SMAIT Technology</div>
                    <div><i class="fas fa-shield-alt"></i> <b>CEH | OSCP</b> Level</div>
                </div>
            </div>
        </div>

        <!-- 9D Stats Dashboard with Hologram Effect -->
        <div align="center" style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin: 40px 0;">
            <div class="glass-card" style="padding: 20px; width: 320px;">
                <img src="https://github-readme-stats.vercel.app/api?username=codersantoshadhikari&show_icons=true&count_private=true&theme=chartreuse-dark&hide_border=true&bg_color=00000000&title_color=00ff9d&icon_color=00ff9d&text_color=fff&border_radius=20" width="100%"/>
            </div>
            <div class="glass-card" style="padding: 20px; width: 320px;">
                <img src="https://github-readme-streak-stats.herokuapp.com/?user=codersantoshadhikari&theme=chartreuse-dark&hide_border=true&background=00000000&stroke=00ff9d&ring=00ff9d&fire=00ff9d&currStreakNum=fff&sideNums=fff&border_radius=20" width="100%"/>
            </div>
            <div class="glass-card" style="padding: 20px; width: 320px;">
                <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=codersantoshadhikari&layout=compact&theme=chartreuse-dark&hide_border=true&bg_color=00000000&title_color=00ff9d&text_color=fff&border_radius=20" width="100%"/>
            </div>
        </div>

        <!-- 3D Trophy Case animated -->
        <div align="center">
            <img src="https://github-profile-trophy.vercel.app/?username=codersantoshadhikari&theme=matrix&no-frame=true&no-bg=true&row=2&column=4&margin-w=15&margin-h=15" width="100%" style="filter: drop-shadow(0 0 12px #00ff9d);"/>
        </div>

        <!-- CORE COMPETENCIES: FLIP 3D Cards (9D Interactive) -->
        <h2 align="center" style="margin: 70px 0 30px;"><span style="background: #00ff9d20; padding: 8px 25px; border-radius: 60px;">⚡ 9D CORE COMPETENCIES ⚡</span></h2>
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 30px;">
            <!-- flip card 1 -->
            <div class="flip-3d" style="width: 250px; height: 280px;">
                <div class="flip-inner relative w-full h-full">
                    <div class="flip-front absolute w-full h-full glass-card flex flex-col items-center justify-center" style="display: flex; flex-direction: column; align-items: center; justify-content: center;">
                        <i class="fas fa-mobile-alt" style="font-size: 55px; color:#00ff9d;"></i>
                        <h3 style="margin-top: 15px;">MOBILE</h3>
                        <p>Flutter • RN • Kotlin</p>
                        <div class="skill-bar w-3/4 mt-2"><div class="skill-fill h-2" style="width: 95%;"></div></div>
                    </div>
                    <div class="flip-back absolute w-full h-full glass-card flex items-center justify-center text-center p-4" style="display: flex; flex-direction: column; align-items: center; justify-content: center;">
                        <p>95% Mastery</p>
                        <p>20+ cross-platform apps</p>
                    </div>
                </div>
            </div>
            <div class="flip-3d" style="width: 250px; height: 280px;">
                <div class="flip-inner relative w-full h-full">
                    <div class="flip-front absolute w-full h-full glass-card flex flex-col items-center justify-center">
                        <i class="fas fa-gamepad" style="font-size: 55px; color:#00ff9d;"></i>
                        <h3>GAME ENGINES</h3>
                        <p>Unity • Unreal • Ludo Logic</p>
                        <div class="skill-bar w-3/4 mt-2"><div class="skill-fill h-2" style="width: 98%;"></div></div>
                    </div>
                    <div class="flip-back absolute w-full h-full glass-card flex items-center justify-center text-center p-4">
                        <p>98% | Ludo Empire: 1M+ DL</p>
                    </div>
                </div>
            </div>
            <div class="flip-3d" style="width: 250px; height: 280px;">
                <div class="flip-inner relative w-full h-full">
                    <div class="flip-front absolute w-full h-full glass-card flex flex-col items-center justify-center">
                        <i class="fas fa-shield-hog" style="font-size: 55px; color:#00ff9d;"></i>
                        <h3>CYBER SECURITY</h3>
                        <p>Kali • Metasploit • CEH</p>
                        <div class="skill-bar w-3/4 mt-2"><div class="skill-fill h-2" style="width: 92%;"></div></div>
                    </div>
                    <div class="flip-back absolute w-full h-full glass-card flex items-center justify-center text-center p-4">
                        <p>Certified Ethical Hacker</p>
                    </div>
                </div>
            </div>
            <div class="flip-3d" style="width: 250px; height: 280px;">
                <div class="flip-inner relative w-full h-full">
                    <div class="flip-front absolute w-full h-full glass-card flex flex-col items-center justify-center">
                        <i class="fas fa-cloud" style="font-size: 55px; color:#00ff9d;"></i>
                        <h3>CLOUD & BACKEND</h3>
                        <p>AWS • Firebase • Node</p>
                        <div class="skill-bar w-3/4 mt-2"><div class="skill-fill h-2" style="width: 90%;"></div></div>
                    </div>
                    <div class="flip-back absolute w-full h-full glass-card flex items-center justify-center text-center p-4">
                        <p>Scalable infra for 1M+ users</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Tech Stack Marquee infinite scroll -->
        <h2 align="center" style="margin: 80px 0 20px;">🔧 9D TECH STACK OVERFLOW 🔧</h2>
        <div class="glass-card" style="overflow: hidden; padding: 20px 0; margin: 20px 0;">
            <div class="tech-marquee">
                <img src="https://skillicons.dev/icons?i=dart,kotlin,swift,js,ts,python,unity,flutter,react,androidstudio,firebase,aws,nodejs,mongodb,git,docker" height="50" style="margin:0 25px;" />
                <img src="https://skillicons.dev/icons?i=dart,kotlin,swift,js,ts,python,unity,flutter,react,androidstudio,firebase,aws,nodejs,mongodb,git,docker" height="50" style="margin:0 25px;" />
            </div>
        </div>

        <!-- Flagship Projects 3D Cards -->
        <h2 align="center"><span style="color:#00ff9d;">🏆 FLAGSHIP PROJECTS [NEO] 🏆</span></h2>
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 30px; margin: 40px 0;">
            <div class="glass-card" style="width: 320px; padding: 20px; text-align: center;">
                <i class="fas fa-dice-d6" style="font-size: 65px; color:#00ff9d;"></i>
                <h3>LUDO EMPIRE</h3>
                <p>Real-time multiplayer | 1M+ downloads</p>
                <div><i class="fab fa-google-play"></i> 4.5★</div>
                <a href="#"><span style="color:#00ff9d;">View Project →</span></a>
            </div>
            <div class="glass-card" style="width: 320px; padding: 20px; text-align: center;">
                <i class="fas fa-chart-line" style="font-size: 65px; color:#00ff9d;"></i>
                <h3>SME BUSINESS SUITE</h3>
                <p>Complete ERP | 10k+ businesses</p>
                <div><i class="fas fa-cloud-upload-alt"></i> 99.9% Uptime</div>
                <a href="#"><span style="color:#00ff9d;">Live Demo →</span></a>
            </div>
            <div class="glass-card" style="width: 320px; padding: 20px; text-align: center;">
                <i class="fas fa-lock" style="font-size: 65px; color:#00ff9d;"></i>
                <h3>SECURE AUTH PRO</h3>
                <p>Banking-grade 2FA, Biometric</p>
                <div><i class="fas fa-shield-alt"></i> Zero breach</div>
                <a href="#"><span style="color:#00ff9d;">GitHub →</span></a>
            </div>
            <div class="glass-card" style="width: 320px; padding: 20px; text-align: center;">
                <i class="fas fa-building" style="font-size: 65px; color:#00ff9d;"></i>
                <h3>SMAIT PORTAL</h3>
                <p>Official Company Nexus</p>
                <div><i class="fas fa-globe"></i> Modern React</div>
                <a href="#"><span style="color:#00ff9d;">smaittechnology.com.np →</span></a>
            </div>
        </div>

        <!-- LIVE ACTIVITY GRAPH -->
        <div align="center" class="glass-card" style="padding: 20px; margin: 40px 0;">
            <h3>📡 LIVE NEURAL ACTIVITY GRAPH</h3>
            <img src="https://github-readme-activity-graph.vercel.app/graph?username=codersantoshadhikari&bg_color=00000000&color=00ff9d&line=00ff9d&point=ffffff&area=true&hide_border=true" width="100%"/>
        </div>

        <!-- Weekly Coding Metrics + Education -->
        <div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center;">
            <div class="glass-card" style="flex: 1; min-width: 280px; padding: 20px;">
                <h3><i class="fas fa-chart-simple"></i> WEEKLY CODING METRICS</h3>
                <img src="https://github-readme-stats.vercel.app/api/wakatime?username=codersantoshadhikari&theme=chartreuse-dark&hide_border=true&bg_color=00000000&title_color=00ff9d" width="100%"/>
            </div>
            <div class="glass-card" style="flex: 1; min-width: 280px; padding: 20px;">
                <h3><i class="fas fa-graduation-cap"></i> CERTIFICATIONS</h3>
                <ul style="list-style: none;">
                    <li><i class="fas fa-check-circle" style="color:#00ff9d;"></i> MBA in Ethical Hacking</li>
                    <li><i class="fas fa-check-circle" style="color:#00ff9d;"></i> Google Flutter Certified</li>
                    <li><i class="fas fa-check-circle" style="color:#00ff9d;"></i> Unity Certified Developer</li>
                    <li><i class="fas fa-check-circle" style="color:#00ff9d;"></i> CEH (EC-Council)</li>
                </ul>
            </div>
        </div>

        <!-- Connect Hologram Cards -->
        <h2 align="center" style="margin: 60px 0 20px;">🌐 DIMENSIONAL CONNECT 🌐</h2>
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; margin-bottom: 50px;">
            <a href="https://santoshadhikari.com.np" class="glass-card hover-lift" style="padding: 15px 25px;"><i class="fas fa-user-astronaut"></i> PORTFOLIO</a>
            <a href="https://linkedin.com/in/codersantoshadhikari" class="glass-card hover-lift" style="padding: 15px 25px;"><i class="fab fa-linkedin"></i> LINKEDIN</a>
            <a href="https://github.com/codersantoshadhikari" class="glass-card hover-lift" style="padding: 15px 25px;"><i class="fab fa-github"></i> GITHUB</a>
            <a href="https://twitter.com/santosh215" class="glass-card hover-lift" style="padding: 15px 25px;"><i class="fab fa-twitter"></i> X</a>
            <a href="https://youtube.com/@smaittechnology" class="glass-card hover-lift" style="padding: 15px 25px;"><i class="fab fa-youtube"></i> YT</a>
            <a href="mailto:santosh.ad215@gmail.com" class="glass-card hover-lift" style="padding: 15px 25px;"><i class="fas fa-envelope"></i> EMAIL</a>
        </div>

        <!-- Support Section -->
        <div align="center" class="glass-card" style="display: inline-block; width: auto; margin: 0 auto; padding: 25px 50px;">
            <h3>💖 Fuel the Matrix 💖</h3>
            <div style="display: flex; gap: 20px; justify-content: center; margin-top: 15px;">
                <a href="https://buymeacoffee.com/santoshadh7"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="50"></a>
                <a href="https://github.com/sponsors/codersantoshadhikari"><img src="https://img.shields.io/badge/SPONSOR-00ff9d?style=for-the-badge&logo=github-sponsors" height="50"></a>
            </div>
        </div>

        <!-- Terminal Easter Egg Quote -->
        <div align="center" style="margin-top: 50px;">
            <img src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=dark" width="80%" style="border-radius: 20px;"/>
        </div>

        <div align="center" style="margin: 40px 0 20px;">
            <sub>
                <i class="fas fa-sync-alt"></i> AUTO-SYNC ACTIVE | <i class="fas fa-charging-station"></i> 9D NEURAL LINK | STATUS: OMEGA ONLINE
            </sub>
        </div>
    </div>

    <!-- Three.js 9D Core Animation -->
    <script type="module">
        import * as THREE from 'three';

        const canvas = document.getElementById('bg-canvas');
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x010101);
        const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.set(0, 2, 8);
        camera.lookAt(0, 0, 0);

        const renderer = new THREE.WebGLRenderer({ canvas, alpha: false });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(window.devicePixelRatio);

        // Core Energy Torus
        const torusGeo = new THREE.TorusGeometry(1.8, 0.25, 64, 200);
        const materialCore = new THREE.MeshStandardMaterial({ color: 0x00ff9d, emissive: 0x00aa66, emissiveIntensity: 1.2, metalness: 0.8, roughness: 0.2 });
        const torus = new THREE.Mesh(torusGeo, materialCore);
        scene.add(torus);

        // Icosahedron floating
        const icoGeo = new THREE.IcosahedronGeometry(0.9, 0);
        const icoMat = new THREE.MeshStandardMaterial({ color: 0x00cc88, wireframe: false, emissive: 0x006633, emissiveIntensity: 0.7 });
        const ico = new THREE.Mesh(icoGeo, icoMat);
        scene.add(ico);

        // Particle system (Matrix rain style)
        const particlesGeo = new THREE.BufferGeometry();
        const particleCount = 1800;
        const posArray = new Float32Array(particleCount * 3);
        for(let i = 0; i < particleCount; i++) {
            posArray[i*3] = (Math.random() - 0.5) * 30;
            posArray[i*3+1] = (Math.random() - 0.5) * 20;
            posArray[i*3+2] = (Math.random() - 0.5) * 15 - 5;
        }
        particlesGeo.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
        const particleMat = new THREE.PointsMaterial({ color: 0x00ff9d, size: 0.07, transparent: true, opacity: 0.5 });
        const particles = new THREE.Points(particlesGeo, particleMat);
        scene.add(particles);

        // Lights
        const ambientLight = new THREE.AmbientLight(0x111111);
        scene.add(ambientLight);
        const pointLight = new THREE.PointLight(0x00ff9d, 1);
        pointLight.position.set(3, 3, 5);
        scene.add(pointLight);
        const backLight = new THREE.PointLight(0x2266ff, 0.5);
        backLight.position.set(-2, 1, -4);
        scene.add(backLight);

        let time = 0;
        function animate() {
            requestAnimationFrame(animate);
            time += 0.008;
            torus.rotation.x += 0.008;
            torus.rotation.y += 0.012;
            ico.rotation.x = Math.sin(time * 0.7) * 0.3;
            ico.rotation.y += 0.01;
            particles.rotation.y += 0.0005;
            particles.rotation.x = Math.sin(time * 0.2) * 0.1;
            camera.position.z = 7 + Math.sin(time * 0.5) * 0.1;
            camera.lookAt(0, 0, 0);
            renderer.render(scene, camera);
        }
        animate();

        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });
    </script>
    <script>
        // Skill bars animation on scroll (simple observer)
        const skillBars = document.querySelectorAll('.skill-fill');
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if(entry.isIntersecting) {
                    const width = entry.target.style.width;
                    entry.target.style.width = width ? width : '95%';
                }
            });
        }, { threshold: 0.3 });
        skillBars.forEach(bar => observer.observe(bar));
        // set default widths manually
        document.querySelectorAll('.skill-fill').forEach((el, idx) => {
            const widths = ['95%','98%','92%','90%'];
            if(el.style.width === '0%') el.style.width = widths[idx % widths.length];
        });
    </script>
</body>
</html>
