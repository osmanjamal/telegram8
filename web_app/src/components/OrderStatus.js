import React, { useState, useEffect } from 'react';
import { getOrderStatus } from '../services/api';

const OrderStatus = ({ orderId }) => {
  const [status, setStatus] = useState('');

  useEffect(() => {
    const fetchStatus = async () => {
      const data = await getOrderStatus(orderId);
      setStatus(data.status);
    };
    fetchStatus();
    const interval = setInterval(fetchStatus, 30000); // تحديث كل 30 ثانية
    return () => clearInterval(interval);
  }, [orderId]);

  return (
    <div className="order-status">
      <h3>حالة الطلب رقم {orderId}</h3>
      <p>{status}</p>
    </div>
  );
};

export default OrderStatus;