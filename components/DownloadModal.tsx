import React, { useState } from 'react';
import { X, Download, Lock } from 'lucide-react';
import Button from './Button';

interface DownloadModalProps {
  isOpen: boolean;
  onClose: () => void;
}

const DownloadModal: React.FC<DownloadModalProps> = ({ isOpen, onClose }) => {
  const [password, setPassword] = useState('');
  const [error, setError] = useState(false);

  if (!isOpen) return null;

  const handleDownload = () => {
    if (password === 'lifesynctest') {
      // Create a temporary link to trigger download
      const link = document.createElement('a');
      // Updated path to point to the Download folder
      link.href = 'Download/app-release.apk'; 
      link.download = 'app-release.apk';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      
      // Reset and close
      setError(false);
      setPassword('');
      onClose();
    } else {
      setError(true);
    }
  };

  return (
    <div className="fixed inset-0 z-[100] flex items-center justify-center px-4">
      <div className="absolute inset-0 bg-slate-900/60 backdrop-blur-sm transition-opacity" onClick={onClose}></div>
      <div className="relative bg-white dark:bg-slate-900 rounded-2xl shadow-2xl w-full max-w-md p-8 border border-slate-200 dark:border-slate-700 transform transition-all scale-100 opacity-100">
        <button 
          onClick={onClose} 
          className="absolute top-4 right-4 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 transition-colors"
        >
          <X size={20} />
        </button>
        
        <div className="text-center mb-8">
          <div className="w-16 h-16 bg-indigo-50 dark:bg-indigo-900/30 rounded-2xl flex items-center justify-center mx-auto mb-5 text-indigo-500 border border-indigo-100 dark:border-indigo-800">
            <Lock size={32} />
          </div>
          <h3 className="text-2xl font-bold text-slate-900 dark:text-white tracking-tight">Erken Erişim</h3>
          <p className="text-slate-500 dark:text-slate-400 mt-3 text-base leading-relaxed">
            Beta sürümünü cihazınıza indirmek için lütfen size verilen erişim şifresini giriniz.
          </p>
        </div>

        <div className="space-y-5">
          <div>
            <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-2">
              Erişim Şifresi
            </label>
            <input
              type="password"
              value={password}
              onChange={(e) => {
                setPassword(e.target.value);
                setError(false);
              }}
              placeholder="Şifrenizi girin"
              className={`w-full px-4 py-3.5 rounded-xl border ${error ? 'border-red-500 focus:ring-red-500' : 'border-slate-200 dark:border-slate-700 focus:ring-indigo-500'} bg-slate-50 dark:bg-slate-800 text-slate-900 dark:text-white focus:ring-2 focus:border-transparent outline-none transition-all placeholder:text-slate-400`}
              onKeyDown={(e) => e.key === 'Enter' && handleDownload()}
            />
            {error && (
              <p className="text-red-500 text-sm mt-2 font-medium flex items-center gap-1 animate-pulse">
                Hatalı şifre, tekrar deneyin.
              </p>
            )}
          </div>
          
          <Button fullWidth size="lg" onClick={handleDownload}>
            <div className="flex items-center gap-2">
              <Download size={20} />
              APK İndir
            </div>
          </Button>
        </div>
      </div>
    </div>
  );
};

export default DownloadModal;