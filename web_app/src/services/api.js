const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:5000/api';

export const getMenu = async () => {
  const response = await fetch(`${API_BASE_URL}/menu`);
  if (!response.ok) throw new Error('Failed to fetch menu');
  return response.json();
};

export const getMenuItem = async (id) => {
  const response = await fetch(`${API_BASE_URL}/menu/${id}`);
  if (!response.ok) throw new Error('Failed to fetch menu item');
  return response.json();
};

export const createOrder = async (orderData) => {
  const response = await fetch(`${API_BASE_URL}/orders`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(orderData),
  });
  if (!response.ok) throw new Error('Failed to create order');
  return response.json();
};

export const getOrderStatus = async (orderId) => {
  const response = await fetch(`${API_BASE_URL}/orders/${orderId}/status`);
  if (!response.ok) throw new Error('Failed to fetch order status');
  return response.json();
};

export const getOrderHistory = async () => {
  const response = await fetch(`${API_BASE_URL}/orders`);
  if (!response.ok) throw new Error('Failed to fetch order history');
  return response.json();
};

export const getUserInfo = async () => {
  const response = await fetch(`${API_BASE_URL}/user`);
  if (!response.ok) throw new Error('Failed to fetch user info');
  return response.json();
};

export const updateUserInfo = async (userInfo) => {
  const response = await fetch(`${API_BASE_URL}/user`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(userInfo),
  });
  if (!response.ok) throw new Error('Failed to update user info');
  return response.json();
};

export const processPayment = async (paymentDetails) => {
  const response = await fetch(`${API_BASE_URL}/payment`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(paymentDetails),
  });
  if (!response.ok) throw new Error('Payment processing failed');
  return response.json();
};