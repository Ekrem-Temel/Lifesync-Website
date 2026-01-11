import React, { useState } from 'react';
import { ArrowRight, Smartphone, Mic } from 'lucide-react';
import Button from './Button';

interface HeroProps {
  onDownloadClick?: () => void;
}

const Hero: React.FC<HeroProps> = ({ onDownloadClick }) => {
  const [logoError, setLogoError] = useState(false);

  return (
    <section className="relative pt-32 pb-20 lg:pt-48 lg:pb-32 overflow-hidden">
      {/* Background decoration */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full -z-10 pointer-events-none">
        <div className="absolute top-20 left-10 w-72 h-72 bg-indigo-500 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-blob"></div>
        <div className="absolute top-20 right-10 w-72 h-72 bg-pink-500 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-blob animation-delay-2000"></div>
        <div className="absolute -bottom-8 left-1/2 w-72 h-72 bg-purple-500 rounded-full mix-blend-multiply filter blur-3xl opacity-20 animate-blob animation-delay-4000"></div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
        
        <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-indigo-50 dark:bg-indigo-900/30 text-indigo-600 dark:text-indigo-300 text-sm font-semibold mb-8 border border-indigo-100 dark:border-indigo-800">
          <span className="relative flex h-2 w-2">
            <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-indigo-400 opacity-75"></span>
            <span className="relative inline-flex rounded-full h-2 w-2 bg-indigo-500"></span>
          </span>
          Powered by Google Gemini 1.5 Pro
        </div>

        <h1 className="text-5xl md:text-7xl font-extrabold tracking-tight text-slate-900 dark:text-white mb-6">
          Hayatını <span className="bg-gradient-to-r from-indigo-500 to-pink-500 bg-clip-text text-transparent">Yapay Zeka</span> ile <br className="hidden md:block"/>Senkronize Et
        </h1>

        <p className="mt-4 text-xl text-slate-600 dark:text-slate-300 max-w-2xl mx-auto mb-10 leading-relaxed">
          LifeSync AI, ses kayıtlarınızı, fotoğraflarınızı ve notlarınızı otomatik olarak analiz eder, kategorize eder ve organize eder. Düşünmek size kalsın, gerisini biz halledelim.
        </p>

        <div className="flex flex-col sm:flex-row justify-center gap-4 mb-16">
          <Button size="lg" className="shadow-xl shadow-indigo-500/20" onClick={onDownloadClick}>
            <div className="flex items-center gap-2">
              Google Play'den İndir
              <ArrowRight size={20} />
            </div>
          </Button>
          <Button variant="secondary" size="lg" disabled className="cursor-not-allowed opacity-80">
            App Store'da Yakında
          </Button>
        </div>

        {/* Abstract App Preview */}
        <div className="relative mx-auto max-w-4xl transform hover:scale-[1.01] transition-transform duration-500">
            <div className="absolute inset-0 bg-gradient-to-r from-indigo-500 to-pink-500 rounded-2xl blur opacity-30"></div>
            <div className="relative bg-slate-900 rounded-2xl border border-slate-700 p-2 shadow-2xl overflow-hidden">
                <div className="bg-slate-950 rounded-xl overflow-hidden relative aspect-video flex items-center justify-center">
                    {/* Simulated UI for Dashboard */}
                    <div className="absolute inset-0 flex">
                        {/* Sidebar */}
                        <div className="w-20 lg:w-64 border-r border-slate-800 bg-slate-900 p-6 hidden md:block">
                            {logoError ? (
                                <div className="w-8 h-8 rounded bg-gradient-to-br from-indigo-500 to-pink-500 mb-8"></div>
                            ) : (
                                <img 
                                  src="logo.png" 
                                  className="w-8 h-8 object-contain mb-8" 
                                  alt="Logo" 
                                  onError={() => setLogoError(true)}
                                />
                            )}
                            <div className="space-y-4">
                                <div className="h-2 w-24 bg-slate-800 rounded"></div>
                                <div className="h-2 w-32 bg-slate-800 rounded"></div>
                                <div className="h-2 w-20 bg-slate-800 rounded"></div>
                            </div>
                        </div>
                        {/* Main Content */}
                        <div className="flex-1 p-6 lg:p-10">
                            <div className="flex justify-between items-center mb-10">
                                <div className="h-8 w-48 bg-slate-800 rounded-lg"></div>
                                <div className="flex gap-2">
                                    <div className="h-8 w-8 rounded-full bg-slate-800"></div>
                                    <div className="h-8 w-8 rounded-full bg-indigo-500"></div>
                                </div>
                            </div>
                            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                                <div className="p-4 rounded-xl bg-slate-800 border border-slate-700">
                                    <div className="flex items-center gap-3 mb-4">
                                        <div className="p-2 bg-indigo-500/10 text-indigo-500 rounded-lg"><Mic size={20}/></div>
                                        <div className="h-3 w-20 bg-slate-700 rounded"></div>
                                    </div>
                                    <div className="h-2 w-full bg-slate-700 rounded mb-2"></div>
                                    <div className="h-2 w-2/3 bg-slate-700 rounded"></div>
                                </div>
                                <div className="p-4 rounded-xl bg-slate-800 border border-slate-700">
                                    <div className="flex items-center gap-3 mb-4">
                                        <div className="p-2 bg-pink-500/10 text-pink-500 rounded-lg"><Smartphone size={20}/></div>
                                        <div className="h-3 w-20 bg-slate-700 rounded"></div>
                                    </div>
                                    <div className="h-2 w-full bg-slate-700 rounded mb-2"></div>
                                    <div className="h-2 w-2/3 bg-slate-700 rounded"></div>
                                </div>
                                <div className="p-4 rounded-xl bg-gradient-to-br from-indigo-600 to-pink-600 border border-transparent text-white">
                                    <div className="font-semibold mb-2">AI Analizi</div>
                                    <div className="text-xs opacity-80">Bugün 5 yeni görev ve 2 toplantı algılandı. Takvim senkronize edildi.</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

      </div>
    </section>
  );
};

export default Hero;