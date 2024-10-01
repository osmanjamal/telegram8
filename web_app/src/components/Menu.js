import React, { useState, useEffect } from 'react';
import MenuItem from './MenuItem';
import { getMenu } from '../services/api';

const Menu = () => {
  const [menuItems, setMenuItems] = useState([]);

  useEffect(() => {
    const fetchMenu = async () => {
      const data = await getMenu();
      setMenuItems(data);
    };
    fetchMenu();
  }, []);

  return (
    <div className="menu">
      {menuItems.map(item => (
        <MenuItem key={item.id} item={item} />
      ))}
    </div>
  );
};

export default Menu;