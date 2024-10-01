export const validateEmail = (email) => {
    const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return re.test(String(email).toLowerCase());
  };
  
  export const validatePhone = (phone) => {
    const re = /^(05|5)(5|0|3|6|4|9|1|8|7)([0-9]{7})$/;
    return re.test(phone);
  };
  
  export const validateName = (name) => {
    return name.length >= 3;
  };
  
  export const validateAddress = (address) => {
    return address.length >= 10;
  };