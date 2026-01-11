import React from 'react';
import { Database, Lock, Code, Cpu } from 'lucide-react';

const TechnicalSpecs: React.FC = () => {
  return (
    <section id="technical" className="py-20 bg-slate-900 text-white">
       <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-2 gap-12 items-center">
             <div>
                <h2 className="text-3xl font-bold mb-6">Teknoloji Meraklıları İçin</h2>
                <p className="text-slate-400 text-lg mb-8">
                   LifeSync AI, modern mobil geliştirme standartları ve en güçlü yapay zeka modelleri üzerine inşa edilmiştir. Performans ve gizlilik önceliğimizdir.
                </p>
                
                <div className="space-y-6">
                   <div className="flex items-start gap-4">
                      <div className="p-2 bg-indigo-500/20 rounded-lg text-indigo-400 mt-1">
                         <Code size={20} />
                      </div>
                      <div>
                         <h4 className="font-bold text-lg">Flutter & Dart</h4>
                         <p className="text-slate-400 text-sm">Hem iOS hem Android için tek kod tabanı ile yüksek performanslı native deneyim.</p>
                      </div>
                   </div>

                   <div className="flex items-start gap-4">
                      <div className="p-2 bg-pink-500/20 rounded-lg text-pink-400 mt-1">
                         <Cpu size={20} />
                      </div>
                      <div>
                         <h4 className="font-bold text-lg">Google Gemini API</h4>
                         <p className="text-slate-400 text-sm">Multimodal analiz için en son Gemini modelleri entegre edilmiştir.</p>
                      </div>
                   </div>

                   <div className="flex items-start gap-4">
                      <div className="p-2 bg-blue-500/20 rounded-lg text-blue-400 mt-1">
                         <Database size={20} />
                      </div>
                      <div>
                         <h4 className="font-bold text-lg">Hive Local Storage</h4>
                         <p className="text-slate-400 text-sm">Verileriniz cihazınızda şifreli NoSQL veritabanında saklanır. İnternet olmasa bile çalışır.</p>
                      </div>
                   </div>

                   <div className="flex items-start gap-4">
                      <div className="p-2 bg-green-500/20 rounded-lg text-green-400 mt-1">
                         <Lock size={20} />
                      </div>
                      <div>
                         <h4 className="font-bold text-lg">OAuth & Şifreleme</h4>
                         <p className="text-slate-400 text-sm">Google Sign-In ile güvenli giriş ve end-to-end şifreli yedekleme.</p>
                      </div>
                   </div>
                </div>
             </div>
             
             <div className="relative">
                <div className="absolute inset-0 bg-gradient-to-r from-indigo-500 to-pink-500 rounded-2xl blur-2xl opacity-20"></div>
                <div className="relative bg-slate-800 rounded-2xl p-8 border border-slate-700">
                   <h3 className="text-xl font-bold mb-4 font-mono">System Architecture</h3>
                   <div className="space-y-4 font-mono text-sm text-slate-300">
                      <div className="flex justify-between border-b border-slate-700 pb-2">
                         <span>Client</span>
                         <span className="text-indigo-400">Flutter Mobile App</span>
                      </div>
                      <div className="flex justify-between border-b border-slate-700 pb-2">
                         <span>AI Model</span>
                         <span className="text-pink-400">Gemini 1.5 Pro</span>
                      </div>
                      <div className="flex justify-between border-b border-slate-700 pb-2">
                         <span>Database</span>
                         <span className="text-blue-400">Hive Box (AES-256)</span>
                      </div>
                      <div className="flex justify-between pb-2">
                         <span>Cloud Sync</span>
                         <span className="text-green-400">Google Drive API</span>
                      </div>
                   </div>
                   <div className="mt-8 p-4 bg-slate-900 rounded-lg border border-slate-700 overflow-hidden">
                      <code className="text-xs text-green-400 block">
                        &gt; initializing AI core...<br/>
                        &gt; connecting to neural engine...<br/>
                        &gt; LifeSync system ready.
                      </code>
                   </div>
                </div>
             </div>
          </div>
       </div>
    </section>
  );
};

export default TechnicalSpecs;