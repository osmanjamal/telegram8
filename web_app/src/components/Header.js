import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/components/Header.css';

const Header = () => {
  return (
    <header className="header">
      <div className="container">
        <h1 className="logo"><Link to="/">بيت المحاشي</Link></h1>
        <nav>
          <ul>
            <li><Link to="/menu">القائمة</Link></li>
            <li><Link to="/orders">طلباتي</Link></li>
            <li><Link to="/account">حسابي</Link></li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;