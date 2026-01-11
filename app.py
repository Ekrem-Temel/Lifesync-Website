import streamlit as st
from pathlib import Path
import base64

# Page configuration
st.set_page_config(
    page_title="LifeSync AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
def load_css():
    css = """
    <style>
        /* Main styling */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        
        /* Hero section */
        .hero-container {
            text-align: center;
            padding: 4rem 2rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 20px;
            margin-bottom: 3rem;
            color: white;
        }
        
        .hero-title {
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 1rem;
            background: linear-gradient(90deg, #ffffff 0%, #e0e7ff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .hero-subtitle {
            font-size: 1.3rem;
            margin-bottom: 2rem;
            opacity: 0.9;
        }
        
        /* Feature cards */
        .feature-card {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1.5rem;
            transition: transform 0.3s;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
        }
        
        .feature-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        
        /* Badge */
        .badge {
            display: inline-block;
            padding: 0.5rem 1rem;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 50px;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }
        
        /* Technical specs */
        .tech-spec {
            background: #1e293b;
            color: white;
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 1rem;
        }
        
        /* Footer */
        .footer {
            text-align: center;
            padding: 2rem;
            margin-top: 4rem;
            border-top: 1px solid #e2e8f0;
        }
        
        /* Download button */
        .download-btn {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 0.75rem 2rem;
            border-radius: 10px;
            border: none;
            font-weight: 600;
            cursor: pointer;
        }
        
        /* Hide Streamlit default elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def get_base64_image(image_path):
    """Convert image to base64 for embedding"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

def main():
    load_css()
    
    # Navigation
    col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
    
    with col1:
        st.markdown("### 🧠 LifeSync **AI**")
    
    with col2:
        if st.button("Özellikler"):
            st.session_state.page = "features"
    
    with col3:
        if st.button("Nasıl Çalışır"):
            st.session_state.page = "how-it-works"
    
    with col4:
        if st.button("Teknik"):
            st.session_state.page = "technical"
    
    with col5:
        if st.button("İndir"):
            st.session_state.show_download = True
    
    st.markdown("---")
    
    # Hero Section
    st.markdown("""
    <div class="hero-container">
        <div class="badge">✨ Powered by Google Gemini 1.5 Pro</div>
        <h1 class="hero-title">Hayatını Yapay Zeka ile Senkronize Et</h1>
        <p class="hero-subtitle">
            LifeSync AI, ses kayıtlarınızı, fotoğraflarınızı ve notlarınızı otomatik olarak analiz eder, 
            kategorize eder ve organize eder. Düşünmek size kalsın, gerisini biz halledelim.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Download buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📱 Google Play'den İndir", use_container_width=True, type="primary"):
            st.session_state.show_download = True
    
    with col2:
        st.button("🍎 App Store'da Yakında", use_container_width=True, disabled=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Features Section
    st.markdown("## ✨ Özellikler")
    st.markdown("### Sıradan bir not uygulamasından fazlası")
    st.markdown("LifeSync AI, modern yaşamın karmaşasını yönetmek için en son yapay zeka teknolojilerini kullanır.")
    
    features = [
        {
            "icon": "🎤",
            "title": "Multimodal Giriş",
            "description": "Sadece yazarak değil; ses kaydı alarak veya fotoğraf çekerek not alın. AI sizin için her şeyi metne döküp anlamlandırır."
        },
        {
            "icon": "🧠",
            "title": "AI Destekli Analiz",
            "description": "Google Gemini motoru içeriğinizi analiz eder. Toplantı mı, görev mi, fikir mi? Otomatik olarak kategorize eder."
        },
        {
            "icon": "📅",
            "title": "Akıllı Takvim",
            "description": "Notlarınızdaki tarih ve saatleri algılar, Google Takvim'inizle otomatik olarak senkronize eder. Asla bir randevuyu kaçırmayın."
        },
        {
            "icon": "📊",
            "title": "Görsel Dashboard",
            "description": "Hayatınızı verilerle görün. Görev dağılımınızı, harcamalarınızı ve önceliklerinizi grafiklerle takip edin."
        },
        {
            "icon": "📱",
            "title": "Widget Desteği",
            "description": "Uygulamayı açmadan ana ekranınızdan tek dokunuşla ses kaydı başlatın. Fikirlerinizi uçup gitmeden yakalayın."
        },
        {
            "icon": "☁️",
            "title": "Güvenli Yedekleme",
            "description": "Verileriniz cihazınızda şifrelenir (Hive) ve dilerseniz Google Drive hesabınıza güvenli bir şekilde yedeklenir."
        }
    ]
    
    # Display features in grid
    cols = st.columns(3)
    for idx, feature in enumerate(features):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{feature['icon']}</div>
                <h3>{feature['title']}</h3>
                <p>{feature['description']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Technical Specs Section
    st.markdown("## 🔧 Teknoloji Meraklıları İçin")
    st.markdown("LifeSync AI, modern mobil geliştirme standartları ve en güçlü yapay zeka modelleri üzerine inşa edilmiştir. Performans ve gizlilik önceliğimizdir.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        tech_items = [
            {"icon": "💻", "title": "Flutter & Dart", "desc": "Hem iOS hem Android için tek kod tabanı ile yüksek performanslı native deneyim."},
            {"icon": "🤖", "title": "Google Gemini API", "desc": "Multimodal analiz için en son Gemini modelleri entegre edilmiştir."},
            {"icon": "💾", "title": "Hive Local Storage", "desc": "Verileriniz cihazınızda şifreli NoSQL veritabanında saklanır. İnternet olmasa bile çalışır."},
            {"icon": "🔒", "title": "OAuth & Şifreleme", "desc": "Google Sign-In ile güvenli giriş ve end-to-end şifreli yedekleme."}
        ]
        
        for item in tech_items:
            st.markdown(f"""
            <div style="display: flex; gap: 1rem; margin-bottom: 1.5rem; padding: 1rem; background: #f8fafc; border-radius: 10px;">
                <div style="font-size: 2rem;">{item['icon']}</div>
                <div>
                    <h4 style="margin: 0; color: #1e293b;">{item['title']}</h4>
                    <p style="margin: 0.5rem 0 0 0; color: #64748b; font-size: 0.9rem;">{item['desc']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="tech-spec">
            <h3 style="font-family: monospace; margin-bottom: 1rem;">System Architecture</h3>
            <div style="font-family: monospace; font-size: 0.9rem;">
                <div style="display: flex; justify-content: space-between; padding: 0.5rem 0; border-bottom: 1px solid #334155;">
                    <span>Client</span>
                    <span style="color: #818cf8;">Flutter Mobile App</span>
                </div>
                <div style="display: flex; justify-content: space-between; padding: 0.5rem 0; border-bottom: 1px solid #334155;">
                    <span>AI Model</span>
                    <span style="color: #ec4899;">Gemini 1.5 Pro</span>
                </div>
                <div style="display: flex; justify-content: space-between; padding: 0.5rem 0; border-bottom: 1px solid #334155;">
                    <span>Database</span>
                    <span style="color: #60a5fa;">Hive Box (AES-256)</span>
                </div>
                <div style="display: flex; justify-content: space-between; padding: 0.5rem 0;">
                    <span>Cloud Sync</span>
                    <span style="color: #34d399;">Google Drive API</span>
                </div>
            </div>
            <div style="margin-top: 2rem; padding: 1rem; background: #0f172a; border-radius: 8px; border: 1px solid #334155;">
                <code style="color: #34d399; font-size: 0.8rem;">
                    &gt; initializing AI core...<br/>
                    &gt; connecting to neural engine...<br/>
                    &gt; LifeSync system ready.
                </code>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Download Modal
    if st.session_state.get('show_download', False):
        with st.expander("📥 Erken Erişim - APK İndir", expanded=True):
            st.markdown("""
            Beta sürümünü cihazınıza indirmek için lütfen size verilen erişim şifresini giriniz.
            """)
            
            password = st.text_input("Erişim Şifresi", type="password", placeholder="Şifrenizi girin", key="download_password")
            
            col1, col2 = st.columns([1, 1])
            
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
                st.warning("⚠️ APK dosyası bulunamadı! Lütfen Download/app-release.apk dosyasının mevcut olduğundan emin olun.")
            
            with col2:
                if st.button("❌ İptal", use_container_width=True):
                    st.session_state.show_download = False
                    st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div class="footer">
        <h4>🧠 LifeSync <span style="color: #667eea;">AI</span></h4>
        <p>Kişisel yaşam asistanınız. Yapay zeka gücüyle organize olun, daha fazlasını başarın.</p>
        <p style="color: #94a3b8; font-size: 0.9rem;">© 2024 LifeSync AI. Tüm hakları saklıdır.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    if 'page' not in st.session_state:
        st.session_state.page = "home"
    if 'show_download' not in st.session_state:
        st.session_state.show_download = False
    
    main()
