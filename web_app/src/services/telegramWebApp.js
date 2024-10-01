const tg = window.Telegram.WebApp;

export const closeTelegramWebApp = () => {
  tg.close();
};

export const sendData = (data) => {
  tg.sendData(JSON.stringify(data));
};

export const showAlert = (message) => {
  tg.showAlert(message);
};

export const showConfirm = (message) => {
  return new Promise((resolve) => {
    tg.showConfirm(message, (confirmed) => {
      resolve(confirmed);
    });
  });
};

export const setMainButtonText = (text) => {
  tg.MainButton.setText(text);
};

export const showMainButton = () => {
  tg.MainButton.show();
};

export const hideMainButton = () => {
  tg.MainButton.hide();
};

export const onMainButtonClicked = (callback) => {
  tg.MainButton.onClick(callback);
};

export const getUserData = () => {
  return tg.initDataUnsafe?.user;
};