import React from 'react';
import { 
  Mic, 
  Camera, 
  Brain, 
  Calendar, 
  LayoutDashboard, 
  Smartphone,
  ShieldCheck,
  Cloud
} from 'lucide-react';

const features = [
  {
    icon: Mic,
    title: "Multimodal Giriş",
    description: "Sadece yazarak değil; ses kaydı alarak veya fotoğraf çekerek not alın. AI sizin için her şeyi metne döküp anlamlandırır."
  },
  {
    icon: Brain,
    title: "AI Destekli Analiz",
    description: "Google Gemini motoru içeriğinizi analiz eder. Toplantı mı, görev mi, fikir mi? Otomatik olarak kategorize eder."
  },
  {
    icon: Calendar,
    title: "Akıllı Takvim",
    description: "Notlarınızdaki tarih ve saatleri algılar, Google Takvim'inizle otomatik olarak senkronize eder. Asla bir randevuyu kaçırmayın."
  },
  {
    icon: LayoutDashboard,
    title: "Görsel Dashboard",
    description: "Hayatınızı verilerle görün. Görev dağılımınızı, harcamalarınızı ve önceliklerinizi grafiklerle takip edin."
  },
  {
    icon: Smartphone,
    title: "Widget Desteği",
    description: "Uygulamayı açmadan ana ekranınızdan tek dokunuşla ses kaydı başlatın. Fikirlerinizi uçup gitmeden yakalayın."
  },
  {
    icon: Cloud,
    title: "Güvenli Yedekleme",
    description: "Verileriniz cihazınızda şifrelenir (Hive) ve dilerseniz Google Drive hesabınıza güvenli bir şekilde yedeklenir."
  }
];

const Features: React.FC = () => {
  return (
    <section id="features" className="py-24 bg-slate-50 dark:bg-slate-800/50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center max-w-3xl mx-auto mb-16">
          <h2 className="text-base text-indigo-500 font-semibold tracking-wide uppercase mb-2">Özellikler</h2>
          <p className="text-3xl md:text-4xl font-bold text-slate-900 dark:text-white mb-4">
            Sıradan bir not uygulamasından fazlası
          </p>
          <p className="text-lg text-slate-600 dark:text-slate-400">
            LifeSync AI, modern yaşamın karmaşasını yönetmek için en son yapay zeka teknolojilerini kullanır.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <div 
              key={index} 
              className="group p-8 bg-white dark:bg-slate-800 rounded-2xl shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 border border-slate-100 dark:border-slate-700"
            >
              <div className="w-12 h-12 rounded-lg bg-indigo-50 dark:bg-indigo-900/50 flex items-center justify-center text-indigo-500 mb-6 group-hover:bg-indigo-500 group-hover:text-white transition-colors duration-300">
                <feature.icon size={24} />
              </div>
              <h3 className="text-xl font-bold text-slate-900 dark:text-white mb-3">
                {feature.title}
              </h3>
              <p className="text-slate-600 dark:text-slate-400 leading-relaxed">
                {feature.description}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Features;