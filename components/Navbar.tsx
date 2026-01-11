import React, { useState, useEffect } from 'react';
import { Menu, X, Moon, Sun, BrainCircuit } from 'lucide-react';
import { Theme } from '../types';
import Button from './Button';

interface NavbarProps {
  theme: Theme;
  toggleTheme: () => void;
  onDownloadClick?: () => void;
}

const Navbar: React.FC<NavbarProps> = ({ theme, toggleTheme, onDownloadClick }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const [logoError, setLogoError] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 20);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const navLinks = [
    { label: 'Özellikler', href: '#features' },
    { label: 'Nasıl Çalışır', href: '#how-it-works' },
    { label: 'Teknik', href: '#technical' },
  ];

  return (
    <nav className={`fixed w-full z-50 transition-all duration-300 ${scrolled ? 'bg-white/80 dark:bg-slate-900/80 backdrop-blur-md shadow-lg' : 'bg-transparent'}`}>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-20">
          
          {/* Logo */}
          <div className="flex-shrink-0 flex items-center gap-2 cursor-pointer" onClick={() => window.scrollTo(0,0)}>
            {logoError ? (
              <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-indigo-500 to-pink-500 flex items-center justify-center text-white">
                <BrainCircuit size={24} />
              </div>
            ) : (
              <img 
                src="logo.png" 
                alt="LifeSync AI Logo" 
                className="w-10 h-10 object-contain" 
                onError={() => setLogoError(true)}
              />
            )}
            <span className="font-bold text-xl tracking-tight text-slate-900 dark:text-white">
              LifeSync <span className="text-indigo-500">AI</span>
            </span>
          </div>

          {/* Desktop Menu */}
          <div className="hidden md:flex items-center space-x-8">
            {navLinks.map((link) => (
              <a 
                key={link.label}
                href={link.href}
                className="text-slate-600 dark:text-slate-300 hover:text-indigo-500 dark:hover:text-indigo-400 font-medium transition-colors"
              >
                {link.label}
              </a>
            ))}
            
            <button 
              onClick={toggleTheme}
              className="p-2 rounded-full text-slate-500 hover:bg-slate-100 dark:text-slate-400 dark:hover:bg-slate-800 transition-colors"
              aria-label="Toggle Dark Mode"
            >
              {theme === 'dark' ? <Sun size={20} /> : <Moon size={20} />}
            </button>

            <Button size="sm" onClick={onDownloadClick}>İndir</Button>
          </div>

          {/* Mobile Menu Button */}
          <div className="md:hidden flex items-center gap-4">
             <button 
              onClick={toggleTheme}
              className="p-2 rounded-full text-slate-500 hover:bg-slate-100 dark:text-slate-400 dark:hover:bg-slate-800 transition-colors"
            >
              {theme === 'dark' ? <Sun size={20} /> : <Moon size={20} />}
            </button>
            <button
              onClick={() => setIsOpen(!isOpen)}
              className="text-slate-600 dark:text-slate-300 hover:text-indigo-500 focus:outline-none"
            >
              {isOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Menu */}
      {isOpen && (
        <div className="md:hidden bg-white dark:bg-slate-900 border-t dark:border-slate-800 absolute w-full shadow-xl">
          <div className="px-4 pt-2 pb-6 space-y-2">
            {navLinks.map((link) => (
              <a
                key={link.label}
                href={link.href}
                className="block px-3 py-4 rounded-md text-base font-medium text-slate-700 dark:text-slate-200 hover:bg-slate-50 dark:hover:bg-slate-800 hover:text-indigo-500"
                onClick={() => setIsOpen(false)}
              >
                {link.label}
              </a>
            ))}
            <div className="pt-4">
              <Button fullWidth onClick={() => {
                setIsOpen(false);
                if(onDownloadClick) onDownloadClick();
              }}>Hemen Başla</Button>
            </div>
          </div>
        </div>
      )}
    </nav>
  );
};

export default Navbar;