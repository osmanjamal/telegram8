import React from 'react';
import { Link } from 'react-router-dom';
import { useCart } from '../hooks/useCart';

const MenuItem = ({ item }) => {
  const { addToCart } = useCart();

  return (
    <div className="menu-item">
      <img src={item.image_url} alt={item.name} />
      <h3>{item.name}</h3>
      <p>{item.description}</p>
      <p className="price">{item.price} ريال</p>
      <button onClick={() => addToCart(item)}>أضف إلى السلة</button>
      <Link to={`/item/${item.id}`}>التفاصيل</Link>
    </div>
  );
};

export default MenuItem;