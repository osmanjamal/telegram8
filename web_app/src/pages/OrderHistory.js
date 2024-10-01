import React, { useState, useEffect } from 'react';
import { getOrderHistory } from '../services/api';
import OrderStatus from '../components/OrderStatus';

const OrderHistory = () => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    const fetchOrders = async () => {
      const data = await getOrderHistory();
      setOrders(data);
    };
    fetchOrders();
  }, []);

  return (
    <div className="order-history">
      <h2>سجل الطلبات</h2>
      {orders.length === 0 ? (
        <p>لا يوجد طلبات سابقة</p>
      ) : (
        orders.map(order => (
          <div key={order.id} className="order-item">
            <h3>طلب رقم {order.id}</h3>
            <p>التاريخ: {new Date(order.createdAt).toLocaleDateString()}</p>
            <p>المجموع: {order.total} ريال</p>
            <OrderStatus orderId={order.id} />
          </div>
        ))
      )}
    </div>
  );
};

export default OrderHistory;