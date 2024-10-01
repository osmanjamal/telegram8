import React, { useState, useEffect } from 'react';
import { getUserInfo, updateUserInfo } from '../services/api';

const Account = () => {
  const [userInfo, setUserInfo] = useState({
    name: '',
    email: '',
    phone: ''
  });

  useEffect(() => {
    const fetchUserInfo = async () => {
      const data = await getUserInfo();
      setUserInfo(data);
    };
    fetchUserInfo();
  }, []);

  const handleChange = (e) => {
    setUserInfo({ ...userInfo, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await updateUserInfo(userInfo);
      alert('تم تحديث معلومات الحساب بنجاح');
    } catch (error) {
      console.error('Error updating user info:', error);
      alert('حدث خطأ أثناء تحديث المعلومات. يرجى المحاولة مرة أخرى.');
    }
  };

  return (
    <div className="account">
      <h2>حسابي</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="name">الاسم</label>
          <input
            type="text"
            id="name"
            name="name"
            value={userInfo.name}
            onChange={handleChange}
          />
        </div>
        <div>
          <label htmlFor="email">البريد الإلكتروني</label>
          <input
            type="email"
            id="email"
            name="email"
            value={userInfo.email}
            onChange={handleChange}
          />
        </div>
        <div>
          <label htmlFor="phone">رقم الهاتف</label>
          <input
            type="tel"
            id="phone"
            name="phone"
            value={userInfo.phone}
            onChange={handleChange}
          />
        </div>
        <button type="submit">حفظ التغييرات</button>
      </form>
    </div>
  );
};

export default Account;