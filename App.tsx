import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import Features from './components/Features';
import AppPreview from './components/AppPreview';
import TechnicalSpecs from './components/TechnicalSpecs';
import Footer from './components/Footer';
import DownloadModal from './components/DownloadModal';
import { Theme } from './types';

const App: React.FC = () => {
  // Initialize theme from system preference or default to dark (looks cooler for AI apps)
  const [theme, setTheme] = useState<Theme>(() => {
    if (typeof window !== 'undefined' && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      return 'dark';
    }
    return 'light';
  });

  const [isDownloadModalOpen, setIsDownloadModalOpen] = useState(false);

  useEffect(() => {
    const root = window.document.documentElement;
    if (theme === 'dark') {
      root.classList.add('dark');
    } else {
      root.classList.remove('dark');
    }
  }, [theme]);

  const toggleTheme = () => {
    setTheme(prev => prev === 'dark' ? 'light' : 'dark');
  };

  const openDownloadModal = () => {
    setIsDownloadModalOpen(true);
  };

  return (
    <div className="min-h-screen flex flex-col">
      <Navbar 
        theme={theme} 
        toggleTheme={toggleTheme} 
        onDownloadClick={openDownloadModal}
      />
      <main className="flex-grow">
        <Hero onDownloadClick={openDownloadModal} />
        <Features />
        <AppPreview />
        <TechnicalSpecs />
      </main>
      <Footer />
      <DownloadModal 
        isOpen={isDownloadModalOpen} 
        onClose={() => setIsDownloadModalOpen(false)} 
      />
    </div>
  );
};

export default App;