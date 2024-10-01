import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { CartProvider } from './context/CartContext';
import { AuthProvider } from './context/AuthContext';
import './styles/index.css';

const tg = window.Telegram.WebApp;

tg.expand();

ReactDOM.render(
  <React.StrictMode>
    <AuthProvider>
      <CartProvider>
        <App tg={tg} />
      </CartProvider>
    </AuthProvider>
  </React.StrictMode>,
  document.getElementById('root')
);