import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { getMenuItem } from '../services/api';
import { useCart } from '../hooks/useCart';

const ItemDetails = () => {
  const { id } = useParams();
  const [item, setItem] = useState(null);
  const { addToCart } = useCart();

  useEffect(() => {
    const fetchItem = async () => {
      const data = await getMenuItem(id);
      setItem(data);
    };
    fetchItem();
  }, [id]);

  if (!item) return <div>جاري التحميل...</div>;

  return (
    <div className="item-details">
      <h2>{item.name}</h2>
      <img src={item.image_url} alt={item.name} />
      <p>{item.description}</p>
      <p className="price">{item.price} ريال</p>
      <button onClick={() => addToCart(item)}>أضف إلى السلة</button>
    </div>
  );
};

export default ItemDetails;