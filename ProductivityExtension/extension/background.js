getTrackingData = () => {
    fetch(`${CONFIG.BACKEND_URL}/track`)
        .then(response => response.json())
        .then(data => {
            console.log("Time Elapsed:", data.time_elapsed);
            console.log("Time Focused:", data.time_focused);
        })
        .catch(error => console.error('Error:', error));
}

chrome.runtime.onInstalled.addListener(() => {
    console.log("Extension installed");
    // Periodically fetch tracking data
    setInterval(getTrackingData(), 5000);  // Fetch every 5 seconds
});
