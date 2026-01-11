import React from 'react';
import { Mic, Calendar } from 'lucide-react';

const AppPreview: React.FC = () => {
  return (
    <section id="how-it-works" className="py-24 overflow-hidden relative">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid lg:grid-cols-2 gap-16 items-center">
          
          {/* Text Content */}
          <div className="order-2 lg:order-1">
            <h2 className="text-3xl md:text-4xl font-bold text-slate-900 dark:text-white mb-6">
              Karmaşık Düşüncelerden <br />
              <span className="text-indigo-500">Düzenli Eylemlere</span>
            </h2>
            <div className="space-y-8">
              <div className="flex gap-4">
                <div className="flex-shrink-0 w-8 h-8 rounded-full bg-indigo-100 dark:bg-indigo-900 text-indigo-600 dark:text-indigo-300 flex items-center justify-center font-bold">1</div>
                <div>
                  <h4 className="text-lg font-bold text-slate-900 dark:text-white mb-2">Yakala</h4>
                  <p className="text-slate-600 dark:text-slate-400">Aklına geleni widget üzerinden sesli söyle veya fotoğrafını çek. Uygulamayı açmana bile gerek yok.</p>
                </div>
              </div>
              <div className="flex gap-4">
                <div className="flex-shrink-0 w-8 h-8 rounded-full bg-pink-100 dark:bg-pink-900 text-pink-600 dark:text-pink-300 flex items-center justify-center font-bold">2</div>
                <div>
                  <h4 className="text-lg font-bold text-slate-900 dark:text-white mb-2">Analiz Et</h4>
                  <p className="text-slate-600 dark:text-slate-400">Gemini API arka planda çalışır. "Yarın saat 3'te Ahmet ile toplantı" dediğinde, bunu bir Takvim Etkinliği olarak algılar.</p>
                </div>
              </div>
              <div className="flex gap-4">
                <div className="flex-shrink-0 w-8 h-8 rounded-full bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300 flex items-center justify-center font-bold">3</div>
                <div>
                  <h4 className="text-lg font-bold text-slate-900 dark:text-white mb-2">Organize Ol</h4>
                  <p className="text-slate-600 dark:text-slate-400">Dashboard'unda gününü planla, önceliklerini gör ve hiçbir şeyi unutma.</p>
                </div>
              </div>
            </div>
          </div>

          {/* Phone Mockup */}
          <div className="order-1 lg:order-2 flex justify-center [perspective:1000px]">
             {/* Phone Body */}
             <div className="relative w-[300px] h-[600px] bg-slate-900 rounded-[3rem] shadow-2xl border-8 border-slate-950 overflow-hidden transform [transform:rotateY(12deg)] hover:[transform:rotateY(0deg)] transition-transform duration-700">
                {/* Notch */}
                <div className="absolute top-0 left-1/2 transform -translate-x-1/2 w-32 h-6 bg-slate-950 rounded-b-2xl z-20"></div>
                
                {/* Screen Content */}
                <div className="w-full h-full bg-slate-50 dark:bg-slate-900 flex flex-col pt-10">
                   {/* Header */}
                   <div className="px-6 pb-4 flex justify-between items-center">
                      <div>
                        <div className="text-xs text-slate-500 uppercase font-semibold">Bugün</div>
                        <div className="text-2xl font-bold text-slate-900 dark:text-white">Dashboard</div>
                      </div>
                      <div className="w-10 h-10 rounded-full bg-gray-200 dark:bg-slate-800"></div>
                   </div>

                   {/* Stats Cards */}
                   <div className="flex gap-4 px-6 mb-6 overflow-x-auto no-scrollbar">
                      <div className="flex-shrink-0 w-32 p-4 bg-indigo-500 rounded-2xl text-white">
                        <div className="text-2xl font-bold mb-1">12</div>
                        <div className="text-xs opacity-80">Bekleyen Görev</div>
                      </div>
                      <div className="flex-shrink-0 w-32 p-4 bg-pink-500 rounded-2xl text-white">
                        <div className="text-2xl font-bold mb-1">3</div>
                        <div className="text-xs opacity-80">Toplantı</div>
                      </div>
                   </div>

                   {/* List */}
                   <div className="flex-1 bg-white dark:bg-slate-800 rounded-t-[2.5rem] p-6 shadow-inner">
                      <h5 className="font-bold text-slate-900 dark:text-white mb-4">Son Aktiviteler</h5>
                      <div className="space-y-4">
                        {[1, 2, 3, 4].map((i) => (
                          <div key={i} className="flex items-center gap-3 p-3 rounded-xl bg-slate-50 dark:bg-slate-700/50">
                            <div className={`w-10 h-10 rounded-full flex items-center justify-center ${i % 2 === 0 ? 'bg-indigo-100 text-indigo-500' : 'bg-pink-100 text-pink-500'}`}>
                              {i % 2 === 0 ? <Mic size={18} /> : <Calendar size={18} />}
                            </div>
                            <div className="flex-1">
                              <div className="h-2 w-24 bg-slate-200 dark:bg-slate-600 rounded mb-2"></div>
                              <div className="h-2 w-16 bg-slate-200 dark:bg-slate-600 rounded"></div>
                            </div>
                          </div>
                        ))}
                      </div>
                      
                      {/* FAB */}
                      <div className="absolute bottom-6 right-6 w-14 h-14 bg-gradient-to-r from-indigo-500 to-pink-500 rounded-full shadow-lg shadow-indigo-500/40 flex items-center justify-center text-white text-2xl">
                        +
                      </div>
                   </div>
                </div>
             </div>
             
             {/* Secondary Phone (Behind) */}
             <div className="absolute top-12 -right-12 lg:-right-4 w-[280px] h-[560px] bg-slate-800 rounded-[2.5rem] shadow-xl border-8 border-slate-900 -z-10 opacity-50 blur-[1px] transform rotate-12 hidden md:block"></div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default AppPreview;