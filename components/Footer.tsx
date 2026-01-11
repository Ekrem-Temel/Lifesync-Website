import React, { useState } from 'react';
import { Twitter, Github, Instagram, BrainCircuit } from 'lucide-react';

const Footer: React.FC = () => {
  const [logoError, setLogoError] = useState(false);

  return (
    <footer className="bg-white dark:bg-slate-900 border-t border-slate-200 dark:border-slate-800 pt-16 pb-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-12 mb-12">
          <div className="col-span-1 md:col-span-2">
            <div className="flex items-center gap-2 mb-4">
              {logoError ? (
                <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-pink-500 flex items-center justify-center text-white">
                  <BrainCircuit size={20} />
                </div>
              ) : (
                <img 
                  src="logo.png" 
                  alt="LifeSync AI Logo" 
                  className="w-8 h-8 object-contain" 
                  onError={() => setLogoError(true)}
                />
              )}
              <span className="font-bold text-xl text-slate-900 dark:text-white">
                LifeSync <span className="text-indigo-500">AI</span>
              </span>
            </div>
            <p className="text-slate-600 dark:text-slate-400 max-w-sm">
              Kişisel yaşam asistanınız. Yapay zeka gücüyle organize olun, daha fazlasını başarın.
            </p>
          </div>
          
          <div>
            <h4 className="font-bold text-slate-900 dark:text-white mb-4">Ürün</h4>
            <ul className="space-y-2 text-slate-600 dark:text-slate-400">
              <li>Özellikler</li>
              <li>İndir</li>
              <li>Premium</li>
            </ul>
          </div>

          <div>
            <h4 className="font-bold text-slate-900 dark:text-white mb-4">Şirket</h4>
            <ul className="space-y-2 text-slate-600 dark:text-slate-400">
              <li>Hakkımızda</li>
              <li>Gizlilik Politikası</li>
              <li>İletişim</li>
            </ul>
          </div>
        </div>

        <div className="border-t border-slate-200 dark:border-slate-800 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
          <p className="text-slate-500 text-sm">
            © {new Date().getFullYear()} LifeSync AI. Tüm hakları saklıdır.
          </p>
          <div className="flex gap-4">
            <span className="text-slate-400"><Twitter size={20} /></span>
            <span className="text-slate-400"><Github size={20} /></span>
            <span className="text-slate-400"><Instagram size={20} /></span>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;