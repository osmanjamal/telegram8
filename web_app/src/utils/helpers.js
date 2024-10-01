export const formatPrice = (price) => {
    return `${price.toFixed(2)} ريال`;
  };
  
  export const formatDate = (dateString) => {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('ar-SA', options);
  };