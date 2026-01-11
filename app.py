import streamlit as st
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="LifeSync AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Orijinal tasarıma çok daha yakın
def load_css():
    css = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
        
        * {
            font-family: 'Inter', sans-serif;
        }
        
        /* Hide Streamlit default elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Main container */
        .main .block-container {
            padding-top: 0;
            padding-bottom: 0;
            max-width: 1280px;
        }
        
        /* Navbar */
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(226, 232, 240, 0.8);
            padding: 1rem 0;
            transition: all 0.3s;
        }
        
        .navbar-content {
            max-width: 1280px;
            margin: 0 auto;
            padding: 0 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        .navbar-logo {
            font-size: 1.25rem;
            font-weight: 700;
            color: #0f172a;
        }
        
        .navbar-logo .ai {
            color: #6366f1;
        }
        
        .navbar-links {
            display: flex;
            gap: 2rem;
            align-items: center;
        }
        
        .navbar-link {
            color: #64748b;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.2s;
        }
        
        .navbar-link:hover {
            color: #6366f1;
        }
        
        /* Hero Section */
        .hero-section {
            position: relative;
            padding: 8rem 2rem 5rem;
            overflow: hidden;
            margin-top: 80px;
        }
        
        .hero-bg-blobs {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            z-index: -1;
            pointer-events: none;
        }
        
        .blob {
            position: absolute;
            border-radius: 50%;
            filter: blur(80px);
            opacity: 0.2;
            animation: blob 7s infinite;
        }
        
        .blob-1 {
            width: 288px;
            height: 288px;
            background: #6366f1;
            top: 80px;
            left: 40px;
        }
        
        .blob-2 {
            width: 288px;
            height: 288px;
            background: #ec4899;
            top: 80px;
            right: 40px;
            animation-delay: 2s;
        }
        
        .blob-3 {
            width: 288px;
            height: 288px;
            background: #a855f7;
            bottom: -32px;
            left: 50%;
            transform: translateX(-50%);
            animation-delay: 4s;
        }
        
        @keyframes blob {
            0%, 100% { transform: translate(0px, 0px) scale(1); }
            33% { transform: translate(30px, -50px) scale(1.1); }
            66% { transform: translate(-20px, 20px) scale(0.9); }
        }
        
        .hero-content {
            max-width: 1280px;
            margin: 0 auto;
            text-align: center;
            position: relative;
            z-index: 10;
        }
        
        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.5rem 1rem;
            background: rgba(99, 102, 241, 0.1);
            border: 1px solid rgba(99, 102, 241, 0.2);
            border-radius: 9999px;
            color: #6366f1;
            font-size: 0.875rem;
            font-weight: 600;
            margin-bottom: 2rem;
        }
        
        .hero-badge-dot {
            width: 8px;
            height: 8px;
            background: #6366f1;
            border-radius: 50%;
            position: relative;
        }
        
        .hero-badge-dot::before {
            content: '';
            position: absolute;
            width: 100%;
            height: 100%;
            background: #6366f1;
            border-radius: 50%;
            animation: ping 2s infinite;
            opacity: 0.75;
        }
        
        @keyframes ping {
            75%, 100% {
                transform: scale(2);
                opacity: 0;
            }
        }
        
        .hero-title {
            font-size: 3.5rem;
            font-weight: 800;
            line-height: 1.1;
            color: #0f172a;
            margin-bottom: 1.5rem;
            letter-spacing: -0.02em;
        }
        
        .hero-title .gradient-text {
            background: linear-gradient(90deg, #6366f1 0%, #ec4899 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .hero-subtitle {
            font-size: 1.25rem;
            color: #475569;
            max-width: 42rem;
            margin: 0 auto 2.5rem;
            line-height: 1.6;
        }
        
        .hero-buttons {
            display: flex;
            gap: 1rem;
            justify-content: center;
            margin-bottom: 4rem;
            flex-wrap: wrap;
        }
        
        .btn-primary {
            background: linear-gradient(90deg, #6366f1 0%, #ec4899 100%);
            color: white;
            padding: 1rem 2rem;
            border-radius: 12px;
            font-weight: 600;
            border: none;
            cursor: pointer;
            box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.2);
            transition: all 0.2s;
        }
        
        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 20px 25px -5px rgba(99, 102, 241, 0.3);
        }
        
        .btn-secondary {
            background: white;
            color: #0f172a;
            padding: 1rem 2rem;
            border-radius: 12px;
            font-weight: 600;
            border: 1px solid #e2e8f0;
            cursor: not-allowed;
            opacity: 0.8;
        }
        
        /* Features Section */
        .features-section {
            background: #f8fafc;
            padding: 6rem 2rem;
        }
        
        .features-container {
            max-width: 1280px;
            margin: 0 auto;
        }
        
        .section-header {
            text-align: center;
            max-width: 48rem;
            margin: 0 auto 4rem;
        }
        
        .section-label {
            font-size: 0.875rem;
            font-weight: 600;
            color: #6366f1;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.5rem;
        }
        
        .section-title {
            font-size: 2.25rem;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 1rem;
        }
        
        .section-description {
            font-size: 1.125rem;
            color: #64748b;
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }
        
        .feature-card {
            background: white;
            padding: 2rem;
            border-radius: 16px;
            border: 1px solid #e2e8f0;
            transition: all 0.3s;
            cursor: pointer;
        }
        
        .feature-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
            border-color: #c7d2fe;
        }
        
        .feature-icon {
            width: 48px;
            height: 48px;
            background: rgba(99, 102, 241, 0.1);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            margin-bottom: 1.5rem;
            transition: all 0.3s;
        }
        
        .feature-card:hover .feature-icon {
            background: #6366f1;
            color: white;
        }
        
        .feature-title {
            font-size: 1.25rem;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 0.75rem;
        }
        
        .feature-description {
            color: #64748b;
            line-height: 1.6;
        }
        
        /* App Preview Section */
        .app-preview-section {
            padding: 6rem 2rem;
        }
        
        .app-preview-container {
            max-width: 1280px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            align-items: center;
        }
        
        .steps-list {
            display: flex;
            flex-direction: column;
            gap: 2rem;
        }
        
        .step-item {
            display: flex;
            gap: 1rem;
        }
        
        .step-number {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            flex-shrink: 0;
        }
        
        .step-number-1 {
            background: rgba(99, 102, 241, 0.1);
            color: #6366f1;
        }
        
        .step-number-2 {
            background: rgba(236, 72, 153, 0.1);
            color: #ec4899;
        }
        
        .step-number-3 {
            background: rgba(71, 85, 105, 0.1);
            color: #475569;
        }
        
        .step-content h4 {
            font-size: 1.125rem;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 0.5rem;
        }
        
        .step-content p {
            color: #64748b;
            line-height: 1.6;
        }
        
        /* Technical Specs */
        .tech-section {
            background: #1e293b;
            color: white;
            padding: 5rem 2rem;
        }
        
        .tech-container {
            max-width: 1280px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 3rem;
        }
        
        .tech-item {
            display: flex;
            gap: 1rem;
            margin-bottom: 1.5rem;
            padding: 1rem;
            background: #f8fafc;
            border-radius: 12px;
        }
        
        .tech-icon {
            font-size: 2rem;
        }
        
        .tech-content h4 {
            font-size: 1.125rem;
            font-weight: 700;
            color: #1e293b;
            margin-bottom: 0.5rem;
        }
        
        .tech-content p {
            color: #64748b;
            font-size: 0.875rem;
        }
        
        .tech-box {
            background: #0f172a;
            border: 1px solid #334155;
            border-radius: 16px;
            padding: 2rem;
        }
        
        .tech-box h3 {
            font-family: monospace;
            font-size: 1.25rem;
            font-weight: 700;
            margin-bottom: 1rem;
        }
        
        .tech-row {
            display: flex;
            justify-content: space-between;
            padding: 0.5rem 0;
            border-bottom: 1px solid #334155;
            font-family: monospace;
            font-size: 0.875rem;
        }
        
        .tech-row:last-child {
            border-bottom: none;
        }
        
        .tech-code {
            margin-top: 2rem;
            padding: 1rem;
            background: #0f172a;
            border-radius: 8px;
            border: 1px solid #334155;
        }
        
        .tech-code code {
            color: #34d399;
            font-size: 0.75rem;
            font-family: monospace;
        }
        
        /* Footer */
        .footer {
            background: white;
            border-top: 1px solid #e2e8f0;
            padding: 4rem 2rem 2rem;
        }
        
        .footer-container {
            max-width: 1280px;
            margin: 0 auto;
        }
        
        .footer-content {
            display: grid;
            grid-template-columns: 2fr 1fr 1fr;
            gap: 3rem;
            margin-bottom: 2rem;
        }
        
        .footer-logo {
            font-size: 1.25rem;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 1rem;
        }
        
        .footer-logo .ai {
            color: #6366f1;
        }
        
        .footer-description {
            color: #64748b;
            max-width: 24rem;
        }
        
        .footer-column h4 {
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 1rem;
        }
        
        .footer-column ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        
        .footer-column li {
            color: #64748b;
            margin-bottom: 0.5rem;
        }
        
        .footer-bottom {
            border-top: 1px solid #e2e8f0;
            padding-top: 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            color: #94a3b8;
            font-size: 0.875rem;
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .hero-title {
                font-size: 2.5rem;
            }
            
            .app-preview-container {
                grid-template-columns: 1fr;
            }
            
            .tech-container {
                grid-template-columns: 1fr;
            }
            
            .footer-content {
                grid-template-columns: 1fr;
            }
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def main():
    load_css()
    
    # Navbar
    st.markdown("""
    <div class="navbar">
        <div class="navbar-content">
            <div class="navbar-logo">
                🧠 LifeSync <span class="ai">AI</span>
            </div>
            <div class="navbar-links">
                <a href="#features" class="navbar-link">Özellikler</a>
                <a href="#how-it-works" class="navbar-link">Nasıl Çalışır</a>
                <a href="#technical" class="navbar-link">Teknik</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <div class="hero-bg-blobs">
            <div class="blob blob-1"></div>
            <div class="blob blob-2"></div>
            <div class="blob blob-3"></div>
        </div>
        <div class="hero-content">
            <div class="hero-badge">
                <span class="hero-badge-dot"></span>
                Powered by Google Gemini 1.5 Pro
            </div>
            <h1 class="hero-title">
                Hayatını <span class="gradient-text">Yapay Zeka</span> ile<br/>
                Senkronize Et
            </h1>
            <p class="hero-subtitle">
                LifeSync AI, ses kayıtlarınızı, fotoğraflarınızı ve notlarınızı otomatik olarak analiz eder, 
                kategorize eder ve organize eder. Düşünmek size kalsın, gerisini biz halledelim.
            </p>
            <div class="hero-buttons">
                <button class="btn-primary" onclick="window.downloadModal=true; window.location.reload()">
                    Google Play'den İndir →
                </button>
                <button class="btn-secondary" disabled>
                    App Store'da Yakında
                </button>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Download buttons (Streamlit buttons)
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("📱 Google Play'den İndir", use_container_width=True, type="primary"):
            st.session_state.show_download = True
            st.rerun()
    
    with col2:
        st.button("🍎 App Store'da Yakında", use_container_width=True, disabled=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Features Section
    st.markdown("""
    <div class="features-section" id="features">
        <div class="features-container">
            <div class="section-header">
                <div class="section-label">Özellikler</div>
                <h2 class="section-title">Sıradan bir not uygulamasından fazlası</h2>
                <p class="section-description">
                    LifeSync AI, modern yaşamın karmaşasını yönetmek için en son yapay zeka teknolojilerini kullanır.
                </p>
            </div>
            <div class="features-grid">
    """, unsafe_allow_html=True)
    
    features = [
        {"icon": "🎤", "title": "Multimodal Giriş", "desc": "Sadece yazarak değil; ses kaydı alarak veya fotoğraf çekerek not alın. AI sizin için her şeyi metne döküp anlamlandırır."},
        {"icon": "🧠", "title": "AI Destekli Analiz", "desc": "Google Gemini motoru içeriğinizi analiz eder. Toplantı mı, görev mi, fikir mi? Otomatik olarak kategorize eder."},
        {"icon": "📅", "title": "Akıllı Takvim", "desc": "Notlarınızdaki tarih ve saatleri algılar, Google Takvim'inizle otomatik olarak senkronize eder. Asla bir randevuyu kaçırmayın."},
        {"icon": "📊", "title": "Görsel Dashboard", "desc": "Hayatınızı verilerle görün. Görev dağılımınızı, harcamalarınızı ve önceliklerinizi grafiklerle takip edin."},
        {"icon": "📱", "title": "Widget Desteği", "desc": "Uygulamayı açmadan ana ekranınızdan tek dokunuşla ses kaydı başlatın. Fikirlerinizi uçup gitmeden yakalayın."},
        {"icon": "☁️", "title": "Güvenli Yedekleme", "desc": "Verileriniz cihazınızda şifrelenir (Hive) ve dilerseniz Google Drive hesabınıza güvenli bir şekilde yedeklenir."}
    ]
    
    cols = st.columns(3)
    for idx, feature in enumerate(features):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{feature['icon']}</div>
                <h3 class="feature-title">{feature['title']}</h3>
                <p class="feature-description">{feature['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("</div></div></div>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # App Preview Section
    st.markdown("""
    <div class="app-preview-section" id="how-it-works">
        <div class="app-preview-container">
            <div>
                <h2 class="section-title" style="text-align: left; margin-bottom: 1.5rem;">
                    Karmaşık Düşüncelerden<br/>
                    <span style="color: #6366f1;">Düzenli Eylemlere</span>
                </h2>
                <div class="steps-list">
                    <div class="step-item">
                        <div class="step-number step-number-1">1</div>
                        <div class="step-content">
                            <h4>Yakala</h4>
                            <p>Aklına geleni widget üzerinden sesli söyle veya fotoğrafını çek. Uygulamayı açmana bile gerek yok.</p>
                        </div>
                    </div>
                    <div class="step-item">
                        <div class="step-number step-number-2">2</div>
                        <div class="step-content">
                            <h4>Analiz Et</h4>
                            <p>Gemini API arka planda çalışır. "Yarın saat 3'te Ahmet ile toplantı" dediğinde, bunu bir Takvim Etkinliği olarak algılar.</p>
                        </div>
                    </div>
                    <div class="step-item">
                        <div class="step-number step-number-3">3</div>
                        <div class="step-content">
                            <h4>Organize Ol</h4>
                            <p>Dashboard'unda gününü planla, önceliklerini gör ve hiçbir şeyi unutma.</p>
                        </div>
                    </div>
                </div>
            </div>
            <div style="text-align: center;">
                <div style="display: inline-block; width: 300px; height: 600px; background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border-radius: 3rem; padding: 1rem; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5); position: relative;">
                    <div style="background: #f8fafc; border-radius: 2rem; height: 100%; padding: 1.5rem; display: flex; flex-direction: column;">
                        <div style="margin-bottom: 1rem;">
                            <div style="font-size: 0.75rem; color: #64748b; text-transform: uppercase; font-weight: 600; margin-bottom: 0.25rem;">Bugün</div>
                            <div style="font-size: 1.5rem; font-weight: 700; color: #0f172a;">Dashboard</div>
                        </div>
                        <div style="display: flex; gap: 1rem; margin-bottom: 1.5rem;">
                            <div style="flex: 1; background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%); padding: 1rem; border-radius: 1rem; color: white;">
                                <div style="font-size: 1.5rem; font-weight: 700; margin-bottom: 0.25rem;">12</div>
                                <div style="font-size: 0.75rem; opacity: 0.8;">Bekleyen Görev</div>
                            </div>
                            <div style="flex: 1; background: linear-gradient(135deg, #ec4899 0%, #f472b6 100%); padding: 1rem; border-radius: 1rem; color: white;">
                                <div style="font-size: 1.5rem; font-weight: 700; margin-bottom: 0.25rem;">3</div>
                                <div style="font-size: 0.75rem; opacity: 0.8;">Toplantı</div>
                            </div>
                        </div>
                        <div style="flex: 1; background: white; border-radius: 1.5rem; padding: 1.5rem;">
                            <div style="font-weight: 700; color: #0f172a; margin-bottom: 1rem;">Son Aktiviteler</div>
                            <div style="display: flex; flex-direction: column; gap: 0.75rem;">
                                <div style="display: flex; gap: 0.75rem; padding: 0.75rem; background: #f8fafc; border-radius: 0.75rem;">
                                    <div style="width: 40px; height: 40px; background: rgba(99, 102, 241, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #6366f1;">🎤</div>
                                    <div style="flex: 1;">
                                        <div style="height: 8px; background: #e2e8f0; border-radius: 4px; width: 60%; margin-bottom: 0.5rem;"></div>
                                        <div style="height: 8px; background: #e2e8f0; border-radius: 4px; width: 40%;"></div>
                                    </div>
                                </div>
                                <div style="display: flex; gap: 0.75rem; padding: 0.75rem; background: #f8fafc; border-radius: 0.75rem;">
                                    <div style="width: 40px; height: 40px; background: rgba(236, 72, 153, 0.1); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #ec4899;">📅</div>
                                    <div style="flex: 1;">
                                        <div style="height: 8px; background: #e2e8f0; border-radius: 4px; width: 60%; margin-bottom: 0.5rem;"></div>
                                        <div style="height: 8px; background: #e2e8f0; border-radius: 4px; width: 40%;"></div>
                                    </div>
                                </div>
                            </div>
                            <div style="position: absolute; bottom: 1.5rem; right: 1.5rem; width: 56px; height: 56px; background: linear-gradient(135deg, #6366f1 0%, #ec4899 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 1.5rem; box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.4);">+</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Technical Specs Section
    st.markdown("""
    <div class="tech-section" id="technical">
        <div class="tech-container">
            <div>
                <h2 class="section-title" style="color: white; text-align: left; margin-bottom: 1.5rem;">Teknoloji Meraklıları İçin</h2>
                <p style="color: #94a3b8; font-size: 1.125rem; margin-bottom: 2rem; line-height: 1.6;">
                    LifeSync AI, modern mobil geliştirme standartları ve en güçlü yapay zeka modelleri üzerine inşa edilmiştir. Performans ve gizlilik önceliğimizdir.
                </p>
    """, unsafe_allow_html=True)
    
    tech_items = [
        {"icon": "💻", "title": "Flutter & Dart", "desc": "Hem iOS hem Android için tek kod tabanı ile yüksek performanslı native deneyim."},
        {"icon": "🤖", "title": "Google Gemini API", "desc": "Multimodal analiz için en son Gemini modelleri entegre edilmiştir."},
        {"icon": "💾", "title": "Hive Local Storage", "desc": "Verileriniz cihazınızda şifreli NoSQL veritabanında saklanır. İnternet olmasa bile çalışır."},
        {"icon": "🔒", "title": "OAuth & Şifreleme", "desc": "Google Sign-In ile güvenli giriş ve end-to-end şifreli yedekleme."}
    ]
    
    for item in tech_items:
        st.markdown(f"""
        <div class="tech-item">
            <div class="tech-icon">{item['icon']}</div>
            <div class="tech-content">
                <h4>{item['title']}</h4>
                <p>{item['desc']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
            </div>
            <div class="tech-box">
                <h3>System Architecture</h3>
                <div class="tech-row">
                    <span>Client</span>
                    <span style="color: #818cf8;">Flutter Mobile App</span>
                </div>
                <div class="tech-row">
                    <span>AI Model</span>
                    <span style="color: #ec4899;">Gemini 1.5 Pro</span>
                </div>
                <div class="tech-row">
                    <span>Database</span>
                    <span style="color: #60a5fa;">Hive Box (AES-256)</span>
                </div>
                <div class="tech-row" style="border-bottom: none;">
                    <span>Cloud Sync</span>
                    <span style="color: #34d399;">Google Drive API</span>
                </div>
                <div class="tech-code">
                    <code>
                        &gt; initializing AI core...<br/>
                        &gt; connecting to neural engine...<br/>
                        &gt; LifeSync system ready.
                    </code>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Download Modal
    if st.session_state.get('show_download', False):
        with st.expander("📥 Erken Erişim - APK İndir", expanded=True):
            st.markdown("""
            Beta sürümünü cihazınıza indirmek için lütfen size verilen erişim şifresini giriniz.
            """)
            
            password = st.text_input("Erişim Şifresi", type="password", placeholder="Şifrenizi girin", key="download_password")
            
            apk_path = Path("Download/app-release.apk")
            password_correct = password == "lifesynctest"
            
            if password_correct and apk_path.exists():
                with open(apk_path, "rb") as f:
                    apk_data = f.read()
                    st.download_button(
                        label="📥 APK Dosyasını İndir",
                        data=apk_data,
                        file_name="app-release.apk",
                        mime="application/vnd.android.package-archive",
                        use_container_width=True,
                        type="primary"
                    )
            elif password and not password_correct:
                st.error("❌ Hatalı şifre, tekrar deneyin.")
            elif password_correct and not apk_path.exists():
                st.warning("⚠️ APK dosyası bulunamadı!")
            
            if st.button("❌ İptal", use_container_width=True):
                st.session_state.show_download = False
                st.rerun()
    
    # Footer
    st.markdown("""
    <div class="footer">
        <div class="footer-container">
            <div class="footer-content">
                <div>
                    <div class="footer-logo">
                        🧠 LifeSync <span class="ai">AI</span>
                    </div>
                    <p class="footer-description">
                        Kişisel yaşam asistanınız. Yapay zeka gücüyle organize olun, daha fazlasını başarın.
                    </p>
                </div>
                <div class="footer-column">
                    <h4>Ürün</h4>
                    <ul>
                        <li>Özellikler</li>
                        <li>İndir</li>
                        <li>Premium</li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h4>Şirket</h4>
                    <ul>
                        <li>Hakkımızda</li>
                        <li>Gizlilik Politikası</li>
                        <li>İletişim</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p>© 2024 LifeSync AI. Tüm hakları saklıdır.</p>
                <div>🐦 📱 📷</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    if 'page' not in st.session_state:
        st.session_state.page = "home"
    if 'show_download' not in st.session_state:
        st.session_state.show_download = False
    
    main()
