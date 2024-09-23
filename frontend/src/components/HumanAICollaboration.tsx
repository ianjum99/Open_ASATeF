import React, { useState } from 'react';
import axios from 'axios';

interface Claim {
  id: string;
  content: string;
  aiResponse: string;
  humanVerification: string;
}

const HumanAICollaboration: React.FC = () => {
  const [claims, setClaims] = useState<Claim[]>([]);
  const [currentClaim, setCurrentClaim] = useState('');

  const handleSubmitClaim = async () => {
    if (!currentClaim) return;

    try {
      const response = await axios.post('http://localhost:8000/api/verify-claim', { content: currentClaim });
      const newClaim: Claim = {
        id: Date.now().toString(),
        content: currentClaim,
        aiResponse: response.data.aiResponse,
        humanVerification: ''
      };

      setClaims([...claims, newClaim]);
      setCurrentClaim('');
    } catch (error) {
      console.error('Error submitting claim:', error);
    }
  };

  const handleHumanVerification = async (id: string, verification: string) => {
    try {
      await axios.post(`http://localhost:8000/api/human-verification/${id}`, { verification });
      setClaims(claims.map(claim => 
        claim.id === id ? { ...claim, humanVerification: verification } : claim
      ));
    } catch (error) {
      console.error('Error submitting human verification:', error);
    }
  };

  return (
    <div className="human-ai-collaboration mt-8">
      <h2 className="text-2xl font-bold mb-4">Human-AI Collaboration</h2>
      <div className="mb-4">
        <input
          type="text"
          value={currentClaim}
          onChange={(e) => setCurrentClaim(e.target.value)}
          placeholder="Enter a claim to verify"
          className="w-full p-2 border rounded"
        />
        <button onClick={handleSubmitClaim} className="mt-2 bg-blue-500 text-white px-4 py-2 rounded">
          Submit Claim
        </button>
      </div>
      <div className="claims-list">
        {claims.map(claim => (
          <div key={claim.id} className="bg-gray-100 p-4 mb-4 rounded">
            <p className="font-semibold">Claim: {claim.content}</p>
            <p className="mt-2"><strong>AI Response:</strong> {claim.aiResponse}</p>
            <textarea
              value={claim.humanVerification}
              onChange={(e) => handleHumanVerification(claim.id, e.target.value)}
              placeholder="Enter your verification here"
              className="w-full mt-2 p-2 border rounded"
            />
          </div>
        ))}
      </div>
    </div>
  );
};

export default HumanAICollaboration;
