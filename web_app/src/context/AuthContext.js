import React, { createContext, useState, useEffect } from 'react';
import { getUserData } from '../services/telegramWebApp';
import { setItem, getItem } from '../services/localStorageService';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(() => {
    const savedUser = getItem('user');
    return savedUser || null;
  });

  useEffect(() => {
    const telegramUser = getUserData();
    if (telegramUser) {
      setUser(telegramUser);
      setItem('user', telegramUser);
    }
  }, []);

  const login = (userData) => {
    setUser(userData);
    setItem('user', userData);
  };

  const logout = () => {
    setUser(null);
    setItem('user', null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};