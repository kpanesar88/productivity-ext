document.addEventListener('DOMContentLoaded', () => {
  let displayButton = document.getElementById('refresh-button');

  displayButton.addEventListener('click', () => {
      chrome.runtime.getBackgroundPage((backgroundPage) => {
          backgroundPage.getTrackingData();
      });
  });
});
