export default async function handler(req, res) {
    // Fix: method check
    if (req.method !== 'POST') {
        return res.status(405).json({ error: 'Method not allowed' });
    }

    const { messages } = req.body;

    // Fix: validate that messages exists and is an array
    if (!messages || !Array.isArray(messages) || messages.length === 0) {
        return res.status(400).json({ error: 'Invalid request: messages array is required' });
    }

    // Fix: cap messages to last 20 to prevent token abuse
    const cappedMessages = messages.slice(-20);

    const apiKey = process.env.GROQ_API_KEY;

    if (!apiKey) {
        return res.status(500).json({ error: 'Server configuration error: Missing API Key' });
    }

    try {
        const response = await fetch('https://api.groq.com/openai/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${apiKey}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                messages: cappedMessages,
                model: 'llama-3.3-70b-versatile',
                max_tokens: 512,        // Fix: prevent runaway responses
                temperature: 0.7,       // Fix: consistent, natural tone
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error?.message || 'Failed to fetch from Groq');
        }

        return res.status(200).json(data);
    } catch (error) {
        console.error('Groq API Error:', error);
        return res.status(500).json({ error: 'Internal Server Error', details: error.message });
    }
}
