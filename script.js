document.getElementById('hate-speech-form').addEventListener('submit', function (event) {
    event.preventDefault();
    const sentence = document.getElementById('sentence').value;
    const resultBox = document.getElementById('result');
    console.log(sentence)
    
    var url = "http://localhost:5000/predict_hate_speech"
    $.post(url, { sentence: sentence }, function (data, status) {
        if (data.prediction.includes('hate') || data.prediction.includes('offensive')) {
            resultBox.textContent = 'Hate Speech Detected!';
            resultBox.className = 'result-box negative';
        } else {
            resultBox.textContent = 'No Hate Speech Detected.';
            resultBox.className = 'result-box positive';
        }

    })

    // Mock logic to simulate hate speech detection
    // Replace with your actual logic or API call
  
});
