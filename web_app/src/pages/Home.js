import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="home">
      <h1>مرحباً بك في بيت المحاشي</h1>
      <p>اكتشف أشهى أنواع المحاشي لدينا</p>
      <Link to="/menu" className="cta-button">استعرض القائمة</Link>
    </div>
  );
};

export default Home;