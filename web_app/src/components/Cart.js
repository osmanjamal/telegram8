import React from 'react';
import { useCart } from '../hooks/useCart';

const Cart = () => {
  const { cart, removeFromCart, updateQuantity } = useCart();

  const total = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);

  return (
    <div className="cart">
      <h2>السلة</h2>
      {cart.length === 0 ? (
        <p>السلة فارغة</p>
      ) : (
        <>
          {cart.map(item => (
            <div key={item.id} className="cart-item">
              <h3>{item.name}</h3>
              <p>{item.price} ريال</p>
              <input 
                type="number" 
                value={item.quantity} 
                onChange={(e) => updateQuantity(item.id, parseInt(e.target.value))}
                min="1"
              />
              <button onClick={() => removeFromCart(item.id)}>إزالة</button>
            </div>
          ))}
          <p>المجموع: {total} ريال</p>
          <button>إتمام الشراء</button>
        </>
      )}
    </div>
  );
};

export default Cart;