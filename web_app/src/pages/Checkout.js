import React, { useState } from 'react';
import { useCart } from '../hooks/useCart';
import PaymentForm from '../components/PaymentForm';
import { createOrder } from '../services/api';

const Checkout = () => {
  const { cart, clearCart } = useCart();
  const [address, setAddress] = useState('');
  const [showPaymentForm, setShowPaymentForm] = useState(false);

  const totalAmount = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setShowPaymentForm(true);
  };

  const handlePaymentComplete = async () => {
    try {
      await createOrder({ items: cart, address, total: totalAmount });
      clearCart();
      alert('تم إتمام الطلب بنجاح!');
      // يمكنك هنا توجيه المستخدم إلى صفحة تأكيد الطلب
    } catch (error) {
      console.error('Error creating order:', error);
      alert('حدث خطأ أثناء إنشاء الطلب. يرجى المحاولة مرة أخرى.');
    }
  };

  return (
    <div className="checkout">
      <h2>إتمام الطلب</h2>
      {!showPaymentForm ? (
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor="address">عنوان التوصيل</label>
            <textarea
              id="address"
              value={address}
              onChange={(e) => setAddress(e.target.value)}
              required
            />
          </div>
          <p>المجموع: {totalAmount} ريال</p>
          <button type="submit">متابعة للدفع</button>
        </form>
      ) : (
        <PaymentForm totalAmount={totalAmount} onPaymentComplete={handlePaymentComplete} />
      )}
    </div>
  );
};

export default Checkout;