const express = require('express');
const bodyParser = require('body-parser');
const fetch = require('node-fetch'); // installed for server-side requests if needed
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;
const FLASK_BACKEND_URL = process.env.FLASK_BACKEND_URL || 'http://backend:5000';

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'public')));

// Serve index.html at root
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Optional: proxy endpoint to forward form (if you want server -> backend)
app.post('/submit', async (req, res) => {
  try {
    // Forward the form data to Flask backend
    const response = await fetch(`${FLASK_BACKEND_URL}/submit`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(req.body)
    });

    const resultHtml = await response.text();
    // send backend response html as-is
    res.send(resultHtml);
  } catch (err) {
    console.error('Error forwarding to backend:', err);
    res.status(500).send('Error contacting backend');
  }
});

app.listen(PORT, () => {
  console.log(`Frontend running on port ${PORT}`);
});
