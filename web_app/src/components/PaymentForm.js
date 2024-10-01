import React, { useState } from 'react';
import { processPayment } from '../services/api';

const PaymentForm = ({ totalAmount, onPaymentComplete }) => {
  const [cardNumber, setCardNumber] = useState('');
  const [expiryDate, setExpiryDate] = useState('');
  const [cvv, setCvv] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await processPayment({ cardNumber, expiryDate, cvv, amount: totalAmount });
      onPaymentComplete();
    } catch (error) {
      console.error('Payment failed:', error);
      alert('فشلت عملية الدفع. يرجى المحاولة مرة أخرى.');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="payment-form">
      <h3>تفاصيل الدفع</h3>
      <div>
        <label htmlFor="cardNumber">رقم البطاقة</label>
        <input
          type="text"
          id="cardNumber"
          value={cardNumber}
          onChange={(e) => setCardNumber(e.target.value)}
          required
        />
      </div>
      <div>
        <label htmlFor="expiryDate">تاريخ الانتهاء</label>
        <input
          type="text"
          id="expiryDate"
          value={expiryDate}
          onChange={(e) => setExpiryDate(e.target.value)}
          placeholder="MM/YY"
          required
        />
      </div>
      <div>
        <label htmlFor="cvv">CVV</label>
        <input
          type="text"
          id="cvv"
          value={cvv}
          onChange={(e) => setCvv(e.target.value)}
          required
        />
      </div>
      <button type="submit">إتمام الدفع</button>
    </form>
  );
};

export default PaymentForm;