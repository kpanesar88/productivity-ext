document.addEventListener("DOMContentLoaded", () => {
  chrome.storage.local.get(["trackingData"], function (result) {
    if (result.trackingData) {
      document.getElementById("time_elapsed").innerText =
        result.trackingData.time_elapsed;
      document.getElementById("time_focused").innerText =
        result.trackingData.time_focused;
    }
  });

  // Optionally refresh the data displayed every second
  setInterval(() => {
    chrome.storage.local.get(["trackingData"], function (result) {
      if (result.trackingData) {
        document.getElementById("percentage").innerText =
          result.trackingData.time_focused / result.trackingData.time_elapsed;
        document.getElementById("seconds").innerText =
          result.trackingData.time_focused;
      }
    });
  }, 1000);
});
