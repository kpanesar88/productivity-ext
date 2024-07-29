getTrackingData = () => {
  fetch(`${CONFIG.BACKEND_URL}/track`)
    .then((response) => response.json())
    .then((data) => {
      console.log("Time Elapsed:", data.time_elapsed);
      console.log("Time Focused:", data.time_focused);
      chrome.storage.local.set({ trackingData: data });
    })
    .catch((error) => console.error("Error:", error));
};

chrome.runtime.onInstalled.addListener(() => {
  console.log("Extension installed");
  // Periodically fetch tracking data
});

// chrome.alarms.onAlarm.addListener((alarm) => {
//   if (alarm.name === "getTrackingData") {
//     getTrackingData();
//   }
// });

// // Example: Set an alarm to fetch data every minute
// chrome.alarms.create("getTrackingData", { periodInMinutes: 1 });

// Set an interval to fetch tracking data every 10 seconds
setInterval(getTrackingData, 10000); // 10000 milliseconds = 10 seconds

// Optionally, you can add a one-time initial fetch
getTrackingData();
