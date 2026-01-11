import React from 'react';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'outline';
  size?: 'sm' | 'md' | 'lg';
  fullWidth?: boolean;
}

const Button: React.FC<ButtonProps> = ({ 
  children, 
  variant = 'primary', 
  size = 'md', 
  fullWidth = false,
  className = '',
  ...props 
}) => {
  const baseStyles = "inline-flex items-center justify-center rounded-xl font-medium transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed";
  
  const variants = {
    primary: "bg-gradient-to-r from-indigo-500 to-pink-500 text-white hover:shadow-lg hover:shadow-indigo-500/25 border-transparent",
    secondary: "bg-white text-slate-900 hover:bg-slate-50 border border-slate-200 shadow-sm dark:bg-slate-800 dark:text-white dark:border-slate-700 dark:hover:bg-slate-700",
    outline: "bg-transparent border-2 border-slate-200 text-slate-600 hover:border-indigo-500 hover:text-indigo-500 dark:border-slate-700 dark:text-slate-300 dark:hover:border-indigo-400 dark:hover:text-indigo-400"
  };

  const sizes = {
    sm: "px-4 py-2 text-sm",
    md: "px-6 py-3 text-base",
    lg: "px-8 py-4 text-lg"
  };

  const widthClass = fullWidth ? "w-full" : "";

  return (
    <button 
      className={`${baseStyles} ${variants[variant]} ${sizes[size]} ${widthClass} ${className}`}
      {...props}
    >
      {children}
    </button>
  );
};

export default Button;